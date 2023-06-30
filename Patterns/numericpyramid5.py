"""
1
2 3
4 5 6
7 8 9 10
"""
count=1
rows = int(input("Please enter a value"))
for x in range(1,rows+ 1):#rows
  for v in range(1,x+1,1):#columns
    print(count,end="")
    count=count+1
  print()