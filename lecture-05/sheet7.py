def print_all(*args):
    """
    ฟังก์ชันรับ argument กี่ตัวก็ได้ แล้วพิมพ์ค่าแต่ละตัวพร้อมหมายเลขลำดับ
    """
    for index, arg in enumerate(args):  # ใช้ enumerate เพื่อได้ทั้ง index และค่า argument
        print(f'Argument {index + 1}: {arg}')  
        # index + 1 → เริ่มนับจาก 1 แทนที่จะเริ่มจาก 0
        # {arg} → แสดงค่าของ argument
        # ผลรับ (Output) จะเป็นข้อความที่แสดงลำดับและค่าของแต่ละ argument

# เรียกใช้งานฟังก์ชัน พร้อม argument หลายประเภท
print_all("Python", 3.8, True, [1,2,3], {"key": "value"})

# ผลรับ (Output) ของโค้ดด้านบนจะเป็น:
# Argument 1: Python
# Argument 2: 3.8
# Argument 3: True
# Argument 4: [1, 2, 3]
# Argument 5: {'key': 'value'}