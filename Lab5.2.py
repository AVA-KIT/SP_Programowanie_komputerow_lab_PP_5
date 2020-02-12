
sl = [x for x in input('Wprowadź sekwęcję liczb binarnych oddzielonych przecinkami: ').split(',')]
sl2 = []
for x in sl:
    if int(x,2) % 5 == 0:
        sl2.append(x)

for i in sl2:
    print(int(i,2), end=",") #Zamiana z systemu binarnego (zapisanego jako string np. "11101") na dziesiętny
print()
for i in sl2:
    print(i, end=",")
    



