from nltk.stem import PorterStemmer
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import getcwd
import numpy as np
from math import log2

def _getVocabularySet(corpus : list):
    result = set(corpus[0])
    for doc in range(1,len(corpus)):
        result.update(corpus[doc])
    return result

def buildFreqMatrix(corpus : list[list]):
    set_vocabulary = _getVocabularySet(corpus)
    freq_matrix = np.zeros((len(set_vocabulary), len(corpus)))
    vocabulary = {}
    docs_max_freq = {}
    for doc in range(len(corpus)):
        count_docs = 0
        max_freq = -1
        term_index = 0
        docs_freq = set()
        for term in set_vocabulary:
            freq = corpus[doc].count(term)
            
            try:
                vocabulary[term]
            except KeyError:
                vocabulary[term] = [term_index, 0, freq]
            
            if freq > 0:
                docs_freq.add(term_index)
                vocabulary[term][1] += 1

            if freq > max_freq:
                max_freq = freq

            vocabulary[term][2] += freq
            freq_matrix[term_index, doc] = freq
            term_index += 1
        
        for term in docs_freq:
            freq_matrix[term, doc] *= 1/max_freq

        docs_max_freq.update({doc: max_freq})

    for term in set_vocabulary:
        vocabulary[term][1] = log2(len(corpus)/vocabulary[term][1])

    return vocabulary, freq_matrix
        






def filter_corpus(corpus : str, keywords : set = set()):
    ps = PorterStemmer()
    stwords = set(stopwords.words('english'))
    stwords = stwords - keywords
    doc_tokenized = word_tokenize(corpus)
    doc_review = [ps.stem(word) for word in doc_tokenized if not word in stwords]
    return doc_review

def process_datasets(names : str) -> tuple :
    """method for process documents dataset

    Args:
        names (str): names of datasets to process 

    Returns:
        tuple: 
            1st : vocabulary of all documents (keywords)

            2nd : matrix of terms frequencies in all documents
    """
    corpus = []
    for name in [names]:
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

        
        
        for doc in documents:
            doc_review = filter_corpus(doc)
            corpus.append(doc_review)

    return buildFreqMatrix(corpus)




          

        
