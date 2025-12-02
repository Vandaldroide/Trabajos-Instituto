import random
ndig = random.randint(2,10) #random para saber cuantos digitos va a tener la lista
nf = random.randint(2,10)  #numero de filas
list = [] #lista a ordenar
cn = 0 #cache numeros
flgc = False #cambio para parar
for i in range(nf):
    list.append([])
    for j in range(ndig):
        list[i].append(random.randint(0,99))
print(list)
for i in range(len(list)):
    for j in range(len(list[0])):
        flgc = False
        for k in range(len(list[0])-j-1):
            if list[i][k] > list[i][k+1]:
                flgc = True
                cn = list[i][k]
                list[i][k] = list[i][k+1]
                list[i][k+1] = cn
        if not flgc:
            break
for i in range(nf):
    print("\n",end="")
    for j in range(ndig):
        print(f"{list[i][j]}".center(2), end=" ")