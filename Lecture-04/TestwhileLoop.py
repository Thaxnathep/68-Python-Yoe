keep_going = 'y'
while keep_going.lower() == 'y':
    sales = float(input('Enter The item wholesale cost: '))
    commission = sales * 2.5
    print(f'Retail price: ${commission:.2f}')
    keep_going = input('Do you have another item? (y/n): ')