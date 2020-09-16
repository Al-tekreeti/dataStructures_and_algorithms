class linkedListUnit:
        def __init__(self, elem):
            self.elem = elem
            self.addr = None

class linkedList:
    def __init__(self, itemList=None):
        if itemList:
            self.head = None
            for item in itemList:
                self.insert(item)
    def insert(self, item):
        node = linkedListUnit(item)
        if self.head:
            node.addr = self.head
            self.head = node
        else:
            self.head = node
    def delete(self):
        if self.head:
            node = self.head
            self.head = node.addr
        else:
            print("The list is empty!")
    def __repr__(self):
        tmp = self.head
        llist =[]
        while tmp:
            node = tmp
            llist.append(node.elem)
            tmp = node.addr
        return str(llist)
        
