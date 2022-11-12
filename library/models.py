from library.datasets import *
from library.queryProcessor import QueryProcessor
from sklearn.feature_extraction.text import TfidfTransformer


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
        self.processor= QueryProcessor()
    
    def EvalQuery(self,query):
        dataSQuery=self.processor.processQuery(query)
        tfidf_Transformer = TfidfTransformer()
        weight = tfidf_Transformer.fit_transform(self.dataS.freq_matrix)
        data_set_weight = Dataset(freq_matrix=weight,vocabulary=self.dataS.vocabulary)
        vocDataQuery = dataSQuery.vocabulary
        sim=[len(weight)]
        simNormD=[len(dataSQuery)]
        simNormQ=[len(dataSQuery)]
        for doc in range(len(data_set_weight)):
            for word in vocDataQuery:
                try:
                    sim[doc] += (data_set_weight[doc,word]*dataSQuery[doc,word])
                    simNormD[word] = data_set_weight[doc,word]
                    simNormQ[word] = dataSQuery[0,word]
                except:
                    continue
            normQueryVector= np.nomr(simNormQ)
            normDocVector= np.norm(simNormD)
            sim[doc] = sim[doc]/normQueryVector*normDocVector
            doclist = [i for i in range(len(weight))]
        return self.Rank(sim,doclist)
    
    def Rank(self,sim:list[float], doc):
        for i in range(len(sim)):
            for j in range(i+1,len(sim)):
                if sim[i]>sim[j]:
                    temp = sim[i]
                    sim[i] = sim[j]
                    sim[j] = temp
                    temp = doc[i]
                    doc[i]= doc[j]
                    doc[j]=temp
        return doc



class BooleanExtendedModel(Models):
    def __init__(self,dataS:Dataset):
        super().__init__(dataS)
    def EvalQuery(self):
        #TODO: Implementation of the search of Documents
        pass



