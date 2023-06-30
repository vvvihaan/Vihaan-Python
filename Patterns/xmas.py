"""
    *
   * *
  * * *
 * * * *
* * * * *
    *
   * *
  * * *
 * * * *
* * * * *
    *
   * *
  * * *
 * * * *
* * * * *
   ***
   ***
   ***
   ***
"""
for x in range(1,6):#rows
  for y in range(5,x,-1):#spaces
   print(" ",end="")
  for i in range(1,x+1):#columns
   print("* ",end="")
  print()
  
for q in range(1,6):#rows
  for t in range(5,q,-1):#spaces
   print(" ",end="")
  for c in range(1,q+1):#columns
   print("* ",end="")
  print()
  
for a in range(1,6):#rows
  for b in range(5,a,-1):#spaces
   print(" ",end="")
  for v in range(1,a+1):#columns
   print("* ",end="")
  print()
  
for e in range(4):
    print("   ", end="")
    for r in range(3):
        print("*", end="")
    print()

  