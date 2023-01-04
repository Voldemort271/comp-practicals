'''
Ques 29

Write a Python & MySQL connectivity program  to generate following queries.
To increase the price of all books of EPB publishers by 50.
To display all the books sorted by name in descending order.
Display a list of books with prices more than 400 and sorted by publishers.

TABLE : BOOKS

BOOK_NAME      PUBLISHERS      PRICE

FAST COOK       EPB             355

THE TEARS       FIRST PUBL.     650

MY FIRST C++    EPB             350

C++ BRAINWORKS  TDH             350

THUNDERBOLTS    FIRST PUBL.     750

'''


import mysql.connector

sql = mysql.connector.connect(
    host="localhost",
    username="root",
    password="helloworld"
)

ex = sql.cursor()

ex.execute("create database if not exists x")
ex.execute("use x")

queries = [
    "update BOOKS set price = price + 50 where publishers = 'EPB'",
    "select * from BOOKS order by BOOK_NAME desc",
    "select * from books where price > 400 order by publishers"
]


for i in queries:
    ex.execute(i)
    sql.commit()
    for result in ex:
        print(result)
    print("\n___________________\n")
