count = 1
R = int(input("How many rows?"))
k = 100 / R
while count <= 100:
        if count >= k:
            print(count, end=" ")
            count = count + 1