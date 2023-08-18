#Code to check if letter is within code and how many times it is present

word = input("Enter a string, " )
search_word = input("Enter a letter")

#manual way
count = 0

for i in word:
  if (i == search_word):
    count = count + 1 
print(f"{search_word},is present in {word}, and {search_word} occurs {count} times within {word}")

#string interpolation
print(f"Occurence of letter is = {count}")


#using functions
if(search_word in word):
  print(f"{search_word} is present in {word}")
count=word.count(search_word)
print(count)


