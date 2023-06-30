"""Write a Python code to accept a number and print the sum of digits.

Eg- 745
Output: 7+4+5
=16"""

sum=0
x = int(input("Please enter a value"))
while (x>0):
  digit= x%10
  sum=sum+digit
  x = int(x/10)
print(sum)