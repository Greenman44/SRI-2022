from ..datasets import Dataset
from nltk.stem import PorterStemmer
from ..query_processor import VectorialQueryProcessor, BooleanQueryProcessor 
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
from sympy import true, false

class Models:
    def __init__(self, dataS: Dataset):
        self.dataS = dataS

    def EvalQuery(self, query: str):
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
                    bool_doc.update({word :false})
                
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
        weight = tfidf_Transformer.fit_transform(self.dataS.freq_matrix)
        data_set_weight = Dataset(freq_matrix=weight, vocabulary=self.dataS.vocabulary)
        vocDataQuery = dataSQuery.vocabulary
        sim = []
        query_weights = processor.weightUp_query(
            dataSQuery, tfidf_Transformer.idf_, self.dataS.vocabulary
        )
        for doc in range(len(data_set_weight)):
            sim.append(doc)
            simNormD = []
            simNormQ = []
            for word in vocDataQuery:
                try:
                    sim[doc] += data_set_weight[doc, word] * query_weights[0, word]
                    simNormD.append(data_set_weight[doc, word])
                    simNormQ.append(dataSQuery[0, word])
                except:
                    continue
            normQueryVector = np.linalg.norm(simNormQ)
            normDocVector = np.linalg.norm(simNormD)
            sim[doc] = sim[doc] / normQueryVector * normDocVector
            doclist = [i for i in range(len(data_set_weight))]
        return self.Rank(sim, doclist)

    def Rank(self, sim: list[float], doc):
        for i in range(len(sim)):
            for j in range(i + 1, len(sim)):
                if sim[i] < sim[j]:
                    sim[i], sim[j] = sim[j], sim[i]
                    doc[i], doc[j] = doc[j], doc[i]

        return doc


class BooleanExtendedModel(Models):
    def __init__(self, dataS: Dataset):
        super().__init__(dataS)

    def EvalQuery(self, query : str):
        pass
        
        
