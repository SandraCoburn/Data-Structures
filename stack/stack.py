from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size = len(self.storage)

#     def pop(self):
#         if self.size == 0:
#             return None
#         else:
#             popped = self.storage.pop()
#             self.size = len(self.storage)
#             return popped


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        self.size = self.storage.size()
        return self.size

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
            
s = Stack()
print(s.size)
s.push(2)
print(s.storage)
s.push(8)
print(s.size)