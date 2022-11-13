from library.models import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from library.datasets import *
from nltk.corpus import stopwords
class QueryProcessor:
    def __init__(self):
        pass
    def processQuery(query:str):
        pass
    
    def weightUp_query(queryDataset : Dataset, docs_idf, docs_vocabulary : list[str]):
        pass


class QueryProcessorVectorial(QueryProcessor):
    def __init__(self):
        super().__init__()
    
    def processQuery(self, query:str):
        stwords = set(stopwords.words('english'))
        cv = CountVectorizer(stop_words= list(stwords))
        matrixFreqs = cv.fit_transform([query])
        vocabulary = cv.get_feature_names_out()
        return Dataset(freq_matrix=matrixFreqs, vocabulary=vocabulary)
    
    def weightUp_query(self, queryDataset : Dataset, docs_idf, docs_vocabulary : list[str]):
        a = 0.4
        tf_transformer = TfidfTransformer(use_idf=False)
        queryDataset.freq_matrix = tf_transformer.fit_transform(queryDataset.freq_matrix)

        for word in queryDataset.vocabulary:
            try :
                currentIdf = docs_idf[docs_vocabulary.index(word)]
            except :
                currentIdf = 0
            queryDataset[0 , word] = (a + (1.0 - a) * queryDataset[0, word]) * currentIdf

        return queryDataset         
