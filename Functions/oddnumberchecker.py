def odd(a:int):
  if (a % 2 !=0):
    print("This is a odd number")
  else:
     print("This is not a odd number")

#driver code
a = int(input("Enter a number to be checked"))
b = odd(a)
print(b)