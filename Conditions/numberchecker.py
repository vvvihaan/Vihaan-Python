"""Write a python code to input a number and check if it is a single digit number or a double digit number or a 3 digit number"""
x = int(input("Please enter a value of up to 3 digits"))
if (x>=-9 and x<=9):
  print("This is a one digit value")
elif((x<=-10 and x>=-99) or (x>=10 and x<=99)):
  print("This is a 2 digit value")
elif((x<=-100 and x>=-999) or (x>=100 and x<=999)):
  print("This is a 3 digit value")
else:
  print("This value does not satisfy the condition")