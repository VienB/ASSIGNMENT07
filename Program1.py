# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

from typing import Text


print("VIEN ANGELO BERNALES | BSCOE 1-1 \n")

sentence = input("Enter your sentence: ")

Input = sentence
NumVowel = 0
NumConsonant = 0
NumWords = 0 


for NumVowel in Input:
    if NumVowel in "AEIOUaeiou":
        NumVowel = NumVowel + 1

for NumConsonant in Input:
    if NumConsonant in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
        NumConsonant = NumConsonant + 1

for space in Input:
        if space == " ":
            NumWords = NumWords + 1
            NumSpace = NumWords + 1
        if NumWords == 0:
            Numspace = 1

print(f"NUMBER OF WORDS: {NumWords}")
print(f"NUMBER OF VOWELS: {NumVowel}")
print(f"NUMBER OF CONSONANTS: {NumConsonant}")