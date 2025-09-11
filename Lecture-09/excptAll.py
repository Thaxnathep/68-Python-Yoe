try:
    value = float(input('Enter a number: '))
    result = 10 / value
    print(f'Resolt is {result}')
except Exception as e:
    print(f'An error occurred: {e}')


print("End of the program")