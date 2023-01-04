'''
Ques 30

Write a Python & MySQL connectivity program to search  following details from WORKER table
To display the Wno and Name of those workers from the table WORKER who are born between '1987-01-01' and '1991-12-01'.
List the details of those employees who have 5 lettered names.
List details of all employees whose annual salary crosses 50000

TABLE : WORKER

WNO         NAME        DOB         JOB         SALARY

1001        JITHIN      1991-09-01  CLERK       2000

1002        ANANYA      1990-12-15  SALESMAN    4500

1003        MOHIT       1987-09-04  MANAGER     7000

1009        ANOOP       1988-10-02  MANAGER     3000

1007        AMIR        1984-10-19  CLERK       2000

1004        KULDEEP     1986-11-14  ANALYST     5000
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
    "select wno, name from WORKER where DOB between '1987-01-01' and '1991-12-01'",
    "select * from WORKER where name like '_____'",
    "select * from WORKER where salary * 12 > 50000"
]


for i in queries:
    ex.execute(i)
    sql.commit()
    for result in ex:
        print(result)
    print("\n___________________\n")
