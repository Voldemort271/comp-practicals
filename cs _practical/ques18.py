'''
Ques 18
Write python program using function to sort a series of numbers using either
insertion sort or bubble sort.
'''


def bubbleSort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubbleSort([64, 34, 25, 12, 22, 11, 90]))
