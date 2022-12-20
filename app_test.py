from tkinter import Tk
from frontend import Google
from backend import run
# from sympy import to_dnf
# from boolean import BooleanAlgebra

# aquí especificar el dataset con el que se va  a trabajar("Prueba", "cranfield", "20NewGroups")
# alguno de los que están entre paréntesis


# # aquí escribir la query
# if __name__ == "__main__":
#     root = Tk()
#     menu = Google(root)
#     root.mainloop()
print(run('cranfield','VectorialModel','communism' ))

