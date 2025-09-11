filename = input('Enter a filename: ')
try:
    infile = open(filename, 'r')
    contents = infile.read()
    print(contents)
    infile.close()
except IOError:
    print(f"Error: Cloud not open or read the file '{filename}'")

print("End of program")
