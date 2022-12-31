'''
Ques 3

Write a method in python to read lines from a text file MYNOTES.TXT and display those
lines which start with alphabets 'K'.
'''


with open("mynotes.txt") as file:
    for line in file.readlines():
        if line[0] == "K":
            print(line)
