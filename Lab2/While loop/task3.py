password = input("Enter the password: ")

while True:
    if(password == "admin123"):
        print("Password is correct")
        break
    else:
        print("Password is wrong try again")
        password = input("Enter the password: ")
  