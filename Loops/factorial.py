"""Write a python code to input a number and print the factorial of it.

Example: Input=9
factorial= 1*2*3*4*5*6*7*8*9 = 362880
note: Do not include zero in the times series."""
sum = 1
x = int(input("Please enter a value"))
for i in range(1,x+1,1):
  sum = sum*i
print(sum)