"""
Write a python code to print the pattern

*
**
***
****
*****

"""
x = int(input("Enter a value"))

for i in range(1,x+1):#rows
  for j in range(1,i+1):#columns
    print("*",end="")
  print()