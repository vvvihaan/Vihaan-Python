"""Write a program to find the length of the longest word in a string."""
x = input("Enter a sentence or a word ")
sep_word = x.split()
sep_length = len(sep_word)
max_length = len(sep_word[0])
max_position = 0


for i in range(0,sep_length):
  if len(sep_word[i]) > max_length:
    max_length = len(sep_word[i])
    max_position = i
print("The longest word is: ", sep_word[max_position] , "which has the length of", max_length)
  

