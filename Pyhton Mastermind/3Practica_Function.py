
###FUNCIONES
def my_function (argumento):
    print("Hola, me podrias decir tu nombre?")
    name = input("->>>")
    array_name = list(name)
    array_name_contrario = []
    for letra in array_name:
        array_name_contrario.insert(0, letra.upper())
    name_contrario = "".join(array_name_contrario)
    argumento = argumento[::-1] #Sirve para darle vuelta a un string
    print("Hola {}, mi nombre es {}. ".format(name_contrario, argumento))
my_function("ALCACHOFA")