"""Write a python which inputs the year of birth from the user and make a function which calculates the age"""
a = int(input("Please enter your date of birth"))
def age(a:int):
  result = 2023 - a
  return result

print("Your age is ",age(a))