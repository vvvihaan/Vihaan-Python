"""Write a program to count vowels and consonants in a string."""

vowel_input = input("Enter a sentence or word, ")
vowel = "aeiouAEIOU"
counter_vowel = 0
counter_consonant = 0

for i in vowel_input:
  if (i in vowel):
    counter_vowel = counter_vowel + 1
  elif ( i not in vowel):
    counter_consonant = counter_consonant + 1
print("These are the number of vowels ",counter_vowel)
print("These are the number of consonants ", counter_consonant)

