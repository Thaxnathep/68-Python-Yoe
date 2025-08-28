with open("sales.txt", "r") as infile:
    total = 0.0
    for line in infile:
        amount = float(line.strip())
        total += amount
        print(f"sales amount: {amount:.2f}")
    print(f"Total sales: {total:.2f}")