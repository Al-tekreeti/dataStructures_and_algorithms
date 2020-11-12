import pytest
from pointers_techniques.linked_list.singlyLinkedList import LinkedList

#1. empty array is passed
def test_singlyLinkedList1():
    List = LinkedList()
    assert List.getSize() == 0

#2. deleting an element from an empty list
def test_singlyLinkedList2():
    List = LinkedList()
    with pytest.raises(Exception) as e:
        assert List.delete()
        assert str(e.value) == "Delete from an empty list"


#3. array with three elements is passed
def test_singlyLinkedList3():
    List = LinkedList([1,2,3])
    assert List.getSize() == 3

#4. deleting an element from the list decreases its size by 1
def test_singlyLinkedList4():
    List = LinkedList([1,2,3])
    n_before = List.getSize()
    List.delete()
    n_after = List.getSize()
    assert n_after == n_before - 1

#5. inserting an element into the list increases its size by 1
def test_singlyLinkedList5():
    List = LinkedList([1,2,3])
    n_before = List.getSize()
    List.insert(4)
    n_after = List.getSize()
    assert n_after == n_before + 1

#6. removing the nth element from the end of the list
def test_singlyLinkedList6():
    List = LinkedList([1,2,3])
    with pytest.raises(Exception) as e:
        assert List.removeFromEnd(4)
        assert str(e.value) == f'The size of the list is smaller than 4'

#7. removing the nth element from the end of the list
def test_singlyLinkedList7():
    List = LinkedList()
    with pytest.raises(Exception) as e:
        assert List.removeFromEnd(4)
        assert str(e.value) == f'The list is empty!'

#8. returning the middle element in a list with odd length
def test_singlyLinkedList8():
    List = LinkedList([1,2,3,4,5])
    element = List.findMiddle()
    assert element == 3

#9. returning the middle element with index length/2 - 1 in a list with even length
def test_singlyLinkedList9():
    List = LinkedList([1,2,3,4])
    element = List.findMiddle()
    assert element == 2

#10. returning the only element if the length is 1
def test_singlyLinkedList10():
    List = LinkedList([1])
    element = List.findMiddle()
    assert element == 1

#11. returning the middle of an empty list raises an expception
def test_singlyLinkedList11():
    List = LinkedList()
    with pytest.raises(Exception) as e:
        assert List.findMiddle()
        assert str(e.value) == f'The list is empty!'

#12. Passing zero to getNode() function should return the head node
def test_singlyLinkedList12():
    List = LinkedList([1,2,3,4])
    node = List.getNode(0)
    assert node == List.head

#13. Passing a positive number greater than the length of the list
def test_singlyLinkedList13():
    List = LinkedList([1,2,3,4])
    with pytest.raises(Exception) as e:
        assert List.getNode(7)
        assert str(e.value) == f'The list is shorter than expected!'

#14. Passing length-1 to getNode() function should return a node with None addr
def test_singlyLinkedList14():
    List = LinkedList([1,2,3,4])
    node = List.getNode(3)
    assert node.addr == None

#15. Detect a cyclic list with only one element
def test_singlyLinkedList15():
    List = LinkedList([1])
    node1 = List.getNode(0)
    node1.addr = node1
    assert List.detectCycle() == True

#16. Detect a normal list is acyclic
def test_singlyLinkedList16():
    List = LinkedList([1,2,3,4,5,6,7])
    assert List.detectCycle() == False

#17. The last node linked to a node in the middle
def test_singlyLinkedList17():
    List = LinkedList([1,2,3,4,5,6,7,8,9,10])
    node1 = List.getNode(9)
    node2 = List.getNode(4)
    node1.addr = node2
    assert List.detectCycle() == True

#18.An empty list raises an expception
def test_singlyLinkedList18():
    List = LinkedList()
    with pytest.raises(Exception) as e:
        assert List.detectCycle()
        assert str(e.value) == f'The list is empty!'

if __name__ == "main":
    test_singlyLinkedList1()
    test_singlyLinkedList2()
    test_singlyLinkedList3()
    test_singlyLinkedList4()
    test_singlyLinkedList5()
    test_singlyLinkedList6()
    test_singlyLinkedList7()
    test_singlyLinkedList8()
    test_singlyLinkedList9()
    test_singlyLinkedList10()
    test_singlyLinkedList11()
    test_singlyLinkedList12()
    test_singlyLinkedList13()
    test_singlyLinkedList14()
    test_singlyLinkedList15()
    test_singlyLinkedList16()
    test_singlyLinkedList17()
    test_singlyLinkedList18()