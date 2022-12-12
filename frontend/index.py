from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from backend import run
import webbrowser
from tkinter.font import Font, nametofont


class Google:
    def __init__(self, root : Tk):
        self.window = root
        self.window.title("Documents Finder")
        self.window.geometry("1920x1024")
        self.window.config(background="white")
        self.doc=None

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

        queryLabel = Label(self.window, text="Introduce query:")
        queryLabel.grid(row=5, column=7)
        self.NumSerie = StringVar()
        queryUser = Entry(self.window, textvariable=self.NumSerie)
        queryUser.grid(row=5, column=10)
        self.queryUser = queryUser.get()

        queryButton = Button(self.window, text= "Search", command = self.Begin)
        queryButton.grid(row=5, column=11)
        self.linkrow=7
        self.linkcol=-1


    def Begin(self):

        try :
          rank = run(self.selecteddocument.get(), self.selectedModel.get(), self.NumSerie.get())
          aux = 0
          for doc in rank:
           
            self.ShowTitle(doc)
            aux += 1
        except Exception as e :
          raise e
        


    def ShowTitle(self,doc):
        self.doc=doc
        self.linkcol+=1
        self.linkrow+=1
        try:
            Linkbutton(self.window, text= doc["title"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
        except:
            Linkbutton(self.window, text= doc["name"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
        # docButton.grid(row=self.linkrow,column=0)
    def OpenWindowDoc(self,doc):
        newwindow =Toplevel(self.window,background="white")
        mensaje = Text(newwindow, background="white", width=165, height=25)
        mensaje.grid(column=0,row=0,padx=0, pady=125)
        mensaje.insert("insert",doc["body"])

        newwindow.mainloop()


    def MessageForModel(self, event):
        if self.selectedModel.get() == "BooleanModel":
            showinfo(
                title="Query info",
                message="For this model use boolean lenguage in query(Example: a & b, a | b, a and/or b, ~a & b)",
            )
    def callback(url):
        webbrowser.open_new(url)

listA = ["BooleanModel", "VectorialModel", "LSIModel"]
listD = ["Prueba","cranfield", "20NewGroups"]

class Linkbutton(Button):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener el nombre de la fuente por defecto.
        label_font = nametofont("TkDefaultFont").cget("family")
        self.font = Font(family=label_font, size=9)
        
        # Crear un estilo para el hipervínculo.
        style = Style()
        style.configure(
            "Link.TLabel", foreground="#357fde", font=self.font)
        
        # Aplicarlo a la clase actual.
        self.configure(style="Link.TLabel", cursor="hand2")
        
        # Configurar los eventos de entrada y salida del mouse.
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)
    
    def on_mouse_enter(self, event):
        # Aplicar subrayado.
        self.font.configure(underline=True)
    
    def on_mouse_leave(self, event):
        # Remover subrayado.
        self.font.configure(underline=False)




