p1 = True #flag pregunta personas lista
nn = "" #numero de personas de la lista
li = "" #lista invertida
while p1 == True:
    nn = input("Introduce el numero de personas que quieres listar: ")
    if nn.isdigit():
        nn = int(nn)
        p1 = False
    else:
        print("Valor invalido, introduce un numero entero")
li = input(f"Introduce el nombre de la 1 persona")
for i in range(nn-1):
    li = input(f"Introduce el nombre de la {i + 2} persona") + "," + li
print(li)