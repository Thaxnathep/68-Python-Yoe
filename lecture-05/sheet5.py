def format_strings(*args):
    """
    ฟังก์ชันรวมข้อความหลายตัวเป็น string เดียว
    - รวมทุก argument เข้าด้วยกัน
    - แทนช่องว่างด้วย "-" 
    - แปลงเป็นตัวพิมพ์ใหญ่
    """
    return "".join(args).replace(" ", "-").upper()
    # 1. "".join(args) → รวมทุก argument เป็น string เดียว
    # 2. .replace(" ", "-") → แทนช่องว่างด้วย "-"
    # 3. .upper() → แปลงเป็นตัวพิมพ์ใหญ่

# ส่วนนี้เป็นจุดเริ่มต้นของโปรแกรม
if __name__ == '__main__':
    result = format_strings("Hello", "world", "this", "is", "a", "test")
    print(result)  # ผลลัพธ์: HELLOWORLDTHISISATEST

    result = format_strings("Python", "is", "fun")
    print(result)  # ผลลัพธ์: PYTHONISFUN

    result = format_strings("Hello world")
    print(result)  # ผลลัพธ์: HELLO-WORLD