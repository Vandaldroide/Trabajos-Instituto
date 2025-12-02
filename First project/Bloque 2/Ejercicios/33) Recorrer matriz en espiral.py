from operator import truediv

matriz = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
posicion = [0,0]
print("Matriz orignial".center(25,"*"), end="")
for i in range(len(matriz)):
    print("\n")
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]}".center(4), end=" ")
limit_izq = 0
limit_der = len(matriz[0]) - 1
limit_sup = 0
limit_inf = len(matriz) - 1
lista = []
while True:
    for i in range(limit_izq, limit_der):
        lista.append(matriz[limit_sup][i])
    for i in range(limit_sup, limit_inf):
        lista.append(matriz[i][limit_der])
    for i in range(limit_der, limit_izq-1,-1):
        lista.append(matriz[limit_inf][i])
    if limit_sup != (len(matriz)-1)//2:
        for i in range(limit_inf-1, limit_sup,-1):
            lista.append(matriz[i][limit_izq])
    else:
        break
    limit_izq += 1
    limit_der -= 1
    limit_sup += 1
    limit_inf -= 1

print("\n",lista)
