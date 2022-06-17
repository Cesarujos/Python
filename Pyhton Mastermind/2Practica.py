import os

print("CALCULADORA DE FACTORIAL\n")
numero =int(input("Inserta un numero: "))
x = 1
factorial = 1
while numero >= x:
    factorial *= x
    x +=1
print(factorial)

input("Enter para continuar ...")
os.system("clear")

###################### WHILE
print("CALCULADORA DE FABONACCI\n")
fibonacci = int(input("Inserta un numero : "))
n = 1
a = 1
b = 1
print(a,end=" ")
print(b,end=" ")
while fibonacci -2 >= n :
    suma = a + b
    if n != fibonacci - 2:
        print(suma,end=" ")
    else:
        print(suma)
    a = b
    b = suma
    n +=1

input("Enter para continuar ...")
os.system("clear")


####################### LISTAS
print("ARRAYS\n")
lista = [1, 2, 3, 4]
permanecer = True
while permanecer:
    numerito = int(input('Inserta un número causa: '))
    if numerito in lista: #Lo contrario seria not in
        print("Numero encontrado")
    else:
        print("Numero NO encontrado")
        lista.append(numerito) #Agregar un numero a un array
        print("Se agrego el numero a la lista")
        print("Hay {} numero en la lista".format(len(lista)))
    salir = input(" ¿Quieres salir del programa? (Y) \t : ")
    if salir == 'Y':
            permanecer = False
 
lista.pop() #Quitar el ultimo al array       

input("Enter para continuar ...")

################## FOR
lista2 = [2, 4, 6, 13, 5, 10, 5]
suma = 0     
for item in lista2:
    suma = suma + item
print(suma)

n_repeat = int(input("Inserta el nuemro se repeticiones: "))
for repeat in range(n_repeat):
    print("Eres cabro", end=" ")
input("\nEnter para continuar ...")

####### RANGE
listarange = list(range(3, 6))
print(listarange)


#######LIST COMPRENHESION
palabras = "2,4,4,45,6,7,8,5,10,4,4,3,3,1"
lista_numeros = [int(numero) for numero in palabras.split(",")]
print(lista_numeros)

##### LIST FILTER
print(lista_numeros[1:5])

### NUMERO MAYOR Y MENOR
mayor = lista_numeros[0]
menor = lista_numeros[0]
for numero in lista_numeros:
    if mayor < numero:
        mayor = numero
    if menor > numero:
        menor = numero
print("El mayor es: {} y el menor es {}. ".format(mayor, menor))

#### ORDENAR EN PYTHON
lista_numeros.sort()
lista_ordenada = lista_numeros
print(lista_ordenada)