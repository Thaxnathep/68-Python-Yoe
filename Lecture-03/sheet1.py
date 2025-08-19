while True:
    try:
        num = float(input("Input Your Number: "))
        break  # ออกจากลูปถ้าแปลงสำเร็จ
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if num > 0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")