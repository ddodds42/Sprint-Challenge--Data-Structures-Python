"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

from linked_list import Node, LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.storage.length

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()
    
    def print_links(self):
        current = self.storage.head
        while current:
            print(current.value)
            current = current.get_next()

# lynx = Queue()
# lynx.enqueue('Super')
# lynx.enqueue('kala')
# lynx.enqueue('fragile')
# lynx.enqueue('istic')
# lynx.enqueue('expi')
# lynx.enqueue('ali')
# lynx.dequeue()
# lynx.print_links()