# เริ่มต้นคลังสินค้า
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

# ฟังก์ชันอัปเดตสินค้าเมื่อขาย
def update_inventory(inventory, item_name, quantity_sold):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            item[1] -= quantity_sold
            return True
    return False

# ฟังก์ชันคำนวณมูลค่ารวม
def calculate_total_value(inventory):
    total = 0
    for item in inventory:
        total += item[1] * item[2]
    return total

# ฟังก์ชันหาสินค้าแพงที่สุด
def find_most_expensive(inventory):
    most_expensive = inventory[0]
    for item in inventory:
        if item[2] > most_expensive[2]:
            most_expensive = item
    return most_expensive[0]

# ฟังก์ชันเพิ่มหรืออัปเดตรายการ
def add_item(inventory, item_name, quantity, price):
    for item in inventory:
        if item[0].lower() == item_name.lower():
            item[1] = quantity
            item[2] = price
            return "Updated"
    inventory.append([item_name, quantity, price])
    return "Added"

# เมนูหลัก
while True:
    print("\n=== Inventory Management ===")
    print("1. Update inventory after sale")
    print("2. Calculate total inventory value")
    print("3. Find most expensive item")
    print("4. Add or update an item")
    print("5. Show current inventory")
    print("0. Exit")
    
    choice = input("Choose an option (0-5): ")

    if choice == "1":
        item = input("Enter item name to sell: ")
        qty = int(input("Enter quanitty sold: "))
        if update_inventory(inventory, item, qty):
            print("Inventory updated.")
        else:
            print("Item not found!")

    elif choice == "2":
        total = calculate_total_value(inventory)
        print(f"Total value of inventory: ${total:.2f}")

    elif choice == "3":
        expensive = find_most_expensive(inventory)
        print(f"Most expensive item: {expensive}")

    elif choice == "4":
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price per unit: "))
        result = add_item(inventory, name, qty, price)
        print(f"Item {result.lower()} successfully.")

    elif choice == "5":
        print("\nCurrent Inventory:")
        for item in inventory:
            print(f"{item[0]} - {item[1]} units at ${item[2]:.2f} each")

    elif choice == "0":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
