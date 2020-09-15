def sumThree(arr, target):
    """ 
        Find three elements in a sorted array that sums to a target value. Assume this target value appears only once.

        Arguments: 
        arr -- a sorted array of integer or floating numbers.
        target -- an integer or floating number value.

        Returns:
        Three indices of the found elements (the index of the 1st element is 1 not 0). If not found, a print message that shows that.
    """
    index1 = 0
    index2 = 1
    index3 = len(arr) - 1
    while index1 < index3 and index2 < index3:
        total = arr[index1] + arr[index2] + arr[index3]
        if total > target:
            index3 -= 1
        elif total < target:
            if index2 - 1 > index1:
                index1 += 1
            else:
                index2 += 1
        else:
            return index1 + 1, index2 + 1, index3 +1
    print("It is not possible!")

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9,10]
    print(f"The indices are {sumThree(a, 13)}")
