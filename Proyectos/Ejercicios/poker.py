import random
na = input("Introduce el nombre del jugador 1: ") #Nombre jugador 1
nb = input("Introduce el nombre del jugador 2: ") #Nombre jugador 2
tpa = 0 #tipo de pareja jugador 1 (1 nada,2 pareja de letras, 3 pareja de numeros)
tpb = 0 #tipo de pareja jugador 2 (1 nada,2 pareja de letras, 3 pareja de numeros)
cga = 0 #carta mas grande del par 1
cgb = 0 #carta mas grande del par 1
flga = True #flag para la pregunta de repetir carta 1
flgb = True #flag para la pregunta de repetir carta 2
flgar = "" #Variable respuesta 1
flgbr = "" #Variable respuesta 2
flgaa = True #flag para la pregunta cual carta repetir 1
flgbb = True #flag para la pregunta cual carta repetir 2
ca1 = random.randint(1,13) #Carta 1 Jugador 1
ca2 = random.randint(1,13) #Carta 2 Jugador 1
cb1 = random.randint(1,13) #Carta 1 Jugador 2
cb2 = random.randint(1,13) #Carta 2 Jugador 2
if ca1 in range(1,11): #transforma los numeros a letras si corresponde
    nca1 = ca1
elif ca1 == 11:
    nca1 = "J"
elif ca1 == 12:
    nca1 = "Q"
elif ca1 == 13:
    nca1 = "K"
if ca2 in range(1,11):
    nca2 = ca2
elif ca2 == 11:
    nca2 = "J"
elif ca2 == 12:
    nca2 = "Q"
elif ca2 == 13:
    nca2 = "K"
if cb1 in range(1,11):
    ncb1 = cb1
elif cb1 == 11:
    ncb1 = "J"
elif cb1 == 12:
    ncb1 = "Q"
elif cb1 == 13:
    ncb1 = "K"
if cb2 in range(1,11):
    ncb2 = cb2
elif cb2 == 11:
    ncb2 = "J"
elif cb2 == 12:
    ncb2 = "Q"
elif cb2 == 13:
    ncb2 = "K"
while flga: #le dice al jugador 1 que cartas tiene y si quiere cambiarlas
    flgar = input(f"{na} has sacado {nca1} y {nca2} quieres cambiar una carta? (y/n) ")
    if flgar == "y":
        while flgaa:
            flgar = input("Que carta quieres cambiar la 1º o la 2ª? (1/2)")
            if flgar == "1":
                ca1 = random.randint(1, 13)  # Carta 1 Jugador 1
                if ca1 in range(1, 11):
                    nca1 = ca1
                elif ca1 == 11:
                    nca1 = "J"
                elif ca1 == 12:
                    nca1 = "Q"
                elif ca1 == 13:
                    nca1 = "K"
                print(f"la nueva carta es {nca1}")
                flga = False
                flgaa = False
            elif flgar == "2":
                ca2 = random.randint(1, 13)  # Carta 2 Jugador 1
                if ca2 in range(1, 11):
                    nca2 = ca2
                elif ca2 == 11:
                    nca2 = "J"
                elif ca2 == 12:
                    nca2 = "Q"
                elif ca2 == 13:
                    nca2 = "K"
                print(f"la nueva carta es {nca2}")
                flga = False
                flgaa = False
            else:
                print("Valor no valido introduce 1 o 2")
    elif flgar == "n":
        flga = False
    else:
        print("Valor no valido introduce y para si y n para no")
while flgb: #le dice al jugador 2 que cartas tiene y si quiere cambiarlas
    flgbr = input(f"{nb} has sacado {ncb1} y {ncb2} quieres cambiar una carta? (y/n) ")
    if flgbr == "y":
        while flgbb:
            flgbr = input("Que carta quieres cambiar la 1º o la 2ª? (1/2)")
            if flgbr == "1":
                cb1 = random.randint(1, 13)  # Carta 1 Jugador 2
                if cb1 in range(1, 11):
                    ncb1 = cb1
                elif cb1 == 11:
                    ncb1 = "J"
                elif cb1 == 12:
                    ncb1 = "Q"
                elif cb1 == 13:
                    ncb1 = "K"
                print(f"la nueva carta es {ncb1}")
                flgb = False
                flgbb = False
            elif flgbr == "2":
                cb2 = random.randint(1, 13)  # Carta 2 Jugador 2
                if cb2 in range(1, 11):
                    ncb2 = cb2
                elif cb2 == 11:
                    ncb2 = "J"
                elif cb2 == 12:
                    ncb2 = "Q"
                elif cb2 == 13:
                    ncb2 = "K"
                print(f"la nueva carta es {ncb2}")
                flgb = False
                flgbb = False
            else:
                print("Valor no valido introduce 1 o 2")
        flgb = False
    elif flgbr == "n":
        flgb = False
    else:
        print("Valor no valido introduce y para si y n para no")

if ca1 == ca2: #comprueba el tipo de pareja y quien es mejor para que gane
    tpa = 3
elif ca1 in range(11,14) and ca2 in range(11,14):
    tpa =2
else:
    tpa = 1
if cb1 == cb2:
    tpb = 3
elif cb1 in range(11,14) and cb2 in range(11,14):
    tpb = 2
else:
    tpb = 1
if tpa > tpb:
    print(f"Ha ganado {na}")
elif tpa < tpb:
    print(f"Ha ganado {nb}")
else: #si es el tipo de pareja es igual, cogemos la carta mas grande de cada uno y la comparamos, el mas grande gana, si son iguales es empate
    if ca1 > ca2:
        cga = ca1
    else:
        cga = ca2
    if cb1 > cb2:
        cgb = cb1
    else:
        cgb = cb2
    if cga > cgb:
        print(f"Ha ganado {na}")
    elif cga < cgb:
        print(f"Ha ganado {nb}")
    else:
        print(f"Ha habido un empate")