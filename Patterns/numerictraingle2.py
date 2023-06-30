"""
   1
  1 2
 1 2 3
1 2 3 4
"""

f = int(input("Enter a number"))

for x in range(1,f+1):
  for y in range(f,x,-1):
    print(" ",end="")
  for v in range(1,x+1):
    print(v,end=" ")
  print()