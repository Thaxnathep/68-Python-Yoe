import struct

num_records = int(input("Enter number of records: "))
with open("records.bin", "wb") as outfile:
    for _ in range(num_records):
        id_num = int(input("Enter your ID: "))
        name = input("Enter your name: ")
        age = int(input("Enter your Age: "))
        gpa = float(input("Enter GPA: "))
        data = struct.pack("i20sif", id_num, name.encode(), age, gpa)
        outfile.write(data)