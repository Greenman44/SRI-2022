



from pathlib import Path

base = Path(r'D:\Cibernética\!!!!Tercer año\SRI\20news-bydate-train\alt.atheism\49960')

text = base.read_text()
print(text.strip("\n"))