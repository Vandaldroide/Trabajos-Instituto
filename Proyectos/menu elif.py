print("Menu".center(10, "*"))
print("escribe 1 para escojer manzanas")
print("escribe 2 para escojer peras")
opcion = int(input("Escribe el numero deseado: "))
if opcion == 1:
    print("has escogido manzanas manzanas")
    print("la quieres pelada(1) o con piel (2)?")
    opcion = int(input("Escribe el numero deseado: "))
    if opcion == 1:
        print("has escogido manzana pelada")
    elif opcion == 2:
        print("has escogido manzana con piel")
    else:
        print("has introducido una opcion no valida")
elif opcion == 2:
    print("has escogido peras")
    print("la quieres pelada(1) o con piel (2)?")
    opcion = int(input("Escribe el numero deseado: "))
    if opcion == 1:
        print("has escogido pera pelada")
    elif opcion == 2:
        print("has escogido pera con piel")
    else:
        print("has introducido una opcion no valida")
else:
    print("has introducido una opcion no valida")