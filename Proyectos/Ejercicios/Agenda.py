flgs = True #flag salir del programa
menu = 0 #selector de menu
opc = 0 # opcion menu
contacts = [] #lista de contactos
while flgs:
    if menu == 0: #menu inicial
        print(
            "Menu Principal\n" +
            "1) Introducir Contacto\n" +
            "2) Eliminar contacto\n" +
            "3) Editar contacto\n" +
            "4) Mostrar constactos\n"+
            "5) Salir\n"
        )
        opc = input(
            "Introduce el digito de la opcion: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
            time.sleep(1)
        else:
            opc = int(opc)
            if opc > 0 and opc <= 5:
                menu = opc
            else:
                print("esa opcion no es valida")
                menu = 0
                time.sleep(1)
    elif menu == 1: #nuevo contacto

    elif menu == 2: #eliminar contacto

    elif menu == 3: #editar contacto

    elif menu == 4: #mostrar contactos

    else: #salir
        flgs = False