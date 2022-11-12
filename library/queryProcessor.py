from library.models import *
from sklearn.feature_extraction.text import CountVectorizer
from library.datasets import *

class QueryProcessor:
    def __init__(self):
        pass
    def processQuery(query:str):
        pass

class QueryProcessorVectorial(QueryProcessor):
    def __init__(self):
        super().__init__()
    def processQuery(query:str):
        a=0.4
        cv = CountVectorizer()
        matrixFreqs = cv.fit_transform(query)
        vocabulary = cv.get_feature_names_out()
        return Dataset(freq_matrix=matrixFreqs, vocabulary=vocabulary)
        
    

