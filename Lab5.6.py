from random import randint
a = randint(1,9)
b = 0
c = 'exit'
print ('Program wygenerował dla Ciebie cyfrę całkowitą z zakresu od 1 do 9, zgadnij jaka to cyfra')

while a != int(b):
    b = input('Wprowadź cyfrę lub wyjdź z programu wpisując exit: ')
    if b == c:
        print('Opuściłeś program')
        break
    elif a > int(b):
        print('Cyfra jest mniejsza od wylosowanej')
    elif a < int(b):
        print('Cyfra jest większa od wylosowanej')
    else:
        print ('Zgadłeś - program zakończył działanie')
        

