from pointers_techniques.sum_three import sumThree

#1. If an empty array is passed, return three -1 as indices values
def test_sumThree1():
    index1, index2, index3 = sumThree([], 5)
    assert index1 == -1 and index2 == -1 and index3 == -1

#2. The length of the passed array should be more than 3
def test_sumThree2():
    index1, index2, index3 = sumThree([1,5], 6)
    assert index1 == -1 and index2 == -1 and index3 == -1
 
 #3. The target value is not there in the array
def test_sumThree3():
    result = sumThree([3, 4, 9, 92], 7)
    assert result == None


if __name__ == "main":
    test_sumThree1()
    test_sumThree2()
    test_sumThree3()