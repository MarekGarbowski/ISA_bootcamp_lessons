# Napisz program który policzy liczbę liter w danym stringu.
def letters_counter(str):
    letter_counter = str.replace(" ", "")
    letters = {}
    for letter in letter_counter:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters


my_string = "The quick brown fox jumps over the lazy dog"


def calculation(collatz):
    numbers = []
    while collatz > 1:
        if collatz % 2:
            collatz = 3 * collatz + 1
            numbers.append(collatz)
        else:
            collatz = collatz / 2
            numbers.append(collatz)
    return numbers


# Napisz funkcję która zwróci True jezeli lista zawiera duplikaty

def duplicate_fn(lista):
    x = set(lista)
    if len(x) == len(lista):
        print('False')
    else:
        print('True')


my_list = [1,2,3,4,1,1,6,6,5]

if __name__ == "__main__":
    # print(letters_counter(my_string))
    # print(calculation(26))
    duplicate_fn(my_list)