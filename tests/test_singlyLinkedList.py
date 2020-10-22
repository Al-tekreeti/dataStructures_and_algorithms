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


if __name__ == "main":
    test_singlyLinkedList1()
    test_singlyLinkedList2()
    test_singlyLinkedList3()
    test_singlyLinkedList4()
    test_singlyLinkedList5()