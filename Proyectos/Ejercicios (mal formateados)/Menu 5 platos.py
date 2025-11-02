entrante=input("Ingrese el nombre del entrante (max 10 caracteres): ")
pentrante=input("Ingrese el precio del entrante: ")
principal=input("Ingrese el nombre del plato principal(max 10 caracteres): ")
pprincipal=input("Ingrese el precio del plato principal: ")
postre=input("Ingrese el nombre del postre (max 10 caracteres): ")
ppostre=input("Ingrese el precio del postre: ")
menu="*"*57+"\n"+"CARTA DEL RESTAURANTE".center(57)+"\n"+"*"*57+\
    "\n"+"Categoria".ljust(37)+"Plato".ljust(10)+"Precio".rjust(10)+"\n"+\
    "*"*57+"\n"+\
    "Entrantes".ljust(37)+entrante.ljust(10)+pentrante.rjust(10)+"\n"+\
    "Principales".ljust(37)+principal.ljust(10)+pprincipal.rjust(10)+"\n"+\
    "Postres".ljust(37)+postre.ljust(10)+ppostre.rjust(10)+"\n"

print(menu)