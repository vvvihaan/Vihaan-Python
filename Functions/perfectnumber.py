def factors(x:int):
  sum = 0
  for i in range(1, x):
    if (x % i == 0):
      sum = sum + i
      
  print(sum)
  if(sum==x):
    return True 
  else:
    return False 

x = int(input("Please enter a input"))
y = factors(x)
print(y)
