import time
t = 1
b1 = 100
b2 = 50
ca = 100
while (b1 > 0 and ca > 0) or (b1 > 0 and b2 > 0) or (b2 > 0 and ca > 0):
    ca = ca*2
    print(f">inicio segundo nº{t} \nca se duplican ahora hay {ca} ca")
    if t % 2 == 0:
        if b1*3 < ca:
            ca = ca - b1*3
            b1 = b1*2
            print("todas las b1 han comido")
        else:
            cc = ca // 3
            ca = ca % 3
            b1 = cc*2
            print(f"solo {cc} b1 han podido comer")
    if t % 3 == 0:
        if b1 - b2//2 > 0:
            b1 = b1 - b2//2
        else:
            if b1 - b2//2 == 0:
                b1 = 0
        if b1*2 < ca:
            ca = ca - b1*2
            b1 = b1*2
            print("todas las b1 han comido")
        else:
            cc = ca // 2
            ca = ca % 2
            b1 = cc*2
            print(f"solo {cc} b1 han podido comer")
    if t % 4 == 0:
        b1 = b1 - ca // 5
        b2 = b2 - b1 // 3
    print(f">final segundo nº{t} tenemos {ca} ca, {b1} b1, {b2} b2")
    t = t + 1
    time.sleep(1)
print("ya solo queda una especie")