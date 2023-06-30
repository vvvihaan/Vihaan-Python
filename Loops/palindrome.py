"""Palindrome number is a number, which when reversed, it is same as the original number.
eg- 454
reverse : 454

Write a python code to input a number and check if its a palindrome number or not."""

reverse = 0
x = int(input("Please enter a value"))
xcopy = x
while (x>0):
  digit = x%10
  x = int(x/10)
  reverse = (reverse*10)+digit
if (reverse==xcopy):
  print("This is a palindrome number")
else:
  print("This is not a palindrome number")