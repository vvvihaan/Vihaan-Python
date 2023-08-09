x = input("Please enter your name, " )
#y = len(x)

# x=" "+x #adds a space

# for i in (0,y):
#  if (x[i]==' '):
#    print(x[i+1])
  

# Hello,    I     am      good
#  0         1      2       3
list=x.split(" ")
list_length = len(list)
for i in range(list_length):
  word=list[i]
  print(word[0])