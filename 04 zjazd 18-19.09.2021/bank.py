from cash_machine import Card


class Bank:
    client_list = []
    card_list = []

    def __init__(self):
        self.main()

    def main(self):
        while True:
            print('wybierz opcje')
            print('*' * 10)
            print('1. Dodaj karte.')
            print('2. Lista kart')
            print('3. Odczytaj saldo')
            option = input('Podaj opcję: ')
            if option == '1':
                pin = input('Podaj pin: ')
                saldo = input('Podaj saldo: ')
                card = Card(pin, saldo)
                Bank.card_list.append(card)
            elif option == '2':
                print(Bank.card_list)
            elif option == '3':
                #   1.Przyjęcie od użytkownika numeru karty
                card_number = input('Podaj numer karty: ')
                #   2. Sprawdzenie czy karta istnieje
                card_numbers = [card_number for card in self.card_list]
                #   3. Przyjęcie od użytkowniak numeru PIN
                #   4. sprawdzenie czy PIN jest zgodny
                card_exits = card_number in card_numbers
                if card_exits:
                    pin = input('Podaj pin: ')
                    index_card = card_numbers.index(card_number)
                    card = self.card_list[index_card]
                    if pin == card.pin:
                        print(card.saldo)
                    else:
                        print('PIN nieprawidłowy')
                else:
                    print('Nie ma takiej karty.')


Bank()
