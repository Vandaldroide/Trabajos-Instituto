import random
p1 = 0 #puntos jugador 1
p2 = 0 #puntos jugador 2
t1 = 0 #puntos de esta tirada jugador 1
t2 = 0 #puntos de esta tirada jugador 2
nt1 = 0 #numero de tiradas jugador 1
nt2 = 0 #numero de tiradas jugador 2
flgcpt1 = True #Flag para comprobar el y/n jugador 1
flgcpt2 = True #Flag para comprobar el y/n jugador 2
flgpv = True #flag para el la puntuacion maxima
flgcp1 = True #el jugador 1 quiere seguir jugando
flgcp2 = True #el jugador 1 quiere seguir jugando
while flgpv:
    pv = input("Introduce que puntuacion maxima quieres: ") #puntuacion limite para el juego
    if pv.isdigit():
        pv = int(pv)
        flgpv = False
    else:
        print("Solo son validos numeros")
n1 = input("Introduce el nombre del jugador 1: ") #nombre jugador 1
n2 = input("Introduce el nombre del jugador 2: ") #nombre jugador 2
while  (p1 <= pv and p2 <= pv) and not (flgcp1 == False and flgcp2 == False):
    flgcpt1 = True
    flgcpt2 = True
    while flgcpt1 and flgcp1:
        flgcp1 = input(f"{n1} quieres tirar esta ronda? (y/n) ")
        if flgcp1 == "y":
            flgcp1 = True
            flgcpt1 = False
        elif flgcp1 == "n":
            flgcp1 = False
            flgcpt1 = False
        else:
            print("Valor no valido introduce y para si y n para no")
    while flgcpt2 and flgcp2:
        flgcp2 = input(f"{n2} quieres tirar esta ronda? (y/n) ")
        if flgcp2 == "y":
            flgcp2 = True
            flgcpt2 = False
        elif flgcp2 == "n":
            flgcp2 = False
            flgcpt2 = False
        else:
            print("Valor no valido introduce y para si y n para no")
    if flgcp1 == True:
        t1 = random.randrange(1,7)
        p1 += t1
        nt1 += 1
    else:
        t1 = "no a tirado"
    if flgcp2 == True:
        t2 = random.randrange(1,7)
        p2 += t2
        nt2 += 1
    else:
        t2 = "no a tirado"
    print(f"{n1} a sacado {t1} y ahora tiene {p1} puntos \n"+
        f"{n2} a sacado {t2} y ahora tiene {p2} puntos"
        )
if p1 > pv and p2 < pv:
    print(f"A ganado {n2} por pasarse {n1} de puntos")
elif p1 < pv and p2 > pv:
    print(f"A ganado {n1} por pasarse {n2} de puntos")
elif p1 > pv and p2 > pv:
    print(f"Empate por pasarse ambos")
elif p1 > p2:
    print(f"A ganado {n1} por mayor puntuacion")
elif p2 > p1:
    print(f"A ganado {n2} por mayor puntuacion")
elif p1 == p2 :
    if nt1 > nt2:
        print(f"A ganado {n2} por menor numero de tiradas")
    elif nt1 < nt2:
        print(f"A ganado {n2} por menor numero de tiradas")
    else:
        print("Empate en todos los aspectos")
print ("FIN DEL JUEGO")