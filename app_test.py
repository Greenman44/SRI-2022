from tkinter import Tk
from frontend import Google
from backend import run, set_parser


if __name__ == "__main__":
    root = Tk()
    menu = Google(root)
    root.mainloop()

# rank, metrics = run('cranfield', 'VectorialModel', "what chemical kinetic system is applicable to hypersonic aerodynamic problems .")
# print("aqui el rank", metrics)

