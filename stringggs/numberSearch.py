#write a python code to input a digit and search if it is present in the number or not

# Example
# harsh sir python
# python


integerval = input("Enter a phone number, ")
number_search = input("Enter a integer to search, ")
count = 0

#manual way
# for i in integerval:
#   if (i == number_search):
#     count = count+1
# print(f"{number_search} was present in {integerval},{count} number of times")

#using functions
if (number_search in integerval):
  count = integerval.count(number_search)
  print(f"{number_search} is present in {integerval} and occurs {count} times ")
else:
  print(f"{integerval} is not present in {integerval}")



