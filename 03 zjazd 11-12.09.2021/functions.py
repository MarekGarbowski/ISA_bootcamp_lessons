from database import users


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
    if user_authenticated == 'admin':
        print('Wybierz co chiałbyś zrobić:')
        print('1. Utwórz nowego uzytkownika')
        print('2. Dodaj film do bazy danych')
        print('3. Zmodyfikuj film w bazie danych')
        print('4. Zobacz filmy w bazie danych')
        choice = input('podaj numer opcji: ')
        if choice == '1':
            # step 1 - przyjmij dane usera
            login = input('Podaj nazwę użytkownika: ')
            passowrd = input('Podaj hasło użytkownika: ')
            # step 2 - zapisz dane usera
            users[login] = passowrd
            print(users)
        if choice == '2':
            pass
        if choice == '3':
            pass
        if choice == '4':
            pass
    else:
        print('Wybierz co chiałbyś zrobić:')
        print('1. Zobacz ofertę ')
        print('2. Sprawdź dostępnośćfilmu')
        print('3. Wypożycz film')
        choice = input('podaj numer opcji: ')
        if choice == '1':
            pass
        if choice == '2':
            pass
        if choice == '3':
            pass
