def cyclic_sort(arr):
    """"""
    index = 0
    while index < len(arr):
        if arr[index] != index + 1:
            tmp = arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = tmp
        else:
            index += 1
    return arr

def find_duplicates(arr):
    """Remove all duplicates in place"""
    index = 0
    while index < len(arr):
        if arr[index] != index + 1:
            if arr[index] == arr[arr[index] - 1]:
                index += 1
                continue
            tmp = arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = tmp
        else:
            index += 1

    index = len(arr) - 1
    while index >= 0:
        if arr[index] == index + 1:
            arr.pop(index)
        index -= 1
    return arr

def find_missings(arr):
    """Find all missing numbers"""
    index = 0
    missings = []
    while index < len(arr):
        if arr[index] != index + 1:
            if arr[index] == arr[arr[index] - 1]:
                index += 1
                continue
            tmp = arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = tmp
        else:
            index += 1

    index = 0
    while index < len(arr):
        if arr[index] != index + 1:
            missings.append(index + 1)
        index += 1
    return missings

def find_smallest_missing_positive(arr):
    """"""
    index = 0
    while index < len(arr):
        if arr[index] > 0 and arr[index] <= len(arr) and arr[index] != index + 1:
            if arr[index] == arr[arr[index] - 1]:
                index += 1
                continue
            tmp = arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = tmp
        else:
            index += 1
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1
def find_first_k_missing_positive(arr, k):
    """ The time complexity is of order O(N + k). The space complexity is of order O(k), where N is the length of the array arr.
    """
    missings = []
    index = 0
    while index < len(arr):
        if arr[index] != index + 1 and arr[index] <= len(arr) and arr[index] > 0 and arr[index] != arr[arr[index] - 1]:
            tmp = arr[arr[index] - 1]
            arr[arr[index] - 1] = arr[index]
            arr[index] = tmp
        else:
            index += 1
            
    index = 0
    while index < len(arr) and k > 0:
        if arr[index] != index + 1:
            missings.append(index + 1)
            k -= 1
        index += 1
    
    # numbers that are in missings' positions
    list_missings = [arr[i - 1] for i in missings]
    while k > 0:
        index += 1
        if index not in list_missings:
            missings.append(index)
            k -= 1


    return missings

def main():
  #print(cyclic_sort([1, 5, 6, 4, 3, 2]))
  #print(find_duplicates([3, 4, 4, 5, 5]))
  #print(find_missings([2, 3, 2, 1]))
  #print(find_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_k_missing_positive([-2, -3, 4], 2))

main()