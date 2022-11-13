from library.datasets import Dataset
from library.models import VectorialModel

docs = Dataset("Prueba")

vectorial_Model = VectorialModel(docs)

rank = vectorial_Model.EvalQuery("I hate economic and stupid political")


print(rank)
print("*************************************************************")
print(docs[1,"allan"])

# basePath = getcwd() + "\\datasets\\Prueba_data.json"
# df = pd.read_json(basePath, orient="body")

# docs = df["body"]
# docs = docs.map(lambda x: re.sub('[,\.!?()1234567890=;:$%&#]', '', x))
# docs = docs.map(lambda x: re.sub(r'[^a-zA-Z0-9.\s]', ' ', x))  # Replace all non-alphanumeric characters with space
# docs = docs.map(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))  # Remove all dots, e.g. U.S.A. becomes USA
# docs = docs.map(lambda x: x.lower())
# docs = docs.map(lambda x: x.strip())
