phonebook = {"Thanathep": '777-1111', "Yoey": "777-2222", "Tonor": "777-3333"}
phonebook["brat"] = [1, 3, 5]

elements = len(phonebook)
print("There are ", elements, "names in phonebook")

for key in phonebook:
    print((key, "phone number is: ", phonebook[key]))

phonebook["brat"][1] = 9
print(phonebook)