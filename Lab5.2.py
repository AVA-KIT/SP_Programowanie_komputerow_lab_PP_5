
sl = [x for x in input('Wprowadź sekwęcję liczb binarnych oddzielonych przecinkami: ').split(',')]
sl2 = []
for x in sl:
    if int(x,2) % 5 == 0: #Zamiana z systemu binarnego (zapisanego jako string np. "11101") na dziesiętny
        sl2.append(x)
sl3 =[]
for i in sl2:
    sl3.append(str(int(i,2))) 
print()
print(','.join(sl3))
print(','.join(sl2))
print()
