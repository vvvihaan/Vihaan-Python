"""Write a Program to input a number and print the count of even digits and odd digits.

Example : 25347
Output : Even=2
         Odd=3"""
even=0
odd=0
x = int(input("Please enter a value"))
while (x>0):
  digit = x%10
  x = int(x/10)
  if (digit%2==0):
    even=even+1
  elif (digit%2!=0):
    odd=odd+1
print("This is the number of odd value",odd,"\nThis is the number of even values",even)