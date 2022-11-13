from library.datasets import *
from library.queryProcessor import QueryProcessorVectorial
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

class Models:
    def __init__(self,dataS:Dataset):
        self.dataS=dataS
    def EvalQuery(self):
        pass
class BooleanModel(Models):
    def __init__(self,dataS:Dataset):
        super().__init__(dataS)
    def EvalQuery(self):
        pass

class VectorialModel(Models):
    def __init__(self,dataS:Dataset):
        super().__init__(dataS)
        self.processor = QueryProcessorVectorial()
    
    def EvalQuery(self,query):
        dataSQuery = self.processor.processQuery(query)
        tfidf_Transformer = TfidfTransformer(smooth_idf=False)
        weight = tfidf_Transformer.fit_transform(self.dataS.freq_matrix)
        data_set_weight = Dataset(freq_matrix=weight,vocabulary=self.dataS.vocabulary)
        vocDataQuery = dataSQuery.vocabulary
        sim = []
        query_weights = self.processor.weightUp_query(dataSQuery, tfidf_Transformer.idf_ , self.dataS.vocabulary)
        for doc in range(len(data_set_weight)):
            sim.append(doc)
            simNormD = []
            simNormQ = []
            for word in vocDataQuery:
                try:
                    sim[doc] += (data_set_weight[doc,word] * query_weights[0, word])
                    simNormD.append(data_set_weight[doc,word])
                    simNormQ.append(dataSQuery[0,word])
                except:
                    continue
            normQueryVector = np.linalg.norm(simNormQ)
            normDocVector = np.linalg.norm(simNormD)
            sim[doc] = sim[doc]/normQueryVector*normDocVector
            doclist = [i for i in range(len(data_set_weight))]
        return self.Rank(sim, doclist)
    
    def Rank(self,sim:list[float], doc):
        for i in range(len(sim)):
            for j in range(i+1,len(sim)):
                if sim[i] < sim[j]:
                    sim[i], sim[j] = sim[j], sim[i]
                    doc[i], doc[j] = doc[j], doc[i] 
        
        return doc



class BooleanExtendedModel(Models):
    def __init__(self,dataS:Dataset):
        super().__init__(dataS)
    def EvalQuery(self):
        #TODO: Implementation of the search of Documents
        pass



