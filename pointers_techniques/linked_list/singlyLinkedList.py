class LinkedListUnit:
        def __init__(self, elem):
            self.elem = elem
            self.addr = None

class LinkedList:
    def __init__(self, itemList=None):
        self.head = None
        if itemList:
            for item in itemList:
                self.insert(item)

    def insert(self, item):
        node = LinkedListUnit(item)
        if self.head:
            node.addr = self.head
        
        self.head = node

    def delete(self):
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

    def __repr__(self):
        tmp = self.head
        llist = []
        while tmp:
            node = tmp
            llist.append(node.elem)
            tmp = node.addr

        return str(llist)
        
if __name__ == "__main__":
    List = LinkedList([])
    List.delete()
    print(List.getSize())