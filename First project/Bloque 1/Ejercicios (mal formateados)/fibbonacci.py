print("0,1,",end="")
num1 = 0
num2 = 0
num3 = 1
while num3 < 200:
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    print (num3,",",sep="",end="")