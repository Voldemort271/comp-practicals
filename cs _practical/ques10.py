'''
Ques 10

Create a binary file with name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
'''


import pickle
wfile = open('entry.dat', 'wb')
n = int(input("Enter no of records: "))
entry = {}

for i in range(n):
    roll = int(input("Enter roll no: "))
    name = input("Enter name: ").title()
    entry["rno"] = roll
    entry["name"] = name
    pickle.dump(entry, wfile)
print("Appended all records")
wfile.close()

search = int(input("Enter roll to search: "))
rfile = open("entry.dat", "rb")
found = False

try:
    while True:
        check = pickle.load(rfile)
        if check["rno"] == search:
            print(check["name"])
            found = True
except:
    rfile.close()

if not found:
    print("entry dont exist")
