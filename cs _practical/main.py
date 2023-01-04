import pickle
import csv
import mysql.connector



'''
Ques 1A
'''

N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack = []


def push():
    for i in N:
        if i > 33:
            stack.append(i)


def pop():
    if len(stack) == 0:
        print("Underflow")
    else:
        item = stack.pop()


def display():
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=",")
    print()


push()
pop()
display()


'''
Ques 1B
'''


sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld" # replace w/ own password
)
cursor = sql.cursor()

cursor.execute("create database if not exists sample")
cursor.execute("use sample")

create_table = '''
create table STUDENT (
    no int not null primary key,
    name text,
    age int,
    sex char(1)
)
'''

insert_values = '''
insert into STUDENT values
    (1, 'PANKAJ', 24, 'M'),
    (2, 'SHALINI', 21, 'F'),
    (3, 'SANJAY', 22, 'M'),
    (4, 'SUDHA', 25, 'F'),
    (5, 'RAKESH', 22, 'M')
'''

cursor.execute(create_table)
cursor.execute(insert_values)
sql.commit()

cursor.execute("select * from STUDENT where sex = 'F'")

for i in cursor:
    print(i)

cursor.execute("select name, age from STUDENT where age > 23")

for i in cursor:
    print(i)

cursor.execute("select * from STUDENT where name like 'S%'")

for i in cursor:
    print(i)


'''
Ques 2A
'''


def countlines():
    with open("XYZ.txt") as file:
        count = 0
        lines = file.readlines()
        for i in lines():
            if i[0] in "AE":
                count += 1
    print("Number of lines starting with A or E:", count)

countlines()


'''
Ques 2B
'''


sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld"  # replace w/ own password
)
cursor = sql.cursor()

cursor.execute("create database if not exists sample")
cursor.execute("use sample")

create_table = '''
create table STUDENT (
    rollno int not null primary key,
    name text,
    stream text,
    class char(3),
    gender char(1)
)
'''

insert_values = '''
insert into STUDENT values
    (1, 'Karan', 'Medical', '12B', 'M'),
    (2, 'Divakar', 'Commerce', '11C', 'M'),
    (3, 'Divya', 'Nonmedical', '12B', 'F'),
    (4, 'Arun', 'Humanities', '12C', 'M'),
    (5, 'Sabina', 'Nonmedical', '12A', 'F'),
    (6, 'Rubina', 'Medical', '12C', 'F'),
    (7, 'Harsha', 'Commerce', '12B', 'F')
'''

cursor.execute(create_table)
cursor.execute(insert_values)
sql.commit()

cursor.execute("select * from STUDENT where class like '12%' and stream = 'Nonmedical'")

for i in cursor:
    print(i)

cursor.execute("select * from STUDENT where class like '12%' order by name")

for i in cursor:
    print(i)

cursor.execute("select name from STUDENT where gender = 'F' and stream = 'Commerce'")

for i in cursor:
    print(i)


'''
Ques 3A
'''


wfile = open("marks.csv", "w")
write = csv.writer(wfile)
n = int(input("Enter no of records: "))

for i in range(n):
    rno = int(input("Enter roll no: "))
    name = str(input("Enter name: "))
    marks = float(input("Enter marks: "))
    record = [rno, name, marks]
    write.writerow(record)
    
wfile.close()

rfile = open("marks.csv", "r")
read = csv.reader(rfile)

for i in read():
    print(i)

rfile.close()


'''
Ques 3B
'''


sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld"  # replace w/ own password
)
cursor = sql.cursor()

cursor.execute("create database if not exists sample")
cursor.execute("use sample")

create_table = '''
create table STUDENT (
    name text,
    avgmark decimal,
    grade char(1),
    class char(3)
)
'''

insert_values = '''
insert into STUDENT values
    ('Karan', 78.5, 'B', '12B'),
    ('Divakar', 89.2, 'A', '11C'),
    ('Divya', 68.6, 'C', '12C'),
    ('Arun', 73.1, 'B', '12C'),
    ('Sabina', 90.6, 'A', '11A')
'''

cursor.execute(create_table)
cursor.execute(insert_values)
sql.commit()

cursor.execute(
    "select name from STUDENT where class like '12%' order by avgmark")

for i in cursor:
    print(i)

cursor.execute("select min(avgmark) from STUDENT where avgmark < 75")

for i in cursor:
    print(i)

cursor.execute("delete from STUDENT where avgmark < 80")
sql.commit()


'''
Ques 4A
'''


def CreateEmp():
    f1 = open("emp.dat", 'wb')
    eid = input("Enter E. Id: ")
    ename = input("Enter Name: ")
    designation = input("Enter Designation: ")
    salary = int(input("Enter Salary: "))
    l = [eid, ename, designation, salary]
    pickle.dump(l, f1)
    f1.close()


def display():
    f2 = open("emp.dat", "rb")
    try:
        while True:
            rec = pickle.load(f2)
            if rec[3] > 5000:
                print(rec)
    except:
        f2.close()


'''
Ques 4B
'''


sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld"  # replace w/ own password
)
cursor = sql.cursor()

cursor.execute("create database if not exists sample")
cursor.execute("use sample")

create_table = '''
create table BOOKS (
    book_name text,
    publishers text,
    price int
)
'''

insert_values = '''
insert into BOOKS values
    ('FAST COOK', 'EPB', 355),
    ('THE TEARS', 'FIRST PUBL.', 650),
    ('MY FIRST C++', 'EPB', 350),
    ('C++ BRAINWORKS', 'TDH', 350),
    ('THUNDERBOLTS', 'FIRST PUBL.', 750)
'''

cursor.execute(create_table)
cursor.execute(insert_values)
sql.commit()

cursor.execute("update BOOKS set price = price + 50 where publishers = 'EPB'")
sql.commit()

cursor.execute("select * from BOOKS order by name desc")

for i in cursor:
    print(i)

cursor.execute("select * from BOOKS where price > 400 order by publishers")

for i in cursor:
    print(i)


'''
Ques 5A
'''


N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack = []


def push():
    for i in N:
        if i % 2 != 0:
            stack.append(i)


def pop():
    if len(stack) == 0:
        print("Underflow")
    else:
        item = stack.pop()


def display():
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=",")
    print()


push()
pop()
display()


'''
Ques 5B
'''


sql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld"  # replace w/ own password
)
cursor = sql.cursor()

cursor.execute("create database if not exists sample")
cursor.execute("use sample")

create_table = '''
create table WORKER (
    wno int not null primary key,
    name text,
    dob date,
    job text,
    salary int
)
'''

insert_values = '''
insert into BOOKS values
    (1001, 'JITHIN', '1991-09-01', 'CLERK', 2000),
    (1002, 'ANANYA', '1990-12-15', 'SALESMAN', 4500),
    (1003, 'MOHIT', '1987-09-04', 'MANAGER', 7000),
    (1009, 'ANOOP', '1988-10-02', 'MANAGER', 3000),
    (1007, 'AMIR', '1984-10-19', 'CLERK', 2000),
    (1004, 'KULDEEP', '1986-11-14', 'ANALYST', 5000),
'''

cursor.execute(create_table)
cursor.execute(insert_values)
sql.commit()

cursor.execute("select wno, name from WORKERS where dob between '1987-01-01' and '1991-12-01'")

for i in cursor:
    print(i)

cursor.execute("select * from WORKER where name like '_____'")

for i in cursor:
    print(i)

cursor.execute("select * from WORKER where salary * 12 > 50000")

for i in cursor:
    print(i)
