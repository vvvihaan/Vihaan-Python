"""
   1
  2 2
 3 3 3
4 4 4 4
"""
for x in range(1,5):
  for y in range(5,x,-1):
    print(" ",end="")
  for v in range(1,x+1):
    print(x,end=" ")
  print()