def down(n):
    for i in range(n, 0, -1):
        yield i 

n = int(input("Write your number: "))
for i in down(n):
    print(i)