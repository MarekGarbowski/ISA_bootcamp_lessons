import random
# Napisz funkcję która:
# Symuluje rzut monetą
# Rzuca monetą określoną ilość razy i zwraca najdłuższy ciąg orlów
# Zeby bylo prosciej, mozecie przyjac ze wartosc Reszki to 0, a orła 1


def coin():
    n = int(input('Ile razy rzucić monetą?: '))
    sides = [0, 1]
    list_1 = []
    for x in range(n):
        list_1.append(random.choice(sides))
    return list_1



def long_string(toss):
    longest = 0
    current = 0
    previous = 0
    for number in toss:
        if number == 1:
            current += 1
        else:
            current += 1
            continue
    return longest, current


x = coin()
print(x)
print(long_string(x))
