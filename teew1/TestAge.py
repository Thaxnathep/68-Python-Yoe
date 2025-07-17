age = float(input("Enter Your Old: "))

if age > 0 and age < 13:
    print("Deg")
elif age >= 13 and age <= 19:
    print("Wai Ruan")
elif age >= 20 and age <=59:
    print("Phu Yai")
elif age >= 60:
    print("Phu Sung A Yuu")
else:
    print("Unknow")
