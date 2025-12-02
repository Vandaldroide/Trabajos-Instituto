import random
m = [] #matriz a usar
opc = 0 #opcion del usuario
mc = [] #matriz temporal
flgs = True #flag para salir
pm = [int(input("Cuantas filas quieres que tenga la matriz? ")), int(input("Cuantas columnas quieres que tenga la matriz? "))]  #preguntamos al usuario el tamaño matriz
for i in range(pm[0]): #generamos la tabla
    m.append([])
for i in range(pm[0]):
    for j in range(pm[1]):
        m[i].append(random.randint(1,99))
for i in range(len(m)):
    print(m[i]) #imprimimos la tabla
while flgs:
    if opc == 0:
        print ( #Mostramos el menu
            "Menu\n"+
            "1) Imprimir filas impares\n"+
            "2) Imprimir Columnas pares\n"+
            "3) Imprimir coordenadas que la suma de sus indices sea multiplo de 3\n"+
            "4) Imprimir Columna 2 al reves\n"+
            "5) Salir\n"
        )
        opc = input("Introduce el digito de la opcion: ") # Preguntamos al usuario que quiere hacer
        if opc.isdigit():
            opc = int(opc)
        else:
            print("Opcion no valida, introduce un numero")
        mc = []
    elif opc == 1: #Imprime filas impares
        for i in range(len(m)): #bucle que se repite la cantidad de filas que tengas
            if not (i+1)%2 == 0: #si las filas + 1 (para que la primera fila sea 1 y no 0 etc) es impar se printea
                print(m[i])
        opc = 0
    elif opc == 2: #imprime columnas pares
        for i in range(len(m)):
            mc.append([])
        for i in range(len(m[1])):
            if (i+1)%2 == 0:
                for j in range(len(m)):
                        mc[j].append(m[j][i])
        for i in range(len(mc)):
            print(mc[i])
        opc = 0
    elif opc == 3: #imprime datos en coordenadas que la suma de sus ejes sea multiplo de 3
        for i in range(len(m)):
            mc.append([])
        for i in range(len(m)):
            for j in range(len(m[i])):
                if (j+i)%3 == 0:
                    mc[j].append(m[j][i])
                else:
                    mc[j].append("-")
        for i in range(len(mc)):
            print(mc[i])
        opc = 0
    elif opc == 4: #imprime la segunda columna al reves
        for i in range(len(m)):
            print([m[len(m)-i-1][1]])
        opc = 0
    elif opc == 5:#salimos del programa
        flgs = False
    else: #si el usuario no a intrducido un valor valido se lo dice y vuelve al menu
        print("Opcion no valida")
        opc = 0
print("Has salido del programa")