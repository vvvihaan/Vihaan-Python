"""Write a python code to create a function which takes a number as a parameter and returns its square root"""

import math

b = int(input("Enter a value"))
def squareroot(b:int):
  result = math.sqrt(b)
  return result 

x = squareroot(b)
print("The square root of",b, "is =", x)
