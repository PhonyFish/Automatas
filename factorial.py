# Nombre: factorial.py
# Objetivo: Conseguir el factorial de un numero
# Autor: Luis Javier Ortiz Olguin
# Fecha: 01 de julio de 2019

import math

def main():
    num=float(input("Ingresa un número: "))
    print("El factorial es: ", math.factorial(num))

if __name__=="__main__":
    main()