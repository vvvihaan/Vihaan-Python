"""
*****
 ****
  ***
   **
    *
"""
num = int(input("PLease enter a value for the number of rows you want"))

for x in range(1,num+1):#rows
  for y in range(1,x):#spaces
   print(" ",end="")
  # for i in range(6,x,-1):#columns
  for i in range(x,num+1):
    print("*",end="")
  print()