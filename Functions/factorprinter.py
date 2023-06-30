"""Write a python code to create a function which takes a number as a parameter and print all of its factors"""

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if (x % i == 0):
           print(i)


b = int(input("Enter a number of which you want the factors"))

print_factors(b)