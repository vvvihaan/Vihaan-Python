"""Write a python code to print the sum of squares of 1 to 10
Example : (1*1)+(2*2)+(3*3)+...(10*10)"""
i = 0
sum = 0
sqr = 0
while (i <=10):
  sqr = i*i
  sum = sum+sqr
  i = i+1
print(sum)
