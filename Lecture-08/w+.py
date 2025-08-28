def example_mode():
    with open('example_w+.txt', 'w+') as file:
        file.write("This is a first\n")
        file.write("This is a second\n")
        file.seek(0)
        count = file.read()
        print(count)

example_mode()