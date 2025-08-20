# สร้างลิสต์ฮีโร่หลัก
heroes = ["Ironman", "Thor", "Hulk", "Superman", "Spiderman"]

# สร้างลิสต์ฮีโร่เสริม
h2 = ["Dr.strange", "cap.america", "Black Panther", "Ant Man"]

# แทรก "Dr.strange" ไว้หน้า list
heroes.insert(0, h2[0])

# หาตำแหน่งของ "Thor"
print(heroes.index("Thor"))  # Output: 2

# แทรก "cap.america" ก่อน "Thor"
heroes.insert(heroes.index("Thor"), h2[1])
print(heroes)  
# Output: ['Dr.strange', 'Ironman', 'cap.america', 'Thor', 'Hulk', 'Superman', 'Spiderman']

# ลบ "Superman" ออกจาก list
heroes.remove("Superman")

# เพิ่ม "Ant Man" ไปท้าย list
heroes.append("Ant Man")
print(heroes)
# Output: ['Dr.strange', 'Ironman', 'cap.america', 'Thor', 'Hulk', 'Spiderman', 'Ant Man']

# เรียงลำดับตัวอักษร A-Z
heroes.sort()
print(heroes)
# Output: ['Ant Man', 'Dr.strange', 'Hulk', 'Ironman', 'Spiderman', 'Thor', 'cap.america']

# กลับลำดับ list
heroes.reverse()
print(heroes)
# Output: ['cap.america', 'Thor', 'Spiderman', 'Ironman', 'Hulk', 'Dr.strange', 'Ant Man']

# newheros ชี้ไปยัง list เดียวกับ heroes
newheros = heroes

# แก้ค่า index 0 ของ newheros → heroes ก็เปลี่ยนด้วย
newheros[0] = "Wonder Women"
print(heroes)
# Output: ['Wonder Women', 'Thor', 'Spiderman', 'Ironman', 'Hulk', 'Dr.strange', 'Ant Man']

# สร้างสำเนา list แยกจาก heroes
copyheros = [] + heroes
print(copyheros)
# Output: ['Wonder Women', 'Thor', 'Spiderman', 'Ironman', 'Hulk', 'Dr.strange', 'Ant Man']

# แก้ค่า index 0 ของ copyheros → heroes ไม่เปลี่ยน
copyheros[0] = "Hunuman"
print(heroes)
# Output: ['Wonder Women', 'Thor', 'Spiderman', 'Ironman', 'Hulk', 'Dr.strange', 'Ant Man']
print(copyheros)
# Output: ['Hunuman', 'Thor', 'Spiderman', 'Ironman', 'Hulk', 'Dr.strange', 'Ant Man']
