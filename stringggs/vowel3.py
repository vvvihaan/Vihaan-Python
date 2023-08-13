"""Write a program to remove all the vowels from a string."""
# vihaan
# vhn

vowel_input = input("Enter a sentence or word, ")
vowel = "aeiouAEIOU"
input_without_vowels = ""

for i in vowel_input:
  if (i not in vowel):
    input_without_vowels = input_without_vowels + i
print("Input without vowels, "input_without_vowels)
    

