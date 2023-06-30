"""Write a python code to input a Year and check if it is a leap year or not."""
x = int(input("Please enter a value"))
if (x%4 == 0):
  print("This is a leap year")
else:
  print("This is not a leap year")