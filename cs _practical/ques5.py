'''
Ques 5

Write a function SRCount() in Python, which should read each character of a text file
STORY.TXT, should count and display the occurrence of alphabets S and R (including
small cases s and r too).
'''


def SRCount():
    r = s = 0
    with open("story.txt") as file:
        for letter in file.read():
            if letter.lower() == "r":
                r += 1
            elif letter.lower() == "s":
                s += 1
    print("r =", r, "\ns =", s)

SRCount()
