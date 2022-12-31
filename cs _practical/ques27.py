'''
Ques 27

Write a Python program to solve the queries.
To search records from the following STUDENT table based on non medical students of class 12.
List the details of those students who are in class 12 sorted by name.
To list names of female students who are in commerce stream.

TABLE: STUDENT
Rollno       Name      Stream        Class     Gender

1            Karan     Medical        12B        M

2            Divakar   Commerce       11C        M

3            Divya     Nonmedical     12B        F

4            Arun      Humanities     12C        M

5            Sabina    Nonmedical     12A        F

6            Rubina    medical        12C        F

7            Harsha    Commerce       11B        F
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
    "select * from STUDENT where stream = 'Nonmedical' and class like '12%'",
    "select * from STUDENT where class like '12%' order by name",
    "select name from STUDENT where stream = 'Commerce' and gender = 'F'"
]


for i in queries:
    ex.execute(i)
    sql.commit()
    for result in ex:
        print(result)
    print("\n___________________\n")
