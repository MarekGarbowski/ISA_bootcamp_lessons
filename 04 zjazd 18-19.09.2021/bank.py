from cash_machine import Card
from accounts import BankAccount
from operation_history import Operation


class Bank:
    client_list = []
    card_list = []
    operation_history = []

    def __init__(self):
        self.main()

    def print_menu(self):
        print('wybierz opcje')
        print('*' * 10)
        print('1. Dodaj karte.')
        print('2. Lista kart')
        print('3. Odczytaj saldo')
        print('4. założ konto')
        print('5. Pokaż wszystkie konta')
        print('6. Przelej pieniądze na inne konto')
        print('7. Zmień balans konta')
        print('8. Pokaż historie operacji')

    def add_operation_history(self, operation: str) -> None:
        """
        Creates an OperatioHistory object, then adds it to Bank.operation_history
        :param operation: name of operation
        :return: None
        """
        new_operation = Operation(operation)
        Bank.operation_history.append(new_operation)

    def add_card(self):
        pin = input('Podaj pin: ')
        saldo = input('Podaj saldo: ')
        card = Card(pin, saldo)
        print(f'Numer Tojej karty to: {card.number}')
        Bank.card_list.append(card)
        input('Wciśnij enter aby wrócić do głównego menu')
        self.add_operation_history('New card added')

    def cards_list(self):
        print(vars(Bank.card_list))
        input('Wciśnij enter aby wrócić do głównego menu')
        self.add_operation_history('Card information requested')

    def show_saldo(self):
        card_number = input('Podaj numer karty: ')
        card_numbers = [card_number for card in self.card_list]
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
        self.add_operation_history('Ballance show requested')
        input('Wciśnij enter aby wrócić do głównego menu')

    def add_bank_account(self):
        owner = input('Proszę podać właściciela: ')
        password = input('Proszę podać hasło')
        account = BankAccount(owner, password)
        Bank.client_list.append(account)
        self.add_operation_history('Bank account added')
        print('Dodano konto')
        input('Wciśnij enter aby wrócić do głównego menu')

    def show_bank_accounts(self):
        #  Pierwszy sposób
        # for bank_account in Bank.client_list:
        #     print(bank_account)
        #  Drugi sposób
        for bank_account in Bank.client_list:
            bank_account.print_self()
        input('Wciśnij enter aby wrócić do głównego menu')

    def check_if_account_exist(self, check_id):
        for bank_account in Bank.client_list:
            if bank_account.id == check_id:
                return bank_account
            else:
                continue
        return False

    def send_money(self):
        #  1. wybrać konto z którego ma nastąpić przelew
        try:
            account_id = int(input('Podaj Id konta z którego konta chcesz wysłać pieniadze: '))
        except ValueError:
            print('Jako numer konta trzeba podać liczby: ')
            input('Wciśnij enter aby wrócić do głównego menu')
            return
        account = self.check_if_account_exist(account_id)
        if account:
            #  2. wybrać sumę i sprawdzić czy jest to mozliwe
            amount = int(input('Podaj ilość pieniędzy do wysłania: '))
            if account.balance >= amount:
                #  3. wybrać konto na które wysłac pieniądze
                reciever_account_id = int(input('Podaj id konta na które wysyłasz pieniądze: '))
                reciever_account = self.check_if_account_exist(reciever_account_id)
                if reciever_account:
                    #  4. wysłac pieniadze
                    account.balance -= amount
                    reciever_account.balance += amount
                    print(f'Twoje aktualne saldo wynosi: {account.balance} zł')
                else:
                    print('Przepraszamy ale konto nie istnieje.')
        else:
            print('Przepraszamy, wybrane konto nie istnieje.')
        input('Wciśnij enter aby wrócić do głównego menu')

    def set_balance(self):
        try:
            account_id = int(input('Podaj numer konta którego saldo chcesz zmienic: '))
        except ValueError:
            print('Jako numer konta trzeba podać liczby: ')
            input('Wciśnij enter aby wrócić do głównego menu')
            return
        account = self.check_if_account_exist(account_id)
        if account:
            new_balance = int(input('Podaj nowe saldo konta: '))
            BankAccount.set_balance(account, new_balance)
            # account.balance = new_balance
            print(f'Twoje nowe saldo wynosi: {account.balance} zł')
        else:
            print('Nie ma takiego konta')
        input('Wciśnij enter aby wrócić do głównego menu')

    def show_history(self):
        for operation in Bank.operation_history:
            print(vars(operation))

    def main(self):
        while True:
            self.print_menu()
            option = input('Podaj opcję: ')
            if option == '1':
                self.add_card()
            elif option == '2':
                self.cards_list()
            elif option == '3':
                self.show_saldo()
            elif option == '4':
                self.add_bank_account()
            elif option == '5':
                self.show_bank_accounts()
            elif option == '6':
                self.send_money()
            elif option == '7':
                self.set_balance()
            elif option == '8':
                self.show_history()
            elif option == 'e':
                break



Bank()
