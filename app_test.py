
#Path Nouser D:\Universidad\Tercer año\Segundo semestre\SRI\documentos a leer\20news-bydate-train\alt.atheism\49960
#Path Orejo D:\Cibernética\!!!!Tercer año\SRI\20news-bydate-train\alt.atheism\49960

from pathlib import Path

base = Path(r'D:\Universidad\Tercer año\Segundo semestre\SRI\documentos a leer\20news-bydate-train\alt.atheism\49960')

text = base.read_text()
print(text.strip("\n"))