"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
for x in range(1,6):#Rows
  for y in range(4,x-1,-1):#spaces
    print(" ",end="")
  for j in range(1,x+1):#Columns
    print("* ",end="")
  print()