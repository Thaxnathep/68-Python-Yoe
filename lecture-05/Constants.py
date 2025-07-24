import random

#ไม่เปลี่ยนค่า
Heads = 1
Tatls = 2
Tosses = 10 

def tosses_coin():
    for toss in range(Tosses):
        if random.randint(Heads, Tatls) == Heads:
            print("Heads")
        else:
            print("Tails")

tosses_coin()