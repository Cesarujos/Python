from ast import Try
import random
from time import sleep
import os

def arrys_number_random():
    listin = []
    for item in range(0, 10):
        listin.append(str(random.randint(1, 100)))
    return listin

def guardar_archivo(lista):
    nom_archivo = input("Como quieres que se le llame el archivo? : ")
    with open(nom_archivo + ".txt", 'w') as mi_archivo:
        mi_archivo.write('\n'.join(lista)) ###De esta forma no se cierra

def main():
    os.system("clear")
    lista = []
    if input("Te interesa cargar una lista anterior? S/N : ") =="S":
        try:
            with open("Archivo.txt", 'r') as a:
                lista = (a.read().split("\n"))
        except FileNotFoundError: ##GESTIONA LOS ERRORES o EXCEPCIONES
            print("No hay lista anterior!!!")

    lista = arrys_number_random()
    print(",".join(lista)) #Join solo funciona con STR


    a = open("Archivo.txt", 'w')
    a.write("\n".join(lista))
    a.close()

    guardar_archivo(lista)

    datos = open("Datos.txt")
    datos = [row.split(" ") for row in datos.read().split('\n')]
    print(datos[7][4])

    sleep(3)
    os.system("clear")

if __name__ == "__main__":
    main()