dict_characters = {
    1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" :7,"experience": 0},
    2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience":0},
    3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" :6,"experience": 0 },
    4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4,"experience" : 0},
    5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience": 0},
    6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5,"experience" : 0},
    7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3,"experience" : 0},
    8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1,"experience" : 0},
    9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4,"experience" : 0},
    10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8,"experience" : 0},
    11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4,"experience" : 0},
    12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3,"experience" : 0},
    13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5,"experience" : 0},
    14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4,"experience" : 0},
    15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4,"experience" : 0}
}
dict_weapons = {
    1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
    2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
    3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
    4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
    5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
}
dict_crews = {
    1 : {"name" : "Straw hat","members": [8,6]},
    2 : {"name" : "Pirates Buggy","members": [1,3,5]},
    3 : {"name": "Pirates Rocks","members": [2,4,7,]}
}
dict_ranks = {
    1 : {"name" : "Admiral","members": [9,10,11]},
    2 : {"name" : "ViceAdmiral","members": [12,13]},
    3 : {"name": "Lieutenant","members": [14,15]}
}
dict_categorys = {
    1:"Straw hat",
    2:"Pirates Buggy",
    3:"Pirates Rocks",
    4:"Admiral",
    5:"ViceAdmiral",
    6:"Lieutenant"
}

#Todo lo anterior son dicccionarios dados por el profe

#Variables varias
menu = 0 #selector de menu
opc = 0 #Selector de opciones
ide = 0 #ID del personaje o objeto a editar
avw = [] #Aviable weapons
dsum = dict_characters.copy() #Copia del diccionario de personajes donde se suman sus stats con la de sus arma
itc = [] # Weapons equiped
list = []  # lista a ordenar

#Caches
ns = 0 #Cache new speed/strength
cn = "" #Cache nombre Create
cws = 0 #Cache weapon strength
cwsp = 0 #Cache weapon speed
cwh = False #Cache weapon hand

#Flags
flgc = False #flag para parar el ordenado
flgs = False #flag para salir del programa
flggb = False #flag go back
flggb_ = False #flag go back anidado
flggb__ = False #flag go back 2 anidao
flggna = False #flag para saber si el valor no esta disponible

while not flgs:
    flggb = False
    if menu == 0: #Menu Principal
        print(
            "Menu 0 (OnePice)".center(30, "=")+"\n"+
            "1) Create\n"+
            "2) Edit\n"+
            "3) List\n"+
            "4) Exit\n"
        )
        opc = input("Introduce el digito de la opcion: ")#le pedimos al usuario la opcion que quiere y confirmamos que sea valida
        if not opc.isdigit():
            print("Invalid Option".center(30, "="))
            input("press enter to continue...")
        else:
            opc = int(opc)
            if  opc > 0 and opc <= 4:
                menu = opc
            else:
                print("Invalid Option".center(30, "="))
                input("press enter to continue...")
    elif menu == 1: #Menu Create
        flggb = False
        flggb_ = False
        flggb__ = False
        print(
            "Menu 02 Create".center(30, "=") + "\n" +
            "1) Create character\n" +
            "2) Create weapon\n" +
            "3) Go Back\n"
        )
        opc = input("Introduce el digito de la opcion: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
        if not opc.isdigit():
            print("Invalid Option".center(30, "="))
            input("press enter to continue...")
        else:
            opc = int(opc)
            if opc == 1: #Create character
                print("Menu 02 Create".center(30, "=") + "\n")
                cn = input("Name of the new character: ")
            elif opc == 2:#Create weapon
                cn = input("Name of the new weapon: ")
                while not flggb:
                    print("Weapon Strength 1-9: \n")
                    cws = input("->Strength: ")
                    if cws.isdigit():
                        cws = int(cws)
                        if cws > 0 and cws < 10:
                            flggb = True
                        else:
                            print("Invalid Option".center(30, "="))
                            input("press enter to continue...")
                    else:
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                while not flggb_:
                    print("Weapon Speed 1-9: ")
                    cwsp = input("->Speed: \n")
                    if cwsp.isdigit():
                        cwsp = int(cws)
                        if cwsp > 0 and cwsp < 10:
                            flggb_ = True
                        else:
                            print("Invalid Option".center(30, "="))
                            input("press enter to continue...")
                    else:
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                while not flggb__:
                    print("Kind of weapon:\n"
                        "1)One hand\n"
                        "2)Two hands\n")
                    opc = input("->Option: \n")
                    if opc.isdigit():
                        opc= int(opc)
                        if opc == 1:
                            cwh = False
                            flggb__ = True
                        elif opc == 2:
                            cwh = True
                            flggb__ = True
                        else:
                            print("Invalid Option".center(30, "="))
                            input("press enter to continue...")
                    else:
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                flggb__ = False
                while not flggb__:
                    print(
                        f"Name: {cn}\n"+
                        f"Strength: {cws}\n"+
                        f"Speed: {cwsp}\n"+
                        f"Two hands type: {cwh}"
                    )
                    opc = input("Save this weapon S/N: ")
                    if opc == "s" or opc == "S":
                        dict_weapons[int(len(dict_weapons) + 1)] = {"name": f"{cn}", "strength": cws, "speed": cwsp,"two_hand": cwh}
                        flggb__ = True
                    elif opc == "n" or opc == "N":
                        flggb__ = True
                    else:
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
            elif opc == 3:#Go Back
                menu = 0
            else:
                print("Invalid Option".center(30, "="))
                input("press enter to continue...")
    elif menu == 2: #Menu Edit
        flggb = False
        flggb_ = False
        flggb__ = False
        print(
            "Menu 03 (Edit Menu)".center(30, "=") + "\n" +
            "1) Edit character\n" +
            "2) Edit weapon\n" +
            "3) Go Back\n"
        )
        opc = input("Introduce el digito de la opcion: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
        if not opc.isdigit():
            print("Invalid Option".center(30, "="))
            input("press enter to continue...")
        else:
            opc = int(opc)
            if opc == 1: #Edit character
                for i in range(1,len(dict_characters)+1):
                    if len(dict_characters[i]["weapons"]) == 1:
                        print(f"ID:{i}, Name:{dict_characters[i]["name"]} Category:{dict_characters[i]["category"]} Weapons:{dict_weapons[dict_characters[i]["weapons"][0]]["name"]} Strength:{dict_characters[i]["strength"]} Speed:{dict_characters[i]["speed"]} Experience:{dict_characters[i]["experience"]}\n")
                    else:
                        print(f"ID:{i}, Name:{dict_characters[i]["name"]} Category:{dict_characters[i]["category"]} Weapons:{dict_weapons[dict_characters[i]["weapons"][0]]["name"]},{dict_weapons[dict_characters[i]["weapons"][1]]["name"]} Strength:{dict_characters[i]["strength"]} Speed:{dict_characters[i]["speed"]} Experience:{dict_characters[i]["experience"]}\n")
                while not flggb:
                    ide = input("ID to edit: ")  # le pedimos al usuario el id que quiere y confirmamos que sea valida
                    if not ide.isdigit():
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                    elif int(ide) in range(1,len(dict_characters)+1):
                        ide = int(ide)
                        flggb = True
                    else:
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                while not flggb_:
                    flggb_ = False
                    flggb__ = False
                    print(
                        f"Select feature to edit to character ID:{ide} Name:{dict_characters[ide]["name"]} \n\n" +
                        "1) Name\n" +
                        "2) Weapon\n" +
                        "3) Go Back\n"
                    )
                    opc = input("->Option: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
                    if not opc.isdigit():
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                    elif not int(ide) in range(1, len(dict_characters) + 1):
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                    else:
                        opc = int(opc)
                        if opc == 1:  # Edit Name
                            dict_characters[ide]["name"] = input("Enter the new name:")
                        elif opc == 2: # Edit Weapon
                            while not flggb__:
                                avw = []
                                print("Available Weapons".center(30, "=")+"\n")
                                if len(dict_characters[ide]["weapons"]) == 0:
                                    for i in range(1, len(dict_weapons) + 1):
                                        print(f"{i}) Name:{dict_weapons[i]["name"]} Strength:{dict_weapons[i]["strength"]} Speed:{dict_weapons[i]["speed"]} Two Hands:{dict_weapons[i]["two_hand"]}\n")
                                        avw.append(i)
                                elif len(dict_characters[ide]["weapons"]) == 1:
                                    if dict_weapons[dict_characters[ide]["weapons"][0]]["two_hand"] == True:
                                        print("none".center(30, "=")+"\n")
                                    else:
                                        for i in range(1, len(dict_weapons) + 1):
                                            if dict_weapons[i]["two_hand"] == False:
                                                print(f"{i}) Name:{dict_weapons[i]["name"]} Strength:{dict_weapons[i]["strength"]} Speed:{dict_weapons[i]["speed"]} Two Hands:{dict_weapons[i]["two_hand"]}\n")
                                                avw.append(i)
                                else:
                                    print("none".center(30, "=")+"\n")
                                print("Character Weapons".center(30, "=")+"\n")
                                for i in range(len(dict_characters[ide]["weapons"])):
                                    print (f"{dict_characters[ide]["weapons"][i]}) {dict_weapons[dict_characters[ide]["weapons"][i]]["name"]} Strength:{dict_weapons[dict_characters[ide]["weapons"][i]]["strength"]} Speed:{dict_weapons[dict_characters[ide]["weapons"][i]]["speed"]}")
                                if len(dict_characters[ide]["weapons"]) == 0:
                                    print("none".center(30, "=") + "\n")
                                print("\n Add Weapons: ID (positive)\n Delete Weapons: ID (negative)\n Exit: 0\n")
                                opc = input("->Option: ")
                                if not opc.isdigit() and opc[0] != "-":
                                    print("Invalid Option".center(30, "="))
                                    input("press enter to continue...")
                                elif int(opc) == 0:
                                    opc = int(opc)
                                    flggb__ = True
                                else:
                                    flggna = False
                                    opc = int(opc)
                                    for i in range(len(avw)):
                                        if avw[i] == opc:
                                            dict_characters[ide]["weapons"].append(avw[i])
                                            flggna = True
                                    if not flggna and not len(dict_characters[ide]["weapons"]) == 0:
                                        for i in range(len(dict_characters[ide]["weapons"])):
                                            if dict_characters[ide]["weapons"][i] == -opc:
                                                dict_characters[ide]["weapons"].pop(i)
                                                flggna = True
                                    if not flggna:
                                        print("Invalid Option".center(30, "="))
                                        input("press enter to continue...")
                        else:
                            flggb_ = True
            elif opc == 2:#Edit weapon
                flggb = False
                flggb_ = False
                flggb__ = False
                for i in range(1,len(dict_weapons)+1):
                    print(f"ID:{i}, Name:{dict_weapons[i]["name"]} Strength:{dict_weapons[i]["strength"]} Speed:{dict_weapons[i]["speed"]} Two Hands:{dict_weapons[i]["two_hand"]}\n")
                while not flggb:
                    ide = input("ID to edit: ")  # le pedimos al usuario el id que quiere y confirmamos que sea valida
                    if not ide.isdigit():
                        print("Invalid Option".center(30,"="))
                        input("press enter to continue...")
                    elif int(ide) in range(1,len(dict_weapons)+1):
                        ide = int(ide)
                        flggb = True
                    else:
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                while not flggb_:
                    flggb__ = False
                    print(
                        "\nMenu 032X (Weapon Feature to Edit)".center(30, "=")+"\n"+
                        "1) Name"+"\n"+
                        "2) Plus Strength"+"\n"+
                        "3) Plus speed"+"\n"+
                        "4) Go Back" + "\n"
                        )
                    print(f"Select feature to edit to weapon ID: {ide}, Name: {dict_weapons[ide]["name"]}")
                    opc = input("->Option: ")
                    if not opc.isdigit():
                        print("Invalid Option".center(30, "="))
                        input("press enter to continue...")
                    else:
                        opc = int(opc)
                        if opc > 0 and opc <= 4:
                            if opc == 1: #Name
                                dict_weapons[ide]["name"] = input("Enter the new name: ")
                            elif opc == 2: #Plus Strength
                                while not flggb__:
                                    ns = input("Enter the new strength: ")
                                    if ns.isdigit():
                                        ns = int(ns)
                                        if ns > 0 and ns < 10:
                                            dict_weapons[ide]["strength"] = ns
                                            flggb__ = True
                                        else:
                                            print("Invalid Option".center(30, "="))
                                            input("press enter to continue...")
                                    else:
                                        print("Invalid Option".center(30, "="))
                                        input("press enter to continue...")
                            elif opc == 3: #Plus speed
                                while not flggb__:
                                    ns = input("Enter the new speed: ")
                                    if ns.isdigit():
                                        ns = int(ns)
                                        if ns > 0 and ns < 10:
                                            dict_weapons[ide]["speed"] = ns
                                            flggb__ = True
                                        else:
                                            print("Invalid Option".center(30, "="))
                                            input("press enter to continue...")
                                    else:
                                        print("Invalid Option".center(30, "="))
                                        input("press enter to continue...")
                            else: #Go Back
                                flggb_ = True
                        else:
                            print("Invalid Option".center(30, "="))
                            input("press enter to continue...")

            elif opc == 3:#Go Back
                menu = 0
            else:
                print("Invalid Option".center(30, "="))
                input("press enter to continue...")
    elif menu == 3:#Menu List
        flggb = False

        print(
            "Menu 04 (List)".center(30, "=") + "\n" +
            "1) List character\n" +
            "2) List weapon\n" +
            "3) Go Back\n"
        )
        opc = input(
            "Introduce el digito de la opcion: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
        if not opc.isdigit():
            print("Introduce un digito, el texto no es valido")
        else:
            opc = int(opc)
            if opc == 1: #List character
                dsum = dict_characters.copy()
                for i in dsum:  # esto suma los valores de los items a los del personaje
                    if len(dsum[i]["weapons"]) != 0:
                        itc = dsum[i]["weapons"]
                        for j in itc:
                            dsum[i]["strength"] += dict_weapons[j]["strength"]
                            dsum[i]["speed"] += dict_weapons[j]["speed"]
                list = []  # lista a ordenar
                for i in dsum:  # esto crea una lista con los personages que definira en que orden se printearan
                    print(i)
                    list.append(i)
                while not flggb:
                    print(
                        "Menu 41 (List Character)".center(30, "=") + "\n" +
                        "1) List by ID\n" +
                        "2) List by Name\n" +
                        "3) List by Strength\n"+
                        "4) List by Speed\n"+
                        "5) Go Back\n"
                    )
                    opc = input(
                        "Introduce el digito de la opcion: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
                    if not opc.isdigit():
                        print("Introduce un digito, el texto no es valido")
                    else:
                        opc = int(opc)
                        if opc == 1: #List character by ID
                            print(
                                "Characters ordered by Id".center(56,"=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".ljust(10) + "experience".rjust(10) + "\n" +
                                "*" * 56
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if list[j] > list[j + 1]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dsum)):
                                    print(f"{list[i]}".ljust(10) +
                                          f"{dsum[list[i]]["name"]}".ljust(16) +
                                          f"{dsum[list[i]]["strength"]}".ljust(10) +
                                          f"{dsum[list[i]]["speed"]}".ljust(10) +
                                          f"{dsum[list[i]]["experience"]}".rjust(10)
                                          )
                            print("\n")
                        elif opc == 2: #List character by Name
                            print(
                                "Characters ordered by Name".center(56, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".ljust(10) + "experience".rjust(10) + "\n" +
                                "*" * 56
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if dsum[list[j]]["name"] > dsum[list[j + 1]]["name"]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dsum)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dsum[list[i]]["name"]}".ljust(16) +
                                      f"{dsum[list[i]]["strength"]}".ljust(10) +
                                      f"{dsum[list[i]]["speed"]}".ljust(10) +
                                      f"{dsum[list[i]]["experience"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 3: #List character by Strength
                            print("Characters ordered by Strength".center(56, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".ljust(10) + "experience".rjust(10) + "\n" +
                                "*" * 56
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if dsum[list[j]]["strength"] > dsum[list[j + 1]]["strength"]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dsum)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dsum[list[i]]["name"]}".ljust(16) +
                                      f"{dsum[list[i]]["strength"]}".ljust(10) +
                                      f"{dsum[list[i]]["speed"]}".ljust(10) +
                                      f"{dsum[list[i]]["experience"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 4: #List character by Speed
                            print("Characters ordered by Speed".center(56, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".ljust(10) + "experience".rjust(10) + "\n" +
                                "*" * 56
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if dsum[list[j]]["speed"] > dsum[list[j + 1]]["speed"]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dsum)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dsum[list[i]]["name"]}".ljust(16) +
                                      f"{dsum[list[i]]["strength"]}".ljust(10) +
                                      f"{dsum[list[i]]["speed"]}".ljust(10) +
                                      f"{dsum[list[i]]["experience"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 5: # Go Back
                            flggb = True
                        else:
                            print("Invalid Option".center(30, "="))
                            input("press enter to continue...")
            elif opc == 2:#List weapon
                list = []  # lista a ordenar
                for i in dict_weapons:  # esto crea una lista con las ar,as que definira en que orden se printearan
                    print(i)
                    list.append(i)
                while not flggb_:
                    print(
                        "Menu042 (List weapon)".center(30, "=") + "\n" +
                        "1) List by ID\n" +
                        "2) List by Name\n" +
                        "3) List by Strength\n" +
                        "4) List by Speed\n" +
                        "5) Go Back\n"
                    )
                    opc = input(
                        "Introduce el digito de la opcion: ")  # le pedimos al usuario la opcion que quiere y confirmamos que sea valida
                    if not opc.isdigit():
                        print("Introduce un digito, el texto no es valido")
                    else:
                        opc = int(opc)
                        if opc == 1: #List weapon by ID
                            print(
                                "Weapons ordered by Id".center(46, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".rjust(10)+  "\n" +
                                "*" * 46
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if list[j] > list[j + 1]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dict_weapons)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["name"]}".ljust(16) +
                                      f"{dict_weapons[list[i]]["strength"]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["speed"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 2: #List weapon by Name
                            print(
                                "Weapons ordered by Name".center(46, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".rjust(10) + "\n" +
                                "*" * 46
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if dict_weapons[list[j]]["name"] > dict_weapons[list[j + 1]]["name"]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dict_weapons)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["name"]}".ljust(16) +
                                      f"{dict_weapons[list[i]]["strength"]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["speed"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 3: #List weapon by Strength
                            print(
                                "Weapons ordered by Strength".center(46, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".rjust(10) + "\n" +
                                "*" * 46
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if dict_weapons[list[j]]["strength"] > dict_weapons[list[j + 1]]["strength"]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dict_weapons)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["name"]}".ljust(16) +
                                      f"{dict_weapons[list[i]]["strength"]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["speed"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 4: #List weapon by Speed
                            print(
                                "Weapons ordered by Speed".center(46, "=") + "\n" +
                                "id".ljust(10) + "name".ljust(16) + "strength".ljust(10) + "speed".rjust(10) + "\n" +
                                "*" * 46
                            )
                            for i in range(len(list)):  # por ultimo esto ordena la lista
                                flgc = False
                                for j in range(len(list) - i - 1):
                                    if dict_weapons[list[j]]["speed"] > dict_weapons[list[j + 1]]["speed"]:
                                        flgc = True
                                        cn = list[j]
                                        list[j] = list[j + 1]
                                        list[j + 1] = cn
                                if not flgc:
                                    break
                            for i in range(len(dict_weapons)):
                                print(f"{list[i]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["name"]}".ljust(16) +
                                      f"{dict_weapons[list[i]]["strength"]}".ljust(10) +
                                      f"{dict_weapons[list[i]]["speed"]}".rjust(10)
                                      )
                            print("\n")
                        elif opc == 5: # Go Back
                            flggb_ = True
                        else:
                            print("esa opcion no es valida")
            elif opc == 3:#Go Back
                menu = 0
    elif menu == 4:  # Salir del programa
        flgs = True
    else:  # Simplemente esta linea es para prevenir bugs
        menu = 0