"""
   1
  2 1
 3 2 1
4 3 2 1
"""
g = int(input("Enter a value"))
for x in range(1,g+1):
  for y in range(g,x,-1):
    print(" ",end="")
  for v in range(x,0,-1):
    print(v,end=" ")
  print()