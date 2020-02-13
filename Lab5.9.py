from datetime import date

year = input('Podaj rok: ')
month = input('Podaj miesiąc: ')
day = input('Podaj dzień: ')

def daysToEndOfYear(year = date.today().year,month = date.today().month,day = date.today().day):
    delta = date(year,12,31) - date(year,month,day)
    print(delta.days)

print('Data: 2020-1-20. Dni do końca roku:', end=" "), daysToEndOfYear(2020,1,20)
print('Data: dzisiaj. Dni do końca roku:', end=" "), daysToEndOfYear()
daysToEndOfYear(day = 23, month =12, year = 2023)
daysToEndOfYear()
daysToEndOfYear(year=2021)
daysToEndOfYear(year=2021, month=10)
daysToEndOfYear(day=1)
