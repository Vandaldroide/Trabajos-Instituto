import random
ndig = random.randint(2,10) #random para saber cuantos digitos va a tener la lista
list = [] #lista a ordenar
cn = 0 #cache numeros
for i in range(ndig):
    list.append(random.randint(0,99))
print(list)
for i in range(len(list)):
    for j in range(len(list)-1-i):
        if list[i] > list[i+j+1]:
            cn = list[i]
            list[i] = list[i+j+1]
            list[i+j+1] = cn
print(list)