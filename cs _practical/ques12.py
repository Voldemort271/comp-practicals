'''
Ques 12

consider a binary file employee.dat containing entry such as
empno:ename:salary(separator ':') write a python function to display entry of those
employees who are earning between 20000 and 30000(both values inclusive).
'''


def display():
    import pickle
    file = open("employee.dat", "rb")
    try:
        while True:
            entry = pickle.load(file).split(':')
            if (int(entry[2]) >= 20000) and (int(entry[2]) <= 30000):
                print(entry)
    except:
        file.close()

display()
