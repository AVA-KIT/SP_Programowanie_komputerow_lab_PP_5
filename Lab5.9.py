from datetime import date



def daysToEndOfYear(y = date.today().year , m = date.today().month,d = date.today().day):
    r = input('Podaj rok: ')
    print(y,m,d)

daysToEndOfYear(r)