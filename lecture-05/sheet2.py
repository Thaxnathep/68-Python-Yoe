import random                   # นำเข้ามอดูล random เพื่อสุ่มตัวเลข

# กำหนดค่าคงที่ ไม่เปลี่ยนค่า
Heads = 1                        # กำหนดให้ 1 = หัว
Tatls = 2                        # กำหนดให้ 2 = ก้อย
Tosses = 10                       # จำนวนครั้งที่โยนเหรียญ

# ฟังก์ชันสำหรับโยนเหรียญ
def tosses_coin():
    for toss in range(Tosses):          # วนลูปจำนวน Tosses ครั้ง (10 ครั้ง)
        if random.randint(Heads, Tatls) == Heads:   # สุ่มตัวเลขระหว่าง 1-2 ถ้าได้ 1 = หัว
            print("Heads")                          # แสดง "Heads"
        else:
            print("Tails")                          # ถ้าไม่ใช่ 1 แสดง "Tails"

tosses_coin()  # เรียกใช้ฟังก์ชันเพื่อทำการโยนเหรียญ