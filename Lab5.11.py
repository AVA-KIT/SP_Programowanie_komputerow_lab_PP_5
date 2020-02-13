import calendar
def DniWMiesiacu(r,m):
        print(calendar.monthrange(r,m)[1])

r = int(input('Podaj rok: '))
m = int(input('Podaj miesiąc: '))
DniWMiesiacu(r,m)