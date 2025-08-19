num_employees = 6

def maim():
    house = [0] * num_employees

    for index in range(num_employees):
        print("Enter you house worked by employee", \
              index + 1, ": ", sep="", end="")
        house[index] = float(input())

    pay_rayt = float(input("Enter your hourly pay rate: "))

    for index in range(num_employees):
        gross_pay = house[index] * pay_rayt
        print("Gross pay for employee : ", index + 1, ": $", \
            format(gross_pay, ",.2f"), sep="")
maim()