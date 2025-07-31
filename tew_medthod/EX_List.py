foods = ["pizza", "burger", "salad"]
print(f"original Food: {foods}")

foods.append("pasta")
print(foods)

foods.remove("salad")
print(foods)

foods.sort()
print(foods)

print(f"total Food: ", len(foods))