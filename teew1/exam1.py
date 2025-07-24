num = [1, 2, 3, 4, 5, 1, 2, 3]
print(num)

# สร้างลิสต์ใหม่สำหรับเก็บตัวเลขที่ไม่ซ้ำกัน
unique = []

# ใช้ for + if เพื่อตรวจสอบว่าเลขนั้นเคยอยู่ใน unique_list หรือยัง
for number in num:
    if number not in unique:
        unique.append(number)

# เรียงลำดับเพื่อความเรียบร้อย
unique.sort()
print(unique)

