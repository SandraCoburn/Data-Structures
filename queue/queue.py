from singly_linked_list import Node
from singly_linked_list import LinkedList
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
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.insert(0, value)
#         self.size = len(self.storage)

#     def dequeue(self):
#         if self.size != 0:
#             removed = self.storage.pop()
#             self.size = len(self.storage)
#             return removed

class Queue:
    def __init__(self):
        self.front = self.rear = None
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        self.size = self.storage.size()
        return self.size

    def enqueue(self, value):
      self.storage.add_to_tail(value) #O(1)
      self.size = self.size + 1
      

    def dequeue(self):
        if self.size != 0:
        #if not self.storage:
            self.size -= 1
            return self.storage.remove_head() #O(n)
        return None
            
            
q = Queue()
q.enqueue(100)
q.enqueue(105)
print("new item: ", str(q.storage.head.value)) 
print("tail: ", str(q.storage.tail.value))
print(q.size)