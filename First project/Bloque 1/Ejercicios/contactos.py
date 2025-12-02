import time
menu = 0 #selector menu
flgg = False #flag confirmar guardado
flgt = False #flag pregunta telefono
salir = False #flag salir
tlfm = False #saber si el telefono es fijo o movil
nombre = "" #cache del nombre
mail = "" #cache del mail
telefono = "" #cache del telefono
datos = "" #cache de los datos unificados
filas = "" #datos guardados en la tabla
opc = 0 #selector del segundo menu

while not salir:
    if menu == 0: #Menu Principal
        print(
            "Menu Principal\n"+
            "1) Introducir Contacto\n"+
            "2) Ver Contactos\n"+
            "3) Salir\n"
        )
        opc = input("Introduce el digito de la opcion: ") #introducimos la opcion y comprobamos si es valida
        if not opc.isdigit(): #comprueba si es un numero
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else: #si es un numero comprueba que sea una de las opciones
            opc = int(opc)
            if  opc > 0 and opc <= 3:
                menu = opc
            else: #si no dice que es incorrecto y vuelve a preguntar
                print("esa opcion no esta disponible")
                menu = 0
                time.sleep(1)
    elif menu == 1: #Menu Introducir Gastos
        print(
            "Menu Introduccion de Contacto\n" +
            "1)Nombre \n" +
            "2)Telefono \n" +
            "3)Mail \n"+
            "4)Guardar Datos actuales \n" +
            "5)Volver al menu principal \n"
        )
        opc = input("Introduce el digito de la opcion: ") #Misma estructura que el primer menu
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            # apartir de aqui mientras que en el primer menu nos llevava a otro menu o tabla,
            # en este dos da la opcion de introducir el dato y de guardar los que tenemos.
            if opc == 1:
                nombre = input("Introduce el Nombre: ")
            elif opc == 2:
                flgt = False
                while not flgt: #Aqui preguntamos si el telefono es fijo o movil
                    opc = input("Es un telefono fijo o movil?(f/m) ")
                    if opc == "f":
                        flgt = True
                        tlfm = False
                    elif opc == "m":
                        flgt = True
                        tlfm = True
                    else:
                        print("Esa opcion no esta disponible, intoduce f para fijo y m para movil")
                        flgt = False
                telefono = input("Introduce el Telefono: ")
            elif opc == 3:
                mail = input("Introduce el Mail: ")
            elif opc == 4:
                # opcion de guardar, unifica la cache de todos los datos de la forma correcta dependiendo
                # si el telefono es movil o fijo
                # te pregunta que si estas seguro de querer guardarlos si no vuelves al menu, si si,
                # pues los guarda en una nueva fila de la tabla y deja todas las caches vacias.
                if not tlfm:
                    datos = f"{nombre}".ljust(15)+f"{telefono}".ljust(15)+"".ljust(15)+f"{mail}".rjust(25)
                    print( #te dice los datos que vas a guardar
                        "estos son los datos: \n"+
                        "*" * 55 + "\n" +
                        "Nombre".ljust(15) + "Telefono Fijo".ljust(15) + "Mail".rjust(25) + "\n" +
                        "*" * 55 + "\n" +
                        f"{nombre}".ljust(15)+f"{telefono}".ljust(15)+f"{mail}".rjust(25)
                    )
                else:
                    datos = f"{nombre}".ljust(15)+"".ljust(15)+f"{telefono}".ljust(15)+f"{mail}".rjust(25)
                    print( #te dice los datos que vas a guardar
                        "estos son los datos: \n"+
                        "*" * 55 + "\n" +
                        "Nombre".ljust(15) + "Telefono Movil".ljust(15) + "Mail".rjust(25) + "\n" +
                        "*" * 55 + "\n" +
                        f"{nombre}".ljust(15)+f"{telefono}".ljust(15)+f"{mail}".rjust(25)
                    )
                flgg = False
                while not flgg: #pregunta estas seguro de guardarlo
                    ps = input("estas seguro de que quieres añadir estos datos? los datos que no hayas introducido quedaran en blanco  (y/n) ")
                    if ps == "y":
                        filas = filas + "\n" + datos
                        print("se han guardado los datos")
                        datos = " "
                        nombre = " "
                        telefono = " "
                        mail = " "
                        time.sleep(1)

                        flgg = True
                    elif ps == "n":
                        print("no se han guardado los datos")
                        time.sleep(1)
                        flgg = True
                    else:
                        print("respuesta invalida, escriba y para si y n para no")
                        time.sleep(1)
            elif opc == 5: #vuelves al menu principal
                datos = " "
                menu = 0
            else: #error de opcion
                print("esa opcion no es valida")
                menu = 1
                time.sleep(1)
    elif menu == 2: # Tabla para ver Contactos
        print(
            "Contactos".center(70,"*")+"\n"+
            "Nombre".ljust(15)+"Telefono Fijo".ljust(15)+"Telefono Movil".ljust(15)+"Mail".rjust(25)+"\n"+
            "*"*70+
            filas+"\n"+
            "*" * 70 + "\n"
        )
        time.sleep(1)
        menu = 0
    elif menu == 3: #Salir del programa
        salir = True

print("has salido del programa")