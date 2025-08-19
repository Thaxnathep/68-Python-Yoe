weight = float(input("Enter your weight: "))

height = float(input("Enter your height: "))
height = height/100


bmi =weight/(height*height)

print("Your BMI is " ,format(bmi, '5.2f'))
