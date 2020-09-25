from pointers_techniques.remove_duplicates import removeDups

#1. If an empty array is passed, return 0
def test_removeDups1():
    r = removeDups([])
    assert r == 0

#2. The array does not have duplicates
def test_removeDups2():
    arr = [0,1,2,3,4,5,6,7,8,9]
    r = removeDups(arr)
    assert r == len(arr)

#3. The array has negative numbers
def test_removeDups3():
    arr = [-2,0,1,2,3,3,4,5,6,7,8,9]
    r = removeDups(arr)
    assert r == 11

if __name__ == "main":
    test_removeDups1()
    test_removeDups2()
    test_removeDups3()