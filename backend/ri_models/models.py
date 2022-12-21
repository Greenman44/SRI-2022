from ..datasets import Dataset
from nltk.stem import PorterStemmer
from ..query_processor import VectorialQueryProcessor, BooleanQueryProcessor, LSIQueryProcessor 
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sympy import true, false
from math import log2

class Models:
    def __init__(self, dataS: Dataset):
        self.dataS = dataS
        self._weightUp_terms()

    def EvalQuery(self, query: str):
        pass

    def _weightUp_terms(self):
        pass

    def metrics(self, query, rank):
        id = -1
        rr = 0
        for q in self.dataS.querys_data:
            if query == q["query"]:
                id = int(q["query number"])
                break

        if id != -1:
            qdoc = []
            for item in self.dataS.rel_data:
                if int(item["query_num"]) == id and item["position"] > 0:
                    qdoc.append(item["id"])
                if int(item["query_num"]) > id: break
                   
            for index in rank:
                if str(self.dataS.data[index]["id"]) in qdoc :
                    rr = rr + 1
            prec = rr / len(rank)
            rec = rr / len(qdoc)
            f1=0
            if prec>0 or rec>0:
                f1 = (2*prec*rec)/ (prec + rec)
            return prec, rec, f1
        return -1,-1,-1

class BooleanModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)

    def EvalQuery(self, query : str):
        bool_exp, query_vocabulary = BooleanQueryProcessor(query).processQuery()
        
        result = []
        for doc in range(len(self.dataS)):
            bool_doc = {}
            for word in query_vocabulary:
                try:
                    freq=true if self.dataS[word,doc]>0 else false
                except:
                    freq=false
                bool_doc.update({word:freq})
                
            if bool_exp.subs(bool_doc):
                result.append(doc)
        
        return result,(-1,-1,-1)


class VectorialModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)


    def EvalQuery(self, query):
        processor = VectorialQueryProcessor(query)
        dataSQuery = processor.processQuery()
        vocDataQuery = dataSQuery.vocabulary
        sim = []
        query_weights = processor.weightUp_query(
            dataSQuery, self.dataS.vocabulary
        )
        for doc in range(len(self.dataS)):
            sim.append(doc)
            simNormD = []
            simNormQ = []
            for word in vocDataQuery:
                try:
                    weight_term = self.dataS[word, doc] * self.dataS.vocabulary[word][1]
                    sim[doc] += weight_term * query_weights[word,0]
                    simNormD.append(weight_term)
                    simNormQ.append(query_weights[word, 0])
                except:
                    continue

            normQueryVector = np.linalg.norm(simNormQ)
            normDocVector = np.linalg.norm(simNormD)
            sim[doc] = sim[doc] / normQueryVector * normDocVector
        doclist = [i for i in range(len(self.dataS))]
        rank = _Rank(sim, doclist)
        return rank, self.metrics(query, rank) if self.dataS.enableOp else rank

        



class LSIModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)

    def EvalQuery(self, query : str):
        processor = LSIQueryProcessor(query)
        query_set = processor.processQuery()
        query_set = self._growQuerySet(query_set)
        lsi_query = np.dot(np.dot(self.S, np.transpose(self.T)),query_set.freq_matrix)
        lsi_query = np.transpose(lsi_query)
        values = np.dot(lsi_query, self.D)
        docTras=np.transpose(self.D)
        sim = []
        for doc in range(len(self.dataS)):
            current_sim = values[0][doc]/(np.linalg.norm(lsi_query) * np.linalg.norm(docTras[doc]))  
            sim.append(current_sim)
        r = _Rank(sim, np.arange(len(self.dataS)))
        

        rank = _Rank(sim, np.arange(len(self.dataS)))
        return rank, self.metrics(query, rank) if self.dataS.enableOp else rank


    def _weightUp_terms(self):
        global_weight = self._computeGlobalWeight() 
        for doc in range(len(self.dataS)):
            for word in self.dataS.vocabulary:
                self.dataS[word, doc] = log2(self.dataS[word, doc] + 1) * global_weight[word]
        
        k=int(len(self.dataS)*0.7)

        self.T , self.S, self.D = np.linalg.svd(self.dataS.freq_matrix, full_matrices= False)
        self.S = np.diag(self.S)
        self.T = self.T[:, : np.shape(self.T)[1] - k]
        self.S = self.S[: np.shape(self.S)[0] - k, : np.shape(self.S)[1] - k]
        self.D = self.D[: np.shape(self.D)[0] - k, : ]
        self.S = np.linalg.inv(self.S)

    def _computeGlobalWeight(self):
        global_weight = {}
        g_i = 1
        for word in self.dataS.vocabulary:  
            p_ij = 1/self.dataS.vocabulary[word][2]
            for doc in range(len(self.dataS)):
                p_ij *= self.dataS[word,doc]
                g_i += (p_ij + log2(p_ij+1))/log2(len(self.dataS))
            global_weight.update({word : g_i})
        return global_weight
        
    def _growQuerySet(self, query_set : Dataset):
        matrix = np.zeros((len(self.dataS.vocabulary.keys()), 1))
        newSet = Dataset(freq_matrix=matrix, vocabulary=self.dataS.vocabulary)
        for word in query_set.vocabulary:
            try:
                newSet[word, 0] = query_set[word, 0]
            except Exception as e:
                print(str(e))
                continue
        return newSet

def _Rank(sim: list[float], doc):
    print("**********************************************")
    for i in range(len(sim)):
        for j in range(i + 1, len(sim)):
            if sim[i] < sim[j]:
                sim[i], sim[j] = sim[j], sim[i]
                doc[i], doc[j] = doc[j], doc[i]

    return doc[0:200] if len(doc) > 200 else doc