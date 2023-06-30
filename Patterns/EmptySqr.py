"""
Write a python code to print the pattern

*****
*   *
*   *
*****
"""
print("*****")
for i in range(1,3):#row
  print("*", end="")
  for x in range(1,4): #column
    print(" ",end="")
  print("*")
print("*****")