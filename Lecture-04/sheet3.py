input_string = input("Enter a String: ")   # รับข้อความจากผู้ใช้
modified_string = ""                        # สร้างตัวแปรว่างไว้เก็บข้อความที่ถูกแก้ไข
vowels = "aeiouAEIOU"                       # กำหนดตัวอักษรสระทั้งตัวเล็กและตัวใหญ่

for char in input_string:                   # วนลูปทีละตัวอักษรในข้อความที่ผู้ใช้ป้อน
    upper_char = char.upper()               # แปลงอักษรที่ได้ให้เป็นตัวพิมพ์ใหญ่
    if upper_char in vowels:                # ถ้าตัวอักษรเป็นสระ (a, e, i, o, u)
        modified_string += "*"              # แทนที่ด้วยเครื่องหมาย *
    else:
        modified_string += upper_char       # ถ้าไม่ใช่สระ เก็บตัวอักษร (ที่เป็นพิมพ์ใหญ่แล้ว) ไว้ในข้อความใหม่

print("modified string:", modified_string)  # แสดงข้อความใหม่ที่ถูกแก้ไข