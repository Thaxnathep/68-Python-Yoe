# สร้างลิสต์เก็บคะแนนนักเรียน
grades = [85, 90, 78, 92, 88]

# ลบค่าเกรดลำดับที่ 3 (index = 2) ออกจากลิสต์ แล้วเก็บค่าไว้ในตัวแปร third_grade
third_grade = grades.pop(2)  
# ตอนนี้ grades = [85, 90, 92, 88]
# และ third_grade = 78

# นำค่า third_grade ที่ถูกลบออกมา เพิ่มกลับไปไว้ท้ายลิสต์
grades.append(third_grade)
# ตอนนี้ grades = [85, 90, 92, 88, 78]

# แสดงลิสต์หลังจากทำ pop และ append
print(f"Grades after pop: {grades}")
# Output: Grades after pop: [85, 90, 92, 88, 78]

# หาค่าคะแนนสูงสุดจากลิสต์
max_grade = max(grades)
print(f"Max grade: {max_grade}")   # Output: Max grade: 92