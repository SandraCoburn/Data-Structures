"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        #change head to point to new node
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            #change head to point to next
            old_head = self.head
            self.head = new_node
            self.head.next = old_head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None and self.tail is None:
            return
        elif self.head.next is None:
            self.length -= 1
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.value
        else:
            old_head = self.head
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            # none <-> head <-> number <-> tail -> new_node
            new_node.prev = self.tail
            # none <-> head <-> number <-> tail <-> new_node
            self.tail = new_node
            # none <-> head <-> number <-> number <-> new_node(tail) -> None
        self.length += 1
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        #access the tail value
        if self.head is None and self.tail is None:
            return 
        self.length -= 1
        if self.head.next is None and self.head is not None:
            value = self.head.value
            self.head = None 
            self.tail = None
            return value
        n = self.head
        value = self.tail.value 
        # None <-> Head <-> number(Tail) -> None
        while n.next is not None:
            n = n.next
        # None <-> Head <-> number <-> Tail -> None
     
        self.tail = n.prev
        #None <-> Head <-> number(Tail) <-> number -> None
        n.prev = None
        self.tail.next = None
        n = None
        return value
        #None <-> Head <-> number(Tail) -> None 
       
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.delete(node)
       
        self.add_to_head(node.value)
        
        return self.head.value
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.delete(node)
        self.add_to_tail(node.value)
        return self.tail.value

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length < 1:
            return
        if self.length > 1:
            if node is self.head:
                self.remove_from_head()
            elif node is self.tail:
                #self.tail = self.tail.prev
                self.remove_from_tail()
            else:
                self.length -= 1
                next_node = node.next
                prev_node = node.prev
                next_node.prev = prev_node
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return None
        max = self.head.value
        current = self.head
        while current is not None:
            #compare value with max
            if current.value > max:
                max = current.value
            current = current.next
        return max
        


dl = DoublyLinkedList(ListNode(9))
print("head is: ", str(dl.head.value))
print("tail is: ", str(dl.tail.value))
dl.add_to_head(2)
dl.add_to_head(4)
print("head is: ", str(dl.head.value))
print("tail is: ", str(dl.tail.value))
dl.add_to_tail(6)
print("head is add tail: ", str(dl.head.value))
print("tail is add tail: ", str(dl.tail.value))
print("tail is add tail: ", str(dl.tail.prev))
print("==============================")
dl.remove_from_head()
print("head is: ", str(dl.head.value))
print("tail is: ", str(dl.tail.value))
print("================================")
dl.remove_from_tail()
print("head is: ", str(dl.head.value))
#print("tail is: ", str(dl.tail.value))