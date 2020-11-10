class LinkedListUnit:
        def __init__(self, elem=None, addr=None):
            self.elem = elem
            self.addr = addr

class LinkedList:
    def __init__(self, itemList=None):
        self.head = None
        if itemList:
            for item in itemList:
                self.insert(item)

    def insert(self, item):
        node = LinkedListUnit(item)
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
    List.removeFromEnd(1)
    print(List)