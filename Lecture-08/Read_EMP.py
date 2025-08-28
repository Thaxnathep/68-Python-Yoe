with open("employees.txt", "r") as infile:
    for line in infile:
        print(f"Name : ", line.strip())
        print(f"ID : ", line.strip())
        print(f"Dept : ", line.strip())
