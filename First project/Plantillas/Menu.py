menu = 0 #selector de menu
opc = 0 #Selector de opciones
flgs = False #flag para salir del programa
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
        else:
            opc = int(opc)
            if  opc > 0 and opc <= 4:
                menu = opc
            else:
                print("esa opcion no es valida")
                menu = 0

    elif menu == 4:  # Salir del programa
        flgs = True
    else:  # Simplemente esta linea es para prevenir bugs
        menu = 0