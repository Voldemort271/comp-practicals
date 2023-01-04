'''
Ques 6

Write a function Display( ) in python to read lines from a text file “XYZ.txt” and
display those words, which are greater than equal to 3 characters.
'''


def Display():
    with open("xyz.txt") as file:
        for word in file.read().split():
            if len(word) >= 3:
                print(word, end=" ")

Display()
