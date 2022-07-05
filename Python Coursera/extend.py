a = ["animales", "Juanito"]
b = ["lucas", "Error"]
c = [100, 200]
a.extend(b)
a.insert(2,c)

primer = a.pop() #Elimina el ultimo elemento
a.remove("lucas")

n = a.index(c)
a = "ssjsk,sss,ssff,dff,fd"
n = a.split(",")


contactos = "Marcelo, Alvaro; Elena, Karen; Jaime; Carmen"
splitted = contactos.split(";")
print(splitted)

a = ["animales", "Juanito"]
b = ["lucas", "Error"]
c = [100, 200]
tempo = a + b + c
print(tempo)

def mostrar_estados_amigos(lista_amigos):
  for amigo in lista_amigos:
    archivo = open(amigo+".user", "r")
    for i in range(7):
      linea = archivo.readline().rstrip()
    print(amigo+":", linea)
    archivo.close()

