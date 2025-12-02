m = [[5,7,4],[5,6,28],[9,5,6]] #matriz a usar
opc = 0 #opcion del usuario
mc = [] #matriz temporal
for k in range(len(m)):
    print(m[k])
print (
    "Menu\n"+
    "1) Imprimir filas impares\n"+
    "2) Imprimir Columnas pares\n"+
    "3) Imprimir coordenadas que la suma de sus indices sea multiplo de 3\n"
)
opc = input("Introduce el digito de la opcion: ")
if opc.isdigit():
    opc = int(opc)
    if opc == 1:
        for i in range(len(m)):
            if not (i+1)%2 == 0:
                print(m[i])
    elif opc == 2:
        for n in range(len(m)):
            mc.append([])
        for i in range(len(m[1])):
            if (i+1)%2 == 0:
                for j in range(len(m)):
                        mc[j].append(m[j][i])
        for l in range(len(mc)):
            print(mc[l])
    elif opc == 3:
        for n in range(len(m)):
            mc.append([])
        for i in range(len(m)):
            for j in range(len(m[i])):
                if (j+i)%3 == 0:
                    mc[j].append(m[i][j])
                else:
                    mc[j].append("-")
        for l in range(len(mc)):
            print(mc[l])
    else:
        print("Opcion no valida se cierra el programa")
else:
    print("Opcion no valida se cierra el programa")