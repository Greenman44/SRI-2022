from tkinter import *
from tkinter.ttk import * 
from PIL import Image, ImageTk
# TODO: Importar Models


class Menu:
    def __init__(self,root):
        self.window=root
        self.window.title("Menu")
        self.window.geometry("1920x1024")
        self.window.config(background="white")


        # lupa= PhotoImage(file='OIP.png')
        # lupa1=lupa.subsample(x=2,y=2)

        Label(self.window, text = "Select the model to use in your search :",
          font = ("Times New Roman", 10),background = "white").grid(column = 0,
          row = 5, padx = 10, pady = 25)
        n = StringVar()
        modelchoosen = Combobox(self.window, width = 27, 
                                    textvariable = n,
                                    font=("Times New Roman", 10),
                                    background = "white")
        # TODO: Lista de modelos
        modelchoosen['values'] = (' LSI Model ', 
                          ' Boolean Model ',
                          ' Vectorial Model')
  
        modelchoosen.grid(column = 1, row = 5)
        modelchoosen.current()
        self.modelchoosen=modelchoosen.get()
        Label(self.window,text = "                                             ",
                    background="white").grid(column=2,row=5)

        queryLabel=Label(self.window,text="Introduce la query:")
        queryLabel.grid(row=5,column=4)
        #NumSerie=StringVar()
        queryUser=Entry(self.window)
        queryUser.grid(row=5,column=3)
        self.queryUser=queryUser.get()
        queryUser.bind("<Return>", self.Search)


    def Search(self, event):
        Label(self.window,text = "La query es: " + self.queryUser + " y el modelo es: " + self.modelchoosen).grid(column=1,row=10)




if __name__ == "__main__":
    root=Tk()
    menu = Menu(root)
    root.mainloop()