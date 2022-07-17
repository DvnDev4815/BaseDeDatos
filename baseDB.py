import sqlite3, Funciones, datetime, os, pandas as pd

CARPETA= ".baseDB"
fnc= Funciones.funciones()

if CARPETA in os.listdir():
	os.chdir(CARPETA)
else:
    os.mkdir(CARPETA)
    os.chdir(CARPETA)
    
class Log:
    def __init__(self)-> None:
        self.Nm_Archivo= "log.txt"
        
        if self.Nm_Archivo in os.listdir():
            self.ARCHIVO= open(self.Nm_Archivo, "a")
        else:
            self.ARCHIVO= open(self.Nm_Archivo, "w")
         
        self.time= datetime.datetime.now()
        self.date= self.time.strftime("%H:%M:%S")
        
    def LOG_COMMAND(self, lct:int, command:str)-> None:
        if lct == 1:
            self.ARCHIVO.write(f"{self.date}(SUCCES) {command} \n")
        elif lct == 2:
            self.ARCHIVO.write(f"{self.date}(ERROR) {command}\n")
        else:
            print("No se puede crear el log")

#Creo la clase que gestionara la base de datos
class sql3:
	def __init__(self, NombreDeBase:str):
		self.tabla= "Alumnos"
		self.columnas= ["ID", "Nombre", "Matricula"]
		self.conexion= sqlite3.connect(f"{NombreDeBase}.db")
		self.Cursor= self.conexion.cursor()
		self.loc= Log()

	#Comprueba la conexion de la base de datos con la aplicacion
	def ComprobarRed_DB(self):
		try:
			self.conexion
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, "CONEXION: Base se datos establecida")
			print("CONEXION: Base se datos establecida")
					
		except self.conexion.Error as ERRN:
			fnc.Func("Limpiar")
   
			self.loc.LOG_COMMAND(2, f"CONEXION: {ERRN}")
			print("CONEXION: No se pudo conectar a la base de datos")

	#Crea la tabla
	def CrearTabla_DB(self):
		try:
			self.Cursor.execute(f"CREATE TABLE {self.tabla}({self.columnas[0]} INT NOT NULL PRIMARY KEY, {self.columnas[1]} TEXT NOT NULL, {self.columnas[2]} TEXT NOT NULL)")
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, "CONEXION: Lista creada")
			print("CONEXION: Lista creada")
   
		except self.conexion.Error as ERRN:
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(2, f"CONEXION {ERRN}")
			print("CONEXION: La Lista ya a ha sido creada")

	def InsertarNuevos_DB(self, datos:list):
		try:
			self.Cursor.execute(f"INSERT INTO {self.tabla} VALUES({datos[0]}, '{datos[1]}', '{datos[2]}')")
			self.conexion.commit()

			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, "CONEXION: Los valores establecidos")
			print("CONEXION: Los valores establecidos")
   
		except self.conexion.Error as ERRN:
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(2, f"CONEXION: {ERRN}")
			print("CONEXION: Los valores de entrada no pueden ser establecidos")

	def MostrarDatos_DB(self):
		self.Cursor.execute(f"SELECT * FROM {self.tabla}")
		return self.Cursor

	def Acutalizar_DB(self, id:int , datos2:list):
		try:
			self.Cursor.execute(f"UPDATE {self.tabla} SET ID={datos2[0]}, Nombre='{datos2[1]}', matricula={datos2[2]} WHERE ID={id}")
			self.conexion.commit()

			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, "CONEXION: Los valores establecidos")
			print("CONEXION: Los valores establecidos")
   
		except self.conexion.Error as ERRN:
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(2, f"CONEXION: {ERRN}")
			print("CONEXION: Los valores de entrada no pueden ser establecidos")

	def Borrar_DB(self, iD):
		try:
			self.Cursor.execute(f"DELETE FROM {self.tabla} WHERE ID={iD}")
			self.conexion.commit()

			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, "CONEXION: Datos eleminados correctamente")
			print("CONEXION: Datos eleminados correctamente")

		except self.conexion.Error as ERRN:
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, f"CONEXION: {ERRN}")
			print("CONEXION: No se pudieron eleminar los datos")
   
	def Exportar(self, ext:str):
		try:
			self.extrac= pd.read_sql(f"SELECT * FROM {self.tabla}", self.conexion, index_col=self.columnas[0])
			self.dataframe= pd.DataFrame(self.extrac)
   
		except sqlite3.Error as ERRN:
			fnc.Func("Limpiar")
			self.loc.LOG_COMMAND(1, f"CONEXION: {ERRN}")
			print("CONEXION: No se pudo exportar correctamente la tabla")
   
		else:
			if ext == "xlsx":
				self.dataframe.to_excel(f"{self.tabla}.xlsx")
			elif ext == "csv":
				self.dataframe.to_csv(f"{self.tabla}.csv")
			elif ext == "txt":
				self.dataframe.to_json(f"{self.tabla}.txt")



