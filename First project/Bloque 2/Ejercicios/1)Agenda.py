import time
flgs = True #flag salir del programa
flge = True #flag comprobar edicion
flgdel = True #flag comprobar eliminacion
menu = 0 #selector de menu
opc = 0 # opcion menu
ce = 0 #Numero de contacto a sustituir
cdel = 0 #numero de contacto a eliminr
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
        contacts.append([input("Introduce el nombre del contacto: "), input("Introduce el numero de telefono: "), input("Introduce el mail: ")])
        menu = 0
    elif menu == 2: #eliminar contacto
        flgdel = True
        while flgdel:
            cdel = input("Introduce el ID del contacto que quieres eliminar: ")
            if cdel.isdigit() and int(cdel) in range(len(contacts)):
                contacts.pop(int(cdel))
                flgdel = False
            else:
                print("Ese ID no es valido")
        menu = 0
    elif menu == 3: #editar contacto
        flge = True
        while flge:
            ce = input("Introduce el ID del contacto que quieres modificar: ")
            if ce.isdigit() and int(ce) in range(len(contacts)):
                contacts.pop(int(ce))
                contacts.insert(int(ce),[input("Introduce el nombre del contacto: "), input("Introduce el numero de telefono: "), input("Introduce el mail: ")])
                flge = False
            else:
                print("Ese ID no es valido")
        menu = 0
    elif menu == 4: #mostrar contactos
        print(
            "Contactos".center(63,"*")+"\n"+
            "ID".ljust(3)+"Nombre".ljust(15)+"Telefono".ljust(15)+"Mail".rjust(30)+"\n"+
            "*"*63+"\n"
        )
        for i in range(len(contacts)):
            print(f"{i})".ljust(3)+contacts[i][0].ljust(15)+contacts[i][1].ljust(15)+contacts[i][2].rjust(30)+"\n")
        print(
            "*"*63 + "\n"
            "Presiona enter para salir"
        )
        input()
        menu = 0
    else: #salir
        flgs = False