from tkinter import messagebox, ttk
import baseDB, tkinter, Funciones, Insercion


Conx= baseDB.sql3("Almanaque")
Func= Funciones.funciones()

class Ventana(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.prin= root
        
        #Propiedades de la ventana
        self.prin.title("Base de datos: Gupo E -v1.0-")
        self.prin.resizable(False, False)
        self.prin.geometry("750x400")
        
        #Variables
        self.var_id= tkinter.StringVar()
        self.var_nombre= tkinter.StringVar()    
        self.var_matricula= tkinter.StringVar()
        
        #Botones de accion
        self.btn_agregar= ttk.Button(text= "Agregar Elemento", command=self._second)
        self.btn_agregar.place(x= 600, y= 30, width= 140)
        
        #self.btn_modificar= ttk.Button(text= "Modificar Elemento")
        #self.btn_modificar.place(x= 600, y= 60, width= 140)
        
        self.btn_borrar= ttk.Button(text= "Borrar Elemento", command= self._delete)
        self.btn_borrar.place(x= 600, y= 60, width= 140)
        
        self.btn_exit= ttk.Button(text= "Salir", command= self._exit)
        self.btn_exit.place(x= 630, y= 100)
        
        self.btn_actualizar= ttk.Button(text= "Actualizar", command= self._show)
        self.btn_actualizar.place(x= 600, y= 360, width= 140)
        
        #Lista de datos
        self.tree_datos= ttk.Treeview(columns= ("#0", "#1", "#2"))
        self.tree_datos.place(x= 10, y= 30, width= 580, height= 350)
        #Configuracion de las columnas
        #Columna 0
        self.tree_datos.heading('#0', text="ID", anchor= tkinter.CENTER)
        self.tree_datos.column('#0', width= 50)
        #Columna 1
        self.tree_datos.heading('#1', text= "Nombre", anchor= tkinter.CENTER)
        self.tree_datos.column('#1', width= 250)
        #columna 2
        self.tree_datos.heading('#2', text= "Matricula", anchor= tkinter.CENTER)
        #Metodo que identifica cuando se hace click a un elemento
        self.tree_datos.bind("<Double-1>", self._select)
        
    #metodo de salida del programa
    def _exit(self):
        self.salir= messagebox.askquestion("¿Salir?", "¿Estas seguro?")
        if self.salir == "yes":
            self.prin.destroy()
            
    def _select(self, event):
        self.item= self.tree_datos.identify("item", event.x, event.y)
        
        self.var_id.set(self.tree_datos.item(self.item, "text"))
        self.var_nombre.set(self.tree_datos.item(self.item, "values")[0])
        self.var_matricula.set(self.tree_datos.item(self.item, "values")[1])
            
    def _show(self):
        self.registro= self.tree_datos.get_children()
        for elementos in self.registro:
            self.tree_datos.delete(elementos)
            
        for casilla in Conx.MostrarDatos_DB():
            self.tree_datos.insert("", 0, text= casilla[0], values=(casilla[1], casilla[2]))
            
    def _delete(self):
        Conx.Borrar_DB(self.var_id.get())
        self._show()
    
    #metodo para abrir el panel de insercion de datos
    def _second(self):
        if not Insercion.Insercion_datos.En_uso:
            self.Ven_sec= Insercion.Insercion_datos()
        
        self._show()
            
#Conectar con la base de datos            
Conx.ComprobarRed_DB()
Conx.CrearTabla_DB() 
      
#Iniciar la ventana
inicializador = tkinter.Tk()
app= Ventana(inicializador)
app._show()
app.mainloop()