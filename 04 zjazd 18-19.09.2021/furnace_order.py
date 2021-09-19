from furnace import Furnace
from furnace_customers import Customer


class Order:
    customers_accounts = []
    furnaces_orders = []

    def __init__(self):
        self.main()

    def show_menu(self):
        print('Wybierz opcję')
        print('1. Zaloguj się')
        print('2. Dodaj konto')
        print('3. Dodaj zamówienie')
        print('4. Sprawdź zamówienie')
        print('Wciśniej "e" aby wyjść z programu')

    def add_account(self):
        name = input('Podaj nazwę konta: ')
        coutry = input('podaj swój kraj: ')
        print('Rynki to: próznia, atmosfera, CAB')
        market = input('Na jakim rynku parcujesz? ')
        account = Customer(name, coutry, market)
        Order.customers_accounts.append(account)
        account.print_self()
        input('Wciśnij enter aby wrócić do głównego menu')

    def add_order(self):
        construction = input('Podaj typ budowy pieca, V-pionowy, H-poziomy:')
        if construction == 'V':
            try:
                w1 = int(input('Podaj średnicę w mm:  '))
                h1 = int(input('Podaj wysokość w mm: '))
                d1 = 0
            except ValueError:
                print('Podane wartości myszą być liczbami')
                input('Wciśnij enter aby wrócić do głównego menu')
                return
        elif construction == 'H':
            try:
                w1 = int(input('Podaj szerokość w mm: '))
                h1 = int(input('Podaj wysokość w mm: '))
                d1 = int(input('Podaj głębohość w mm: '))
            except ValueError:
                print('Podane wartości myszą być liczbami')
                input('Wciśnij enter aby wrócić do głównego menu')
                return
        else:
            print('Podałeś nieprawidłowe wartości, spróbuj jeszcze raz.')
            input('Wciśnij enter aby wrócić do głównego menu')
            return
        medium = input("Podaj typ medium chłodzącego (gas/oil):")
        pump_sys = input('System pompowy podstawowy czy z dufuzją (t/n)? ')
        work_atm = input('typ atmosfery kontrolnej (vac/gas): ')
        order = Furnace(construction, w1, h1, d1, medium, pump_sys,work_atm)
        Order.furnaces_orders.append(order)
        order.print_self()
        input('Wciśnij enter aby wrócić do głównego menu')

    def print_order(self):
        for order in Order.furnaces_orders:
            print(vars(order))
        input('Wciśnij enter aby wrócić do głównego menu')

    def main(self):
        while True:
            self.show_menu()
            choice = input('Podaj swój wybór: ')
            if choice == '1':
                self.add_account()
            if choice == '2':
                self.add_order()
            if choice == '3':
                self.print_order()
            if choice == 'e':
                break


Order()
