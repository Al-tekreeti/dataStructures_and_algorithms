import random

def quick_sort(arr):
    """Implementation of quick sort algorithm using the divide and conquer technique, where the pivot is the 1st element of the array"""
    if len(arr) <= 1:
        return arr
    
    l_index = 0
    # to get performance close to n*log(n), choose the pivot randomly
    random.shuffle(arr)
    for g_index in range(1, len(arr)):
        if arr[g_index] <= arr[0]:
            tmp = arr[g_index]
            arr[g_index] = arr[l_index + 1]
            arr[l_index + 1] = tmp
            l_index += 1

    # put the pivot in its right place at l_index
    tmp = arr[l_index]
    arr[l_index] = arr[0]
    arr[0] = tmp

    return quick_sort(arr[:l_index]) + [arr[l_index]] + quick_sort(arr[l_index +  1:])

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"The sorted array is {quick_sort(arr1)}")