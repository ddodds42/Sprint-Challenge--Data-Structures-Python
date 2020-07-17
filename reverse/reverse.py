class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_head(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1

        else:
            node.set_next(self.head)
            self.head = node
            self.length += 1

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def remove_tail(self):
        if not self.head:
            return None
        
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        
        current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        value = self.tail.get_value()
        self.tail = current
        self.tail.next_node = None
        self.length -= 1
        return value

    def add_to_tail(self, value):
        new_node = Node(value, None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
            self.length += 1

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return head.get_value()
        value = self.head.get_value()
        self.head = self.head.get_next()
        self.length -= 1
        return value
    
    def print_links(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()

# node, prev

    def reverse_list(self):
        pass
        # if not self.head:
        #     return self
        # if self.head is self.tail:
        #     return self
        # if self:

        # shuffle = LinkedList()
        # if not self.head:
        #     return shuffle.print_links()
        # shuffle.add_to_head(self.head.value)
        # self.remove_head()
        # self.reverse_list()

        # stopping condition if not self.head.get_next()
        # swap head and tail
        # print the whole linked list
        # else 


# while chachaslide.head:
#     shuffle.add_to_head(chachaslide.head.value)
#     chachaslide.remove_head()

# shuffle.print_links()


        # def the_reversal(ll):
        #     if ll.tail is totheback:
        #         return ll.print_links()
        #     ll.add_to_head(ll.tail)
        #     ll.remove_tail()
        #     # shuffle = ll
        # return the_reversal(ll)
    

chachaslide = LinkedList()
chachaslide.add_to_head('clap5')
chachaslide.add_to_head('clap4')
chachaslide.add_to_head('clap3')
chachaslide.add_to_head('clap2')
chachaslide.add_to_head('clap1')

chachaslide.print_links()
print('\n')

newlist = LinkedList()
while chachaslide.head:
    newlist.add_to_head(chachaslide.head.value)
    chachaslide.remove_head()

newlist.print_links()
print('\n')
print(newlist.length)
print('\n')

newlist.reverse_list()

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(7))

# chachaslide.print_links()