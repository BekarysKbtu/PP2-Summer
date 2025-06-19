import os

file_path = input("Enter the path to the file you want to delete: ")

if not os.path.exists(file_path):
    print("The specified path does not exist.")
elif not os.path.isfile(file_path):
    print("The specified path is not a file.")
elif not os.access(file_path, os.W_OK):
    print("You don't have permission to delete this file.")
else:
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except Exception as e:
        print("Error while deleting file:", e)
