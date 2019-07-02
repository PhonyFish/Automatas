# Nombre: listas.py
# Objetivo: muestra el funcionamiento de las listas en python
# Autor: Luis Javier Ortiz Olguin
# Fecha: 02 de julio de 2019

from os import system

#-----------------------------------------------
# Se crea la lista
#-----------------------------------------------
lista = []

#-----------------------------------------------
# Método para crear la lista
#-----------------------------------------------
def agregarItem(dato):
    lista.append(dato)

#-----------------------------------------------
# Método para crear la lista
#-----------------------------------------------
def imprimirLista():
    j=0
    for i in lista:
        print("Item: ",j,", ",i)
        j+=1

#-----------------------------------------------
# Método para eliminar un dato de la lista
#-----------------------------------------------
def eliminarDato(dato):
    if (dato in lista):
        lista.remove(dato)
        print("Dato eliminado")
    else:
        print("Dato no encontrado")

#-----------------------------------------------
# Método principal del programa
#-----------------------------------------------
def main():
    ciclo=True
    while ciclo:
        system("cls")
        print("--- Script para listas ---")
        print("1.- Agregar")
        print("2.- Buscar")
        print("3.- Modificar")
        print("4.- Eliminar")
        print("5.- Imprimir")
        print("6.- Salir")
        opc=int(input("Eliga de 1 - 6: "))
        if opc==1:
            dato=input("Ingrese dato a guardar: ")
            agregarItem(dato)
        elif opc==2:
            print("")
        elif opc==3:
            print("")
        elif opc==4:
            d2=input("Ingrese dato a eliminar: ")
            eliminarDato(d2)
        elif opc==5:
            imprimirLista()
        elif opc==6:
            print("*** Fin del programa ***")
        res=input("¿Otra operación?(s/n)")
        if (res=="S" or res=="s"):
            ciclo=True
        else:
            ciclo=False

if __name__=="__main__":
    main()