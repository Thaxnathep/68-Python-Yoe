phonebook = {"Thanathep": '777-1111', "Yoey": "777-2222", "Tonor": "777-3333",
             "Pluto": "777-4444"}
heroesdivt = {}
heroesdivt["Hulk"] = "888-1111"
heroesdivt["Iron Man"] = "888-2222"
print(heroesdivt.get("Halk", "key not found"))
print(heroesdivt.get("Hulk", "key not found"))

for key, value in phonebook.items():
    print(key, value)
    