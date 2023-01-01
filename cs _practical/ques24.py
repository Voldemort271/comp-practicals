'''
Ques 24

A list of 10 students, marks is given below.Write a program with separate user defined functions to perform the following operation.
Traverse the content of the list and push the numbers higher than 33 into a stack.
pop and display the content of the stack.
For example:
	If N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
sample output should be 38, 35, 98, 79, 56, 34
'''


N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack = []


def push(input, output):
    for i in input:
        if i > 33:
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
