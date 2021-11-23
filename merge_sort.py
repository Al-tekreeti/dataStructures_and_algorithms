
def merge_sort(arr):
    """Implementation of merge sort algorithm using the divide and conquer technique"""
    sorted_arr = []
    if len(arr) == 1:
        return arr

    left_arr = merge_sort(arr[:len(arr) // 2])
    right_arr = merge_sort(arr[len(arr) // 2:])
    
    index1, index2 = 0, 0
    while index1 < len(left_arr) and index2 < len(right_arr):
        if right_arr[index2] > left_arr[index1]:
            sorted_arr.append(left_arr[index1])
            index1 += 1
        else:
            sorted_arr.append(right_arr[index2])
            index2 += 1

    if index1 < len(left_arr):
        for elem in left_arr[index1:]:
            sorted_arr.append(elem)
    if index2 < len(right_arr):
        for elem in right_arr[index2:]:
            sorted_arr.append(elem)

    return sorted_arr

if __name__ == "__main__":
    arr1 = [6, 3, 11, 5, 91, 42, 53, 2]
    print(f"The sorted array is {merge_sort(arr1)}")