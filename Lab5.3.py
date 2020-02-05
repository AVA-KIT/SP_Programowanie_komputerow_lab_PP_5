a = input('Podaj ciąg znaków: ')
b = list(a)
litery = []
cyfry = []
for i in b:
    if i.isalpha() == True:
        litery.append(i)
    elif i.isdigit() == True:
        cyfry.append(i)

print('Litery: ', len(litery))
print('Cyfry: ', len(cyfry))
