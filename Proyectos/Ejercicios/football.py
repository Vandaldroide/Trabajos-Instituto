import random
m1 = "000" #partidos equipo 1
m2 = "000" #partidos equipo 2
m3 = "000" #partidos equipo 3
m4 = "000" #partidos equipo 4
cn = 0 #cache numero random
filas = "" #datos partidos para imprimir
m1 = str(random.randint(1,3)+1)+"0"*2
if m1[0] == "2":
    m2 = "100"
    m3 = "400"
    m4 = "300"
    filas = "1".ljust(15)+"1".ljust(15)+"2".rjust(15)+"\n"+\
            "1".ljust(15)+"3".ljust(15)+"4".rjust(15)+"\n"
elif m1[0] == "3":
    m3 = "100"
    m2 = "400"
    m4 = "200"
    filas = "1".ljust(15)+"1".ljust(15)+"3".rjust(15)+"\n"+\
            "1".ljust(15)+"2".ljust(15)+"4".rjust(15)+"\n"
elif m1[0] == "4":
    m4 = "100"
    m3 = "200"
    m2 = "300"
    filas = "1".ljust(15)+"1".ljust(15)+"4".rjust(15)+"\n"+\
            "1".ljust(15)+"2".ljust(15)+"3".rjust(15)+"\n"
for i in range(1,3):
    cn = random.randint(1,(3-i))+1
    if cn == m1[i-1]:
       m1 = m1[:i]+str(cn+1)+m1[i+1:]
    else:
        m1 = m1[:i]+str(cn)+m1[i+1:]
    if m1[i] == "2":
        m2 = m2[:i]+"1"+m2[i+1:]
        m3 = m3[:i]+"4"+m3[i+1:]
        m4 = m4[:i]+"3"+m4[i+1:]
        filas += f"{i+1}".ljust(15) + "1".ljust(15) + "2".rjust(15) + "\n" + \
                 f"{i+1}".ljust(15) + "3".ljust(15) + "4".rjust(15) + "\n"

    elif m1[i] == "3":
        m3 = m3[:i]+"1"+m3[i+1:]
        m2 = m2[:i]+"4"+m2[i+1:]
        m4 = m4[:i]+"2"+m4[i+1:]
        filas += f"{i+1}".ljust(15) + "1".ljust(15) + "3".rjust(15) + "\n"+\
                 f"{i+1}".ljust(15)+"2".ljust(15)+"4".rjust(15)+"\n"

    elif m1[i] == "4":
        m4 = m4[:i]+"1"+m4[i+1:]
        m2 = m2[:i]+"3"+m2[i+1:]
        m3 = m3[:i]+"2"+m3[i+1:]
        filas += f"{i+1}".ljust(15) + "1".ljust(15) + "4".rjust(15) + "\n"+\
                 f"{i+1}".ljust(15)+"2".ljust(15)+"3".rjust(15)+"\n"

print(
    "Partidos".center(45, "*") + "\n" +
    "Jornada".ljust(15) + "Equipo 1".ljust(15) + "Equipo 2".rjust(15) + "\n" +
    "*" * 45 + "\n" +
    filas + "\n" +
    "*" * 45
)
print(f"partidos equipo 1: {m1}\n"+
      f"partidos equipo 2: {m2}\n"+
      f"partidos equipo 3: {m3}")