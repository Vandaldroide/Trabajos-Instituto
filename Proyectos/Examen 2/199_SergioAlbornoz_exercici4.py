import random
ncb = "" #numero de carta jugador 2
ntca = "" #string tipo de carta jugador 1
ntcb = "" #string tipo de carta jugador 2
tca = random.randint(1,2) #tipo de carta jugador 1
nca = random.randint(1,10) #numero de carta jugador 1
tcb = random.randint(1,2) #tipo de carta jugador 2
if tca == tcb:
    ncb = random.randint(1,9)
    if ncb >= nca:
        ncb += 1
else:
    ncb = random.randint(1,10)
if tca == 1:
    ntca = "blau"
else:
    ntca = "vermell"
if tcb == 1:
    ntcb = "blau"
else:
    ntcb = "vermell"
print(f"Jugador 1 escull a l'atzar la carta {nca}-{ntca}")
print(f"Jugador 2 escull a l'atzar la carta {ncb}-{ntcb}")
if tca == 1 and nca == 1:
    print("Jugador 1 guanya la partida")
elif tcb == 1 and ncb == 1:
    print("Jugador 2 guanya la partida")
elif  tca == tcb:
    if nca > ncb:
        print("Jugador 1 guanya la partida")
    else:
        print("Jugador 2 guanya la partida")
elif tca == 2:
    print("Jugador 1 guanya la partida")
else:
    print("Jugador 2 guanya la partida")