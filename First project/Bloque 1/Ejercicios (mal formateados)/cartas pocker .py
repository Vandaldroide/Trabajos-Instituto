import random

na = input("Nombre de jugador a: ")
nb = input("Nombre de jugador b: ")

tca = random.randrange(1,5) #tipo de carta jugador a
nca = random.randrange(1,14) #numero de carta jugador a

if tca == 1: #transformar a string el tipo de carta a
    tcan = "rombos"
elif tca == 2:
    tcan = "treboles"
elif tca == 3:
    tcan = "picas"
else:
    tcan = "corazones"

if tca == 1: #tipo de carta jugador b
    tcb = random.randrange(2,5)
elif tca == 4:
    tcb = random.randrange(1,4)
else:
    tcb = random.randrange(1,tca and tca+1,5 )

if nca == 1: #numero de carta jugador b
    ncb = random.randrange(2,14)
elif nca == 13:
    ncb = random.randrange(1,13)
else:
    ncb = random.randrange(1,nca and nca+1,14 )

if tcb == 1: #transformar a string el tipo de carta b
    tcbn = "rombos"
elif tcb == 2:
    tcbn = "treboles"
elif tcb == 3:
    tcbn = "picas"
else:
    tcbn = "corazones"

print(f"El jugador {na} a sacado la carta {str(nca)} de {tcan}")
print(f"El jugador {nb} a sacado la carta {str(ncb)} de {tcbn}")

if nca == ncb: #Calcular Ganador
    if tca > tcb:
        print(f"a ganado {na}")
    else:
        print(f"a ganado {nb}")
elif nca > ncb:
    print(f"a ganado {na}")
else:
    print(f"a ganado {nb}")