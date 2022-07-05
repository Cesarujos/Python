from dataclasses import replace


a = "Hola. Mi nombre es César, ¿cual es tu nombre?"
a = a.lower().strip(".") ##Solo borra si estan al inicio o al final

x = "abracadabra pata de cabra"
y = x.strip("a")
z = y.upper()

a = a.replace("a", "😊")
print(a)

def reemplazo(string):
  for i in string:
    if i.isupper():
      string = string.replace(i,"$")
  return string # aquí debes retornar el resultado

print(reemplazo("Viva la Vida"))