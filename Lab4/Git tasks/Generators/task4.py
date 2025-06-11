def squares(a, b):
    for i in range(a, b):
        yield i ** 2

a = int(input("Write your first number: "))
b = int(input("Write your second number: "))

for i in squares(a, b):
    print(i)