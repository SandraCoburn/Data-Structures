
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if value < Node's value
        if value < self.value:
            #we need to go left. Check if there is no left child
            if self.left is None:
                #wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            #otherwise there is a child
            else:
                #call the left child's insert method
                self.left.insert(value)
        #otherwise, value > = Node's value
        elif value >= self.value:
            #we need to go right, check if there is no right child:
            if self.right is None:
                #wrap the value in a BSTNode and park it:
                self.right = BSTNode(value)
            #otherwise there is a child
            else:
                #call the right child's insert method:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #check if target is in root
        #Using recursion:
        #base case, to check if target matches the current value
        if self.value == target:
            return True
        #compare target agians this node's value to determine wich dirct to go
        if target > self.value:
            if self.right is None:
                return False
            else:
                #call contain on the right child
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)


        # if target == self.value:
        #     return True
        # elif target == self.left.value:
        #     return True
        # elif target == self.right.value:
        #     return True
        # else:
        #     return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value
        #check if there is no right child to go right since left is lower numbers
        if self.right is None:
            return max_val   
        else: 
            #call the right child get max method
            return self.right.get_max()

    ''' #iterative
        #keep a current largest that we've seen so far
        current_max = self.value
        #keep a "current" pointer to keep track of where we are in the tree
        current = self

        #iterate down the right child of the current node
        while current.right is not None:
            #until we no longer have a right child to go to
            current = current.right #sel.right will alwyas have the largest numbers
        return current.value
        '''

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value:
            # First recur on left child
            if self.left is not None:
                self.left.for_each(fn)

            fn(self.value)
            #recur on right child
            if self.right is not None:

                self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        #DFT: LIFO - last in first out
        #we'll use a stack
        stack = []
        stack.append(self)

        #so long as our stack has nodes in it, there is more nodes to traverse
        while len(stack) > 0:
            #pop the top node from te stack
            current = stack.pop()

            #add the current node's right child first
            if current.right:
                stack.append(current.right)
            #add the current node's left child
            if current.left:
                stack.append(current.left)

                #call the anonymous fucntion
                fn(current.value)
   
    def iterative_breadth_first_for_each(self, fn):
        from collections import deque
        #BFT: FIFO - first in first out
        #we'll use a queue to facilitate ordering
        queue = deque()
        queue.append(self)

        #continue to traverse so long as there are nodes int eh queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            fn(current.value)



    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        #lowest number go to the left
        #base case: if node is None
        #print("this is node: ", node)
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            #print("this is node in order:", node.value)
            self.in_order_print(node.right)

        #recursive case

        #build call stack(builds up then tear down)
        #self.in_order_print(self.left)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        #use a queue
        queue = deque()
       
        #start queu with root node
        queue.append(node)
           
        #print("This is bft", node)
        #while loop checks size of queue, pointer var that updates at begg of each loop
        while len(queue) > 0:
            current = queue.popleft()
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            #print("This is bft node:", current.value)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        #stack that starts with root node
        stack = []
        stack.append(node)
        
        #while loop check stack size, pointer var to update
        while len(stack) > 0:
            current = stack.pop()
            #add current right child
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            #print("This is dft: ", current.value)
            print(current.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
            print(self.value)
            #print("pre order:", self.value)
            if self.left:
                self.left.pre_order_dft(node)
            if self.right:
                self.right.pre_order_dft(node)
          
       
        # if node is not None:
        #     if self.left:
        #         self.pre_order_dft(node.left)
        #     if self.right:
        #         self.pre_order_dft(node.right)
        #     print("pre order:", node.value)
                
    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            #print("post: ", node.value)
            print(node.value)

# bst = BSTNode(5)
# bst.insert(2)
# bst.insert(3)
# bst.insert(7)
# bst.insert(6)
# print(bst.left.right.value)
# print(bst.get_max())
# def printnum(value):
#     return value
    
# print(bst.for_each(printnum))
# Testing
bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.bft_print(bst)
bst.dft_print(bst)
print("elegant methods")
print("pre order")
bst.pre_order_dft(bst)
print("in order")
bst.in_order_print(bst)
print("post order")
bst.post_order_dft(bst)
