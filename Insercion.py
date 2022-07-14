from tkinter import ttk
import tkinter, baseDB, Funciones

Func= Funciones.funciones()
Conx= baseDB.sql3("Almanaque")

class Insercion_datos(tkinter.Toplevel):
    En_uso= False
    def __init__(self, *args, **kwargs):
        #Propiedades de la ventana
        super().__init__(*args, **kwargs)
        self.title("Inserte los datos")
        self.resizable(False, False)
        self.config(width= 400, height= 150)
        
        #---- Variantes ----
        self.var_ID= tkinter.StringVar()
        self.var_Nombre= tkinter.StringVar()
        self.var_Matricula= tkinter.StringVar()

        #---- Etiquetas ----
        self.Lb_ID=ttk.Label(self, text= "ID:")
        self.Lb_ID.place(x=10, y=23 )
        
        self.Lb_nombre=ttk.Label(self, text= "Nombre(Completo): ")
        self.Lb_nombre.place(x=35, y=23 )
        
        self.Lb_matricula=ttk.Label(self, text= "Matricula:")
        self.Lb_matricula.place(x=10, y=63 )
        
        #---- Entradas ----
        self.entr_ID= ttk.Entry(self, textvariable= self.var_ID)
        self.entr_ID.place(x=10, y=40, width= 20)
        
        self.entr_nombre= ttk.Entry(self, textvariable= self.var_Nombre)
        self.entr_nombre.place(x=35 , y=40, width= 235)
        
        self.entr_matricula= ttk.Entry(self, textvariable= self.var_Matricula)
        self.entr_matricula.place(x=10, y=80, width=260)
        
        #---- Botones ----
        self.btn_aceptar= ttk.Button(self, text= "Aceptar", command= self._Acept)
        self.btn_aceptar.place(x=290 , y= 40, width= 100)
        
        self.btn_canelar= ttk.Button(self, text= "Cancelar", command= self._Cancel)
        self.btn_canelar.place(x=290 , y= 75, width= 100)
        
        self.__class__.En_uso= True
        
    #Metodo para cerrar la ventana
    def _Cancel(self):
        self.__class__.En_uso= False
        return super().destroy()
        
    #Metodo para incertar los datos a la base
    def _Acept(self):
        self.data= [int(self.var_ID.get()), self.var_Nombre.get(), int(self.var_Matricula.get())]
        Conx.InsertarNuevos_DB(self.data)
        Func.Esperar(1)
        self._Cancel()