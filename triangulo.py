# Nombre: triangulo.py
# Objetivo: Identifica el tipo de triangulo de acuerdo al valor de sus lados
# Autor: Luis Javier Ortiz Olguin
# Fecha: 01 de julio de 2019

#--------------------------------------------
# Funcion para identificar tipo de triangulo
#--------------------------------------------
def identificar(l1,l2,l3):
    perimetro=l1+l2+l3
    #Equilatero
    if (l1==l2==l3):
        print("El triangulo es equilatero y su perimetro es: ", perimetro)
    elif (l1!=l2!=l3):
        print("El triangulo es escaleno y su perimetro es: ", perimetro)
    else:
        print("El triangulo es isosceles y su perimetro es: ", perimetro)
   
def main():
    print("-- Script para identificar triangulos --")
    l1=float(input("Introduce lado 1: "))
    l2=float(input("Introduce lado 2: "))
    l3=float(input("Introduce lado 3: "))

    #invocar funcion
    identificar(l1,l2,l3)

if __name__=="__main__":
    main()