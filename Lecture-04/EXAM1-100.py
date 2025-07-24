num = 1
total_max = 100
rows = int(input("input your row: "))
for r in range(rows):
    cols = (total_max // rows)
    for c in range(cols):
        if num <= total_max:
            print(f"{num:3}" ,end=" ")
            num += 1
        else:
            print("  ", end=" ")