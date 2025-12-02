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
for i in range(len(list[0])):
    for j in range(len(list)):
        flgc = False
        for k in range(len(list)-1,j,-1):
            if list[k][i] < list[k-1][i]:
                flgc = True
                cn = list[k][i]
                list[k][i] = list[k-1][i]
                list[k-1][i] = cn
        if not flgc:
            break
for i in range(nf):
    print("\n",end="")
    for j in range(ndig):
        print(f"{list[i][j]}".center(2), end=" ")