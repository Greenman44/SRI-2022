from tkinter import Tk
from frontend import Google
from backend import run, set_parser
from sympy import to_dnf




# a = [2, 3, 4]
# b = [1,5,2]
# result = set(b).union(a)
# print(result)

# from boolean import BooleanAlgebra


# aquí especificar el dataset con el que se va  a trabajar("Prueba", "cranfield", "20NewGroups")
# alguno de los que están entre paréntesis


# aquí escribir la query
if __name__ == "__main__":
    root = Tk()
    menu = Google(root)
    root.mainloop()

# rank, metrics = run('cranfield', 'VectorialModel', "what chemical kinetic system is applicable to hypersonic aerodynamic problems .")
# print("aqui el rank", metrics)

