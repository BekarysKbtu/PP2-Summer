source_file = input("Enter the source filename: ")
destination_file = input("Enter the destination filename: ")

try:
    with open(source_file, 'r') as src:
        with open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line)
    print(f"Contents copied from {source_file} to {destination_file}.")
except FileNotFoundError:
    print("Source file not found. Please check the filename and try again.")
