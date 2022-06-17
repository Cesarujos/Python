from ast import While
import readchar
import os
import random

POS_X = 0
POS_Y = 1
MAP_WITH = 20
MAP_HEIGHT = 15


my_position = [3,5]
tail_lenght = 0
tail= []
map_object = []

while len(map_object) < 20:
    new_position = [random.randint(0, MAP_WITH-1), random.randint(0, MAP_HEIGHT)]
    if new_position not in map_object and new_position != my_position:
        map_object.append(new_position)


#direction = input("Donde te quieres mover? [W][A][S][D]: ")
while True:

    print("+" + "-"*MAP_WITH *3 + "+")
    for coodinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WITH):
            char_draw = "  "
            object_in_cell = None
            tail_in_cell = None
            for obstacule in map_object:
                if obstacule[POS_X] == coordinate_x and obstacule[POS_Y]==coodinate_y:
                    char_draw = "❤️ "
                    object_in_cell = obstacule
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y]==coodinate_y:
                    char_draw = '😃'
                    tail_in_cell = tail_piece
            if my_position[POS_X] == coordinate_x and my_position[POS_Y]==coodinate_y:
                char_draw = "😃"
                if object_in_cell:
                    map_object.remove(object_in_cell)
                    tail_lenght +=1
                if tail_in_cell:
                    print("Has muerto")
                    break
            print(" {}".format(char_draw), end='')
        print("|", end="\n")
    print("+" + "-"*MAP_WITH *3+ "+")


    direction = readchar.readchar() #Decode se pude usar en windows, en linux ya te entrega decodificado
    os.system("clear")
    if direction == 'w':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] -=1
    elif direction == 's':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_Y] +=1
    elif direction == 'a':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] -=1
    elif direction == 'd':
        tail.insert(0, my_position.copy())
        tail = tail[:tail_lenght]
        my_position[POS_X] +=1
    elif direction == 'q':
        break

    if my_position[POS_X] == 20:
        my_position[POS_X] = 0
    if my_position[POS_Y] == 15:
        my_position[POS_Y] = 0
    if my_position[POS_X] == -1:
        my_position[POS_X] = 19
    if my_position[POS_Y] == -1:
        my_position[POS_Y] = 14
