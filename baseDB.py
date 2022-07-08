import sqlite3, Funciones
from sqlite3 import Error

fnc= Funciones.funciones()

#Creo la clase que gestionara la base de datos
class sql3:
	def __init__(self, NombreDeBase:str):
		self.conexion= sqlite3.connect(f"{NombreDeBase}.db")
		self.Cursor= self.conexion.cursor()

	#Comprueba la conexion de la base de datos con la aplicacion
	def ComprobarRed_DB(self):
		try:
			self.conexion
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: Base de datos establecida")

		except:
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: No se pudo conectar a la base de datos")

	#Crea la tabla
	def CrearTabla_DB(self):
		try:
			self.Cursor.execute("CREATE TABLE compañero(ID INT NOT NULL PRIMARY KEY, Nombre TEXT NOT NULL, Matricula INT NOT NULL)")
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: Lista creada")
   
		except:
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: La Lista ya a ha sido creada")

	def InsertarNuevos_DB(self, datos):
		try:
			self.Cursor.execute(f"INSERT INTO compañero VALUES(?, ?, ?)", datos)
			self.conexion.commit()

			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: Los valores establecidos")
   
		except Error:
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION_ERROR: Los valores de entrada no pueden ser establecidos ")

	def MostrarDatos_DB(self):
		self.Cursor.execute("SELECT * FROM compañero")
		return self.Cursor

	def Acutalizar_DB(self,idd,datos2):
		try:
			self.Cursor.execute(f"UPDATE compañero SET ID=?, Nombre=?, matricula=? WHERE ID="+ idd, datos2)
			self.conexion.commit()

			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: Los valores establecidos")
			fnc.Func("LineaPautada")
   
		except Error:
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION_ERROR: Los valores de entrada no pueden ser establecidos " + str(Error))
			fnc.Func("LineaPautada")

	def Borrar_DB(self, iD):
		try:
			self.Cursor.execute(f"DELETE FROM compañero WHERE ID={iD}")
			self.conexion.commit()

			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION: Datos eleminados correctamente")

		except:
			fnc.Func("Limpiar")
			fnc.Func("LineaPautada")
			print("CONEXION_ERROR: No se pudieron eleminar los datos")


