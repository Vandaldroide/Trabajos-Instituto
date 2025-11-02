k = float(input("Cualtos kilos a comprado: "))
if k<=2:
    print("pagas el 100%")
else:
    if k<=5:
        print("pagas el 90%")
    else:
        if k<=10:
            print("pagas el 85%")
        else:
            print("pagas el 80%")