"""
Write a python code to print the pattern

1
44
999
16161616
2525252525

"""
for i in range(1,6):
  for x in range(1,i+1):
    print(i*i, end="")
  print()