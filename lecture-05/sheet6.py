import math_operation   # นำเข้าโมดูล math_operation ที่เราสร้างไว้ ซึ่งมีฟังก์ชันคณิตศาสตร์พื้นฐาน

# เรียกใช้ฟังก์ชัน addth ใน math_operation เพื่อบวกเลข 10 + 5
result_add = math_operation.addth(10, 5)

# เรียกใช้ฟังก์ชัน subtract เพื่อหาผลลบ 10 - 5
result_subtract = math_operation.subtract(10, 5)

# เรียกใช้ฟังก์ชัน multiply เพื่อคูณ 10 * 5
result_multiply = math_operation.multiply(10, 5)

# เรียกใช้ฟังก์ชัน divide เพื่อหาร 10 / 5
result_divide = math_operation.divide(10, 5)

# แสดงผลลัพธ์แต่ละการคำนวณ
print(f'Addition: {result_add}')          # Addition: 15
print(f'Subtracyion: {result_subtract}') # Subtracyion: 5
print(f'Multiplication: {result_multiply}') # Multiplication: 50
print(f'Division: {result_divide}')      # Division: 2.0