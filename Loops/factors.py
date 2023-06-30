"""Write a python code to input a number and print the factors of the number."""
x = int(input("Please enter a value"))
print("These are the factors of the number")
for i in range(1,x+1,1):
  if (x%i == 0):
    print(i)