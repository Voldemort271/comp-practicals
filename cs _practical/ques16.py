'''
Ques 16

Create a CSV file by entering user-id and password, read and search the password for given user-id.
'''


import csv
file = open("details.csv", "r", newline="\r\n")
read = csv.reader(file)
username = input("Enter username to be searched: ")
for entry in read:
    if entry[0] == username:
        print("Password:", entry[1])
file.close()
