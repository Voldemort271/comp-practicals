'''
Ques 14

A binary file “Store.dat” has structure [ItemNo, Item_Name, Company, Price].
i) Write a function CountRec(Company) in Python which accepts the Company name as
parameter and count and return number of Items by the given Company.

ii) Write a function AddRecord(<List>) which accepts a List of the record [ItemNo, Item_Name, Company, Price] and appends in the binary file “Store.Dat”.
'''

import pickle


def countRec(company):
    count = 0
    file = open("store.dat", "rb")
    try:
        while True:
            item = pickle.load(file)
            if item[2] == company:
                count += 1
    except:
        print("Count:", count)
        file.close()


def addRecord(list):
    file = open("store.dat", "ab")
    pickle.dump(list, file)
    file.close()


countRec('Samsung')
addRecord([6, 'F', 'Oppo', 1000])
