R = int(input("How many rows? "))
C = int(input("How many columns? "))

for r in range(R):          # ใช้ r แทนแถว
    row = "*" * C           # สร้างแถวที่มี * จำนวน C ตัว
    print(row)              # แสดงผลแถว

