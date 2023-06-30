"""Write a python code to print the sum of CUBEs of 1 to 10
Example : (1*1*1)+(2*2*2)+(3*3*3)+...(10*10*10)"""
i = 1
sum = 0
cube = 0
while (i<=10):
  cube = i*i*i
  sum = cube+sum
  i = i+1
print(sum)