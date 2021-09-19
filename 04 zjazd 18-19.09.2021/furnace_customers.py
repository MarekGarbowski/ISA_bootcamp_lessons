
class Customer:
    next_id = 1

    def __init__(self, name, country, market):
        self.id = self.next_id
        self.name = name
        self.country = country
        self.market = market
        Customer.next_id += 1

    def print_self(self):
        print(30 * '-')
        print(f'Utworzono następującego klienta:')
        print(f'Numer klienta: {self.id}')
        print(f'Nazwa klienta: {self.name}')
        print(f'Kraj klienta: {self.country}')
        print(f'Obszar obróbki cieplnej: {self.market}')
        print(30 * '-')
