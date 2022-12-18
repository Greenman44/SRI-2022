from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.ttk import *
from backend import run
import webbrowser
from tkinter.font import Font, nametofont
from tkinter.constants import DISABLED, NORMAL


class Google:
    def __init__(self, root : Tk):
        self.window = root
        self.window.title("Documents Finder")
        self.window.geometry("1920x1024")
        self.window.config(background="white")
        self.doc=None

        # frame2 = Frame(self.root)
        # frame2.grid(row=0, column=0, sticky='ns')

        # self.frame2=frame2
        # # Add a canvas in that frame.
        # 

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

        queryLabel = Label(self.window, text="Introduce query:",background="white")
        queryLabel.grid(row=5, column=7)
        self.NumSerie = StringVar()
        queryUser = Entry(self.window, textvariable=self.NumSerie)
        queryUser.grid(row=5, column=10)
        self.queryUser = queryUser.get()

        self.queryButton = Button(self.window, text= "Search", command = self.Begin,state=NORMAL)
        self.queryButton.grid(row=5, column=11)
        self.linkrow=7

        menubar=Menu(self.window)
        self.window.config(menu=menubar)
        
        helpText="You have to complete all the camps in the window before press the search button. Every combobox contains all the elements you can use. If you selected the BooleanModel in combobox of Models, you need to use boolean lenguage, in other case use natural lenguage."
        
        
        helpmenu = Menu(menubar,tearoff=0)
        helpmenu.add_command(label="Basic Help", command = lambda m=helpText: self.OpenWindowHelp(m))
        helpmenu.add_separator()
        helpmenu.add_command(label="Quit", command=root.quit)

        menubar.add_cascade(label="Help", menu=helpmenu)

        
        
        stateButton = Button(self.window, text="Search Again", command = self.CloseFrame)
        stateButton.grid(column=10,row=20, padx=20, pady=20)


        

    def on_configure(self,event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def Begin(self):
        self.lf= Frame(self.window,name='documents')
        self.lf.grid(row=6,column=0,columnspan=10,sticky='ns')

        self.canvas = Canvas(self.lf,background="white")
        self.canvas.grid(column=0, row=0)
        
        
        scrollbar = Scrollbar(
                self.lf,
                orient='vertical',
                command=self.canvas.yview
            )
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.config(yscrollcommand=scrollbar.set)
        print(self.canvas.bbox('all'))
        
        
        # self.canvas.bind('<Configure>', self.on_configure)

        try :
          rank = run(self.selecteddocument.get(), self.selectedModel.get(), self.NumSerie.get())
          aux = 0
          for doc in rank:
            self.ShowTitle(doc)
            aux += 1
          
          self.canvas.config(scrollregion=self.canvas.bbox('all'))
          self.queryButton["state"]=DISABLED
        except Exception as e :
          raise e
        


    def ShowTitle(self,doc):
        self.doc=doc
        self.linkrow+=2
        
        try:
            Linkbutton(self.canvas, text= doc["title"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
            Label(self.canvas, text= doc["body"]).grid(row=self.linkrow+1,column=0)
        except:
            Linkbutton(self.canvas, text= doc["name"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
            Label(self.canvas,text = doc["body"],wraplength=1000,background="lightblue").grid(row=self.linkrow+1,column=0)
          
        

    def OpenWindowDoc(self,doc):
        newwindow =Toplevel(self.window,background="white")
        mensaje = Text(newwindow, background="white", width=165, height=25)
        mensaje.grid(column=0,row=0,padx=0, pady=125)
        mensaje.insert("insert",doc["body"])

        newwindow.mainloop()
    
    def OpenWindowHelp(self,textHelp):
        newwindow =Toplevel(self.window,background="white")
        mensaje = Text(newwindow, background="white", width=165, height=25)
        mensaje.grid(column=0,row=0,padx=0, pady=125)
        mensaje.insert("insert",textHelp)

        newwindow.mainloop()

    def CloseFrame(self):
        self.lf.destroy()
        self.queryButton['state'] = NORMAL

    def MessageForModel(self, event):
        if self.selectedModel.get() == "BooleanModel":
            showinfo(
                title="Query info",
                message="For this model use boolean lenguage in query(Example: a & b, a | b, a and/or b, ~a & b)",
            )

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




