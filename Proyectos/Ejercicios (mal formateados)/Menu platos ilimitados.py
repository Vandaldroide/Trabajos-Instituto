np = int(input("Cuantos platos quieres añadir? "))
menu = "*"*57+"\n"+"CARTA DEL RESTAURANTE".center(57)+"\n"+"*"*57+\
    "\n"+"Categoria".ljust(37)+"Plato".ljust(10)+"Precio".rjust(10)+"\n"+\
    "*"*57+"\n"
while np>0:
    categoria = input("Ingrese la categoria del plato: ")
    plato = input("Ingrese el nombre del entrante (max 10 caracteres): ")
    precio = input("Ingrese el precio del entrante: ")
    menu = menu+categoria.ljust(37)+plato.ljust(10)+precio.rjust(10)+"\n"
    np = np-1
print(menu)