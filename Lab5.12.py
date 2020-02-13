from datetime import date

def dzienWRoku(r,m,d):
    try:
        delta =  date(r,12,31) - date(r,m,d)
        ilosc_dni = delta.days
        
        if r%4 == 0 and (r%100 != 0 or r%400 == 0):
            dzien = 366 - ilosc_dni
        else:
            dzien = 365 - ilosc_dni
        
        print(dzien)
    
    except:
         print('Argunent są nieprawidłowe')
         return None
       

r = int(input('Podaj rok: '))
m = int(input('Podaj miesiąc: '))
d = int(input('Podaj dzień: '))
dzienWRoku(r,m,d)

