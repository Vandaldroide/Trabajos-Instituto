import random
m = [] #matriz resultado
flgp = True #Flag tamaño matriz
while flgp:
    pm = input("Introduce el tamaño de la matriz, tiene que ser par: ") #preguntamos al usuario el tamaño matriz
    if pm.isdigit():
        pm = int(pm)
        flgp = False
    else:
        print("Valor invalido, introduce un numero")
for i in range(pm):
    m.append([])
    print("\n")
    for j in range(pm):
        m[i].append(random.randint(1,99))
        print(str(m[i][j]).rjust(2), end=" ")
# Si alguien copia esto solo tiene que saber que el programa te preguntara el tamaño de la matriz, la prinetara y la tendras en la variable m