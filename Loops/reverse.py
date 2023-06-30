"""Write a python code to input a number and print the reverse of it."""
rev=0
x = int(input("Please enter a value"))
while (x>0):
  digit = x%10
  rev=(rev*10)+digit
  x = int(x/10)
print(rev)

#   80+4=840+5=845
# 548/10=54.8=54/10=5.4=5/10=0.5=0