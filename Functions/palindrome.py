"""Write a function that takes a number and returns if it is a Palindrome number or not"""

def palindrome(x:int):
  reverse = 0
  xcopy = x
  while (x>0):
    digit = x%10
    x = int(x/10)
    reverse = (reverse*10) + digit
  if (reverse == xcopy):
    return True
  else:
    return False 

x = int(input("Enter a value"))
y = palindrome(x)
print(y)



