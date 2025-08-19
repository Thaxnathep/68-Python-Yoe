# กำหนดจำนวนพนักงานทั้งหมด
num_employees = 6

# สร้างฟังก์ชันสำหรับคำนวณเงินเดือนรวม
def maim():  # ฟังก์ชันชื่อ maim (แนะนำเปลี่ยนเป็น main จะอ่านง่ายกว่า)
    
    # สร้างลิสต์สำหรับเก็บชั่วโมงทำงานของแต่ละพนักงาน เริ่มต้นด้วย 0
    house = [0] * num_employees

    # รับค่าชั่วโมงทำงานของแต่ละพนักงาน
    for index in range(num_employees):
        # แสดงข้อความขอให้ผู้ใช้กรอกชั่วโมงทำงาน
        print("Enter you house worked by employee", index + 1, ": ", sep="", end="")
        # รับค่าชั่วโมงและแปลงเป็น float แล้วเก็บลงในลิสต์
        house[index] = float(input())

    # รับค่าค่าแรงต่อชั่วโมงและแปลงเป็น float
    pay_rayt = float(input("Enter your hourly pay rate: "))

    # คำนวณและแสดงเงินเดือนรวม (Gross pay) ของแต่ละพนักงาน
    for index in range(num_employees):
        gross_pay = house[index] * pay_rayt  # ชั่วโมงทำงาน × ค่าแรงต่อชั่วโมง
        # แสดงผลลัพธ์พร้อมรูปแบบตัวเลข (มี comma และ 2 ตำแหน่งทศนิยม)
        print("Gross pay for employee : ", index + 1, ": $", \
            format(gross_pay, ",.2f"), sep="")

# เรียกใช้งานฟังก์ชัน
maim()

