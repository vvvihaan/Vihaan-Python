"""
   4
  3 4
 2 3 4
1 2 3 4
"""
t  = int(input("Enter a value"))
for x in range(t,0,-1):#rows
  for y in range(x,1,-1):#spaces
    print(" ",end="")
  for v in range(x,t+1,1):#numbers
    print(v,end=" ")
  print()