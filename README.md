# SP_Programowanie_komputerow_lab_PP_5
Studia podyplomowe Podstawy programowania - Python, Wydział Informatyki, ZUT w Szczecinie - Laboratorium 5

Zadanie 1:
Napisz program, który, jako dane wejściowe, pobiera sekwencję słów oddzielonych
przecinkami i wyświetla te słowa po posortowaniu ich alfabetycznie, także w postaci
z przecinkami.
Przykładowe dane wejściowe: ala,ma,kota
Przykładowe dane wyjściowe: ala,kota,ma
Co się stanie, jeśli po przecinku będą dodatkowe spacje? Czy można je wyeliminować?

Zadanie 2:
Napisz program, który, jako dane wejściowe, pobiera sekwencję liczb binarnych
oddzielonych przecinkami. Program sprawdza czy liczba binarna jest podzielna przez 5 i
zapamiętuje ten fakt. Efektem programu ma być wyświetlenie wszystkich liczb binarnych
podzielnych przez 5 (i ich odpowiedników całkowitych) oddzielonych przecinkami.
Przykładowe dane wejściowe:
111,100011,011,1010,10101010
Przykładowe dane wyjściowe:
35,10,170
100011,1010,10101010

Zadanie 3:
Napisz program, który pobiera od użytkownika ciąg znaków. Program liczy ile jest liter a ile
cyfr w tym ciągu i wyświetla stosowną informację.
Przykładowe dane wejściowe:
ala ma 124 kotów i 2 psy
Przykładowe dane wyjściowe:
Litery: 14
Cyfry: 4

Zadanie 4:
Napisz program, który liczy litery we wczytanym tekście i prezentuje wynik w postaci
uproszczonego histogramu w kolejności alfabetycznej. Dla tekstu na wejściu:
ALA MA KOTA
wynik powinien wyglądać następująco:
A 4
K 1
L 1
M 1
O 1

Zadanie 5:
Napisz program, który sprawdza czy wprowadzone hasło spełnia wymagania stawiane
przez system logowania. Poniżej znajdują się kryteria sprawdzania hasła:
1. Co najmniej 1 litera mała [a-z]
2. Co najmniej 1 cyfra [0–9]
3. Co najmniej 1 litera duża [A-Z]
4. Co najmniej 1 znak specjalny ze zbioru [$ # @]
5. Minimalna długość hasła: 6
6. Maksymalna długość hasła: 12
Wykorzystaj umiejętność pisania funkcji. Argumentem wywołanej funkcji będzie ciąg
znaków. Funkcja zwraca True lub False.

Zadanie 6:
Napisz program, który generuje cyfrę całkowitą z zakresu od 1 do 9 (włącznie). Program
prosi użytkownika, aby zgadł wylosowaną cyfrę, informując go, czy wartość podana przez
użytkownika jest mniejsza czy większa od wylosowanej przez komputer. Jeśli użytkownik
zgadnie wylosowaną cyfrę, to program wypisze ile prób wykorzystał użytkownik.
Program ma działać dopóki użytkownik nie zgadnie wylosowanej cyfry lub nie wpisze
słowa exit aby opuścić program wcześniej.

Zadanie 7:
W 1937 roku niemiecki matematyk Lothar Collatz postawił nieudowodnioną do dziś
hipotezę, którą można przedstawić w postaci następującej recepty:
1. weź dowolną liczbę naturalną c0
2. jeśli c0 jest parzyste, oblicz nowe c0 jako c0 / 2
3. jeśli c0 jest nieparzyste, oblicz nowe c0 jako 3 ⋅ c0 + 1
4. jeśli c0 ≠ 1, przejdź do kroku 2
5. koniec!
Hipoteza Collatza mówi, że niezależnie od początkowej wartości c0, zawsze dochodzi się
do c0 = 1.
Napisz program, który zapyta użytkownika o liczbę, a następnie sprawdzi, czy hipoteza
Collatza jest dla niej spełniona. Twój program powinien wypisać wszystkie pośrednie
wartości c0.

Zadanie 8:
Do ustalania dnia tygodnia przypadającego na pewien dzień roku używa się algorytmu
Zellera-Keitha, którego jedną z wersji można opisać następującymi słowami:
1. pomniejsz numer miesiąca o 2
2. jeśli wartość miesiąca jest mniejsza równa zero, powiększ miesiąc o 12, a rok
zmniejsz o 1
3. weź numer miesiąca, pomnóż przez 83 i podziel przez 32 (wszystkie dzielenia w
algorytmie są całkowite!)
4. do otrzymanego wyniku dodaj numer dnia w miesiącu
5. do otrzymanego wyniku dodaj rok
6. do otrzymanego wyniku dodaj rok/4
7. od otrzymanego wyniku odejmij rok/100
8. do otrzymanego wyniku dodaj rok/400
9. znajdź resztę z dzielenia otrzymanego wyniku przez 7
Brawo! otrzymałeś numer dnia tygodnia w takiej oto konwencji: 0 → niedziela, 1 →
poniedziałek, 2 → wtorek, 3 → środa, 4 → czwartek, 5 → piątek, 6 → sobota
Napisz program, który pyta użytkownika kolejno o rok, miesiąc i dzień, a następnie
wypisuje nazwę dnia tygodnia. Zadbaj o to, aby wprowadzana data miała sens.

Zadanie 9:
Napisz program, który wyświetli ile dni zostało do końca roku (wskazanego przez
użytkownika). Program ma składać się z funkcji, która będzie przyjmowała 3 parametry:
rok, miesiąc, dzień i będzie zwracała liczbę dni do Sylwestra. Zadbaj o to aby w przypadku
braku pewnych argumentów wywołujących funkcję przyjąć wartości domyślne, czyli
dotyczące dnia bieżącego. Przykładowe wywołania funkcji:
print('Data: 2020-1-20. Dni do końca roku: %d' %( DaysToEndOfYear(2020,1,20)))
print('Data: dzisiaj. Dni do końca roku: %d' %( DaysToEndOfYear()))
DaysToEndOfYear(day = 23, month =12, year = 2023)
DaysToEndOfYear()
DaysToEndOfYear(year=2021)
DaysToEndOfYear(year=2021, month=10)
DaysToEndOfYear(day=1)
Przydatne informacje. Uruchom poniższy kod aby potestować.
from datetime import date
print('Data dzisiejsza: ', date.today())
print('Rok: ', date.today().year)
print('Miesiąc: ', date.today().month)
print('Dzień: ', date.today().day)
delta = date(2020, 2, 1) - date(2020, 1, 26)
print('Od ostatnich zajęć minęło', delta.days, 'dni')

Zadanie 10:
Napisz i przetestuj funkcję o nazwie CzyPrzestępny, która otrzymuje jako parametr liczbę
całkowitą reprezentującą rok. Funkcja zwraca True jeśli rok jest przestępny i False w
przeciwnym przypadku.

Zadanie 11:
Napisz i przetestuj funkcję o nazwie DniWMiesiącu, która otrzymuje dwa parametry:
pierwszy (liczba całkowita) reprezentujący numer miesiąca i drugi (liczba całkowita),
reprezentujący rok; funkcja powinna zwracać liczbę dni w podanym miesiącu podanego
roku lub None, jeśli podano nieodpowiednie argumenty.

Zadanie 12:
Napisz i przetestuj funkcję o nazwie DzieńWRoku, która otrzymuje jako parametry trzy
liczby całkowite: pierwsza reprezentuje rok, druga miesiąc, trzecia dzień miesiąca;
funkcja powinna obliczać, którym dniem w roku jest dzień określony w parametrach albo
zwracać None, jeśli argumenty są niepoprawne.

Zadanie 13:
Napisz i przetestuj funkcję o nazwie DzieńTygodnia, która otrzymuje jako parametry trzy
liczby całkowite: pierwsza reprezentuje rok, druga miesiąc, trzecia dzień miesiąca;
funkcja powinna obliczać jaki dzień tygodnia wypada w podany dzień i zwracać 0 dla
niedzieli, 1 dla poniedziałku, etc.; zwróć None jeśli argumenty są niepoprawne.
