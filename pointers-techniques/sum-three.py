

def sumThree(arr, target):
    index1 = 0
    index2 = 1
    index3 = len(arr) - 1
    print(arr[index1], arr[index2], arr[index3])
    while index1 < index3 and index2 < index3:
        total = arr[index1] + arr[index2] + arr[index3]
        if total > target:
            index3 -= 1
            print(arr[index1], arr[index2], arr[index3])
        elif total < target:
            if index2 - 1 > index1:
                index1 += 1
                print(arr[index1], arr[index2], arr[index3])
            else:
                index2 += 1
                print(arr[index1], arr[index2], arr[index3])
        else:
            return index1 + 1, index2 + 1, index3 +1
    print("It is not possible!")
