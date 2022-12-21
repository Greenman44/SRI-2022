from .ri_models import VectorialModel, BooleanModel, LSIModel
from .datasets import Dataset
from os import getcwd
import json

current_doc_set = ""
data = None
_boolean = None
_vectorial = None
_lsi = None
current_dataset = None

def run(doc_set : str, model : str, query : str):
    global current_dataset, current_doc_set, _boolean, _vectorial, _lsi, data
    try :
        if not (doc_set == current_doc_set):
            current_dataset = Dataset(name = doc_set)
            basePath = getcwd() + f"\\datasets\\{doc_set}_data.json"
            with open(basePath) as data_json:
                data = list(json.load(data_json))
                data_json.close()
    except Exception as e:
        raise e
    
    current_model = None
    if model == "BooleanModel":
        if _boolean == None or not (doc_set == current_doc_set):
            _boolean = BooleanModel(current_dataset)
        current_model = _boolean
    elif model == "VectorialModel":
        if _vectorial == None or not (doc_set == current_doc_set):
            _vectorial = VectorialModel(current_dataset)
        current_model = _vectorial
    elif model == "LSIModel" or not (doc_set == current_doc_set):
        if _lsi == None:
            _lsi = VectorialModel(current_dataset)
        current_model = _lsi

    else :
        raise Exception("this model not exist")
    
    current_doc_set = doc_set
    try : 
       rank, metrics = current_model.EvalQuery(query)
    except Exception as e:
        raise e
    
    result = []
    for doc in rank:
        result.append(data[doc])
    return result, metrics