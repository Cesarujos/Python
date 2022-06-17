from time import sleep
import os

def fibonacci (n): #RECURSIVIDAD DE FIBONACCI
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def medir_largos(iterable, *arg): #RESTO DE ARGUMENTOS #TUPLAS
    if arg:
        largos = [len(iterable)]
        for a in arg:
            largos.append(len(a))
        return largos
    else:
        return len(iterable)

def main():

    ################FIBONACCI

    cantidad = int(input("Inserta la cantidad de numero para la secuencia de Fibonacci: "))
    for cant in range(cantidad):
        print(fibonacci(cant))
    sleep(2)
    os.system("clear")

    #################### SI PUSIERAMOS MAS ARGUMENTOS 

    print(medir_largos("Mi nimbre es juanito alcachofa", "y soy feo", "con cara de oso"))
    print(medir_largos("Calla Bruto"))

if __name__ == "__main__":
    main()
