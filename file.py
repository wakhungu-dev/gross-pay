# Open a file
with open ('text.txt', 'r') as file:
    print(file.read())

# Read the file and line by line
with open ('text.txt', 'r') as file:
    for line in file:
        print(line, end='')

# Read the file and line by line
with open ('text.txt', 'r') as file:
    for line in file:
        print(file.readlines ())