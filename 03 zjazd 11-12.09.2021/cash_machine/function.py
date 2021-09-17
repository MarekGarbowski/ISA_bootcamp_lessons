from database import cards


def main():
    while True:
        card = input('podaj nume swojej karty, lub wybierz "0" aby wyjść: ')
        if card == '0':
            break
        if card in cards:
            while True:
                print('Dostępne opcje:')
                print('1. odczytaj saldo')
                print('2. wpłać pieniądze')
                print('3. wypłać pieniądze')
                print('4. zmień pin')
                print('0. wyjście')
                choice = input('Wybierz opcje co chcesz zrobić: ')
                if choice == '1':
                    temp_1 = cards[card]['saldo']
                    print(f'Twoje saldo wynosi {temp_1}zł.')
                    input('Naciśnij enter, aby wrócić do głównego menu')
                elif choice == '2':
                    quantity = int(input('Podaj kwotę rtórą chcesz wpłacic: '))
                    cards[card]['saldo'] += quantity
                    temp_2 = cards[card]['saldo']
                    print(f'Twoje nowe saldo wynosi: {temp_2}zł')
                    input('Naciśnij enter, aby wrócić do głównego menu')
                elif choice == '3':
                    quantity = int(input('Podaj kwotę rtórą chcesz wypłacić: '))
                    temp_2 = cards[card]['saldo']
                    if quantity > temp_2:
                        print('Nie masz wystarczających środków na koncie.')
                    else:
                        cards[card]['saldo'] -= quantity
                        temp_3 = cards[card]['saldo']
                        print(f'Twoje nowe saldo wynosi: {temp_3}zł')
                    input('Naciśnij enter, aby wrócić do głównego menu')
                elif choice == '4':
                    new_pin = input('podaj swój nowy pin: ')
                    cards[card]['pin'] = new_pin
                    print('Pin zmieniono na:', (cards[card]['pin']))
                    input('Naciśnij enter, aby wrócić do głównego menu')
                elif choice == '0':
                    break
