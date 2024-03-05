#Pascal's Triangle
#Date:23/02/2024
#Name : Elsie Muturi
from math import factorial
n = 5
for x in range(n):
    for r in range(n-x+1):
    print( end ="")
    for j in range(x+1):
        print(factorial (x))/ ((factorial(j)) * (factorial(x - j)) )
    print()

