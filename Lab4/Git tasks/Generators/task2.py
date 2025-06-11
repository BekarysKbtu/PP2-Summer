def even_generator(n):
    for i in range(0, n):
        if i % 2 == 0:
           yield i 

n = int(input("Write your number: "))
for i in even_generator(n):
    print(i)