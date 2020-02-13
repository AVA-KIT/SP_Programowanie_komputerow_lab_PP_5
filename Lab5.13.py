#Funkcja oblicza jaki dzień tygodnia wypada w podany dzień 

def DzienTygodnia1(r,m,d): #Rozwiązanie 1
    if r >= 1 and r <= 9999 and m >= 1 and m <= 12 and d >= 1 and d <= 31:
        m -= 2
        if m <= 0:
            m += 12
            r -= 1
        noDay = (m * 83) / 32
        noDay += d
        noDay += r
        noDay += (r/4)
        noDay -= (r/100)
        noDay += (r/400)
        noDay = noDay % 7
        dniTyg = {
            0:'Niedziela',
            1:'Poniedziałek',
            2:'Wtorek',
            3:'Środa',
            4:'Czwartek',
            5:'Piątek',
            6:'Sobota'
            }
        print('Rozwiązanie 1: ',dniTyg[int(noDay)])
    else:
        print('Argunenty są nieprawidłowe')
        return None

def DzienTygodnia2(r,m,d): #Rozwiązanie 2
    import calendar
    try:
        weekday = calendar.weekday(r,m,d)
        dniTyg = {
            0:'Poniedziałek',
            1:'Wtorek',
            2:'Środa',
            3:'Czwartek',
            4:'Piątek',
            5:'Sobota',
            6:'Niedziela',
            }
        print('Rozwiązanie 2: ',dniTyg[weekday])
    except:
        print('Argunenty są nieprawidłowe')
        return None

r = int(input('Podaj rok: '))
m = int(input('Podaj miesiąc: '))
d = int(input('Podaj dzień: '))
DzienTygodnia1(r,m,d)
DzienTygodnia2(r,m,d)