def removeDups(arr):
    """ 
        Remove duplicates from a sorted array.

        Arguments: 
        arr -- a sorted array.

        Returns:
        n -- the number of unique elements.
    """
    n = 0
    if len(arr) == 0:
        return n
  
    for i in range(len(arr)):
        if i == 0 or arr[i] != arr[i-1]:
            arr[n] = arr[i]
            n += 1
    assert n <= len(arr), "Impossible! How array length gets bigger!"
    return n

if __name__ == "__main__":
    a = [1,1,1,1,1,1,1,1,1,1,1]
    print(f"The number of unique elements is {removeDups([])}")
