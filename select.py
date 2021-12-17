import random

def select(arr, pos):
    """Implement the random select algorithm using the divide and conquer technique. It returns the pos-th amallest element in the array arr"""
    if pos > len(arr):
        print(f"The required element position is beyond the array size")
        return

    l_index = 0
    # shuffle arr to randomize the pivot
    random.shuffle(arr)
    for b_index in range(1, len(arr)):
        if arr[b_index] <= arr[0]:# pivot is always 1st element
            tmp = arr[b_index]
            arr[b_index] = arr[l_index + 1]
            arr[l_index + 1] = tmp
            l_index += 1

    # put the pivot in its right location    
    tmp = arr[0]
    arr[0] = arr[l_index]
    arr[l_index] = tmp

    if pos > l_index + 1:
        return select(arr[l_index + 1:], pos - l_index - 1)
    elif pos < l_index + 1:
        return select(arr[:l_index], pos)
    else:
        return arr[l_index]

if __name__ == "__main__":
    arr1 = [6, 3, 11, 5, 91, 42, 53, 2]
    pos = 1
    print(f"The {pos}th element is {select(arr1, pos)}")