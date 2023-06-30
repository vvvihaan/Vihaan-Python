"""Take a number input from the user and check if it is a negative or positive, odd or even number """
x = int(input("Please enter a value"))
if (x%2==0): #checking even
  if(x>=0): #checking positive
    print("This is a positive even number")
  else: #checking negative
    print("This is a negative even number")
else: #checking odd
  if(x>=0):
    print('This is a positive odd number')
  else:
    print("This is a negative odd number") 