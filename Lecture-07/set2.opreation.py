# สร้าง set ตัวอย่าง
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# -------------------
# Union (รวมสมาชิกทั้งสอง set)
union_set = setA | setB
print("Union:", union_set)  # {1, 2, 3, 4, 5, 6}

# Intersection (สมาชิกที่อยู่ทั้งสอง set)
intersection_set = setA & setB
print("Intersection:", intersection_set)  # {3, 4}

# Difference (สมาชิกใน setA แต่ไม่อยู่ setB)
difference_set = setA - setB
print("Difference (A-B):", difference_set)  # {1, 2}

# Symmetric Difference (สมาชิกที่อยู่ set ใด set หนึ่ง แต่ไม่อยู่ทั้งสอง)
symmetric_difference_set = setA ^ setB
print("Symmetric Difference:", symmetric_difference_set)  # {1, 2, 5, 6}