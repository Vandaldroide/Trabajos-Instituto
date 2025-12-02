import random
ndig = random.randint(2,10) #random para saber cuantos digitos va a tener la lista
list = [] #lista a ordenar
cn = 0 #cache numeros
flgc = False #cambio para parar
for i in range(ndig):
    list.append(random.randint(0,99))
print(list)
for i in range(len(list)):
    flgc = False
    for j in range(len(list)-i-1):
        print(f"Comparamos {list[j]} y {list[j+1]}")
        if list[j] > list[j+1]:
            flgc = True
            cn = list[j]
            list[j] = list[j+1]
            list[j+1] = cn
    if not flgc:
        break
    print("*"*30)
print(list)