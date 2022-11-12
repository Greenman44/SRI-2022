from library.datasets import Dataset


docs = Dataset("Prueba")

print(len(docs))
print("*************************************************************")

# basePath = getcwd() + "\\datasets\\Prueba_data.json"
# df = pd.read_json(basePath, orient="body")

# docs = df["body"]
# docs = docs.map(lambda x: re.sub('[,\.!?()1234567890=;:$%&#]', '', x))
# docs = docs.map(lambda x: re.sub(r'[^a-zA-Z0-9.\s]', ' ', x))  # Replace all non-alphanumeric characters with space
# docs = docs.map(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))  # Remove all dots, e.g. U.S.A. becomes USA
# docs = docs.map(lambda x: x.lower())
# docs = docs.map(lambda x: x.strip())
