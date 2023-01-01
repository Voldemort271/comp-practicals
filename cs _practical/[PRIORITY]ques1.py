

import mysql.connector


'''
Ques 1A

A list of 10 students' marks is given below.Write a program  with separate user defined functions to perform the following operation.
Traverse the content of the list and push the numbers higher than 33 into a stack.
Pop and display the content of the stack.
     For example:
        If N=[12,13,34,56,21,79,98,22,35,38]
        sample output should be 38,35,98,79,56,34

'''

N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack = []


def push(input, output):
    for i in input:
        if i > 33:
            output.append(i)


def pop(list):
    if len(list) == 0:
        print("Underflow")
    else:
        item = list.pop()
        print("Popped", item)


def display(list):
    for i in range(len(list) - 1, -1, -1):
        print(list[i], end=" ")


push(N, stack)
display(stack)


'''
Ques 1B

Write a Python & MySQL connectivity program to solve the queries.
Display students' records from the  table based on gender as female.
Display name and age of students whose age is 23 and above.
Display details of all the students whose name starts with 'S'.

           TABLE: STUDENT
           
NO          NAME        AGE         SEX

1           PANKAJ      24          M

2           SHALINI     21          F

3           SANJAY      22          M

4           SUDHA       25          F

5           RAKESH      22          M
'''


sql = mysql.connector.connect(
    host="localhost",
    username="root",
    password="helloworld",
    database="class12"
)

ex = sql.cursor()

queries = [
    "select * from STUDENT where sex = 'F'",
    "select name, age from STUDENT where age >= 23",
    "select * from STUDENT where name like 'S%'"
]


for i in queries:
    ex.execute(i)
    sql.commit()
    for result in ex:
        print(result)
    print("\n___________________\n")


