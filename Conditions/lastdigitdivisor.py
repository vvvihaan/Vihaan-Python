x = int(input("Please enter a value"))
a = x%10
print("The last digit is", a)
if x%a==0:
  print("The last digit is completely divisble by the number")
else:
  print("The last digit is not completely divisible by the number")