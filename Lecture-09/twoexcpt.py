try:
    value = float(input('Enter a number: '))
    result = 10 / value
    print(f'Resolt is {result}')
except ValueError:
    print("Error: Invalid input. please a valid integer.")
except ZeroDivisionError:
    print('Error: division by zero is not allowed.')

print("End of the program")