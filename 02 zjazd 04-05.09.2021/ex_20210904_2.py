import database


def search_fn_1():
    for name_1 in database.base_1:
        if name_1[0] == "Marek":
            print(f"Cześć {name_1[0]}")
        elif name_1[0] == "Andrzej":
            print(name_1)
            break
    for index, name_2 in enumerate(database.base_1):
        print(index, name_2)


def search_surname(name):
    count = 0
    surname = None
    while not surname:
        if database.base_1[count][0] == name:
            surname = database.base_1[count][1]
        count += 1
    print(surname)

    # while True:
    #     for name, number in base_2.items():
    #         if name == ("Karolina", "Nowak"):
    #             print(f'Numer dla {name} to: {number}')
    #     break


def search_number(name, surname):
    return database.base_2[name, surname]


list_1 = [1, 2, 3, 4, 1]
print(list_1[0])
print(list_1.index(3))
list_1.append(5)
print(list_1)
list_1.insert(5, 6)
print(list_1)
list_1.extend([22])
print(list_1)
print(list_1.count(1))
print(list_1)
list_1.sort()
print(list_1)
# if __name__ == "__main__":
    # search_fn_1()
    # name = input('Podaj swoje imię: ')
    # search_surname(name)
    # number = search_number("Adam", "Słodowy")
    # print(number)
    # print(base_3['banan'])
    # fruits = {'apple', 'bananas', 'kiwi'}
    # print(fruits)
    # fruits.add('cherry')
    # print(fruits)
    # print(len(fruits))
