employees = int(input("Enter the number of employees: "))

if employees < 50:
    print("small Company")
elif employees < 250:
    print("Meduim Company")
elif employees >=250:
    print("Large Company")