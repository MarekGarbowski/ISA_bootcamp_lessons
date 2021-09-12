import sys

# try:
#     foo = int(input('podaj liczbę: '))
# # except ValueError:
# #     print('Nie wpisałeś liczby....')
# except TypeError:
#     print('Nie wpisałeś liczby....')
# except:
#     print('Inny błąd...', sys.exc_info())
# else:
#     print('Wpisałeś: ', foo)

# try:
#     foo = int(input('podaj liczbę: '))
# # except ValueError:
# #     print('Nie wpisałeś liczby....')
# except ValueError as t_error:
#     print(t_error)
#     print(t_error.args)
# else:
#     print('Wpisałeś: ', foo)

# try:
#     foo = int(input('podaj liczbę: '))
#     raise TypeError('mój wyjątek')
# # except ValueError:
# #     print('Nie wpisałeś liczby....')
# except ValueError as t_error:
#     print(t_error)
#     print(t_error.args)
#     print('nie wpisałes liczby')
# else:
#     print('Wpisałeś: ', foo)

try:
    foo = int(input('podaj liczbę: '))
# except TypeError:
#     print('Nie wpisałeś liczby....')
except ValueError as t_error:
    print(t_error)
    print(t_error.args)
    print('nie wpisałes liczby')
    # raise
    # print('to nie zadziałą')
else:
    print('Wpisałeś: ', foo)
finally:
    print('to sie zawsze wykona')
