"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
num = int(input("Please enter a value for the number of rows you want"))
for x in range(1,num+1):#rows
  for w in range(1,x):#spaces
    print(" ",end="")
  for y in range(x,num+1):#columns
   print("* ",end="")
  print()