#Nombre: circunferencia.py
#Objetivo: calcula el área y diametro de una circunferencia e import math
#Autor: Luis Javier Ortiz Olguin
#Fecha: 01 de julio de 2019

import math as mat
from os import system

#------------------------------
# Funcion para calcular area
#------------------------------

def calcularArea(r):
	area=mat.pi*(mat.pow(r,2))
	return area

#------------------------------
# Funcion para calcular area
#------------------------------

def calcularDiametro(r):
	diam=r*2
	return diam

def main():
	ciclo=True
	while (ciclo):
		system('cls')
		print("-- Script para calcular área de circunferencia --")
		radio=float(input("Introduce el valor del radio: "))
		#Invocar un método
		print("El área es: ",calcularArea(radio))
		print("El diamtetro es: ",calcularDiametro(radio))
		res=input("¿Otro calculo?(s/n)\n")
		if (res=="S" or res=="s"):
			ciclo=True
		else:
			ciclo=False
	else:
		print("***Fin de programa")

if __name__ == "__main__":
	main()