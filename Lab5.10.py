rok = int(input('Podaj rok: '))

def czyPrzestępny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False

print(czyPrzestępny(rok))