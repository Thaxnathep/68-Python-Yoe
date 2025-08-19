def find_max(*args):             # ฟังก์ชันรับตัวเลขหลายตัวเป็น tuple ผ่าน *args
    if not args:                 # ถ้าไม่มีตัวเลขส่งเข้ามา (empty tuple)
        return None              # คืนค่า None เพราะไม่มีตัวเลขให้เปรียบเทียบ

    max_value = args[0]           # เริ่มต้นสมมติค่ามากที่สุด = ตัวแรกใน args

    for number in args:           # วนลูปเช็คตัวเลขทุกตัว
        if number > max_value:   # ถ้าตัวเลขปัจจุบันมากกว่าค่าที่เก็บไว้
            max_value = number   # อัปเดตค่ามากที่สุด

    return max_value              # คืนค่ามากที่สุดที่เจอ

# เรียกใช้ฟังก์ชันพร้อมเลขหลายตัว
result = find_max(3, 5, 7, 2, 8)

# แสดงผลลัพธ์
print(f"The maximum value is: {result}")