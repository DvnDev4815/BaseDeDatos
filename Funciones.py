'''
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
	Programado por
		Domingo Vaca Nieves 
  		2022

*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
'''

import os, time, platform
from colorama import Fore, Back, Style

Sistemas= ["Windows", "Linux", "Mac"]

class funciones:

	def __init__(self):
		self.Color= ["VERDE", "AZUL", "AMARILLO", "CLASICO", "CELESTE", "PREDERTERMINADO", "BASICO"]

	'''Funciones varias
	Limpiar: Limpia la consola
 
	LineaPautada: Imprime en consola una linea de decoracion(separador)
 
	LineaVacia: Imprime en consola una linea vacia
 
	Pausa: Espera a que la persona presione enter
 
	Cerrar: Cierra todo
 	'''
	def Func(self, fn:str) -> None:
		if platform.system() == Sistemas[1] or Sistemas[2]:
			if fn == "Limpiar":
				os.system("clear")
			elif fn == "LineaPautada":
				print(75 * "*")
			elif fn == "LineaVacia":
				print("")
			elif fn == "Pausa":
				self.a= input("Presiona [Enter] para continuar...")
			elif fn == "Cerrar":
				exit()
		else:
			if fn == "Limpiar":
				os.system("cls")
			elif fn == "LineaPautada":
				print(79 * "*")
			elif fn == "LineaVacia":
				print("")
			elif fn == "Pausa":
				os.system("pause")
			elif fn == "Salir":
				os.system("exit")

	#Establese un retraso en el programa
	def Esperar(self, tm:int) -> None:
		time.sleep(tm)
  
	#Centra un texto
	def Centrar(self, msg:str) -> None:
		espacio = " " * ((64 - len(msg))// 2)
		print(espacio + msg)

	#Establece un tema de colores a la consola
	def ColorDeFont(self, color:str) -> None:
		if platform.system() == Sistemas[1] or Sistemas[2]:
			if color == self.Color[0]:
				print(Fore.GREEN)
			elif color == self.Color[1]:
				print(Fore.BLUE)
			elif color == self.Color[2]:
				print(Fore.YELLOW + Style.BRIGHT)
			elif color == self.Color[3]:
				print(Back.BLUE + Fore.YELLOW + Style.BRIGHT)
			elif color == self.Color[4]:
				print(Fore.CYAN)
			elif color == self.Color[5]:
				print(Fore.WHITE + Back.BLACK)
			elif color == self.Color[6]:
				print(Back.CYAN + Fore.YELLOW + Style.BRIGHT)
			else:
				print("Color no valido")

		else:
			if color == self.Color[0]:
				os.system("color 0a")
			elif color == self.Color[1]:
				os.system("color 09")
			elif color == self.Color[2]:
				os.system("color 0e")
			elif color == self.Color[3]:
				os.system("color 1e")
			elif color == self.Color[4]:
				os.system("color 0b")
			elif color == self.Color[5]:
				os.system("color")
			else:
				print("Color no valido")

	#Establece el titulo en la consola
	def Titulo(self, title:str)-> None:
		if platform.system() == Sistemas[1]:
			os.system("xtitle " + title)
		else:
			os.system("title " + title)

	#Da la vercion del modulo
	def DarVercion_Mdl(self):
		self.Vercion = "v4.6"
		return self.Vercion

	#Da el nombre del creador del modulo
	def DarCreador_Mdl(self):
		self.Creador= "Domingo Vaca Nives"
		return self.Creador

if __name__ == "__main__":
	funcion= funciones()

	funcion.Titulo("Comprobando el Modulo de Funciones" + funcion.DarVercion_Mdl())
	funcion.ColorDeFont("BASICO")


	funcion.Func("Limpiar")

	funcion.Func("LineaPautada")
	funcion.Centrar("Funcionando Correctamente")
	funcion.Func("LineaPautada")

	print("Acerca del Modulo: ")

	if platform.system() == Sistemas[1]:
		print(f"Sistema en el que corre:", Fore.BLUE + Sistemas[1], Fore.RESET)
	else:
		print("Sistema en que corre:", Fore.RED + Sistemas[0], Fore.RESET)

	print("Version del Modulo: ", Fore.CYAN + funcion.DarVercion_Mdl(), Fore.RESET)
	print("Creado por:", Fore.GREEN + funcion.DarCreador_Mdl(), Fore.RESET )
	funcion.Func("Pausa")
	funcion.Func("Limpiar")
	funcion.Func("Salir")