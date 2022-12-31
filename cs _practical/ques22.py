'''
Ques 22

i)Write AddCustomer(Customer) method in Python to add a new customer, considering it to act as a PUSH operation of the stack data structure. Also display the contents of the Stack after PUSH operation.
ii) Write RemoveCustomer(Customer) method in Python to remove a Customer, considering it to act as a POP operation of the stack data structure. Also return the value deleted from stack. Details of the Customer are: CID and Name.
'''


def AddCustomer(customer):
    item = eval(input("Enter customer [ID, name]: "))
    customer.append(item)
    print("Done. The contents are: \n", customer)

stack = [[1, 'A'], [2, 'B'], [3, 'C']]
AddCustomer(stack)

def RemoveCustomer(customer):
    if len(customer) == 0:
        print("Underflow")
    else:
        item = customer.pop()
        print("Popped", item)

RemoveCustomer(stack)