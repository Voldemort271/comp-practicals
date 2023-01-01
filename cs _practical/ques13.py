'''
Ques 13

i)Write a function Count_Rec() in Python that would read contents of the file
“SCHOOL.DAT” and display the details of those students whose percentage is below 33%.
Also display the number of students scoring below 33%.

ii) Write a function Disp_Rec(alphabet) in Python that would read contents of the file
“SCHOOL.DAT” and display the details of those students whose name begin with the
alphabet as passed as parameter to the function.
'''

import pickle
def Count_Rec():
    count = 0
    file = open("school.dat", "rb")
    try:
        while True:
            item = pickle.load(file)
            if item["percent"] < 33:
                print(item)
                count += 1
    except:
        print("Count:", count)
        file.close()

def Disp_Rec(alphabet):
    file = open("school.dat", "rb")
    try:
        while True:
            item = pickle.load(file)
            if item["name"][0] == alphabet:
                print(item)
    except:
        file.close()

Count_Rec()
Disp_Rec('B')
