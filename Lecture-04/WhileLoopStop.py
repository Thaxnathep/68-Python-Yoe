keep_going = 'y'
while keep_going.lower() == 'y':
    sales = float(input('Enter The amount of sales: '))
    comm_rate = float(input('Enter commission of sales: '))
    commission = sales * comm_rate
    print(f'The commission is ${commission:.2f}')
    keep_going = input('Do you want to continue? (y/n): ')