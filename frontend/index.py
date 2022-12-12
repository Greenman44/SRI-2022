from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from backend import run

# TODO: Importar Models


class Google:
    def __init__(self, root : Tk):
        self.window = root
        self.window.title("Google")
        self.window.geometry("1920x1024")
        self.window.config(background="white")

        Label(
            self.window,
            text="Select the Dataset of documents to use in your search :",
            font=("Times New Roman", 10),
            background="white",
        ).grid(column=0, row=5, padx=10, pady=25)

        #document combobox
        self.selecteddocument = StringVar()
        documentchoosen = Combobox(
            self.window,
            width=27,
            textvariable=self.selecteddocument,
            font=("Times New Roman", 10),
            background="white",
            state="readonly",
            values=listD,
        )

        documentchoosen.grid(column=1, row=5)

        Label(
            self.window,
            text="                                             ",
            background="white",
        ).grid(column=2, row=5)

        Label(
            self.window,
            text="Select the model to use in your search :",
            font=("Times New Roman", 10),
            background="white",
        ).grid(column=2, row=5, padx=10, pady=25)

        #model combobox
        self.selectedModel = StringVar()
        modelchoosen = Combobox(
            self.window,
            width=27,
            textvariable=self.selectedModel,
            font=("Times New Roman", 10),
            background="white",
            state="readonly",
            values=listA,
        )

        modelchoosen.bind("<<ComboboxSelected>>", self.MessageForModel)
        modelchoosen.grid(column=3, row=5)
        Label(
            self.window,
            text="                                             ",
            background="white",
        ).grid(column=4, row=5)

        queryLabel = Label(self.window, text="Introduce la query:")
        queryLabel.grid(row=5, column=7)
        self.NumSerie = StringVar()
        queryUser = Entry(self.window, textvariable=self.NumSerie)
        queryUser.grid(row=5, column=10)
        self.queryUser = queryUser.get()
        # queryUser.bind("<Return>", self.Begin)

        queryButton = Button(self.window, text= "Search", command= self.Begin)
        queryButton.grid(row=5, column=11)


    def Begin(self):

        try :
          rank = run(self.selecteddocument.get(), self.selectedModel.get(), self.NumSerie.get())
          for doc in rank:
            try:
              print(doc["name"])
            except KeyError:
              print(doc["title"])
        except Exception as e :
          raise e
        Label(
            self.window,
            text="La query es: "
            + self.NumSerie.get()
            + " y el modelo es: "
            + self.selectedModel.get(),
        ).grid(column=3, row=10)

    def MessageForModel(self, event):
        if self.selectedModel.get() == "BooleanModel":
            showinfo(
                title="Query info",
                message="For this model use boolean lenguage in query(Example: a & b, a | b, a and/or b, ~a & b)",
            )


listA = ["BooleanModel", "VectorialModel", "LSIModel"]
listD = ["Prueba","cranfield", "20NewGroups"]



