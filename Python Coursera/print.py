#Importar modulos
from random import randint as naturalAleatorio

x = naturalAleatorio(1,20)
print(x)

def funcion_misteriosa(x):
  c=0
  while x!=0:
    c+=1
    x = x//10
  return c

a = funcion_misteriosa(32344)
def funcion(x,y):
  return (x-8)*(y**2)

def mayor(edad):
  return edad >= 18
a = mayor(22)
print(a)

def sumador(n, sumando):
  sumando += 1
  n += sumando
  return n
b = 9
sumador(5, b)


def funcion(x):
  n = 3
  return bool(x%n)
print(funcion(9))
print(funcion(10))

def funcion(n):
  a = n ** 3
  b = a ** 2
  c = b + 100
  d = 5 * c
  return print(d)

d = funcion(2)

print(d)

from math import gcd
x = gcd(6, 11)
print(x)

def panprimo(n):
  es_primo = True
  primo = n%1000
  for i in range(2, primo):
    if(primo%i == 0):
      es_primo = False
      break
  cadena = str(n)
  es_pan = True
  for i in range(10):
    if str(i) not in cadena:
      es_pan = False
      break
  if es_pan and es_primo:
    return True
  return False
print(panprimo(10123485769))

def opcion_menu():
  opcion = int(input("Ingresa opción desde 0 a N-1: "))
  while opcion < 0 or opcion > N-1:
    print("Inténtalo otra vez.")
    opcion = int(input("Ingresa opción desde 0 a N-1: "))
  return opcion

opcion_menu(3)

def remover_enesimo(s, n):
  resultado = s[:n]+s[n+1:]
  return resultado # aquí debes retornar el resultado

print(remover_enesimo("Hasta luego",3))

archivo = open("luc.txt","r")
a = archivo.read()
print(a)