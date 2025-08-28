num_EMP = int(input("Enter number of employees: "))

with open ("employees.txt", "w") as outfile:
    for count in range(1,num_EMP +1):
        print("Enter data for employees: ", count, sep='')
        name = input("Name: ")
        id_num = input("ID number: ")
        dept = input("Department: ")
        outfile.write(f"{name}\n{id_num}\n{dept}\n")

print(f"{num_EMP} employee records saved to employees.txt")
