
'''
Ques 19
Write python program using function to sort a series of numbers using either
insertion sort or bubble sort.
'''


def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


print(insertionSort([12, 11, 13, 5, 6]))
