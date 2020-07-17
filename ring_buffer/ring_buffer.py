from queue import Queue
from linked_list import LinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.cue = Queue()
        for i in range(self.capacity):
            self.cue.enqueue(i)

    def append(self, item):
        i = self.cue.dequeue()
        self.storage[i] = item
        self.cue.enqueue(i)

    def get(self):
        return [i for i in self.storage if i is not None]

'''
ring buffer is instantiated with x spots of none in storage
in a seperate queue, enqueue each index value of ring buffer in its respective order

during append
dequeue first index value as i
use i to change storage[i] to given value
enqueue i

during get
print array with list comprehension to avoid none
'''

# mground = RingBuffer(5)
# mground.append('a')
# mground.get()