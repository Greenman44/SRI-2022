from .ri_models import VectorialModel, BooleanModel, LSIModel
from .datasets import Dataset
from os import getcwd
import json

def run(doc_set : str, model : str, query : str):
    try :
        dataS = Dataset(doc_set)
        basePath = getcwd() + f"\\datasets\\{doc_set}_data.json"
        with open(basePath) as data_json:
            data = list(json.load(data_json))
            data_json.close()
    except Exception as e:
        raise e
    

    models = {"BooleanModel" :  BooleanModel(dataS),
        "VectorialModel" : VectorialModel(dataS),
        "LSIModel" : LSIModel(dataS)
    }
    
    try : 
       rank = models[model].EvalQuery(query)
    except Exception as e:
        raise e
    result = []
    for doc in rank:
        result.append(data[doc])
    return result