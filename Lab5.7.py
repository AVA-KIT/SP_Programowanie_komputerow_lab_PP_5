c = int(input('Podaj dowolną liczbę naturalną: '))
e = c

while c != 1:
    if c % 2 == 0:
        c /= 2
        print(c)
    else:
        c = 3 * c + 1
        print(c)
print('Hipoteza Collatza jest spełniona dla liczby {}'.format(e))



