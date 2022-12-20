from .tools import process_datasets
import numpy as np

class Dataset:
    enableData = {"cranfield","cisi"}
    def __init__(self, *names : str, freq_matrix=None, vocabulary=None):
        if len(names)>0:
            vocabulary , self.freq_matrix =  process_datasets(*names)
            self.names = list(names)
            if names in self.enableData:
                self.enableOp = True
            else: self.enableOp = False
        else:
            self.freq_matrix = freq_matrix
        self.vocabulary = list(vocabulary)

    def __getitem__(self, items):
        if len(items) == 2 :
            if  isinstance(items[1], str) : 
                try:
                    word_index = self.vocabulary.index(items[1])
                except ValueError:
                    raise(Exception(f"this word: {items[0][1]} is not in the vocabulary"))

                return self.freq_matrix[items[0], word_index]
            elif isinstance(items[0][1], int):
                return  self.freq_matrix[items[0], items[1]]
            else :
                raise(Exception(f"Bad args was given"))

        if len(items) == 1 :
            if isinstance(items[0], str) :
                pass
                #TODO: devolver la columna de esa palabra
            else:
                #TODO: devolver la fila de ese documento
                pass
        raise(Exception(f"Only takes 2 or less arguments"))

    def __setitem__(self, items, value):
        if len(items) == 2 :
            if  isinstance(items[1], str) : 
                try:
                    word_index = self.vocabulary.index(items[1])
                except ValueError:
                    raise(Exception(f"this word: {items[1]} is not in the vocabulary"))

                self.freq_matrix[items[0], word_index] = value
            elif isinstance(items[1], int):
                self.freq_matrix[items[0], items[1]] = value
            else :
                raise(Exception(f"Bad args was given"))

        elif len(items) == 1 :
            if isinstance(items[0], str) :
                pass
                #TODO: devolver la columna de esa palabra
            else:
                #TODO: devolver la fila de ese documento
                pass
        else :
            raise(Exception(f"Only takes 2 or less arguments"))

    def __len__(self):
        dimension = list(np.shape(self.freq_matrix))
        return dimension[0]

    def getAllOcurrences(self, term : str):
        result = 0
        for i in range(len(self)):
            try:
                result += self[i, term]
            except Exception as e:
                raise e
        return result

    def metrics(self, query,qry,qrel,rank,docs):
        id = -1
        rr = 0
        for q in qry:
            if query == q["query"]:
                id = q["query number"]

        if id != -1:
            qdoc = []
            for item in qrel:
                if docid := item["query_num"] == id and item["id"] > 1:
                    qdoc.append(docid)
                   
            for index in rank:
                if docs[index]["id"] in qdoc :
                    rr = rr + 1
            prec = rr / len(rank)
            rec = rr / len(qdoc)
            f1 = (2*prec*rec)/ (prec + rec)
            return prec, rec, f1
        return -1,-1,-1






