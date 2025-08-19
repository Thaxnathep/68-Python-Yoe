Hour = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the hourly play rate: "))

if Hour > 40:
    paly = ((Hour - 40) * 1.5 *pay_rate) + (40 * pay_rate)
else:
    paly = Hour * pay_rate
print("The gross pay is: " ,format(paly, '5.2f'))