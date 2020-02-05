text = input('Podaj jakiś tekst: ')
listText = list(text)
alfabet =  'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż'
listAlfabet = list(alfabet)
dictText = {}

for i in listText:
        if i in listAlfabet:
            dictText[i] = text.count(i)

for j in dictText.keys():
    print(j, dictText[j])
