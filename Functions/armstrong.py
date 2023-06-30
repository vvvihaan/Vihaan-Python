"""
Write a function that takes a number and returns if its a armstrong number or not

eg=153
1*1*1 +  5*5*5  +  3*3*3
1+125+27
153"""

def armstrong(x:int):
  sum = 0
  temp = x
  while (temp > 0):
    digit = temp % 10
    sum = sum + digit**3
    temp = temp //10
  if (x ==sum):
    return True
  else:
    return False 

x = int(input("Enter a value"))
y = armstrong(x)
print(y)
    







