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
        """Initialize the list if an array is passed"""
        self.head = None
        if itemList:
            for item in itemList:
                self.insert(item)

    def insert(self, item):
        """Insert the node at the end of the list"""
        node = Node(item)
        if self.head == None:
            self.head = node
            return 

        tmp = self.head
        while tmp.addr:
            tmp = tmp.addr

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
        
        # march nTh steps from the head
        node2 = self.head
        count = nTh
        while count:
            node2 = node2.addr
            if node2 == None and count > 1:
                raise Exception(f'The size of the list is smaller than {nTh}')
            count -= 1
        
        node1 = self.head
        # the target node to be removed is the head node
        if node2 == None:
            self.head = node1.addr
            return True
        # not reached the list end yet. The distance between node1 and node2 is nTh. Thus, keep marching thru the list while keeping node2 apart from node1 by nTh steps.
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
        # March thru the list at two different speeds, where node2 is twice as fast as node1.
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
        # March thru the list at two different speeds, where node2 is twice as fast as node1 untill they concide if there is a cycle.
        node1 = self.head
        node2 = self.head

        while node2 and node2.addr:
            if node2.addr == node1:
                return True
            node2 = node2.addr.addr
            node1 = node1.addr
        return False

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

    def findCycleLength(self):
        """Assume the list has a cycle"""
        node1, node2 = self.head, self.head
        # March thru the list at two different speeds until you hit a node that is a part of the cycle
        while node2 and node2.addr:
            node1 = node1.addr
            node2 = node2.addr.addr
            if node1 == node2:
                break
        # March thru the cycle untill we hit the same node
        tmp = node1
        node1 = node1.addr
        length = 1
        while node1 != tmp:
            node1 = node1.addr
            length += 1
        return length
    
    def findFirstNodeCycle(self):
        """Assume the list has a cycle"""
        node1, node2 = self.head, self.head
        length = self.findCycleLength() - 1
        while length:
            node2 = node2.addr
            length -= 1
        
        while True:
            if node1.addr == node1.addr and node1 != node2:
                return node2.addr.elem
            node1 = node1.addr
            node2 = node2.addr

    def __repr__(self):
        tmp = self.head
        llist = []
        while tmp:
            node = tmp
            llist.append(node.elem)
            tmp = node.addr

        return str(llist)
        
if __name__ == "__main__":
    List = LinkedList([1,2,3,4])
    print(f'The list has a cycle: {List.detectCycle()}')
    node1 = List.getNode(3)
    node2 = List.getNode(1)
    node1.addr = node2
    print(f'The list has a cycle: {List.detectCycle()}')
    print(f'The length of the cycle is {List.findCycleLength()}')
    print(f'The first node of the cycle is {List.findFirstNodeCycle()}')