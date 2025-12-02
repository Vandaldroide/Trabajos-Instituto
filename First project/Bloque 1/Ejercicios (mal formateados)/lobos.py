import time
t = 1
c = 5
l = 8
o = 20
while c > 0 and l > 0 and o > 0:
    print(f"Empezamos el dia {t} con {o} obejas, {l} lobos. {c} cazadores")
    o = o + o // 5
    if t % 2 == 0:
        if l // 3 < o:
            lc = l - l % 3
            o = o - l // 3
            l = lc + lc // 3
        else:
            l = o*3 + o
            lc = o*3
            o = 0
        c = c + 1
        print(f" {lc} lobos han comido y a venido un cazador")
    if t % 3 == 0:
        if l >= c//2:
            l = l - c // 2
            lca = 0
        else:
            l = 0
            lca = 1
        if l // 2 < o:
            lc = l - l % 2
            o = o - l // 2
            l = lc + lc // 2
        else:
            l = o*2 + o
            lc = o*2
            o = 0
        if lca == 0:
            print(f"los cazadores han cazado {c//2} lobos y de los supervivientes, {lc} han comido")
        else:
            print(f"los cazadores han cazado a todos los lobos")
    if t % 4 == 0:
        if l >= o // 30:
            l = l - o // 30
            lm = 0
        else:
            l = 0
            lm = 1
        if c >= l // 10:
            c = c - l // 10
            cm = 0
        else:
            c = 0
            cm = 1
        if lm == 0 and cm == 0:
            print(f"las obejas han matado {o//30} lobos y los lobos han matado {l//10} cazadores")
        elif lm == 0 and cm == 1:
            print(f"las obejas han matado {o//30} lobos y los lobos han matado a todos los cazadores")
        elif lm == 1 and cm == 0:
            print(f"las obejas han matado a todos lobos y los lobos han matado {l // 10} cazadores")
        else:
            print(f"las obejas han matado a todos lobos y los lobos han matado a todos los cazadores")
    print(f"Acabamos el dia {t} con {o} obejas, {l} lobos. {c} cazadores")
    t = t + 1
    time.sleep(1)