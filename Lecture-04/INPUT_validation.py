score = float(input("Enter the test score: "))
while score < 0 or score > 100:
    print("ERROR: The score cannot be negative or greater than 100.")
    score = int(input("Enter the test score: "))

print(f"Your score is: {score}")