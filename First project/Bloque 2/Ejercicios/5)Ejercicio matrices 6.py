import random
flgp = True #flag para salir de la pregunta del numero
re = 0 #resultado
m = [] #matriz a usar
mc = [] #matriz temporal
while flgp:
    pm = int(input("Introduce el tamaño de la matriz, tiene que ser par: ")) #preguntamos al usuario el tamaño matriz
    if pm%2 == 0:
        flgp = False
    else:
        print("Valor invalido, introduce un numero par")
for i in range(pm):
    m.append([])
    for j in range(pm):
        m[i].append(random.randint(1,99))
        print(str(m[i][j]).rjust(2), end=" ")
for i in range(0,len(m),2):
    mc.append([])
    for j in range(len(m)):
        if j+1%2 == 0:
            re = m[i][j] + m[i+1][j]
            mc[i].append(re)
            re = 0
        else:
            re = m[i][j] + m[i+1][j]
print(mc)
