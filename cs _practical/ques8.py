'''
Ques 8

Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file.
'''


vowels = consonants = 0
upper = lower = 0

with open("source.txt") as file:
    for letter in file.read():
        if letter.isalpha():
            if letter.lower() in "aeiou":
                vowels += 1
            else:
                consonants += 1
            if letter.islower():
                lower += 1
            else:
                upper += 1

print("Vowels:", vowels, "Consonants:", consonants)
print("Lowercase:", lower, "Uppercase:", upper)
