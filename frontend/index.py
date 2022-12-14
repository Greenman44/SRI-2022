from tkinter import *
from tkinter.messagebox import showinfo, showerror
from tkinter.ttk import *
from backend import run, set_parser
import webbrowser
from tkinter.font import Font, nametofont
from tkinter import filedialog
from tkinter.constants import DISABLED, NORMAL


class Google:
    def __init__(self, root : Tk):
        self.window = root
        self.window.title("Documents Finder")
        an = self.window.winfo_screenwidth()
        al = self.window.winfo_screenheight()
        tam = '%dx%d'%(an,al)
        self.window.geometry(tam)
        self.window.config(background="white")
        self.doc=None
        self.current_names = []
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

        queryLabel = Label(self.window, text="Introduce query:",background="white")
        queryLabel.grid(row=5, column=7)
        self.NumSerie = StringVar()
        queryUser = Entry(self.window, textvariable=self.NumSerie)
        queryUser.grid(row=5, column=10)
        self.queryUser = queryUser.get()

        self.queryButton = Button(self.window, text= "Search", command = self.Begin,state=NORMAL)
        self.queryButton.grid(row=5, column=11)
        self.linkrow=7

  
      
        button_explore = Button(self.window,
                        text = "Browse Files",
                        command = self.browseFiles)
  
        button_exit = Button(self.window,
                     text = "Exit",
                     command = exit)

        self.cbDocs = BooleanVar()
        self.cbDoc = Checkbutton(text="Document",variable=self.cbDocs,onvalue = True, offvalue = False).grid(column=1,row=9)
        self.cbQuerys= BooleanVar()
        self.cbQuery = Checkbutton(text="Query",variable=self.cbQuerys,onvalue = True, offvalue = False).grid(column=2,row=9)
        self.cbRels= BooleanVar()
        self.cbRel=Checkbutton(text="Relevans", variable=self.cbRels,onvalue = True, offvalue = False).grid(column=3,row=9)

        button_explore.grid(column = 0, row = 10)
  
        button_exit.grid(column = 0,row = 11)



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


    def browseFiles(self):
        if self.cbDocs.get() == self.cbQuerys.get() == self.cbRels == 0:
            showerror(title= "Load Error", message= "please select data to load (docs, querys, rels)")
        self.files = filedialog.askopenfiles(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Json files",
                                                        "*.json*"),
                                                       ("all files",
                                                        "*.*")))
        self.current_names = self.setCurrentName()
        # TODO: Pasarle esto al parser
      
    def setCurrentName(self):
        names = set()
        for file in self.files:
            if "cran" in file.name:
                name = "cranfield"
            elif "cisi" in file.name or "CISI" in file.name:
                name = "cisi"
            elif "vaswani" in file.name:
                name = "vaswani"
            else:
                showerror(title= "Load Error", message= "Bad file was given")
            names.add(name)
            set_parser(file, name=name, docs = self.cbDocs.get(), querys= self.cbQuerys.get(), rel= self.cbRels.get())
        return names

    def on_configure(self,event):
    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def Begin(self):
        self.canvas = Canvas(self.window,height=500,width=1000)
        self.canvas.grid(column=0,row=10,columnspan=10)

        self.scrollbar = Scrollbar(self.window, command=self.canvas.yview)
        self.scrollbar.grid(column=21,row=10,sticky='ns')

        self.canvas.configure(yscrollcommand = self.scrollbar.set)
        
        self.canvas.bind('<Configure>', self.on_configure)

        self.frame= Frame(self.canvas)
        self.canvas.create_window((0,10),window=self.frame, anchor='nw')


        
        # self.canvas.bind('<Configure>', self.on_configure)

        try :
          rank, metrics = run(self.selecteddocument.get(), self.selectedModel.get(), self.NumSerie.get())
          aux = 0
          for doc in rank:
            self.ShowTitle(doc)
            aux += 1
          self.queryButton["state"]=DISABLED
        except Exception as e :
          raise e
        
        self.preclb=Label(self.window,
            text="Precision=" +  str(metrics[0]),
            font=("Times New Roman", 10),
            background="white").grid(column=0, row=25)
        
        self.recblb=Label(self.window,
            text="Recovered=" + str(metrics[1]),
            font=("Times New Roman", 10),
            background="white").grid(column=0, row=26)

        self.f1lb=Label(self.window,
            text="F1=" + str(metrics[2]),
            font=("Times New Roman", 10),
            background="white").grid(column=0, row=27)
        


    def ShowTitle(self,doc):
        self.doc=doc
        self.linkrow+=2
        
        try:
            lb=Linkbutton(self.frame, text= doc["title"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
            l=Label(self.frame, text= doc["body"],wraplength=1000,background="lightblue").grid(row=self.linkrow+1,column=0)
            
        except:
            try:
                lb=Linkbutton(self.frame, text = doc["name"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
                l=Label(self.frame,text = doc["body"],wraplength=1000,background="lightblue").grid(row=self.linkrow+1,column=0)
            except:
                lb=Linkbutton(self.frame, text = doc["id"], command= lambda m=doc: self.OpenWindowDoc(m)).grid(row=self.linkrow,column=0)
                l=Label(self.frame,text = doc["body"],wraplength=1000,background="lightblue").grid(row=self.linkrow+1,column=0)
          
        

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
        self.frame.destroy()
        self.canvas.destroy()
        self.scrollbar.destroy()
        self.queryButton['state'] = NORMAL

    def MessageForModel(self, event):
        if self.selectedModel.get() == "BooleanModel":
            showinfo(
                title="Query info",
                message="For this model use boolean lenguage in query(Example: a & b, a | b, a and/or b, ~a & b)",
            )

listA = ["BooleanModel", "VectorialModel", "LSIModel"]
listD = ["cranfield", "cisi", "vaswani"]

class Linkbutton(Button):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener el nombre de la fuente por defecto.
        label_font = nametofont("TkDefaultFont").cget("family")
        self.font = Font(family=label_font, size=9)
        
        # Crear un estilo para el hiperv??nculo.
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




