import random
re = 0 #resultado
m = [] #matriz a usar
mc = [] #matriz temporal
pm = [int(input("Cuantas filas quieres que tenga la matriz? ")), int(input("Cuantas columnas quieres que tenga la matriz? "))]  #preguntamos al usuario el tamaño matriz
for i in range(pm[0]):
    m.append([])
    for j in range(pm[1]):
        m[i].append(random.randint(1,99))
        print(str(m[i][j]).rjust(2), end=" ")
    print()

if len(m) < len(m[0]):
    dd = len(m)
else:
    dd = len(m[0])

for i in range(dd):
    print(m[i][i], end=" ")
    re += m[i][i]

print("\n\n"+str(re))