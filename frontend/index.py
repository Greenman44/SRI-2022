from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import * 
from PIL import Image, ImageTk

# TODO: Importar Models


class Menu():
    def __init__(self,root):
        self.window=root
        self.window.title("Menu")
        self.window.geometry("1920x1024")
        self.window.config(background="white")

        Label(self.window, text = "Select the Dataset of documents to use in your search :",
          font = ("Times New Roman", 10),background = "white").grid(column = 0,
          row = 5, padx = 10, pady = 25)
        
        self.selecteddocument=StringVar()
        documentchoosen = Combobox(self.window, width = 27, 
                                    textvariable = self.selecteddocument,
                                    font=("Times New Roman", 10),
                                    background = "white",state="readonly",values=listD)
        
        documentchoosen.grid(column = 1, row = 5)

        Label(self.window,text = "                                             ",
                    background="white").grid(column=2,row=5)

        Label(self.window, text = "Select the model to use in your search :",
          font = ("Times New Roman", 10),background = "white").grid(column = 2,
          row = 5, padx = 10, pady = 25)
        self.selectedModel = StringVar()
        modelchoosen = Combobox(self.window, width = 27, 
                                    textvariable = self.selectedModel,
                                    font=("Times New Roman", 10),
                                    background = "white",state="readonly",values=listA)
        
        modelchoosen.bind("<<ComboboxSelected>>",self.MessageForModel)
        modelchoosen.grid(column = 3, row = 5)
        Label(self.window,text = "                                             ",
                    background="white").grid(column=4,row=5)

        queryLabel=Label(self.window,text="Introduce la query:")
        queryLabel.grid(row=5,column=7)
        self.NumSerie=StringVar()
        queryUser=Entry(self.window, textvariable=self.NumSerie)
        queryUser.grid(row=5,column=10)
        self.queryUser=queryUser.get()
        queryUser.bind("<Return>", self.Beging)


    def Beging(self, event):
        # TODO: Recoger los datos para procesarlos una vez procesados llamar al otro metodo para visualizarlos
        Label(self.window,text = "La query es: " + self.NumSerie.get() + " y el modelo es: " + self.selectedModel.get()).grid(column=3,row=10)
    
    def MessageForModel(self,event):
        if self.selectedModel.get()=="BooleanModel":
            showinfo(title="Query info", message="For this model use boolean lenguage in query(Example: a & b, a | b, a and/or b, ~a & b)")



listA=["BooleanModel","VectorialModel", "LSIModel"]
listD=["Cranfield","20NewGroups"]



if __name__ == "__main__":
    root=Tk()
    menu = Menu(root)
    root.mainloop()