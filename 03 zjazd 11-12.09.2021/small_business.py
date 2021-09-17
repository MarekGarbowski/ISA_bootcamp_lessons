# Jesteś właścicielem/-elką małego biznesu który prowadzisz online i dużą częścią
# Twojego dnia jest realizacja zamówień. Żeby ułatwić swoją pracę,
# postanowiłeś/-aś napisać funkcję, która pomoże zdecydować czy realizacja zamówienia jest możliwa.
# Funkcja przyjmie trzy argumenty:
# towar: dict – słownik reprezentujący cały towar którym dysponuje Twój biznes
# zamowienie: string – string reprezentujący towar który chce zamówić klient
# n: int – liczba reprezentująca ile sztuk chce zamówić klient
#
# Funkcja ma zdecydować, czy Twój sklep jest w stanie wykonać zamówienie.
# do_realizacji({‘bluzka’: 5, ‘spodnie’: 3}, ‘spodnie’, 2) -> True
# do_realizacji(({‘bluzka’: 5, ‘spodnie’: 3}, ‘spodnie’, 4) - False

warehouse = {'bluzka': 5, 'spodnie': 3}


def shop(wh, order, quantity):
    if order in wh:
        if wh[order] >= quantity:
            print('True')
        else:
            print('False')
    else:
        print('False')


shop(warehouse, 'bluzka', 1)
shop(warehouse, 'bluzki', 1)
shop(warehouse, 'bluzka', 6)
