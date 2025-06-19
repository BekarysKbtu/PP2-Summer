import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("\nThe path exists.")

    filename = os.path.basename(path)

    directory = os.path.dirname(path)

    print("Filename or last part:", filename)
    print("Directory portion:", directory)

else:
    print("\nThe specified path does not exist.")
