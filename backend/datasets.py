import json
from os import getcwd
from .tools import process_datasets
import numpy as np

class Dataset:
    enableData = {"cranfield", "cisi", "vaswani"}
    def __init__(self, name = "", freq_matrix=None, vocabulary=None):
        basePath = getcwd() + f"\\datasets\\"
        if not name == "":
            self.vocabulary , self.freq_matrix =  process_datasets(name)
            self.name = name
            with open(basePath + f"{name}_data.json") as data_json:
                self.data = list(json.load(data_json))
                data_json.close()
            if name in self.enableData:
                try:
                    with open(basePath + f"{name}_query.json") as query_json:
                        self.querys_data = list(json.load(query_json))
                        query_json.close()
                    with open(basePath + f"{name}_rel.json") as rel_json:
                        self.rel_data = list(json.load(rel_json))
                        rel_json.close()
                    self.enableOp = True
                except:
                    self.enableOp = False  
            else: self.enableOp = False
        else:
            self.freq_matrix = freq_matrix
            self.vocabulary = vocabulary

    def __getitem__(self, items): 
        if len(items) == 2 :
            if  isinstance(items[0], str) : 
                try:
                    word_index = self.vocabulary[items[0]]
                except KeyError:
                    raise(Exception(f"this word: {items[0]} is not in the vocabulary"))

                return self.freq_matrix[word_index[0], items[1]]
            elif isinstance(items[0], int):
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
            if  isinstance(items[0], str) : 
                try:
                    word_index = self.vocabulary[items[0]]
                except ValueError:
                    raise(Exception(f"this word: {items[1]} is not in the vocabulary"))

                self.freq_matrix[word_index[0], items[1]] = value
            elif isinstance(items[0], int):
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
        return dimension[1]

    def getAllOcurrences(self, term : str):
        result = 0
        for i in range(len(self)):
            try:
                result += self[i, term]
            except Exception as e:
                raise e
        return result

    






