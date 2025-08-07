phonebook = {"Thanathep": '777-1111', "Yoey": "777-2222", "Tonor": "777-3333"}

print(phonebook)

print(phonebook["Yoey"])
print(phonebook.get("Tonor"))

key = "Pluto"
if key in phonebook:
    print(phonebook["Pluto"])
else: 
    print(key + "not in Phonebook")

phonebook["sim"] = "777-4567"
phonebook["teera"] = "777-4444"
phonebook["Yoey"] = "777-2122"
print(phonebook)

del phonebook["sim"]
print(phonebook)