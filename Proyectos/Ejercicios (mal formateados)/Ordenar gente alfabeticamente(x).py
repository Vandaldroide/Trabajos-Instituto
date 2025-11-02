nomb = "albert,miguel,oscar"
new_nomb = "diego"
list = ""
nnomb = ""
flgin = True
flgm = True
vnl = 1
for i in range(0,len(nomb)-1):
    if nomb[i] == ",":
        flgin = True
        list += nnomb+","
        nnomb = ""
    elif flgin:
        flgm = True
        while flgm:
            if nomb[i] > new_nomb[vnl]:
                list += new_nomb+","
                nnomb += nomb[i]
                flgm = False
                vnl = 1
            elif nomb[i] == new_nomb[vnl]:
                vnl += 1
            else:
                flgm = False
                flgin = False
                vnl = 1
    else:
        nnomb += nomb[i]
print(list)