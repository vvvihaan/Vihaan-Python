# write a python code to input a string and print the vowels only.
vowel_input = input("Enter a sentence or word, ")
vowel_list = "aeiouAEIOU"


for i in vowel_input:
  if (i in vowel_list):
    print(i)
 
    