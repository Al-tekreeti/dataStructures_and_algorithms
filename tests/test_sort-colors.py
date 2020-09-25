from pointers_techniques.sort_colors import sortColors

#1. If an empty array is passed, return the same array
def test_sortColors1():
    arr = sortColors([])
    assert len(arr) == 0

#2. If a sorted array is passed, the same array should be returned
def test_sortColors2():
    arr = [0,0,0,1,1,2]
    sorted_arr = sortColors(arr)
    assert arr == sorted_arr

#3. array with negative numbers
def test_sortColors3():
    arr = [0,0,0,1,1,-1,2]
    result = sortColors(arr)
    assert result == -1

#4. array with numbers > 2
def test_sortColors4():
    arr = [0,0,0,1,1,5,2]
    result = sortColors(arr)
    assert result == -1

if __name__ == "main":
    test_sortColors1()
    test_sortColors2()
    test_sortColors3()
    test_sortColors4()