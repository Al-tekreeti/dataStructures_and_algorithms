from merge_sort import merge_sort


#1.Increasingly sorted array is passed
def test_mergeSort1():
    List = [1,2,3,4,5,6,7,8,9,10]
    assert merge_sort(List) == List

#2.Any random array
def test_mergeSort2():
    List = [6, 3, 11, 5, 91, 42, 53, 2]
    assert merge_sort(List) == sorted(List)

#3.An array with odd number of elements
def test_mergeSort3():
    List = [6, 3, 11, 5, 42, 53, 2]
    assert merge_sort(List) == sorted(List)



if __name__ == "__main__":
    test_mergeSort1()
    test_mergeSort2()
    test_mergeSort3()
