'''
Ques 17

Write a Python program using Binarysearch( List , Element ) to search an element from a list. 
'''


def binary_search(list, element):
    first = 0
    last = len(list) - 1
    mid = (first + last) // 2
    midEl = list[mid]

    found = True

    while found:
        if first == last:
            if midEl != element:
                found = False
                return f"{element} does not appear in the list"

        elif midEl == element:
            return f"{midEl} occurs in position {mid}"

        elif midEl > element:
            new = mid - 1
            last = new
            mid = (first + last) // 2
            midEl = list[mid]
            if midEl == element:
                return f"{midEl} occurs in position {mid}"

        elif midEl < element:
            new = mid + 1
            first = new
            last = len(list) - 1
            mid = (first + last) // 2
            midEl = list[mid]
            if midEl == element:
                return f"{midEl} occurs in position {mid}"


list_container = [16, 18, 20, 50, 60, 81, 84, 89]
print(binary_search(list_container, 81))
print(binary_search(list_container, 10))
