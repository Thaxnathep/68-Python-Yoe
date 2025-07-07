inchar = input("Enter character to cheak: ")
if inchar >= 'A' and inchar <= 'Z' :
    print("Your input is upper case letter: ", inchar)
elif inchar >= 'a'and inchar <= 'z':
    print("Your input is Lower case letter: ", inchar)
elif inchar >= '0'and inchar <= '9':
    print("Your input Number: ", inchar)
else:
    print("It's not a Letter or Number." ,inchar )