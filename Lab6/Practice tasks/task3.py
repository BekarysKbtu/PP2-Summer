import os

def list_files():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files in the current directory:")
        for i, f in enumerate(files, 1):
            print(f"{i}. {f}")
    return files

def create_file():
    filename = input("Enter the name of the new file: ")
    if os.path.exists(filename):
        print("File already exists.")
    else:
        with open(filename, 'w') as f:
            print(f"File '{filename}' created successfully.")

def delete_file():
    files = list_files()
    if not files:
        return
    try:
        choice = int(input("Enter the number of the file you want to delete: "))
        if choice < 1 or choice > len(files):
            print("Invalid choice.")
            return
        filename = files[choice - 1]
        confirm = input(f"Are you sure you want to delete '{filename}'? (y/n): ").lower()
        if confirm == 'y':
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n--- File Manager ---")
        print("1. Create a new file")
        print("2. List all files")
        print("3. Delete a file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_file()
        elif choice == '2':
            list_files()
        elif choice == '3':
            delete_file()
        elif choice == '4':
            print("Exiting file manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
