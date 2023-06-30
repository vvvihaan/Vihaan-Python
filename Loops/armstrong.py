"""Write a Python code to input a number and check if it is an Armstrong Number or not.

Example: 153
(1*1*1)+(5*5*5)+(3*3*3)= 153 
Therefore 153 is an armstrong number.

Note: Armstrong number is a number whose digits when multiplied by itself thrice and added, gives the same number as the original number."""

x = int(input("Please enter a value"))
sum = 0
val = x
cube=0
while  (val > 0):
  digit = val%10
  cube = digit * digit * digit
  sum = sum+cube
  val = int(val/10)
if (x == sum):
  print(sum,"is an armstrong number")
else:
  print(sum,"is not a armstrong number")

