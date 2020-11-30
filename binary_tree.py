class Node:
    """ Individual tree node that may has two or less descendants.
    
    Attributes
    ----------
    value --- a numeric/string value stored in the node.
    left & right --- two descendant node objects.

    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    """
    """
    def __init__(self, rootValue):
        self.root = Node(rootValue)

    def search(self, find_val):
        """Return True if the find_val
        is in the tree, return
        False otherwise. The tree is not sorted.
        """
        if self.preOrderSearch(self.root, find_val):
            return True
        return False
    
    def preOrderSearch(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution. The tree is not sorted.
        """
        if start:
            #print(start.value)
            if start.value == find_val:
                return True
            else:
                # making use of the short circuit evaluation of the OR operation
                return self.preOrderSearch(start.left, find_val) or self.preOrderSearch(start.right, find_val)
        return False
    
    def printTree(self, mode):
        """Print out all tree nodes
        as they are visited in
        a pre-order, in-order, or post-order traversal.
        """
        if mode == "pre":
            return self.preOrderPrint(self.root, "")[:-1]
        elif mode == "in":
            return self.inOrderPrint(self.root, "")[:-1]
        elif mode == "post":
            return self.postOrderPrint(self.root, "")[:-1]
    
    def preOrderPrint(self, start, traversal):
        """A recursive helper method.
        """
        if start:
            traversal += str(start.value) + "-"
            # return traversal and pass it thru the next call, right node
            traversal = self.preOrderPrint(start.left, traversal)
            # only return 
            traversal = self.preOrderPrint(start.right, traversal)
        return traversal

    def inOrderPrint(self, start, traversal):
        """A recursive helper method.
        """
        if start:
            traversal = self.inOrderPrint(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inOrderPrint(start.right, traversal)   
        return traversal

    def postOrderPrint(self, start, traversal):
        """A recursive helper method.
        """
        if start:
            traversal = self.postOrderPrint(start.left, traversal)
            traversal = self.postOrderPrint(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

    def searchSorted(self, find_val):
        """The tree is sorted increasingly from the left to the right.
        """
        return self.searchStep(self.root, find_val)    
    
    def searchStep(self, start, find_val):
        """A recursive helper function to look for find_val in a sorted tree.
        """
        if start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                self.searchStep(start.left, find_val)        
            elif start.value < find_val:
                self.searchStep(start.right, find_val)
        return False
    
    def insert(self, new_val):
        """The tree is sorted increasingly.
        """
        self.searchToInsert(self.root, new_val)

    def searchToInsert(self, start, new_val):
        """A helper recursive function for the insert() method.
        """
        if start:
            if new_val > start.value:
                self.searchToInsert(start.right, new_val)
                if not start.right:
                    start.right = Node(new_val)
            elif new_val < start.value:
                self.searchToInsert(start.left, new_val)
                if not start.left:
                    start.left = Node(new_val)
        return

if __name__ == "__main__":
    # Set up tree
    """ tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5) """
    # complete tree
    """ tree = BinaryTree("A")
    tree.root.left = Node("B")
    tree.root.left.left = Node("D")
    tree.root.left.left.left = Node("H")
    tree.root.left.left.right = Node("I")
    tree.root.left.right = Node("E")
    tree.root.left.right.left = Node("J")
    tree.root.left.right.right = Node("K")
    tree.root.right = Node("C")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")
    tree.root.right.left.left = Node("L")
    tree.root.right.left.right = Node("M")
    tree.root.right.right.right = Node("O")
    tree.root.right.right.left = Node("N") """
    # Set up sorted tree
    tree = BinaryTree(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    

    # Test search
    # Should be True
    print(tree.searchSorted(4))
    # Should be False
    print(tree.searchSorted(6))
    # A-B-D-H-I-E-J-K-C-F-L-M-G-N-O
    print(tree.printTree("pre"))
    # H-D-I-B-J-E-K-A-L-F-M-C-N-G-O
    print(tree.printTree("in"))
    # H-I-D-J-K-E-B-L-M-F-N-O-G-C-A
    print(tree.printTree("post"))