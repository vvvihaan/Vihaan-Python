"""Write a function which checks if the input year is a leap year or not"""
a = int(input("Please enter a value that you want checked "))
def year(a:int):
  if (a%4 ==0):
    return True
  else:
    return False


b = year(a)
if(b==True):
  print("It is leap year")
else:
  print("Its not a leap year")










