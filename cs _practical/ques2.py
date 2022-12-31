'''
Ques 2

Write a function countmy() in python to read the text file "DATA.TXT" and count the
number of times "my" occurs in the file.
'''


def countmy():
    count = 0
    with open("data.txt") as file:
        for word in file.read().split():
            if word == "my":
                count += 1
    print("My occurs", count, "times")

countmy()
