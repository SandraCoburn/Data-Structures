class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.value

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list 
        if self.head is None and self.tail is None:
            return None
        else:
            current = self.head
            removed_head = self.head.value
            if current.next is not None:
                self.head = current.next
                if self.head.next is None:
                    self.tail = None
            else:
                self.head = None
                self.tail = None
            return removed_head
    
    def remove_tail(self):
        if self.head is None:
            return 
        else:
            current = self.head
            if self.head.next is not None:
                while current.next is not None:
                    previous = current
                    current = current.next
                previous.next = None
            else:
                self.head = None
            return current.value
    
    def contains(self, value):
        if self.head is None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
            return False

    def size(self):
        current = self.head
        length = 0
        while current is not None:
            length = length + 1
            current = current.next
        return length

    def get_max(self):
        if self.head is None:
            return None
        else:
            current = self.head
            max_value = self.head.value
            while current.next is not None:
                if current.next.value > max_value:
                    max_value = current.next.value
                current = current.next
        return max_value

sl = LinkedList()
sl.add_to_tail(8)
sl.add_to_tail(5)
sl.add_to_tail(2)
print("head:", sl.head.value)
print("tail: ", sl.tail.value)
sl.remove_head()
print("head: ", sl.head.value)
print("tail: ", sl.tail.value)
sl.remove_tail()
print("tail", sl.tail.value)
