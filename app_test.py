
from backend import Dataset, BooleanModel, VectorialModel, LSIModel
from sympy import to_dnf
from boolean import BooleanAlgebra

# aquí especificar el dataset con el que se va  a trabajar("Prueba", "cranfield", "20NewGroups")
# alguno de los que están entre paréntesis
docs = Dataset("Prueba")

lsi_Model = LSIModel(docs)

# aquí escribir la query
rank = lsi_Model.EvalQuery("communism policy and economy")



print(rank)
print("*************************************************************")
