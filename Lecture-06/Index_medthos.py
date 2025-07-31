animals = ["cat", "dog", "rabbit", "hamster", "dog", "brith"]
first_dog_index = animals.index("dog")
print(f"first dog index: {first_dog_index}")

second_dog_index = animals.index("dog", first_dog_index +1)
print(f"second dog index: {second_dog_index}")