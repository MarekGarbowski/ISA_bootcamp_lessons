class Card:
    provider = 'Mastercard'
    next_number = 1

    def __init__(self, pin, saldo):
        self.number = self.next_number
        self.pin = pin
        self.saldo = saldo
        Card.next_number += 1

    def change_pin(self):
        self.pin = int(input('Podaj nowy numer pin: '))

    def change_saldo(self):
        self.saldo = int(input("Podaj nowe saldo: "))

