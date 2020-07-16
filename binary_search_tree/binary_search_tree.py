from sys import maxsize
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
        else:
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
        if target == self.value:
            return True
        elif target == self.left.value:
            return True
        elif target == self.right.value:
            return True
        else:
            return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        max_val = self.value
        #check if there is no right child to go right since left is lower numbers
        if self.right is None:
            return max_val   
        else: 
            #call the right child get max method
            return self.right.get_max()
        

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

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
bst = BSTNode(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.left.right.value)
print(bst.get_max())
def printnum(value):
    return value
    
print(bst.for_each(printnum))
