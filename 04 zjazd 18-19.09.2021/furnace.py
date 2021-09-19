
class Furnace:
    next_id = 1

    def __init__(self, construction, w, h, d, med, pumps, atm):
        self.id = self.next_id
        self.construction = construction
        self.w = w
        self.h = h
        self.d = d
        self.med = med
        self.pumps = pumps
        self.atm = atm
        self.next_id += 1

    def furnace_construction(self):
        pass

    def furnace_size(self):
        pass

    def quenching_medium(self):
        pass

    def pumping_system(self):
        pass

    def control_atmosphere(self):
        pass

    def print_self(self):
        print(30 * '-')
        print(f'Złozono następujące zamówienie:')
        print(f'Numer zamówienia: {self.id}')
        if self.construction == 'V':
            print('Typ urządzenia: piec pionowy')
        elif self.construction == 'H':
            print('Typ urządzenia: piec pionowyq.')
        if self.construction == 'V':
            print(f'Wymiary przestrzenie roboczej: średnica: {self.w}mm, wysokość: {self.h}mm.')
        elif self.construction == 'H':
            print(f'Wymiary przestrzeni roboczej: szerokość: {self.w}mm, wysokość: {self.h}mm, głębokość: {self.d}mm.')
        if self.med == 'gas':
            print('Typ chłodzenia: gaz neutralny.')
        elif self.med == 'oil':
            print('typ chłodzenia: olej hartowniczy.')
        if self.pumps == 't':
            print('System pompowy: z pompą dyfuzyjną.')
        elif self.med == 'n':
            print('System pompowy: bez pompy dyfuzyjnej.')
        if self.atm == 'vac':
            print('Atmosfera procesu: próżnia.')
        elif self.atm == 'gas':
            print('Atmosfera procesu: gas.')
        print(30 * '-')
