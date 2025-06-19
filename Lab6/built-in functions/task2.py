text = input()
upper_letters = ""
lower_letters = ""

for i in text:
    if i.isupper():
        upper_letters += i
    elif i.islower():
        lower_letters += i

print(len(upper_letters))
print(len(lower_letters))