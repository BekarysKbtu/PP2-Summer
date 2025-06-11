import math

n = int(input("Input number of sides: "))
a = int(input("Input the length of a side: "))

radian = math.pi / n
area = (n * math.pow(a, 2))/(4* math.tan(radian))

print(math.floor(area))