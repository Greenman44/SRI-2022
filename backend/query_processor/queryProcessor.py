from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from boolean.boolean import BooleanAlgebra 
from sympy import sympify
from ..datasets import Dataset
from ..tools import filter_corpus, buildFreqMatrix

class QueryProcessor:
    def __init__(self, query : str):
        self.query = query

    def processQuery(self):
        pass
    
    def weightUp_query(self):
        pass


class VectorialQueryProcessor(QueryProcessor):
    def __init__(self, query : str):
        super().__init__(query)
    
    def processQuery(self):
        query = filter_corpus(self.query)
    
        vocabulary, matrixFreqs = buildFreqMatrix([query])

        return Dataset(freq_matrix=matrixFreqs, vocabulary=vocabulary)
    
    def weightUp_query(self, queryDataset : Dataset, docs_vocabulary : list[tuple]):
        a = 0.4

        for word in queryDataset.vocabulary:
            try :
                currentIdf = docs_vocabulary[word][1]
            except KeyError:
                currentIdf = 0
            queryDataset[word, 0] = (a + (1.0 - a) * queryDataset[word,0]) * currentIdf

        return queryDataset  

class BooleanQueryProcessor(QueryProcessor):
    
    def __init__(self, query: str):
        super().__init__(query)

    def processQuery(self):
        try:
            exp = BooleanAlgebra().parse(self.query)
            ps = PorterStemmer()
            vocabulary = [ps.stem(word) for word in exp.objects]
            return sympify(str(exp)), vocabulary
        except Exception as e:
            raise e
            
class LSIQueryProcessor(QueryProcessor):

    def __init__(self, query: str):
        super().__init__(query)
    
    def processQuery(self):
        query = filter_corpus(self.query)
        vocabulary, matrixFreqs = buildFreqMatrix([query])
        return Dataset(freq_matrix=matrixFreqs, vocabulary=vocabulary)

       

        
    
