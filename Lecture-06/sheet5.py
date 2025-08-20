ss = "Sammy Sharki!"  # สร้างตัวแปรสตริง

print(ss[4])        # แสดงตัวอักษรที่ตำแหน่ง index = 4
# Output: y   (เพราะ S=0, a=1, m=2, m=3, y=4)

print(ss[6:11])     # ตัดสตริงจาก index 6 ถึง 10 (ไม่รวม 11)
# Output: harki   (S=0,a=1,m=2,m=3,y=4, ' '=5, S=6,h=7,a=8,r=9,k=10,i=11)

print(ss[:5])       # ตัดตั้งแต่เริ่มต้นจนถึง index 4 (ไม่รวม 5)
# Output: Sammy

print(ss[7:])       # ตัดตั้งแต่ index 7 ถึงตัวสุดท้าย
# Output: harki!

print(ss[-4:-1])    # ตัดสตริงจากด้านหลัง เริ่มที่ -4 ถึง -2 (ไม่รวม -1)
# Output: rki   (i=-2, k=-3, r=-4, !=-1)

print(ss[6:11])     # ตัดสตริงเหมือนด้านบน index 6 ถึง 10
# Output: harki

print(ss[6:11:1])   # ตัดสตริงจาก 6 ถึง 10 โดยก้าวทีละ 1
# Output: harki   (เหมือนกับบรรทัดบน)

print(ss[0:12:2])   # ตัดตั้งแต่ index 0 ถึง 11 โดยก้าวทีละ 2
# Output: Sm  hrk   (เลือกตัวอักษร index 0,2,4,6,8,10)

print(ss[0:12:4])   # ตัดตั้งแต่ index 0 ถึง 11 โดยก้าวทีละ 4
# Output: SySk   (เลือกตัวอักษร index 0,4,8)

print(ss[::4])      # ตัดสตริงทั้งหมด แต่ก้าวทีละ 4 ตัวอักษร
# Output: SySk   (เลือก index 0,4,8)

print(ss[::-1])     # กลับสตริงจากหลังมาหน้า
# Output: !ikrahS ymmaS

print(ss[::-2])     # กลับสตริงจากหลังมาหน้า แต่ก้าวทีละ 2 ตัว
# Output: ira myS   (เลือก index 12,10,8,6,4,2,0)