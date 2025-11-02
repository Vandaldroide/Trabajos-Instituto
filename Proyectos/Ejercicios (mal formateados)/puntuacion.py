puntuacion = "Pau:2500;izel:500;Jose:10"
print(
    "*"*30+"\n"+
    "Ranking".center(30)+"\n"+
    "*"*30+"\n"+
    "Nombre".ljust(15)+"Puntuacion".rjust(15)+"\n"+
    ("-"*6).ljust(15)+("-"*10).rjust(15)
)
new_us = "ariadna"
new_punt = "250"
endflg = False
flgn = True
stat_start = 0
for i in range(0,len(puntuacion)):
    if i == len(puntuacion)-1:
        stat_end = i + 1
        endflg = True
    else:
        stat_end = i
    if puntuacion[i] == ":":
        name_end = i
    if puntuacion[i] == ";" or endflg:
        if int(puntuacion[name_end+1:stat_end]) < int(new_punt) and flgn:
            print(new_us.ljust(15)+new_punt.rjust(15))
            print(puntuacion[stat_start:name_end].ljust(15)+puntuacion[name_end + 1:stat_end].rjust(15))
            flgn = False
        elif endflg and flgn:
            print(puntuacion[stat_start:name_end].ljust(15)+puntuacion[name_end+1:stat_end].rjust(15))
            print(new_us.ljust(15)+new_punt.rjust(15))
        else:
            print(puntuacion[stat_start:name_end].ljust(15)+puntuacion[name_end + 1:stat_end].rjust(15))
        stat_start = stat_end + 1