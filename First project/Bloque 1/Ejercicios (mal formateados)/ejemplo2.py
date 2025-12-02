

cabecera = "*"*30+"\n"+"comida".center(30)+"\n"+"*"*30+"\n"+\
           "Nombre".ljust(22)+"Precio".rjust(8)+"\n"
cuerpo =   "Entrecot".ljust(22)+"23,35".rjust(8)+"\n"+\
            "Callos".ljust(22)+"15,1".rjust(8)+"\n"+\
            "Patatas Bravas".ljust(22)+"9,5".rjust(8)

print(cabecera+cuerpo)