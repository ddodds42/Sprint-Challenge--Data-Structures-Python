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
  
    def print_links(self):
        current = self.head
        while current:
            print(current.value)
            current = current.get_next()

    def the_reversal(self, current, prev):
        if not current.next_node:
            self.head = current
            current.next_node = prev
            return self
        nexty = current.next_node
        current.next_node = prev
        self.the_reversal(nexty, current)


    def reverse_list(self, headr, noner):
        if not self.head:
            return self
        if self.head is self.tail:
            return self
        self.the_reversal(self.head, None)
    
chachaslide = LinkedList()
chachaslide.add_to_head('clap5')
chachaslide.add_to_head('clap4')
chachaslide.add_to_head('clap3')
chachaslide.add_to_head('clap2')
chachaslide.add_to_head('clap1')

chachaslide.print_links()
print('\n')
chachaslide.reverse_list(None, None)
chachaslide.print_links()