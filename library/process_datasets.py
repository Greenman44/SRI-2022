from nltk.stem import PorterStemmer
import pandas as pd
import re
import nltk
# nltk.download("stopwords")
# nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import getcwd
from sklearn.feature_extraction.text import CountVectorizer


def process_datasets(*names : str) -> tuple :
    """method for process documents dataset

    Args:
        names (str): names of datasets to process 

    Returns:
        tuple: 
            1st : vocabulary of all documents (keywords)

            2nd : matrix of terms frequencies in all documents
    """
    corpus = []
    for name in names:
        basePath = getcwd() + f"\\datasets\\{name}_data.json"
        try:
            df = pd.read_json(basePath, orient = "body")
        except Exception as e :
            raise(e)
            
        documents = df["body"]
        documents = documents.map(lambda x: re.sub('[,\.!?()1234567890=;:$%&#]', '', x))
        documents = documents.map(lambda x: re.sub(r'[^a-zA-Z0-9.\s]', ' ', x))  # Replace all non-alphanumeric characters with space
        documents = documents.map(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))  # Remove all dots, e.g. U.S.A. becomes USA
        documents = documents.map(lambda x: x.lower())
        documents = documents.map(lambda x: x.strip())

        ps = PorterStemmer()
        stwords = set(stopwords.words('english'))
        
        for doc in documents:
            doc_tokenized = word_tokenize(doc)
            doc_review = [ps.stem(word) for word in doc_tokenized if not word in stwords]
            doc_review = ' '.join(doc_review)
            corpus.append(doc_review)
        
    cv = CountVectorizer()

    freq_matrix = cv.fit_transform(corpus)
    vocabulary = cv.get_feature_names_out()
    

    return vocabulary, freq_matrix

          

        
