class Node:
    def __init__(self, elem=None, addr=None):
        self.elem = elem
        self.addr = addr
    
    def setAddr(self, addr):
        self.addr = addr
    
    def setElem(self, elem):
        self.elem = elem

class LinkedList:
    def __init__(self, itemList=None):
        self.head = None
        if itemList:
            for item in itemList:
                self.insert(item)

    def insert(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
            return 

        tmp = self.head
        while True:
            if tmp.addr:
                tmp = tmp.addr
            else:
                break

        tmp.addr = node
        return

    def delete(self):
        """ Remove an element from the head"""
        if self.head:
            node = self.head
            self.head = node.addr
        else:
            raise Exception("Delete from an empty list")
    
    def getSize(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.addr

        return length
    
    def removeFromEnd(self, nTh):
        """ Assume the size of the list is unknown"""
        if self.head == None:
            raise Exception("The list is empty!")
    
        node1 = self.head
        node2 = self.head
        count = nTh
        while count:
            node2 = node2.addr
            if node2 == None and count > 1:
                raise Exception(f'The size of the list is smaller than {nTh}')
            count -= 1
        
        if node2 == None:
            self.head = node1.addr
            return True

        while node2 != None:
            tmp = node1
            node1 = node1.addr
            node2 = node2.addr

        tmp.addr = node1.addr
        return True
    
    def findMiddle(self):
        """ Find and return the value of the middle node. If the length of the list is even, it returns the elem with index of lenght/2 - 1, assuming the first elem of index 0. If the length is 1, it returns that elem."""
        if self.head == None:
            raise Exception("The list is empty!")

        node1 = self.head
        node2 = self.head
    
        while node2.addr:
            node2 = node2.addr
            if node2.addr == None:
                break

            node2 = node2.addr
            node1 = node1.addr
        
        return node1.elem

    def detectCycle(self):
        if self.head == None:
            raise Exception("The list is empty!")

        node1 = self.head
        node2 = self.head
        """if node2.addr == None:
                return False"""

        while True:
            if node2.addr == node1:
                return True
            elif node2.addr == None:
                return False
            node2 = node2.addr
            if node2.addr == node1:
                return True
            elif node2.addr == None:
                return False
            node2 = node2.addr
            node1 = node1.addr
    
    def getNode(self, numOfNodes):
        """ get the node information that is numOfNodes steps apart from the head node"""
        if self.head == None:
            raise Exception("The list is empty!")

        index = self.head
        for _ in range(numOfNodes):
            if index.addr == None:
                raise Exception("The list is shorter than expected!")
            index = index.addr
        return index

    def __repr__(self):
        tmp = self.head
        llist = []
        while tmp:
            node = tmp
            llist.append(node.elem)
            tmp = node.addr

        return str(llist)
        
if __name__ == "__main__":
    List = LinkedList([1,2,3,4,5,6,7,8,9,10])
    print(f'The list has a cycle: {List.detectCycle()}')
    node1 = List.getNode(9)
    #node2 = List.getNode(4)
    node1.addr = node1
    print(f'The list has a cycle: {List.detectCycle()}')