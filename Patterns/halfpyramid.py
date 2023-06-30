"""
    *
   **
  ***
 ****
*****
"""
v = int(input("Please enter a value for the size of the triangle"))
print(v)
for x in range(1,v+1):#Row
  for y in range(v,x,-1):#spaces
    print(" ",end="")
  for i in range(1,x+1):#column
    print("*",end="")
  print()