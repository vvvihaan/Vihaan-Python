"""Write a python code to create a function which takes 3 number as parameter and returns the largest number"""
def max_of_three(x:int,y:int,z:int):
    max_number = max(x,y,z)
    return max_number
 
x = int(input("Enter value "))
y = int(input("Enter value "))
z = int(input("Enter value "))
  
x = max_of_three(x,y,z)
print(x)