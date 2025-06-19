filename = input("Enter the filename: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print(f"Number of lines in the file: {len(lines)}")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
