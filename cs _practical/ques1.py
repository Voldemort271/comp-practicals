'''
Ques 1

Write the definition of a method countnow(places) to find and display those place names, in which there are more than 7 characters.
'''


def countnow(places):
    for i in places:
        if len(i) > 7:
            print(i, end=" ")

list = ["MELBOURNE", "TOKYO", "PINKCITY", "BEIJING"]
countnow(list)
