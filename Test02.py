import math
print("What is the base")
a = int(input(""))
print("What is the height")
b = int(input(""))
area = 1/2*a*b
print(f"The area is {area}")
c = a**2 + b**2
c = math.sqrt(c)
p = a + b + c
print(f"The perm is {p}")