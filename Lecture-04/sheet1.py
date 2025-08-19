for letter in "Thanathep Preammanee":   # วนลูปทีละตัวอักษรจากข้อความ "Thanathep Preammanee"
    if letter == 'p' or letter == 'n':  # ถ้าตัวอักษรที่เจอเป็น 'p' หรือ 'n'
        break                           # หยุดการทำงานของลูปทันที
    print(letter, end=" ")              # ถ้าไม่ใช่ 'p' หรือ 'n' จะแสดงตัวอักษรออกมา พร้อมเว้นวรรค (ไม่ขึ้นบรรทัดใหม่)