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

print(
    "*"*76+"\n"+
    "id".ljust(16)+"name".ljust(10)+"items".ljust(10)+"strength".ljust(10)+"defense".ljust(10)+"agility".ljust(10)+"stamina".rjust(10)+"\n"+
    "*"*76
)

for i in characters:
    if len(characters[i]["items"]) != 0:
        itc = characters[i]["items"]
        for j in itc:
            characters[i]["strength"] += items[j]["strength"]
            characters[i]["defense"] += items[j]["defense"]
            characters[i]["agility"] += items[j]["agility"]
            characters[i]["stamina"] += items[j]["stamina"]
for i in characters:
    if len(characters[i]["items"]) == 0:
        print(f"{i}".ljust(16)+f"{characters[i]["name"]}".ljust(10)+"".ljust(10)+f"{characters[i]["strength"]}".ljust(10)+f"{characters[i]["defense"]}".ljust(10)+f"{characters[i]["agility"]}".ljust(10)+f"{characters[i]["stamina"]}".rjust(10))
    else:
        print(f"{i}".ljust(16)+f"{characters[i]["name"]}".ljust(10)+f"{characters[i]["items"][0]}".ljust(10)+f"{characters[i]["strength"]}".ljust(10)+f"{characters[i]["defense"]}".ljust(10)+f"{characters[i]["agility"]}".ljust(10)+f"{characters[i]["stamina"]}".rjust(10))
    if len(characters[i]["items"]) > 1:
        for j in range(len(characters[i]["items"])-1):
            print("".ljust(16)+"".ljust(10)+f"{characters[i]["items"][j+1]}".ljust(10))
    print("-"*76)