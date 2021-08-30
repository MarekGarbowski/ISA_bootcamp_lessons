
startup_capital = int(input('Podaj kapitał początkowy: '))
monthly_income = int(input('Podaj swój dochód miesięczny: '))
monthly_expenses = int(input('Podaj swoje miesięczne wydatki: '))

savings = startup_capital + (12 * monthly_income) - (12 * monthly_expenses)

if savings > 20000:
    print(f'Masz dużo oczędności ({savings} zł)')
    decision = input('czy chcesz wpłacić oszczędności na lokatę? (y/N): ')
    if decision == 'y':
        print('Dobra decyzja!')
    else:
        print('Szkoda...')
else:
    print('Masz niskie oszcedności.')
    loan = input('Czy moze potrzebujesz pożyczkę (y/N): ')
    if loan == 'y':
        print('Przekierowuję cię na stronę banku')
    else:
        print('Dziękuję za współpracę.')

