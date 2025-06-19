import os

path = input("Enter the path: ")

if not os.path.exists(path):
    print("The specified path does not exist.")
else:
    all_items = os.listdir(path)

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("\nOnly directories:")
    for d in directories:
        print(d)

    print("\nOnly files:")
    for f in files:
        print(f)

    print("\nAll directories and files:")
    for item in all_items:
        print(item)
