'''
Ques 4

Write a program that copies a text file "source.txt" onto "target.txt" barring the lines starting with “A”.
'''


r = open("source.txt", "r")
w = open("target.txt", "w")
for line in r.readlines():
    if line[0] != "A":
        w.write(line)
r.close()
w.close()
