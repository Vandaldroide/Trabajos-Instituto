items = {
    "TR345":{"description":"ring", "strength":6, "defense":1, "agility":1, "stamina":1},
    "ST123":{"description":"sword", "strength":5, "defense":0, "agility":-1, "stamina":2},
    "RV347":{"description":"shield", "strength":1, "defense":4, "agility":1, "stamina":1},
    "BJ023":{"description":"helmet", "strength":2, "defense":3, "agility":2, "stamina":1},
    "VL342":{"description":"belt", "strength":2, "defense":0, "agility":1, "stamina":0}
}
characters = {
    "VTF234":{"name":"Tharion", "strength":6, "defense":1, "agility":1, "stamina":1, "items":["TR345","BJ023"]},
    "TQA123":{"name":"Elyndra", "strength":3, "defense":2, "agility":2, "stamina":1, "items":["RV347"]},
    "OPT411":{"name":"Gorvak", "strength":2, "defense":0, "agility":2, "stamina":2, "items":["BJ023","RV347"]},
    "AAD212":{"name":"Varkos", "strength":5, "defense":2, "agility":1, "stamina":1, "items":["VL342","BJ023"]},
    "FDP345":{"name":"Nyssara", "strength":4, "defense":1, "agility":0, "stamina":2, "items":["TR345","VL342","ST123"]}
}
cn = 0 #cache numeros
list = []  # lista a ordenar
flgc = False #cambio para parar
for i in items:
    list.append(str(i))
for i in range(len(list)):
    flgc = False
    for j in range(len(list)-i-1):
        if items[list[j]]["strength"] > items[list[j+1]]["strength"]:
            flgc = True
            cn = list[j]
            list[j] = list[j+1]
            list[j+1] = cn
    if not flgc:
        break
print(list)
print(
    "*"*66+"\n"+
    "id".ljust(16)+"desc".ljust(10)+"strength".ljust(10)+"defense".ljust(10)+"agility".ljust(10)+"stamina".rjust(10)+"\n"+
    "*"*66+"\n"
)
for i in range(len(list)):
    print(f"{list[i]}".ljust(16) + f"{items[list[i]]['description']}".ljust(10) + f"{items[list[i]]['strength']}".ljust(10) + f"{items[list[i]]['defense']}".ljust(10) + f"{items[list[i]]['agility']}".ljust(10) + f"{items[list[i]]['stamina']}".rjust(10))