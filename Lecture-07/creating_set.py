fruits = {"apple", "Banana", "cherry", "apple"}
print(fruits)

numbers = set([1, 2, 3, 4, 1, 2, 3])
print(numbers)

fruits.add("orange")
print(fruits)

fruits.remove("Banana")
print(fruits)

fruits.discard("grape")
print(fruits)

remove_item = fruits.pop()
print(remove_item)
print(fruits)

fruits.clear()
print(fruits)