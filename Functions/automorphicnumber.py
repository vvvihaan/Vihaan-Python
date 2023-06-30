"""
Write a function that checks for an automorphic number

Eg-
5
25

25*25=625%100    10^2=100

6*6=36%10       10^1=10
"""
# 625%Math.pow(10,digit)
# =25  == 25



import math as m  #Alias 


def count_digits(x:int):
  count = 0
  while (x > 0):
    x = x // 10
    count = count +1 
  return count 

def automorphic_number(x):
  square =  m.pow(x,2)
  digits = count_digits(x)
  power = m.pow(10,digits)
  last_digit = square%power
  if (x == last_digit):
    return True 
  else:
    return False 
  


#driver_code
x = int(input("Enter a value"))
y = automorphic_number(x)
print(y)






