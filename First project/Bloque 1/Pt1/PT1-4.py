from xml.dom.minidom import ProcessingInstruction

nota = float(input("escribe tu nota: "))
if nota >= 5.0:
    if nota >= 6.5:
        if nota >= 8.5:
            print("has sacado un excel en te")
        else:
            print("has sacado un notable")
    else:
        print("has sacado un bien")
else:
    print("has suspendido")