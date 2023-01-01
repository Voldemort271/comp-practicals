'''
Ques 23

Write a menu based program to add, delete and display the records of the hostel using list as stack data structure in python. Record of the hostel contains the fields : Hostel number, Total Students and Total Rooms. 
'''

hostels = [
    [1, 500, 200],
    [2, 750, 200],
    [3, 1000, 200],
    [4, 250, 250],
]


def addRecord(stack):
    hno = int(input("Enter hostel no: "))
    sno = int(input("Enter no of students: "))
    rno = int(input("Enter no of rooms: "))
    stack.append([hno, sno, rno])
    print("Appended\n")


def deleteRecord(stack):
    hno = int(input("Enter hostel no to be deleted: "))
    for i in stack:
        if i[0] == hno:
            stack.remove(i)
    print("Deleted\n")


def displayRecord(stack):
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i])


print('''
      Menu
      1. Add entry
      2. Delete entry
      3. Display entries
      4. Exit
      ''')
ch = int(input("Enter your choice: "))

while True:
    if ch == 1:
        addRecord(hostels)
    elif ch == 2:
        deleteRecord(hostels)
    elif ch == 3:
        displayRecord(hostels)
    elif ch == 4:
        break
    else:
        print("Invalid choice")
    ch = int(input("\nEnter your choice: "))
