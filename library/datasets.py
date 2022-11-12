from library.process_datasets import process_datasets

class Dataset:

    def __init__(self, *names : str):
        vocabulary , self.freq_matrix =  process_datasets(*names)
        self.vocabulary = list(vocabulary)
        self.names = list(names)
    

    def __getitem__(self, *items):
        if len(items[0]) == 2 :
            try:
                word_index = self.vocabulary.index(items[0][1])
            except ValueError:
                raise(Exception(f"this word: {items[0][1]} is not in the vocabulary"))

            return self.freq_matrix[items[0][0], word_index]
        if len(items[0]) == 1 :
            if isinstance(items[0][0], str) :
                pass
                #TODO: devolver la columna de esa palabra
            else:
                #TODO: devolver la fila de ese documento
                pass
        raise(Exception(f"Only takes 2 or less arguments"))




