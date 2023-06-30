"""
Write a python code to print the pattern

1
12
123
1234
12345

"""
for i in range(1,6):
  for x in range(1,i+1):
    print(x,end="")
  print()