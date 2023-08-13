#write a python code to input a string input and count the number of vowels

#vowel checker to check for a e i o u

vowel_input = input("Enter a sentence or word, ")
vowels = "aeiouAEIOU"
counter = 0

for i in vowel_input:
  if(i in vowels):
    counter = counter + 1
print(counter)




