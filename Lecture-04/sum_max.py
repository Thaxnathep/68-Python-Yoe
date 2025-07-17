max = 5
total = 0.0

print("This Program caculates the sum of")
print(max, "numbers you will enter.")

for counter in range(max):
    number = float(input("Enter a number: "))
    total += number

print("The total is", total)
