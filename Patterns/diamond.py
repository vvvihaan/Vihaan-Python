"""
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""
for x in range(1,6):#rows
  for y in range(5,x,-1):#spaces
   print(" ",end="")
  for i in range(1,x+1):#columns
   print("* ",end="")
  print()

for g in range(1,6):#rows
  for f in range(1,g):#spaces
   print(" ",end="")
  for z in range(g,6,):
    print("* ",end="")
  print()