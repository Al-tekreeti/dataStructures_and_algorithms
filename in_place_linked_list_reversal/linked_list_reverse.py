class node:
    def __init__(self, elem=None, addr=None):
        self.elem = elem
        self.addr = addr

class singly_linked_list:
    def __init__(self, head=None):
        self.head = head
    
    def insert_node(self, node):
        """Insert the node at the head
        """
        if not self.head:
            self.head = node
            node.addr = None
        else:
            node.addr = self.head
            self.head = node
    
    def add_list(self, list):
        list.reverse()
        for elem in list:
            n = node(elem)
            self.insert_node(n)

    def reverse(self):
        """Reverse the whole list only"""
        pointer = self.head
        prev = None
        while pointer:
            tmp = pointer.addr
            pointer.addr = prev
            prev = pointer
            pointer = tmp
        
        self.head = prev

    def __repr__(self) -> str:
        lst = []
        e = self.head
        while e:
            lst.append(e.elem)
            e = e.addr
        
        return str(lst)

def reverse_sub_list(head, p=1, q=-1):
    """Reverse from the pth element to the qth element only. Reverse the whole list if p and q values are 1 and -1, respectively.
    """
    # sublist_head is the element at (p - 1)th position
    point1, point2 = head, head
    sublist_head = head
    if p == 2:
        point1 = point1.addr
    elif p > 2:
        point1 = point1.addr
        while p - 2:
            sublist_head = sublist_head.addr
            point1 = point1.addr
            p -= 1

    # let point2 be the element at q by the end of the loop. If q=-1, forward point2 to the last node.
    if q == -1:
        while point2.addr:
            point2 = point2.addr
    else:
        while q - 1:
            point2 = point2.addr
            q -= 1
    
    prev, last_point = point2.addr, point2.addr
    while point1 != last_point:
        tmp = point1.addr
        point1.addr = prev
        prev = point1
        point1 = tmp
    
    if p == 1:
        head = prev
    else:
        sublist_head.addr = prev
    
    return head

def reverse_every_k_elements(head, k):
    """
    """
    pq_list = []
    point = head
    p, q = 1, 1
    #enumerate the p's and q's
    while point.addr:
        point = point.addr
        q += 1
        if q % k == 0:
            pq_list.append((p,q))
            p = p + k
    
    # for the last part of the list that may not fit into a complete k-items
    if q > p:
        pq_list.append((p,q))
    # we seperate doing the reverse operation in order not to corrupt the list while generating the p's and q's
    for pair in pq_list:
        head = reverse_sub_list(head, pair[0], pair[1])

    return head

def rotate_right(head, k):
    """"""
    point1, point2, point3 = head, head, head
    while point3.addr:
        point3 = point3.addr
    
    point3.addr = head
    
    while k:
        point2 = point2.addr
        k -= 1
    
    while point2 != point3:
        point1 = point1.addr
        point2 = point2.addr
    
    tmp = point1.addr
    point1.addr = None
    head = tmp

    return head


def main():
    lst = [0, 1, 2]
    ll = singly_linked_list()
    ll.add_list(lst)
    #ll.reverse()
    print(ll)
    #h = reverse_sub_list(ll.head, 4, 7)
    #h = reverse_every_k_elements(ll.head, 6)
    h = rotate_right(ll.head, 4)
    print(singly_linked_list(h))
    #print(ll)

main()