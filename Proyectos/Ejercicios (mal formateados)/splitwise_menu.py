flgm = 0
flgg = 0
salir = False
pagador = ""
concepto = ""
cantidad = ""
participantes = ""
filas = ""
gt = float(0)

while not salir:
    if flgm == 0: #Menu Principal
        print(
            "Menu Principal\n"+
            "1) Introducir Gastos\n"+
            "2) Ver Gastos\n"+
            "3) Salir\n"
        )
        opc = input("Introduce el digito de la opcion: ")
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if  opc > 0 and opc <= 3:
                flgm = opc
            else:
                print("esa opcion no esta disponible")
                flgm = 0
                time.sleep(1)
    elif flgm == 1: #Menu Introducir Gastos
        print(
            "Menu Introduccion de Gastos\n" +
            "1)Concepto \n" +
            "2)Pagador \n" +
            "3)Cantidad \n"+
            "4)Deudores \n" +
            "5)Guardar Datos actuales \n" +
            "6)Volver al menu principal \n"
        )
        opc = input("Introduce el digito de la opcion: ")
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if opc == 1:
                concepto = input("Introduce el concepto: ")
            elif opc == 2:
                pagador = input("Introduce el pagador: ")
            elif opc == 3:
                sf = 0
                while not sf:
                    cantidad = input("Introduce la cantidad (solo numeros y punto): ")
                    if cantidad.isdigit():
                        cantidad = float(cantidad)
                        sf = 1
                    else:
                        print("introduce numeros y punto unicamente")
            elif opc == 4:
                participantes = input("Introduce a los participantes: ")
            elif opc == 5:
                datos = f"{pagador}".ljust(15)+f" {concepto}".ljust(15)+f" {cantidad}€".ljust(10)+f" {participantes}".rjust(15)
                print(
                    "estos son los datos: \n"+
                    "*" * 55 + "\n" +
                    "Pagador".ljust(15) + "Concepto".ljust(15) + "Cantidad".ljust(10) + "Participantes".rjust(15) + "\n" +
                    "*" * 55 + "\n" +
                    datos
                )
                flgg = 0
                while not flgg:
                    ps = input("estas seguro de que quieres añadir estos datos? los datos que no hayas introducido quedaran en blanco  (y/n) ")
                    if ps == "y":
                        filas = filas + "\n" + datos
                        print("se han guardado los datos")
                        gt = gt + cantidad
                        datos = " "
                        pagador = " "
                        concepto = " "
                        cantidad = " "
                        participantes = " "
                        time.sleep(1)

                        flgg = 1
                    elif not ps == "n":
                        print("respuesta invalida, escriba y para si y n para no")
                        time.sleep(1)
                    else:
                        print("no se han guardado los datos")
                        time.sleep(1)
                        flgg = 1
            elif opc == 6:
                datos = " "
                flgm = 0
            else:
                print("esa opcion no es valida")
                flgm = 1
                time.sleep(1)
    elif flgm == 2: #Ver Gastos
        print(
            "Gastos".center(55,"*")+"\n"+
            "Pagador".ljust(15)+"Concepto".ljust(15)+"Cantidad".ljust(10)+"Participantes".rjust(15)+"\n"+
            "*"*55+
            filas+"\n"+
            "*" * 55 + "\n" +
            f"Gastos Totales: {gt}€"

        )
        time.sleep(1)
        flgm = 0
    elif flgm == 3: #Salir del programa
        salir = True

print("has salido del programa")