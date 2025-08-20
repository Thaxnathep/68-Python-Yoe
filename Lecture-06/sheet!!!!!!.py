# === ระบบจัดการคลังสินค้า ===

# เริ่มต้นคลังสินค้า (Inventory)
# โครงสร้าง: [ชื่อสินค้า, จำนวน, ราคาต่อชิ้น]
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

# -------------------------------
# ฟังก์ชัน: อัปเดตจำนวนสินค้าเมื่อขายออก
def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0].lower() == item_name.lower():  # เทียบชื่อสินค้า (ไม่สนตัวพิมพ์เล็ก/ใหญ่)
            if quantity_sold <= 0:
                return "จำนวนที่ขายต้องมากกว่า 0"
            if quantity_sold > item[1]:
                return f"มี {item[0]} เหลือแค่ {item[1]} ชิ้น ไม่สามารถขาย {quantity_sold} ชิ้นได้"
            item[1] -= quantity_sold
            return "อัปเดตจำนวนสินค้าเรียบร้อยแล้ว"
    return "ไม่พบสินค้าที่ต้องการขาย"

# -------------------------------
# ฟังก์ชัน: คำนวณมูลค่ารวมทั้งหมดของสินค้าในคลัง
def calculate_total_value(inventory):
    return sum(item[1] * item[2] for item in inventory)

# -------------------------------
# ฟังก์ชัน: หาสินค้าที่แพงที่สุด
def find_most_expensive(inventory):
    if not inventory:
        return None
    return max(inventory, key=lambda x: x[2])[0]  # คืนชื่อสินค้าที่แพงที่สุด

# -------------------------------
# ฟังก์ชัน: เพิ่มหรืออัปเดตข้อมูลสินค้า
def add_or_update_item(inventory, item_name, quantity, price):
    if quantity < 0 or price < 0:
        return "จำนวนและราคาต้องไม่ติดลบ"
    for item in inventory:
        if item[0].lower() == item_name.lower():
            item[1] = quantity
            item[2] = price
            return "อัปเดตรายการสินค้าเรียบร้อยแล้ว"
    inventory.append([item_name, quantity, price])
    return "เพิ่มสินค้าใหม่เรียบร้อยแล้ว"

# -------------------------------
# ฟังก์ชัน: แสดงสินค้าทั้งหมดในคลัง
def show_inventory(inventory):
    print("\n=== รายการสินค้าปัจจุบัน ===")
    print(f"{'สินค้า':<10}{'จำนวน':<10}{'ราคา/ชิ้น':<10}")
    print("-" * 30)
    for item in inventory:
        print(f"{item[0]:<10}{item[1]:<10}{item[2]:<10.2f}")
    print("-" * 30)

# -------------------------------
# เมนูหลัก
def main():
    while True:
        print("\n=== ระบบจัดการคลังสินค้า ===")
        print("1. ขายสินค้า")
        print("2. คำนวณมูลค่ารวมของคลังสินค้า")
        print("3. แสดงสินค้าที่แพงที่สุด")
        print("4. เพิ่มหรืออัปเดตข้อมูลสินค้า")
        print("5. แสดงรายการสินค้า")
        print("0. ออกจากโปรแกรม")

        choice = input("กรุณาเลือกเมนู (0-5): ")

        if choice == "1":
            item = input("กรอกชื่อสินค้าที่ต้องการขาย: ")
            qty = int(input("กรอกจำนวนที่ขาย: "))
            result = update_inventory(inventory, item, qty)
            print(result)

        elif choice == "2":
            total = calculate_total_value(inventory)
            print(f"มูลค่ารวมของคลังสินค้า: ${total:.2f}")

        elif choice == "3":
            expensive = find_most_expensive(inventory)
            if expensive:
                print(f"สินค้าที่แพงที่สุดคือ: {expensive}")
            else:
                print("ไม่มีสินค้าในคลัง")

        elif choice == "4":
            name = input("กรอกชื่อสินค้า: ")
            qty = int(input("กรอกจำนวนสินค้า: "))
            price = float(input("กรอกราคาต่อชิ้น: "))
            result = add_or_update_item(inventory, name, qty, price)
            print(result)

        elif choice == "5":
            show_inventory(inventory)

        elif choice == "0":
            print("ปิดโปรแกรมเรียบร้อยแล้ว")
            break

        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

# -------------------------------
# เริ่มทำงานโปรแกรม
main()
