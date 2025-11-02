import random
flgda = False #flag para saber si los dados de a son iguales
flgdb = False #flag para saber si los dados de a son iguales
flgp = True #flag para saber si hay que seguir preguntando por los dados
na = input("Nombre de jugador a: ")
nb = input("Nombre de jugador b: ")
a1 = random.randrange(1,7)
a2 = random.randrange(1,7)
print("dado 1 de "+na+":"+str(a1),"dado 2 de "+na+":"+str(a2))
while flgp:
    p = input("si quieres cambiar el dado 1 responde 1 si quieres cambiar el dado 2 responde 2 si no quieres cambiar ningun dado responde 0: ")
    if p == "1":
        a1 = random.randrange(1,7)
        print("el nuevo numero del dado 1 es:"+str(a1))
        flgp = False
    elif p == "2":
        a2 = random.randrange(1,7)
        print("el nuevo numero del dado 2 es:"+str(a2))
        flgp = False
    elif p == "0":
        flgp = False
        print("no has cambiado ningun dado")
    else:
        print("valor no valido")
b1 = random.randrange(1,7)
b2 = random.randrange(1,7)
print("dado 1 de "+nb+":"+str(b1),"dado 2 de "+nb+":"+str(b2))
flgp = True
while flgp:
    p = input("si quieres cambiar el dado 1 responde 1 si quieres cambiar el dado 2 responde 2 si no quieres cambiar ningun dado responde 0: ")
    if p == "1":
        b1 = random.randrange(1,7)
        print("el nuevo numero del dado 1 es:"+str(b1))
        flgp = False
    elif p == "2":
        b2 = random.randrange(1,7)
        print("el nuevo numero del dado 2 es:"+str(b2))
        flgp = False
    elif p == "0":
        flgp = False
        print("no has cambiado ningun dado")
    else:
        print("valor no valido")
if a1 == a2:
    flgda = True
at = a1 + a2
if b1 == b2:
    flgdb = True
bt = b1 + b2
if at > bt:
    if flgda == flgdb:
        print("a ganado "+na)
    elif flgdb:
        print("a ganado "+na)
    else:
        print("a ganado "+nb)
elif at < bt:
    if flgda == flgdb:
        print("a ganado "+nb)
    elif flgda:
        print("a ganado "+nb)
    else:
        print("a ganado "+na)
else:
    if flgda == flgdb:
        print("han empatado")
    elif flgda:
        print("a ganado "+nb)
    else:
        print("a ganado "+na)