import random
pu = 0 #puntos del usuario
pb = 0 #puntos de la maquina
tu = 0 #eleccion usuario
tb = 0 #eleccion maquina
nu = "" #que ha sacado en texto el usuario
bu = "" #que a sacado en texto el bot
rv = 1 #contador para el while,como las rondas no cuentan si se empata no uso for
flgp = True #flag para comprobar si la opcion del usuario es correcta
print("Bienvenido a piedra,papel o tijeras al mejor de 3, empecemos!!!")
#El usuario y el bot introducen su opcion
while rv < 4:
    flgp = True
    while flgp == True:
        tu = input("Que quieres tirar? Piedra(1) Papel(2) Tijeras(3): ")
        if tu.isdigit():
            tu = int(tu)
            if tu > 0 or tu < 4:
                flgp = False
            else:
                print("El valor no es valido")
        else:
            print("El valor no es valido")
    tb = random.randrange(1,4)
    #asignamos el string depende de lo que se haya escogido
    if tu == 1:
        nu = "Piedra"
    elif tu == 2:
        nu = "Papel"
    elif tu == 3:
        nu = "Tijeras"
    if tb == 1:
        bu = "Piedra"
    elif tb == 2:
        bu = "Papel"
    elif tb == 3:
        bu = "Tijeras"
    #Calculamos el ganador de la ronda y si es empate la ronda se repite
    if tu == tb:
        print(f"habeis sacado los dos {nu}, se repite la ronda")
    elif tu == 1 and tb == 3:
        pu += 1
        print(f"Ronda {rv} has sacado {nu} y el bot {bu}, has ganado \n"
            f"Has ganado {pu} ronda/s y el bot {pb} ronda/s"
            )
        rv += 1
    elif tu == 2 and tb == 1:
        pu += 1
        print(f"Ronda {rv} has sacado {nu} y el bot {bu}, has ganado \n"
            f"Has ganado {pu} ronda/s y el bot {pb} ronda/s"
            )
        rv += 1
    elif tu == 3 and tb == 2:
        pu += 1
        print(f"Ronda {rv} has sacado {nu} y el bot {bu}, has ganado \n"
            f"Has ganado {pu} ronda/s y el bot {pb} ronda/s"
            )
        rv += 1
    elif tb == 1 and tu == 3:
        pb += 1
        print(f"Ronda {rv} has sacado {nu} y el bot {bu}, has perdido \n"
            f"Has ganado {pu} ronda/s y el bot {pb} ronda/s"
            )
        rv += 1
    elif tb == 2 and tu == 1:
        pb += 1
        print(f"Ronda {rv} has sacado {nu} y el bot {bu}, has perdido \n"
            f"Has ganado {pu} ronda/s y el bot {pb} ronda/s"
            )
        rv += 1
    elif tb == 3 and tu == 2:
        pb += 1
        print(f"Ronda {rv} has sacado {nu} y el bot {bu}, has perdido \n"
            f"Has ganado {pu} ronda/s y el bot {pb} ronda/s"
            )
        rv += 1
#Printeamos quien a ganado
if pu > pb:
    print("Has ganado al bot!!!!")
else:
    print("Has perdido...")