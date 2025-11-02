from json.decoder import PosInf

tabla1="*"*57+"\n"+"CARTA DEL RESTAURANTE".center(57)+"\n"+"*"*57+\
    "\n"+"Categoria".ljust(37)+"Plato".ljust(10)+"Precio".rjust(10)+"\n"+\
    "*"*57+"\n"+\
    "Entrantes".ljust(37)+"Ensalada".ljust(10)+"8,50".rjust(10)+"\n"+\
    "Principales".ljust(37)+"Entrecot".ljust(10)+"23,35".rjust(10)+"\n"+\
    "Postres".ljust(37)+"Tarta".ljust(10)+"6,90".rjust(10)+"\n"+\
    "Bebidas".ljust(37)+"Vino".ljust(10)+"12,00".rjust(10)+"\n"

print(tabla1)