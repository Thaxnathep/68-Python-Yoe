setA = {1, 2, 3, 4}       # สร้าง setA
setB = set([8, 9, 10])    # สร้าง setB

setA.add(5)               # เพิ่ม 5 เข้า setA
setB.update([6, 7])       # เพิ่ม 6,7 เข้า setB
Uset = setA | setB        # union ของ setA กับ setB
print(Uset)               # Output: {1,2,3,4,5,6,7,8,9,10}
print(len(Uset))          # Output: 10 → จำนวนสมาชิกทั้งหมด

setB.update('ABCD')       # เพิ่มตัวอักษร A,B,C,D เป็นสมาชิกแยก
setA.update([6, 7, 8])    # เพิ่ม 6,7,8 เข้า setA
print(setB)                # Output: {6,7,8,9,10,'A','B','C','D'}

print(setA.intersection(setB))  # สมาชิกที่อยู่ทั้งสอง set
# Output: {6,7,8}

print(setA ^ setB)              # symmetric difference → สมาชิกที่อยู่ใน set ใด set หนึ่งแต่ไม่อยู่ทั้งสอง
# Output: {1,2,3,4,5,9,10,'A','B','C','D'}

setB.remove('B')        # ลบ 'B' → ถ้าไม่มีจะ error
setB.discard(10)        # ลบ 10 → ถ้าไม่มีไม่ error
print(setB)             # Output: {6,7,8,9,'A','C','D'}

print(setA.clear())     # ลบสมาชิกทั้งหมดใน setA → Output: None

for val in Uset:        # วนลูปสมาชิกใน Uset
    print(val)
# Output: 1 2 3 4 5 6 7 8 9 10 (ลำดับไม่แน่นอน)