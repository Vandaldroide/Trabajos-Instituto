t = 0 #Tiempo
r1 = 10 #Robots
d2 = 6 #Drones
e = 50 #Energia
while r1 > 0 and d2 > 0 and e > 0:
    t += 1
    print(f"dia{t}: R1={r1} D2={d2} E={e}")
    e *= 2
    if t % 2 == 0:
        if r1*4 <= e:
            e -= r1*4
            r1 *= 2
        else:
            r1 = (e//4)*2
            e %= 4
    if t % 3 == 0:
        r1 -= d2//2
        if r1 < 0:
            r1 = 0
        if d2*3 <= e:
            e -= d2*3
            d2 *= 2
        else:
            d2 = (e//3)*2
            e %= 3
    if t % 4 == 0:
        r1 -= (e//50)*2
        if r1 < 0:
            r1 = 0
        if r1//4 <= d2:
            d2 -= r1//4
        else:
            d2 = 0
print(f"Final de la simulacion en el dia {t}")
print(f"R1={r1} D2={d2} E={e}")