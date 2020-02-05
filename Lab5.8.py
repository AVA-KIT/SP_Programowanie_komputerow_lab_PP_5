y = int(input('Podaj rok: '))

while y >= 3000 or y <= 1600:
    y = int(input('Podaj właściwy format roku: '))

m = int(input('Podaj miesiąc: '))

while m > 12 or m < 1:
    m = int(input('Podaj właściwy format miesiąca: '))

d = int(input('Podaj dzień: '))

while d > 31 or d < 1:
    d = int(input('Podaj właściwy format dnia: '))

m -= 2

if m <= 0:
    m += 12
    y -= 1
2
noDay = (m * 83) / 32

noDay += d
noDay += y
noDay += (y/4)
noDay -= (y/100)
noDay += (y/400)

noDay = noDay % 7

dniTyg = {0: 'Niedziela',1:'Poniedziałek',2:'Wtorek',3:'Środa',4:'Czwartek',5:'Piątek',6:'Sobota'}

print(dniTyg[int(noDay)])