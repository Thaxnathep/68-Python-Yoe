try:
    value = float(input('Enter a number: '))
    result = 10 / value
except ZeroDivisionError as e:
    print(f'An error occurred: {e}')
else:
    print(f'Result is {result}')

print("End of the program")