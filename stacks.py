class Stack:
    #The remove() method doesn't return any value. pop() returns deleted value.
    # The del keyword can delete the single value from a list or delete the whole
    # list at a time. At a time it deletes only one value from the list.

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        #the runtime for this method is O(1), or constant time.

    def pop(self):
        if self.items:
            print(self.items.pop())
        return None
        #this method removes the last item of the stack, run time is O(1)
    def peek(self):
        if self.items:
            print(self.items[-1])
        else:
            print('No items in the Stack')
        #return the last item in the stack
    def size(self):
        print(len(self.items))
        #returns the size of the stack

    def is_empty(self):
        print(self.items == [])
        #return Tue if the stack is empty else returns False.
my_stack = Stack()
my_stack.push('apple')
print(my_stack.items)
my_stack.push('banana')
print(my_stack.items)
my_stack.push('carrot')
print(my_stack.items)
my_stack.pop()
# print(my_stack.items)
my_stack.push('Grapes')
my_stack.peek()
my_stack.pop()
my_stack.peek()
my_stack.size()
my_stack.push('peech')
my_stack.size()
my_stack.is_empty()
print(my_stack.items)