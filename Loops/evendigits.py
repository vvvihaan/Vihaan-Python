"""Write a Program to input a number and print only the Even digits.

Example : 2534
Output : 42t"""

x = int(input("Please enter a value"))
while (x>0):
  val = x%10
  x = int(x/10)
  if (val%2==0):
    print(val)
  