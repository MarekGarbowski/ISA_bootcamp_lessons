
for trip in range(5):
    print(trip)
    print("Marek")

for i in range(1, 11, 4):
    print(i)

i = 1
while i < 11:
    print(i)
    i += 1
while True:
    print('1: Dodaj liczby')
    print('2: Odejmij liczby')
    print('3: Pomnóż liczby')
    print('3: Podziel liczby')
    print('5: Wyjście z programu')

    decision = input('Podaj opcję którą chcesz wybrać: ')

    if decision == '1':
        digit_1 = int(input("Podaj pierwszą liczbę: "))
        digit_2 = int(input('Podaj drugą liczbę: '))
        print(digit_1 + digit_2)
    elif decision == '2':
        digit_1 = int(input("Podaj pierwszą liczbę: "))
        digit_2 = int(input('Podaj drugą liczbę: '))
        print(digit_1 - digit_2)
    elif decision == '3':
        digit_1 = int(input("Podaj pierwszą liczbę: "))
        digit_2 = int(input('Podaj drugą liczbę: '))
        print(digit_1 * digit_2)
    elif decision == '4':
        digit_1 = int(input("Podaj pierwszą liczbę: "))
        digit_2 = float(input('Podaj drugą liczbę: '))
        print(digit_1 / digit_2)
    else:
        if decision == '5':
            # quit()
            break
