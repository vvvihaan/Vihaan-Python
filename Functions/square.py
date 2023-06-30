"""Write a python code to input a number and print the square of it using math functions"""

import math
x = int(input("PLease enter a value"))

def square(x:int):
  a = math.pow(x,2)
  print(a)

square(x)