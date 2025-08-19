poin1 = float(input("Enter the score for Test 1: "))
poin2 = float(input("Enter the score for Test 2: "))
poin3 = float(input("Enter the score for Test 3: "))

score = (poin1 + poin2 + poin3) / 3

print("The average score is: " ,format(score, '5.2f'))

if score > 95:
    print("congratulations! ")
elif score <= 95:
    print("So Sad! ")