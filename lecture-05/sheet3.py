def is_armstrong(number):
    string = str(number)            # แปลงตัวเลขเป็นสตริง เพื่อให้สามารถเข้าถึงแต่ละหลักได้
    length = len(string)            # หาจำนวนหลักของตัวเลข (เช่น 153 มี 3 หลัก)
    total = 0                       # ตัวแปรเก็บผลรวมของตัวเลขยกกำลังจำนวนหลัก

    for i in string:                # วนลูปทีละตัวอักษร (แต่ละหลัก) ในสตริง
        total += int(i) ** length   # แปลงตัวอักษรเป็นเลข แล้วยกกำลังด้วยจำนวนหลัก
                                      # จากนั้นบวกเข้ากับ total

    if total == number:             # ถ้าผลรวมที่คำนวณได้ เท่ากับตัวเลขเดิม
        return True                 # → เป็น Armstrong Number
    else:
        return False                # → ไม่ใช่ Armstrong Number

print(is_armstrong(153))           # เรียกฟังก์ชันตรวจ 153 → True
print(is_armstrong(123))           # เรียกฟังก์ชันตรวจ 123 → False