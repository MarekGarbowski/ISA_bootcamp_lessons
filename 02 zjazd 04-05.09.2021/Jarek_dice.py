import random


def dice_throw():
    return random.choice(range(1, 7))


def throw_results(throws):
    throw_list = []
    for idx in range(throws):
        throw_list.append(dice_throw())
    return throw_list


def multiple_result_comparison(result_list):
    result_set = set(result_list)
    if len(result_set) == len(result_list):
        return False
    return True


def double_dice_throw(throws):
    number_of_doubles = 0
    for idx in range(throws):
        result1, result2 = dice_throw(), dice_throw()
        print(f'Result 1: {result1}, Result 2: {result2}')
        if result1 == result2:
            number_of_doubles += 1
    return number_of_doubles


if __name__ == '__main__':
    number_of_throws = int(input('How many dice throws? '))

    if multiple_result_comparison(throw_results(number_of_throws)):
        print('Przy rzucie jedną kością jakaś liczba wypadła conajmniej 2 razy')
    else:
        print('Przy rzucie jedną kością wszystkie liczby są unikatowe')
    print(f'Przy rzucie dwoma kośćmi było {double_dice_throw(number_of_throws)} powtórzeń')
