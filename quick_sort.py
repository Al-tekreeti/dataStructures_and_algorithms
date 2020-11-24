def pivotComp(array):
    """ 
        Sort the first n-1 elements of the array ascendingly with respect to a pivot. By default, the pivot is the last element in the array.

        Arguments: 
        array -- an array of numbers of size n.

        Returns:
        The resultant array and the index of the pivot.
    """
    # loop through all elements except the last one
    for index in range(len(array) - 1):
        if index == 0:
            pivot_index = len(array) - 1
            
        while array[index] > array[pivot_index] and index < pivot_index:
            # swap pivot with the previous element
            temp = array[pivot_index]
            array[pivot_index] = array[pivot_index - 1]
            array[pivot_index - 1] = temp
            
            # this swap only needed when the element to be swaped with the pivot is 2 steps or more before the pivot
            if pivot_index != index + 1:
                temp = array[pivot_index]
                array[pivot_index] = array[index]
                array[index] = temp

            # update the index of the pivot
            pivot_index -= 1
    
    return array, pivot_index

def quickSort(array):
    """ 
        The implementation of quick sort algorithm. The pivot is the last element in the array. It outsources pivot evaluations to another function called pivotComp()

        Arguments: 
        array -- an array of numbers.

        Returns:
        an array sorted ascendingly.
    """
    pivots = []
    while True:
        newPivots = []
        if len(pivots) == 0:# initial round when no pivots are there
            array, piv = pivotComp(array)
            pivots.append(piv)

        for i in range(len(pivots)):
            p1_index = -1# 1 step before 0. left pivot.
            p2_index = len(array)# right pivot.

            if i - 1 >= 0:
                p1_index = pivots[i - 1]
            if i + 1 <= len(pivots) - 1:
                p2_index = pivots[i + 1]

            leftSubArr = array[p1_index + 1:pivots[i]]
            if len(leftSubArr) > 1:
                arr, piv = pivotComp(leftSubArr)
                array = array[0:p1_index+1] + arr + array[pivots[i]:p2_index] + array[p2_index:len(array)]
                newPivots.append(p1_index + piv + 1)
                
            rightSubArr = array[pivots[i] + 1:p2_index]
            if len(rightSubArr) > 1:
                arr, piv = pivotComp(rightSubArr)
                array = array[0:pivots[i]+1] + arr + array[p2_index:len(array)]
                newPivots.append(piv + pivots[i] + 1)
                break # adding a new pivot to the right affects the next pivot

        if len(newPivots) == 0:# stop when no more pivots are generated
            break
        
        pivots += newPivots
        pivots.sort()

    return array

if __name__ == "__main__":
    # test = [8,3,1,7,0,10,2]
    # test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    test = [10,9,8,7,6,5,4,3,2,1]
    print(quickSort(test))