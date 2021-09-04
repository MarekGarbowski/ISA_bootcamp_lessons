from typing import Tuple


def string_concatenation(name: str, surname: str) -> Tuple[str, str]:
    print(type(name))
    print(type(surname))
    return name, surname


if __name__ == "__main__":
    my_name = int(input('Podaj swoje imię: '))
    my_surname = int(input('Podaj swoje nazwosko: '))
#     # full_name = string_concatenation(my_name, my_surname)
#     # print(full_name)
    name1, surname1 = string_concatenation(my_name, my_surname)
    print('Masz na imię i nazwosko: ', name1, surname1)

    if name1 == 'Marek':
        print(f'Cześć {name1} {my_surname}')
