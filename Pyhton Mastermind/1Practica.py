import random # Libreria del random

a =int(input("Inserta un número \n"
            "El numero que tu gustes: ")) #\n significa que das enter
b = random.randint(1, 10) #Se pone el minimo y el maximo

if( a > 100 or a < 0): 
    print("Error")
elif (a>9): 
    print("Soy guapo")
else:
    print("La suma de los números {} y {} es: {}".format(a, b, a+b))


#Type devuelve el tipo de lo que le enviemos
type(a)

#La cantidad de caracteres que esta compuesto algo
letras = "\nJuanito alcachofa es una persona con cara de un dinosaurio"
nletras = len(letras)
print(letras + '\n' +'-'*nletras + '\n')

#Convertir cadena de texto en arrays
palabras = letras.split(" ")
print(palabras)

#String multilinea
print("""Hab\ia
sakdjlksdksd
sadkns,fdsal""")
