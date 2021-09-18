class Flower:
    def __init__(self, name, colour, species, height):
        self.name = name
        self.colour = colour
        self.species = species
        self.height = height

    def grow(self):
        self.height += 10

    def decrease(self):
        self.height -= 10


class Dog:
    def __init__(self, name, species, height, weight):
        self.name = name
        self.species = species
        self.height = height
        self.weight = weight

    def pet(self):
        print('Głaszcze pieska')

    def bark(self):
        print('Szczekaj piesku')


class Human:
    def __init__(self, name, surname, age):
        self.age = age
        self.name = name
        self.surname = surname

    def give_name(self):
        self.name = input('Podaj imię: ')

    def change_name(self):
        self.name = input('Podaj nowe imię: ')

    def introduce_yourself(self):
        print(f'Na imię mam {self.name} a na nazwisko {self.surname}')
        print(f'Mam {self.age} lat')

    def give_age(self):
        self.age = int(input('Podaj swój wiek: '))

    def change_age(self):
        self.age = int(input('Podaj swój nowy wiek: '))

    def give_surname(self):
        self.surname = input('Podaj swoje nazwisko: ')

    def change_surname(self):
        self.surname = input('Podaj swoje nowe nazwisko: ')


class Computer:
    def __init__(self):
        self.on = 0

    def turn_on(self):
        self.on = 1

    def turn_off(self):
        self.on = 0

    def add_digits(self, a, b):
        if self.on == 1:
            return a + b


# digits = Computer()
# digits.turn_on()
# print(digits.add_digits(1, 2))


class Chair:
    def __init__(self, leg, height, material):
        self.leg = leg
        self.height = height
        self.material = material


class Mug:
    def __init__(self, size, material, ear):
        self.size = size
        self.material = material
        self.ear = ear


class Window:
    def __init__(self):
        self.layers = 0
        self.size = str
        self.frame_material = str

    def order_window(self):
        self.size = input('Jakie duże okno potrzebujesz? Podaj wymiar (x*y) ')
        self.layers = input('Ile szyb? ')
        self.frame_material = input('Z czego ma byc rama? ')
        print(f'Zamówione okno ma {self.layers}, wielkość: {self.size}, i rame z: {self.frame_material}')


window = Window()
window.order_window()
print(type(window))
