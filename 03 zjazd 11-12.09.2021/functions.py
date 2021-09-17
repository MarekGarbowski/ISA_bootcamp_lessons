from database import users, movies


def authenticate_user():
    login = input('Podaj nazwę uzytkownika: ')
    if users.get(login):
        password = input('Podaj hasło: ')
        if users[login] == password:
            return login
        else:
            return False
    else:
        return False


def main():
    user_authenticated = False
    while not user_authenticated:
        user_authenticated = authenticate_user()
        print(f'user_authenticated: {user_authenticated}')
    while True:
        if user_authenticated == 'admin':
            print('Wybierz co chiałbyś zrobić:')
            print('1. Utwórz nowego uzytkownika')
            print('2. Dodaj film do bazy danych')
            print('3. Zmodyfikuj film w bazie danych')
            print('4. Zobacz filmy w bazie danych')
            print('0. Wyjdź z programu')
            choice = input('podaj numer opcji: ')
            if choice == '1':
                # step 1 - przyjmij dane usera
                login = input('Podaj nazwę użytkownika: ')
                passowrd = input('Podaj hasło użytkownika: ')
                # step 2 - zapisz dane usera
                users[login] = passowrd
                print(users)
            elif choice == '2':
                title = input('Podaj tytuł filmu: ')
                price = int(input('Podaj cenę filmu: '))
                quantity = int(input("Podaj ilośc sztuk: "))
                movies[title] = {'price': price, 'quantity': quantity}
                print(movies)
                input('Naciśnij enter, aby wrócić do głównego menu')
            elif choice == '3':
                #  krok1: przyjmij dane na temat tytułu filmu
                title = input('podaj tytuł filmu który chcesz zmodyfikować: ')
                # krok2: sprawdź czy tytul jestw bazie danych
                if movies.get(title):
                    pass
                else:
                    print('Nie ma tego filmu w bazie danych.')
            elif choice == '4':
                print(movies)
                input('Naciśnij enter, aby wrócić do głównego menu')
            elif choice == '0':
                break
        else:
            print('Wybierz co chiałbyś zrobić:')
            print('1. Zobacz ofertę ')
            print('2. Sprawdź dostępnośćfilmu')
            print('3. Wypożycz film')
            print('0. Wyjdź z programu')
            choice = input('podaj numer opcji: ')
            if choice == '1':
                for movie, quantity in movies.items():
                    print(f'Filma: {movie}, jest w cenie: {quantity}zł')
                input('Naciśnij enter, aby wrócić do głównego menu')
            elif choice == '2':
                title = input('Podaj tytuł filmu który chcesz znaleść: ')
                if movies.get(title):
                    quantity = movies[title]['quantity']
                    if quantity > 0:
                        print(f'Podany film jest dostpny w {quantity} ilościach')
                    else:
                        print('Niestety nie ma chwilowo tego filmu')
                else:
                    print('Nie mamy podanego filmu.')
                input('Naciśnij enter, aby wrócić do głównego menu')
            elif choice == '3':
                title = input('Podaj tytuł filmu który chcesz wupozyczyć: ')
                if movies.get(title):
                    if movies[title]['quantity'] > 0:
                        movies[title]['quantity'] -= 1
                        temp_1 = movies[title]['quantity']
                        print(f'Wypożyczono film {title}')
                        print(f'Pozostało na stanie {temp_1} sztuk')
                    else:
                        print('chwilowo brak tego filmu.')
                else:
                    print('Nie mamy podanego filmu w bazie.')
                input('Naciśnij enter, aby wrócić do głównego menu')
            elif choice == '0':
                break
