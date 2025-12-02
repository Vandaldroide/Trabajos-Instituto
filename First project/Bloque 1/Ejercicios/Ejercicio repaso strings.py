li = "albaricoque:3/a;tomates:5/a;helado:4/f"
dat = "" #cache de string para luego asignar a cache de cada dato
prd = "" #cache de producto
pre = "" #cache de precio
filas = "" #datos que se van a mostrar en la tabla
for i in range(0,len(li)):
    if li[i] == ":":#cuando el caracter a analizar sea el separador ":" lo guarda en prd y limpia dat
        prd = dat
        dat = ""
    elif li[i] == "/":#cuando el caracter a analizar sea el separador "/" lo guarda en pre y limpia dat
        pre = dat
        dat = ""
    elif li[i] == ";" or li[i] == li[len(li)-1]:#cuando el caracter a analizar sea el separador ";"
        if dat == "f": # como aun no hemos guardado el actual que es ";" el anterior es f o d aqui comprobamos cual es
            # y añadimos en la variable filas una nueva fila con los datos formateados en base a si la cantidad va a f o d
            filas += "\n" + f"{prd}".ljust(15) + f" {pre}".ljust(15)
        elif dat == "a":
            filas += "\n" + f"{prd}".ljust(15) + f" {pre}".rjust(30)
        dat = ""
    else: #Cuando no es un separador, va añadiendo las letras a la variable dat
        dat += li[i]
dat += li[i] #por ultimo como el ultimo caracter no es ";" no se actiba la funcion de printearlo asi que la añadimos
    #la funcion al final fuera del for para que añada el precio del ultimo producto
if dat == "f":
    filas += "\n" + f"{prd}".ljust(15) + f" {pre}".ljust(15)
elif dat == "a":
    filas += "\n" + f"{prd}".ljust(15) + f" {pre}".rjust(30)
dat = ""
print( #y por ultimo printeamos la tabla con la variable filas donde hemos ido escribiendo los datos ya formateados
"Lista de la compra".center(45,"*")+"\n"+
"Producto".ljust(15)+"Frigorifico".ljust(15)+"Armario".rjust(15)+"\n"+
"*"*45+
filas+"\n"+
"*"*45
)