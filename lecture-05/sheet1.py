def calculate_stats(numbers):             # สร้างฟังก์ชัน calculate_stats ที่รับลิสต์ numbers เข้ามา
    total_sum = sum(numbers)              # คำนวณผลรวมของตัวเลขทั้งหมดในลิสต์
    average = total_sum / len(numbers)    # คำนวณค่าเฉลี่ย (ผลรวม / จำนวนสมาชิกในลิสต์)
    maximum = max(numbers)                # หาค่ามากที่สุดในลิสต์
    minimum = min(numbers)                # หาค่าน้อยที่สุดในลิสต์
    return total_sum, average, maximum, minimum  # ส่งค่ากลับทั้งหมดเป็น tuple

# ตัวอย่างข้อมูลที่ใช้ทดสอบ
numbers = [5, 10, 15, 20, 25]

# เรียกใช้ฟังก์ชันแล้วแยกค่าที่ return ออกมาเก็บในตัวแปร
total, avg, max_num, min_num = calculate_stats(numbers)

# แสดงผลลัพธ์
print(f'Total sum: {total}')     # ผลรวม
print(f'Average: {avg}')         # ค่าเฉลี่ย
print(f'maximum: {max_num}')     # ค่ามากที่สุด
print(f'minimum: {min_num}')     # ค่าน้อยที่สุด