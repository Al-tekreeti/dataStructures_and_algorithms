import math

def pairWithTargetSum(arr, target_sum):
    """
    """
    index1 = 0
    index2 = len(arr) - 1
    while index1 <= index2:
        if arr[index1] + arr[index2] == target_sum:
            return [index1, index2]
        if arr[index1] + arr[index2] > target_sum:
            index2 -= 1
        if arr[index1] + arr[index2] < target_sum:
            index1 += 1
    return [-1, -1]

def removeDuplicates(arr):
    """We avoid pop operation since it is costy in list data structures.
    """
    arrLen = len(arr)
    index1 = 0
    for index2 in range(1, arrLen, 1):
        if arr[index2] != arr[index1]:
            index1 += 1
            arr[index1] = arr[index2]
    return index1 + 1

def removeElement(arr, key):
    """Extra problem. We avoid pop operation as well.
    """
    index1, index2 = 0, 0
    while index2 <= len(arr) - 1:
        if arr[index2] != key:
            arr[index1] = arr[index2]
            index1 += 1
            index2 += 1
        else:
            index2 += 1
    return index1

def makeSquares(arr):
    """The arr is sorted, but it may contain negative numbers.
    """
    index1, index2, highestIndex = 0, len(arr) - 1, len(arr) - 1
    squaredArr = [0 for x in range(len(arr))]
    while index1 <= index2:
        if arr[index1] * arr[index1] <= arr[index2] * arr[index2]:
            squaredArr[highestIndex] = arr[index2] * arr[index2]
            index2 -= 1
            highestIndex -= 1
        else:
            squaredArr[highestIndex] = arr[index1] * arr[index1]
            index1 += 1
            highestIndex -= 1
    return squaredArr

def findSummedZeroTriplets(arr):
    """
    """
    arr.sort()
    tripletsList = []
    index = 0
    while arr[index] <= 0:
        index1 = index + 1
        index2 = len(arr) - 1
        while index1 < index2:
            if arr[index] + arr[index1] + arr[index2] == 0:
                # avoid duplicates
                if len(tripletsList) == 0:
                    elem1 = arr[index1]
                    elem2 = arr[index2]
                elif (elem1 == arr[index1] and elem2 == arr[index2]) or (elem1 == arr[index2] and elem2 == arr[index1]):
                    index1 += 1
                    continue
                tripletsList.append([arr[index], arr[index1], arr[index2]])
                index1 += 1
            elif arr[index] + arr[index1] + arr[index2] > 0:
                index2 -= 1
            else:
                index1 += 1
        index += 1
        # avoid duplicates
        while arr[index] == arr[index - 1]:
            index += 1
    return tripletsList

def findSmallestTripletsSumCloseToTarget(arr, target_sum):
    arr.sort()
    index = 0
    min_sum_diff = math.inf
    closest_sum = math.inf
    # since arr is sorted, we stop if the elem exceeds target
    while arr[index] <= target_sum:
        index1 = index + 1
        index2 = len(arr) - 1
        while index1 < index2:
            current_sum = arr[index] + arr[index1] + arr[index2]
            sum_diff = abs(current_sum - target_sum)
            if sum_diff < min_sum_diff:
                min_sum_diff = sum_diff
                closest_sum = current_sum
                index1 += 1
            elif sum_diff > min_sum_diff:
                index2 -= 1
            else:
                if current_sum < closest_sum:
                    closest_sum = current_sum
                index1 += 1
        index += 1
        # we should stop when index reach two steps before last elem
        if index > len(arr) - 3:
            break
    return closest_sum

def findTripletsWithSmallerSum(arr, target_sum):
    """
    """
    triplet_count = 0
    arr.sort()
    index = 0
    while arr[index] < target_sum and index <= len(arr) - 3:
        index1, index2 = index + 1, len(arr) - 1
        while index1 < index2:
            triplet_sum = arr[index] + arr[index1] + arr[index2]
            if triplet_sum < target_sum:
                # this step equates for decrementing index2 (not incrementing index1) by 1 till one step ahead of index1. Why? because by decrementing index2, we are assured that the total sum does not exceed target_sum. However, if we increment index1, there is no guarantee for that.
                triplet_count += index2 - index1
                # therefore, here we have to increment index1 (not decrementing index2) to catch all combinations.
                index1 += 1
            else:
                index2 -= 1
        index += 1
    return triplet_count

def findSubArrays(arr, target):
    """Find all contiguous subarrays in arr whose elements' product is less than the target number. In the worst case, for an n-element array, we have n*(n+1)/2 subarrays. Hence, the time complexity approaches O(n^2). In the manual, it is believed to be O(n^3). Note: as the requirement is to enumerate or print all combinations that satisfy some conditions, there is no short cut. We have to employ the necessary loops to get the combinations.
    """
    list_arr = []
    for index1 in range(len(arr)):
        prod = 1
        for index2 in range(index1, len(arr), 1):
            prod *= arr[index2]
            if prod < target:
                list_arr.append(arr[index1:index2 + 1])
            else:
                break

    return list_arr

def dutchFlagSort(arr):
    """Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.
    """
    # the main idea is to keep two pointers (index0 and index2) that point to 0's at the left and 2's at the right. The third pointer (index1) is to traverse the array from left to right element by element and then push to the right if it is a two or push to the left if it is a zero.
    index0, index1 = 0, 0
    index2 = len(arr) - 1
    while index1 <= index2:
        if arr[index1] == 0:
            temp = arr[index1]
            arr[index1] = arr[index0]
            arr[index0] = temp
            index0 += 1
            if index0 > index1:
                index1 += 1
        elif arr[index1] == 2:
            temp = arr[index1]
            arr[index1] = arr[index2]
            arr[index2] = temp
            index2 -= 1
        else:
            index1 += 1
    return arr

if __name__ == "__main__":
    result = dutchFlagSort([2,2,2,1,0,1,0])
    print(f"The result is {result}")