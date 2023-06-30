"""Write a Python code to accept a number and print the product of digits.

Eg- 745
Output: 7*4*5
=140"""

product=1
x = int(input("Please enter a value"))
while (x>0):
  digit= x%10
  product=product*digit
  x = int(x/10)
print(product)