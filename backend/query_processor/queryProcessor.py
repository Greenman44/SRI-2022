from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from boolean import BooleanAlgebra
from sympy import sympify
from ..datasets import Dataset

class QueryProcessor:
    def __init__(self, query : str):
        self.query = query

    def processQuery(self):
        pass
    
    def weightUp_query(self, queryDataset : Dataset, docs_idf, docs_vocabulary : list[str]):
        pass


class VectorialQueryProcessor(QueryProcessor):
    def __init__(self, query : str):
        super().__init__(query)
    
    def processQuery(self):
        stwords = set(stopwords.words('english'))
        cv = CountVectorizer(stop_words= list(stwords))
        matrixFreqs = cv.fit_transform([self.query])
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
            

       

        
    
