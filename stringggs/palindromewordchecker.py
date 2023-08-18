# write a python code to input a word and check if its palindrome or not

word = input("Enter a word to check if it is palindrome or not. ")

word=word.strip() #strip function removes extra spaces before and after the word


word_length = len(word)
new_word = ""

for i in range(word_length-1,-1,-1):
  new_word = new_word + word[i]
print(new_word)

if(new_word == word):
  print("This word is a palindrome")
else:
  print("This word is not a palindrome")
  