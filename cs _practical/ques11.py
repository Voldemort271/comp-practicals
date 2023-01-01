'''
Ques 11

Create a binary file with roll number, name and marks. Input a roll number and update the marks.
'''


import pickle
wfile = open("marks.dat", "wb")
n = int(input("Enter no of entries: "))
entry = ["roll", "name", "marks"]

for i in range(n):
    roll = int(input("Enter roll: "))
    entry[0] = roll
    name = input("Enter name: ").title()
    entry[1] = name
    marks = float(input("Enter marks: "))
    entry[2] = marks
    pickle.dump(entry, wfile)
print("Recorded all entry")
wfile.close()

update = int(input('Enter roll to update: '))
marks = float(input('Enter new marks: '))
entries = []
rfile = open('marks.dat', 'rb')

try:
    while True:
        content = pickle.load(rfile)
        entries += [content]
except:
    pass

for record in entries:
    if record[0] == update:
        record[2] = marks
        print('Marks updated')
rfile.close()

wfile = open('marks.dat', 'wb')
for record in entries:
    pickle.dump(record, wfile)
wfile.close()
