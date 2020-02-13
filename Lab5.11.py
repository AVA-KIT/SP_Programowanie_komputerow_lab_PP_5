import calendar
def DniWMiesiacu(r,m):
        try:
                print(calendar.monthrange(r,m)[1])
        except:
                print('Argunenty są nieprawidłowe')
                return None

r = int(input('Podaj rok: '))
m = int(input('Podaj miesiąc: '))
DniWMiesiacu(r,m)