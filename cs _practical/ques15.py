'''
Ques 15

Write a program to use methods  ReadCSV(UserName) and WriteCSV() to include username and password as some entries for a  CSV file “mydata.csv” and display them. 
'''


import csv
def writeCSV():
    file = open("mydata.csv", "w")
    write = csv.writer(file)
    name = input("Enter username: ")
    pwd = input("Enter password: ")
    write.writerow([name, pwd])
    print("Added")
    file.close()


def readCSV(username):
    file = open("mydata.csv", "r", newline="\r\n")
    read = csv.reader(file)
    for entry in read:
        if entry[0] == username:
            print(entry)

writeCSV()
readCSV('one')


