'''
Ques 20

Write a program for a linear search from a list using a function.
'''


def linearSearch(list, element):
    for i in list:
        if i == element:
            print(i, "occurs at index", list.index(i))
            break
    else:
        print("Not found")


linearSearch([1, 2, 3, 4, 6, 5, 8, 7, 9], 10)
