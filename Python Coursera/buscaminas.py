tablero = [[' ', 'X', ' ', 'X'],['X', ' ', ' ', ' '],[' ', 'X', 'X', ' '],['X', ' ', ' ', 'X']]
def buscaminas (tablero, i, j):
    coord = [i,j]
    alrededor = []

    if i == 0:
        min_i = 0
        max_i = i + 1
    elif i == len(tablero[0])-1:
        max_i = i
        min_i = i -1
    
    else:
        min_i = i - 1
        max_i = i + 1
    
    if j == 0:
        min_j = 0
        max_j = j + 1
    elif j == len(tablero)-1:
        max_j = j
        min_j = j -1
    
    else:
        min_j = j - 1
        max_j = j + 1


    for item in range(min_i, max_i+1):
        for jtem in range(min_j, max_j+1):
            alrededor.append([item, jtem])
    alrededor.remove([i,j])
    
    contador = 0
    for item in alrededor:
        if tablero[item[0]][item[1]]=='X':
            contador +=1
    return contador

n = buscaminas(tablero, 0, 0)
print(n)