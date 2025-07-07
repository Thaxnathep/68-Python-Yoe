x = 10
y = 20
z = 30

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

if x < y and y < z:
    print("x is less than y and y is less than z.")

if x < y or y > z:
    print("Either x is less than y or y is greater than z.")

if not (x > y):
    print("x is not greater than y.")