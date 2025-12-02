if int(input("Cuantos defectuosos a producido: ")) < 200:
    con1 = True
else:
    con1 = False
if int(input("Cuantos tornillos a producido: ")) > 10000:
    con2 = True
else:
    con2 = False
if con1==False and con2==False:
    print("grado 5")
if con1==True and con2==False:
    print("grado 6")
if con1==False and con2==True:
    print("grado 7")
if con1==True and con2==True:
    print("grado 8")