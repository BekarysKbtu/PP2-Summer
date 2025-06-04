numbers = [1,56,89,45,21]
sum = 0
max = -2222
min = 22222

for i in numbers:
    sum += i
    if i < min:
        min = i
    if i > max:
        max = i

print(f"The sum of this list: {sum}")
print(f"Maximum of this list: {max}")
print(f"Minimum of this list: {min}")
