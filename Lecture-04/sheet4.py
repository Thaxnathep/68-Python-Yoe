max = 5                        # กำหนดจำนวนตัวเลขที่ผู้ใช้จะป้อน (ในที่นี้คือ 5 ครั้ง)
total = 0.0                    # ตัวแปรสำหรับเก็บผลรวม เริ่มต้นที่ 0.0 (ชนิด float)

print("This Program caculates the sum of")  # แสดงข้อความอธิบาย
print(max, "numbers you will enter.")       # แสดงจำนวนตัวเลขที่จะต้องป้อน

for counter in range(max):                  # วนลูปตามจำนวน max (คือ 5 รอบ)
    number = float(input("Enter a number: "))  # รับค่าตัวเลขจากผู้ใช้ และแปลงเป็น float
    total += number                         # บวกค่าที่ป้อนเข้าไปในผลรวม (สะสม)

print("The total is", total)                # แสดงผลรวมของตัวเลขทั้งหมดที่ป้อน