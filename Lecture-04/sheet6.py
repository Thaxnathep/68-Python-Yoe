keep_going = 'y'                                # ตั้งค่าเริ่มต้นเป็น 'y' เพื่อให้เข้า while loop

while keep_going.lower() == 'y':                 # วนลูปตราบใดที่ผู้ใช้ตอบ y (ไม่สนว่าเป็น y หรือ Y)
    sales = float(input('Enter The amount of sales: '))      # รับค่าตัวเลขยอดขายจากผู้ใช้
    comm_rate = float(input('Enter commission of sales: '))  # รับอัตราค่าคอมมิชชั่น (เช่น 0.1 แปลว่า 10%)
    
    commission = sales * comm_rate              # คำนวณค่าคอมมิชชั่น = ยอดขาย × อัตราคอม
    print(f'The commission is ${commission:.2f}')  # แสดงผล โดย .2f หมายถึงทศนิยม 2 ตำแหน่ง
    
    keep_going = input('Do you want to continue? (y/n): ')   # ถามผู้ใช้ว่าจะทำต่อไหม ถ้าพิมพ์ y → loop ทำต่อ