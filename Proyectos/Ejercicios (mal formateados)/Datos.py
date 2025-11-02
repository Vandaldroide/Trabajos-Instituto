nombre = input("Ingrese su nombre (max 20 caracteres): ")
edad = input("Ingrese su edad (max 20 caracteres): ")
dni = input("Ingrese su DNI (max 20 caracteres): ")
telefono = input("Ingrese su telefono (max 20 caracteres): ")
datos = "*"*57+"\n"+\
    "DATOS CLIENTE".center(57)+"\n"+\
    "*"*57+\
    "\n"+"Categoria".ljust(37)+"Dato".rjust(20)+"\n"+\
    "*"*57+"\n"+\
    "Nombre: ".ljust(37)+nombre.rjust(20)+"\n"+\
    "Edad: ".ljust(37)+edad.rjust(20)+"\n"+\
    "DNI: ".ljust(37)+dni.rjust(20)+"\n"+\
    "Telefono: ".ljust(37)+telefono.rjust(20)+"\n"

print(datos)