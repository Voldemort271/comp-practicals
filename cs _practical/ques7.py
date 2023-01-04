'''
Ques 7

Write a function count_is_as() in Python that counts the number of “is” and “as” words
present in a text file “STORY.TXT”.
'''


def count_is_as():
    As = Is = 0
    with open("story.txt") as file:
        for word in file.read().split():
            if word == "is":
                Is += 1
            elif word == "as":
                As += 1
    print("Is:", Is, "As:", As)

count_is_as()
