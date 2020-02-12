s = " "
s = input('Wprowadź sekwęcje słów oddzielonych przecinkami: ').split(',')
sn =[]
for i in s:
    sn.append(i.replace(' ', ''))

sn.sort()
print(','.join(sn))

