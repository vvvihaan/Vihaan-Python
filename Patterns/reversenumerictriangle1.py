"""
Write a python code to print the pattern

11111
2222
333
44
5

"""
v = int(input("PLease enter a value"))
print(v)
for i in range(1,v+1,1):#Row
  for x in range(v+1,i,-1):#column
    print(i,end="")
  print()

#CODE does not work