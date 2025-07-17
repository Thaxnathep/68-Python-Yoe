print('--------------')
print('KPH\tMPH')
print('--------------')

for number in range(60,140,10):
    square = number*0.6214
    print(number, '\t',format(square, '5.1f'))
    print('--------------')