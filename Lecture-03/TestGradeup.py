score = int(input("Enter the score: "))

if score >= 70 :
    if score >= 90 :
        print("Grade: A")
    elif score >= 80 :
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Grade: D or F")