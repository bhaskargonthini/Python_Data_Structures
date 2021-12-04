#first in first out
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        return self.items.insert(0, item)
        #takes an item and insert that item into the 0th index of the list
        #the runtime is O(n), or linear time

    def dequeue(self):
        if self.items:
            return self.items.pop()
        else:
            None
        #pop removes and return the front most items of the queue.
        #so dequeue returns and removes the front most item in the queue
    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            None
        #returns the last item in the list, also we can say
        #front most items in the list
    def size(self):
        return len(self.items)
        #returns the size of the queue
    def is_empty(self):
        return  self.items == []
    #returns whether the queue is empty or not
my_q = Queue()
my_q.enqueue('apple')
print(my_q.items)
my_q.enqueue('banana')
print(my_q.items)
my_q.dequeue()
print(my_q.items)
print(my_q.peek())
my_q.enqueue('tomato')
my_q.enqueue('carrot')
print(my_q.size())