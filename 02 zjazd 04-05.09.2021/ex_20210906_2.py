import random


# Napisz funkcję która:
# 1) symuluje rzut kostką do gry (6 stronna)
# 2) symuluje określoną ilość rzutów kością i zwraca True gdy pewna liczba wypadła conajmniej 2 razy
# 3) symuluje określoną ilość razy rzut dwoma koścmi jednocześnie, a następnie zwraca proporcje ile
#    razy w ciągu tych rzutów na obu kościach wypadły te same numery


def dice(throw):
    cube = [1, 2, 3, 4, 5, 6]
    throw_list = []
    for x in range(throw):
        throw_list.append(random.choice(cube))
    if throw > 1:
        x = set(throw_list)
        if len(x) == len(throw_list):
            print('Liczby się nie powtórzyły')
        else:
            print('Liczby się powtórzyły')
    return throw_list


if __name__ == '__main__':
    dice_throw = int(input('Ile razy rzucić kostką?: '))
    print(dice(dice_throw))
