importe = int(input("Importe del prestamo: "))
ingresos = int(input("Ingreso anual: "))
coste = int(input("Coste del piso: "))
terminio = int(input("Terminio del pagamento (en años): "))
importe80 = (coste/100)*80
importem = importe*2/(terminio*12)
ingresosm = (ingresos/12)/2
if importe80>=importe:
    if not importem > ingresosm:
        print("prestamo aceptado")
else:
    print("prestamo no aceptado")