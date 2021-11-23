from quick_sort2 import quick_sort

#1.Increasingly sorted array is passed
def test_quickSort1():
    List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quick_sort(List) == sorted(List)

#2.Decreasingly sorted array is passed

def test_quickSort2():
    List = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert quick_sort(List) == sorted(List)
    
#3.A random array is passed
def test_quickSort3():
    List = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    assert quick_sort(List) == sorted(List)

#4.A random array with negative numbers
def test_quickSort4():
    List = [8, 3, 1, -7 ,0 ,10, -2]
    assert quick_sort(List) == sorted(List)

#5.An array with floating-point numbers
def test_quickSort5():
    List = [5.5, 2.7, 1, 81, -99, 0, 11]
    assert quick_sort(List) == sorted(List)

#6.An array with 1 element
def test_quickSort6():
    List = [10]
    assert quick_sort(List) == List

if __name__ == "__main__":
    test_quickSort1()
    test_quickSort2()
    test_quickSort3()
    test_quickSort4()
    test_quickSort5()
    test_quickSort6()
