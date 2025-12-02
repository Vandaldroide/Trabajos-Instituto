import random
f = 8 #filas del tablero
c = 4 #columnas del tabero
tablero = [] #matriz tablero ^nave *marciano !disp_mar ¡disp_nav
est_game = 0 #estado partida 0 en curso, 1 perdida, 2 ganada
prov_disp = 8
#crear tablero inicial
for i in range(2):
    tablero.append([])
    for j in range(c):
        tablero[i].append("*")
for i in range(f):
    tablero.append([])
    for j in range(c):
        tablero[i].append(" ")
print (tablero)
#funcion printear tablero
for i in range(f):
    print("\n",end="")
    for j in range(c):
        print(tablero[i][j],end=" ")

#bucle juego
while est_game == 0:
    for i in range(1):
        est_game = 1