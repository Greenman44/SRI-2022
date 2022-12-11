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

class BooleanModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)

    def EvalQuery(self, query : str):
        bool_exp, query_vocabulary = BooleanQueryProcessor(query).processQuery()
        
        result = []
        for doc in range(len(self.dataS)):
            bool_doc = {}
            for word in query_vocabulary:
                if self.dataS[doc, word] > 0:
                    bool_doc.update({word : true})
                else:
                    bool_doc.update({word : false})
                
            if bool_exp.subs(bool_doc):
                result.append(doc)
        
        return result


class VectorialModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)


    def EvalQuery(self, query):
        processor = VectorialQueryProcessor(query)
        dataSQuery = processor.processQuery()
        tfidf_Transformer = TfidfTransformer(smooth_idf=False)
        vocDataQuery = dataSQuery.vocabulary
        sim = []
        query_weights = processor.weightUp_query(
            dataSQuery, tfidf_Transformer.idf_, self.dataS.vocabulary
        )
        for doc in range(len(self.dataS_weight)):
            sim.append(doc)
            simNormD = []
            simNormQ = []
            for word in vocDataQuery:
                try:
                    sim[doc] += self.dataS_weight[doc, word] * query_weights[0, word]
                    simNormD.append(self.dataS_weight[doc, word])
                    simNormQ.append(dataSQuery[0, word])
                except:
                    continue
            normQueryVector = np.linalg.norm(simNormQ)
            normDocVector = np.linalg.norm(simNormD)
            sim[doc] = sim[doc] / normQueryVector * normDocVector
            doclist = [i for i in range(len(self.dataS_weight))]
        return _Rank(sim, doclist)

    def _weightUp_terms(self):
        tfidf_Transformer = TfidfTransformer(smooth_idf=False)
        weight = tfidf_Transformer.fit_transform(self.dataS.freq_matrix)
        self.dataS_weight = Dataset(freq_matrix=weight, vocabulary=self.dataS.vocabulary)
        



class LSIModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)

    def EvalQuery(self, query : str):
        processor = LSIQueryProcessor(query)
        query_set = processor.processQuery()
        query_set = self._growQuerySet(query_set)
        query_trasp = np.transpose(query_set.freq_matrix)
        lsi_query = np.dot(np.dot(self.S, self.T),query_trasp)
        lsi_query = np.transpose(lsi_query)
        values = np.dot(lsi_query, self.D)
        self.D = np.transpose(self.D)
        sim = []
        for doc in range(len(self.dataS)):
            current_sim = values[0][doc]/(np.linalg.norm(lsi_query) * np.linalg.norm(self.D[doc]))  
            sim.append(current_sim)
        return _Rank(sim, np.arange(len(self.dataS)))


    def _weightUp_terms(self):
        global_weight = self._computeGlobalWeight() 
        for doc in range(len(self.dataS)):
            for word in self.dataS.vocabulary:
                self.dataS[doc, word] = log2(self.dataS[doc, word] + 1) * global_weight[word]
        
        self.T , self.S, self.D = np.linalg.svd(np.transpose(self.dataS.freq_matrix.toarray()), full_matrices= False)
        self.S = np.diag(self.S)
        self.T = self.T[:, : np.shape(self.T)[1] - 2]
        self.S = self.S[: np.shape(self.S)[0] - 2, : np.shape(self.S)[1] - 2]
        self.D = self.D[: np.shape(self.D)[0] - 2, : ]
        self.T = np.transpose(self.T)
        self.S = np.linalg.inv(self.S)

    def _computeGlobalWeight(self):
        global_weight = {}
        g_i = 1
        for word in self.dataS.vocabulary:  
            p_ij = 1/self.dataS.getAllOcurrences(word)
            for doc in range(len(self.dataS)):
                p_ij *= self.dataS[doc,word]
                g_i += (p_ij + log2(p_ij+1))/log2(len(self.dataS))
            global_weight.update({word : g_i})
        return global_weight
        
    def _growQuerySet(self, query_set : Dataset):
        matrix = np.zeros((1,len(self.dataS.vocabulary)))
        newSet = Dataset(freq_matrix=matrix, vocabulary=self.dataS.vocabulary)
        for word in query_set.vocabulary:
            try:
                newSet[0,word] = query_set[0,word]
            except Exception as e:
                print(str(e))
                continue
        return newSet

def _Rank(sim: list[float], doc):
        for i in range(len(sim)):
            for j in range(i + 1, len(sim)):
                if sim[i] < sim[j]:
                    sim[i], sim[j] = sim[j], sim[i]
                    doc[i], doc[j] = doc[j], doc[i]

        return doc