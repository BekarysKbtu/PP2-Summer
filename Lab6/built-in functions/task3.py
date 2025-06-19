text = input("Enter a string: ")
reversed_text = ''.join(reversed(text))

if text == reversed_text:
    print("This string is palindrome")
else:
    print("This string is not palindrome")
