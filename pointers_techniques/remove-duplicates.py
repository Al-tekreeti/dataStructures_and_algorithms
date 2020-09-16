def remove_dup(arr):
    n = 0
    if len(arr) == 0:
        print("empty array!")
        return n
  
    for i in range(len(arr)):
        print(n, i)
        if i == 0 or arr[i] != arr[i-1]:
            arr[n] = arr[i]
            n += 1
            print(n, i)
    return n
