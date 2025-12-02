import random
import time
nombre = ""
clase = ""
print(
    "Bienvenido a Arkadia, un mundo de fantasia donde has reencarnado tras ser atropellado por un "+
    "camion, dios te a dado esta oportunidad de tener otra vida, a cambio tendras que "+
    "derrotar al rey demonio en este mundo, ahora dinos tu nuevo nombre y que clase deseas para empezar"+
    "\n\n\n"
)
print(
    "Menu de creacion de Personaje\n"+
    "1) Escoger nombre\n"+
    "2) Escoger Clase\n"+
    "3) Guardar datos"
)
opc = input("Introduce el digito de la opcion: ")
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if  opc > 0 and opc <= 3:

            else:
                print("esa opcion no esta disponible")

                time.sleep(1)