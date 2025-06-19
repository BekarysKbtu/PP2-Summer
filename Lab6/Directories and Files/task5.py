items = ['apple', 'banana', 'cherry', 'date']

filename = 'fruits.txt'

with open(filename, 'w') as file:
    for item in items:
        file.write(item + '\n')

print(f"List written to {filename}")
