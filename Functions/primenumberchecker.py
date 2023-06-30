
x = int(input("Enter value"))
def print_prime(x:int):
    for i in range(2,x):
      if (x % i == 0):
          return False
    return True

b = print_prime(x)
if (b == True):
  print(x," is a prime number")
else:
  print(x,"is not a prime number")


