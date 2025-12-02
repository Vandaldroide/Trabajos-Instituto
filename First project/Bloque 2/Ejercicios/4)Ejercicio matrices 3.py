import random
m = [] #matriz a usar
mc = [] #matriz temporal
pm = [int(input("Cuantas filas quieres que tenga la matriz? ")), int(input("Cuantas columnas quieres que tenga la matriz? "))]  #preguntamos al usuario el tamaño matriz
for i in range(pm[0]): #generamos la tabla
    m.append([])
for i in range(pm[0]):
    for j in range(pm[1]):
        m[i].append(random.randint(1,99))
for i in range(len(m)):
    print(m[i]) #imprimimos la tabla
for i in range(len(m[0])):
    mc.append(0)
    for j in range(len(m)):
        if (j+1)%2 == 0:
            mc[i] += m[i][j]
print(mc)