'''
Ques 25 

A programmer wants to prepare a stack from a given list of integer elements only for numbers which are divisible by 3. Help him create a program with user defined functions to perform the following operations based on this list.
Traverse the content of the list and push the numbers into a stack which are divisible by 3.
1)Pop and display the content of the stack.
2)If  N = [3, 5, 10, 13, 21, 23, 45, 56, 60, 78]
The output will be 60, 45, 21, 3
'''

N = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
stack = []


def push(input, output):
    for i in input:
        if i % 3 == 0:
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

