from library.datasets import Dataset
from library.models import VectorialModel

# aquí especificar el dataset con el que se va  a trabajar("Prueba", "cranfield", "20NewGroups")
# alguno de los que están entre paréntesis
docs = Dataset("Prueba")

vectorial_Model = VectorialModel(docs)

# aquí escribir la query
rank = vectorial_Model.EvalQuery("I hate economic and stupid political")


print(rank)
print("*************************************************************")
