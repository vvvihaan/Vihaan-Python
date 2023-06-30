start = int(input("Enter starting limit"))
end = int(input("Enter ending limit"))
count = 0
print("These are the prime number values within the range",start,end,)
for i in range(start,end+1,1):
  for x in range(1,i+1): #nested_loop
    if (i%x==0):
      count = count+1
  if (count==2):
    print(i)
  count = 0