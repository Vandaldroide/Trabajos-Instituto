import random
ncb = 1 #numero de carta jugador b

tca = random.randint(1,2) #tipo de carta jugador a
nca = random.randint(1,5) #numero de carta jugador a
tcb = random.randint(1,2) #tipo de carta jugador b
if tca == tcb:
    ncb = random.randint(1,5)
else:
    ncb = random.randint(1,4)
    if ncb >= nca:
        ncb += 1
print(f"El jugador A a sacado un {}")
if tca == tcb:
    if nca >= ncb:
        print(a ganado el jugador a)
