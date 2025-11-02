import time
menu = 0 #selector de menu
opc = 0 #Selector de opciones
flgs = False #flag para salir del programa
flgg = True #flag para la confirmacion del guardado
flgsd = True #flag para salir del menu de datos
filas = "" #datos de las ventas guardadas
datos = "" #datos unificados en cache
modelo = "" #dato del modelo en cache
precio = "" #dato del precio en cache
gs = 0 #suma total de suzuki
gh = 0 #suma total honda
while not flgs:
    if menu == 0: #Menu Principal
        print(
            "Menu Principal\n"+
            "1) Introducir Venta Suzuki\n"+
            "2) Introducir Compra Honda\n"+
            "3) Ver Ventas\n"+
            "4) Salir\n"
        )
        opc = input("Introduce el digito de la opcion: ")#le pedimos al usuario la opcion que quiere y confirmamos que sea valida
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if  opc > 0 and opc <= 4:
                menu = opc
            else:
                print("esa opcion no es valida")
                menu = 0
                time.sleep(1)
    elif menu == 1: #menu datos suzuki
        print(
            "Menu Introduccion de Ventas Suzuki\n" +
            "1)Modelo \n" +
            "2)Precio \n" +
            "3)Guardar Datos actuales \n" +
            "4)Volver al menu principal \n"
        )
        #selecionas que quieres hacer
        opc = input("Introduce el digito de la opcion: ")
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if opc == 1:#las dos primeras opciones introducen los datos
                 modelo = input("Introduce el modelo: ")
            elif opc == 2:
                flgt = True
                while flgt:
                    precio = input("Introduce el precio(solo numeros enteros): ")
                    if precio.isdigit():#nos aseguramos de que el precio sea un numero
                        precio = int(precio)
                        flgt = False
                    else:
                        print("El precio no es valido porfabor intrduce solo numeros enteros")
            elif opc == 3: #con esta opcion se guardan los datos
                datos = f"{modelo}".ljust(15)+f" {precio}".ljust(15) #juntamos los datos en una sola variable
                print(
                    "estos son los datos: \n"+
                    "*" * 30 + "\n" +
                    "Modelo".ljust(15) + "Precio".rjust(15)+ "\n" +
                    "*" * 30 + "\n" +
                    f"{modelo}".ljust(15) + f" {precio}".rjust(15)
                )
                flgg = True
                while flgg: #le hemos mostrado los datos al usuario ahora confirmamos si los quiere guardar o aun no
                    ps = input("estas seguro de que quieres añadir estos datos? los datos que no hayas introducido quedaran en blanco  (y/n) ")
                    if ps == "y":
                        filas = filas + "\n" + datos
                        print("se han guardado los datos")
                        gs = gs + precio
                        datos = " "
                        modelo = " "
                        precio = 0
                        time.sleep(1)
                        flgg = False
                    elif not ps == "n":
                        print("respuesta invalida, escriba y para si y n para no")
                        time.sleep(1)
                    else:
                        print("no se han guardado los datos")
                        time.sleep(1)
                        flgg = False
            elif opc == 4: #con esta opcion se sale y se borran los datos
                flgsd = True
                while flgsd:
                    ps = input("estas seguro que quieres salir? los datos que hayas intoducido se borraran (y/n) ")
                    if ps == "y":
                        modelo = " "
                        precio = 0
                        datos = " "
                        menu = 0
                        flgsd = False
                    else:
                        flgsd = False
            else:
                print("esa opcion no es valida")
                menu = 1
                time.sleep(1)
    elif menu == 2:#menu datos honda, es una copia del de suziki con el texto y las variables cambiadas por la versiones de honda
        print(
            "Menu Introduccion de Ventas Honda\n" +
            "1)Modelo \n" +
            "2)Precio \n" +
            "3)Guardar Datos actuales \n" +
            "4)Volver al menu principal \n"
        )
        opc = input("Introduce el digito de la opcion: ")
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if opc == 1:
                 modelo = input("Introduce el modelo: ")
            elif opc == 2:
                flgt = True
                while flgt:
                    precio = input("Introduce el precio(solo numeros enteros): ")
                    if precio.isdigit():
                        precio = int(precio)
                        flgt = False
                    else:
                        print("El precio no es valido porfabor intrduce solo numeros enteros")
            elif opc == 3:
                datos = f"{modelo}".ljust(15)+f" {precio}".rjust(30)
                print(
                    "estos son los datos: \n"+
                    "*" * 30 + "\n" +
                    "Modelo".ljust(15) + "Precio".rjust(15)+ "\n" +
                    "*" * 30 + "\n" +
                    f"{modelo}".ljust(15)+f" {precio}".rjust(15)
                )
                flgg = True
                while flgg:
                    ps = input("estas seguro de que quieres añadir estos datos? los datos que no hayas introducido quedaran en blanco  (y/n) ")
                    if ps == "y":
                        filas = filas + "\n" + datos
                        print("se han guardado los datos")
                        gh = gh + precio
                        datos = " "
                        modelo = " "
                        precio = 0
                        time.sleep(1)
                        flgg = False
                    elif not ps == "n":
                        print("respuesta invalida, escriba y para si y n para no")
                        time.sleep(1)
                    else:
                        print("no se han guardado los datos")
                        time.sleep(1)
                        flgg = False
            elif opc == 4:
                flgsd = True
                while flgsd:
                    ps = input("estas seguro que quieres salir? los datos que hayas intoducido se borraran (y/n) ")
                    if ps == "y":
                        modelo = " "
                        precio = 0
                        datos = " "
                        menu = 0
                        flgsd = False
                    else:
                        flgsd = False
            else:
                print("esa opcion no es valida")
                menu = 2
                time.sleep(1)
    elif menu == 3: #opcion para Ver ventas
        print(
            "Ventas".center(45,"*")+"\n"+
            "Modelo".ljust(15)+"Precio Suzuki".ljust(15)+"Precio Honda".rjust(15)+"\n"+
            "*"*45+
            filas+"\n"+
            "*"*45 + "\n"
            "Suma".ljust(15)+f"Suzuki:{gs}".ljust(15)+f"Honda: {gh}".rjust(15)+"\n\n"+
            "Presiona enter para salir"
        )
        input()
        menu = 0
    elif menu == 4: #Salir del programa
        flgs = True
    else: #Simplemente esta linea es para prevenir bugs
        menu = 0

print("has salido del programa")