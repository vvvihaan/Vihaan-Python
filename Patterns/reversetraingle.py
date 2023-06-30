"""
Write a python code to print the pattern

*****
****
***
**
*

"""
v = int(input("PLease enter value"))
print(v)
for i in range(v,0,-1):
  for x in range(1,i+1):
    print("*", end="")
  print()