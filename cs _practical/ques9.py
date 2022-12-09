'''
Ques 9

Remove all the lines that contain the character 'a' in a file and write it to another file.
'''


sourceRead = open("source.txt")
target = open("target.txt", "w")
a = []
nota = []

for line in sourceRead.readlines():
    if "a" in line:
        a += [line]
    else:
        nota += [line]

sourceRead.close()
target.writelines(a)

sourceWrite = open("source.txt", "w")
sourceWrite.writelines(nota)

sourceWrite.close()
target.close()
