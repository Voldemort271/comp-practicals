'''
Ques 26

Vikram has a list containing 10 integers. You need to help him create a program with separate user defined functions to perform the following operations based on this list.
Traverse the content of the list and push the ODD numbers into a stack.
Pop and display the content of the stack.

For Example If N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38] the sample output should be 35,89,21,13
'''

N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack = []


def push(input, output):
    for i in input:
        if i % 2 != 0:
            output.append(i)


def pop(list):
    if len(list) == 0:
        print("Underflow")
    else:
        item = list.pop()
        print("Popped", item)


def display(list):
    for i in range(len(list) - 1, -1, -1):
        print(list[i], end=" ")


push(N, stack)
display(stack)
