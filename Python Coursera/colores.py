def color_frecuente(lista): # debes modificar todos los elementos de la función
# cuidando el retorno, nombre y argumentos
    azul = 0
    verde = 0
    rojo = 0
    amarillo = 0
    for i in lista:
        if i == 'azul':
            azul +=1
        if i == 'rojo':
            rojo +=1
        if i == 'verde':
            verde +=1
        if i == 'amarillo':
            amarillo +=1
    orden = [[azul,"azul"],[verde, "verde"],[rojo,"rojo"],[amarillo,"amarillo"]]
    orden.sort()
    colores = []
    for item in orden:
        if orden[3][0] == item[0]:
            colores.append(item[1])
    if 'azul' in colores:
        return ('azul', orden[3][0],)
    if 'rojo' in colores:
        return ('rojo', orden[3][0],)
    if 'verde' in colores:
        return ('verde', orden[3][0])
    if 'amarillo' in colores:
        return ('amarillo', orden[3][0])

print(color_frecuente(['rojo', 'rojo', 'azul', 'azul']))