"""
Write a python code to print the pattern

12345
1234
123
12
1

"""
for i in range(6,1,-1):
  for x in range(1,i):
    print(x,end="")
  print()