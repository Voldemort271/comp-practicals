'''
Ques 28

Write a Python program to generate queries .
List the name of students who are in class 12 sorted by average marks.
Search  minimum of average mark from the above table where average mark<75.
Search  following STUDENT table to delete all the records whose Avgmark is less than 80.

            TABLE : STUDENT
Name        AvgMark     Grade       Class

Karan       78.5        B           12B

Divakar     89.2        A           11C

Divya       68.6        C           12C

Arun        73.1        B           12C

Sabina      90.6        A           11A
'''

import mysql.connector

sql = mysql.connector.connect(
    host="localhost",
    username="root",
    password="helloworld",
    database="class12"
)

ex = sql.cursor()

queries = [
    "select * from STUDENT where class like '12%' prder by avgmark",
    "select min(avgmark) from STUDENT where avgmark < 75"
]


for i in queries:
    ex.execute(i)
    sql.commit()
    for result in ex:
        print(result)
    print("\n___________________\n")

