import random
row = 3
col = 4

def main():
    values = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for r in range(row):
        for c in range(col):
            values[r][c] = random.randint(1, 100)
    print(values, end=" ")
    
main()