import time
menu = 0 #selector menu
flgg = True #flag confirmar guardado
flgs = True #flag salir
flgcon = True #flag concepto
flgq = True #flag cantidad
con = "" #cache concepto
can = 0 #cache cantidad
sav = "" #respuesta usuario a si guardar
filas = "" #datos guardados en la tabla
ng = 0 #contador de guiones
opc = 0 #selector del segundo menu
gt = 0 #gastos totales
idat = 0 #numero del string que inicia el dato
exp = False #identificador de si es expense o income
while flgs:
    if menu == 0: #Menu Principal
        print(
            "1) View Expenses\n"+
            "2) New Expenses\n"+
            "3) New Income\n"+
            "4) Exit"
        )
        opc = input("Option: ") #introducimos la opcion y comprobamos si es valida
        if not opc.isdigit(): #comprueba si es un numero
            print("Not Numeric Option")
            time.sleep(1)
        else: #si es un numero comprueba que sea una de las opciones
            opc = int(opc)
            if  opc > 0 and opc <= 4:
                menu = opc
            else: #si no dice que es incorrecto y vuelve a preguntar
                print("Option Out Of Range")
                menu = 0
                time.sleep(1)
    elif menu == 1:  # Ver gastos
        print(
            "My Expenses".center(60,"*")+"\n"+
            "Concept".ljust(30)+"Income".ljust(15)+"Expense".rjust(15)+"\n"+
            "*"*60
        )
        if len(filas) > 1:
            ng = 0
            idat = 0
            exp = False
            for i in range(0,len(filas)):
                if filas[i] == "-":
                    if ng == 0:
                        ng += 1
                        print(f"{filas[idat:i]}".ljust(30), end="")
                        idat = i + 1
                        if filas[idat] == "0":
                            print("".ljust(15), end="")
                            exp = True
                            idat += 3
                    elif ng == 1 and exp == False:
                        ng += 1
                        print(f"{filas[idat:i]}".ljust(15)+"".rjust(15))
                    elif ng == 2 and exp == True:
                        ng += 1
                        idat += 1
                elif filas[i] == ";":
                    if exp == True:
                        print(f"{filas[idat-1:i]}".rjust(15))
                    ng = 0
                    exp = False
                    idat = i + 1
                    print("\n", end="")
        print(
            "-" * 60 + "\n" +
            "Total Gastos".ljust(30) + f"{gt}".rjust(30) + "\n"
        )
        input("Enter to continue")
        menu = 0
    elif menu == 2: #Introducir gastos
        flgcon = True
        while flgcon:
            con = input("New Concept:\n")
            if con == "":
                print("Invalid Concept")
            else:
                flgcon = False
        flgq = True
        while flgq:
            can = input("New Amount:\n")
            if can == "":
                print("Invalid Amount")
            else:
                flgq = False
                can = float(can)

        sav = input("Do you want to save the following expense?Y/n \n"
                    f"{con}".ljust(15)+f"{can}".rjust(15)+"\n")
        if sav == "Y" or sav == "y":
            filas += f"{con}-0-{can};"
            gt += can
            con = ""
            can = ""
            print("Saved")
        else:
            print("Not Saved")
        menu = 0
    elif menu == 3:  # Introducir ingreso
        flgcon = True
        while flgcon:
            con = input("New Concept:\n")
            if con == "":
                print("Invalid Concept")
            else:
                flgcon = False
        flgq = True
        while flgq:
            can = input("New Amount:\n")
            if can == "":
                print("Invalid Amount")
            else:
                flgq = False
                can = float(can)

        sav = input("Do you want to save the following income?Y/n \n"
                    f"{con}".ljust(15)+f"{can}".rjust(15)+"\n")
        if sav == "Y" or sav == "y":
            filas += f"{con}-{can}-0;"
            gt -= can
            con = ""
            can = ""
            print("Saved")
        else:
            print("Not Saved")
        menu = 0
    elif menu == 4:  # Salir
        flgs = False