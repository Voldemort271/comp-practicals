'''
Ques 21

Write PushOn(Book) and Pop(Book) methods/functions in Python to add a new Book
and delete a Book from a list of Book titles, considering them to act as push and pop
operations of the Stack data structure.
'''


def PushOn(book):
    item = input("Enter book: ")
    book.append(item)
    print("Done")

def Pop(book):
    if len(book) == 0:
        print("Underflow")
    else:
        item = book.pop()
        print("Deleted", item)

stack = []
PushOn(stack)
Pop(stack)