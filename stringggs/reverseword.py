#write a python code to take string input and reverse it


x = input("Enter a word")
word_length = len(x)
reverse=""

for i in range(word_length-1,-1,-1):
  reverse = reverse + x[i]
print(reverse)
