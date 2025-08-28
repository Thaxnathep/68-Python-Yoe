num_day = int(input("Enter your number of day "))

with open("sales.txt", "w") as outfile:
    for day in range(1,num_day +1):
        sales = float(input(f"Enter sales for day {day}: "))
        outfile.write(f"{sales}\n")