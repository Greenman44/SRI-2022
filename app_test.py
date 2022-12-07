
from backend import Dataset, BooleanModel, VectorialModel

# aquí especificar el dataset con el que se va  a trabajar("Prueba", "cranfield", "20NewGroups")
# alguno de los que están entre paréntesis
docs = Dataset("Prueba")

boolean_Model = BooleanModel(docs)

# aquí escribir la query
rank = boolean_Model.EvalQuery("hate and policy")

# a =BooleanAlgebra()
# exp = a.parse("x and not b")
# exp = sympify(str(exp))
print(rank)
print("*************************************************************")
