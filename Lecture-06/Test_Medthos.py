heroes = ["Ironman", "Thor", "Hulk", "Superman", "Spiderman"]
h2 = ["Dr.strange", "cap.america", "Black Panther", "Ant Man"]

heroes.insert(0, h2[0])
print(heroes.index("Thor"))
heroes.insert(heroes.index("Thor"), h2[1])
print(heroes)
heroes.remove("Superman")
heroes.append("Ant Man")
print(heroes)
heroes.sort()
print(heroes)
heroes.reverse()
print(heroes)
newheros = heroes
newheros[0] = "Wonder Women"
print(heroes)
copyheros = [] + heroes
print(copyheros)
copyheros[0] = "Hunuman"
print(heroes)
print(copyheros)