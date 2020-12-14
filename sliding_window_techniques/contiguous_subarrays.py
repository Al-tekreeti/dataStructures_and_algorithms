import math

def getSubarrayMean(arr, K):
    """ Evaluate the average of adjacent subarrays.

    Arguments:
    arr -- an array of numeric values
    K -- the length of the subarray

    Outputs:
    return a list of the averages
    """
    # if the length of arr less than K, return empty list
    if len(arr) >= K:
        size = len(arr)
    else:
        return []
    _sum = 0
    averages = []
    # evaluate the sum of the first window
    for i in range(K):
        _sum += arr[i]

    for j in range(size - K):
        averages.append(_sum/K)
        # obtain the sum of the next window by adjusting the sum of the previous window
        _sum = _sum - arr[j] + arr[j + K]

    # we add the last average
    averages.append(_sum/K)
    return averages

def getSubarrayMaxSum(arr, K):
    """ Identify and evaluate the biggest sum of a subarray of a specific size K.

    Arguments:
    arr -- an array of positive numeric values
    K -- the length of the subarray

    Outputs:
    return the sum
    """
    # if the length of arr less than K, return -1
    if len(arr) >= K:
        size = len(arr)
    else:
        return -1
    _sum = 0

    # evaluate the sum of the first window
    for i in range(K):
        _sum += arr[i]
    
    max_sum = _sum

    # for static window, no need to define window start and end
    for j in range(size - K):
        # obtain the sum of the next window by adjusting the sum of the previous window
        _sum = _sum - arr[j] + arr[j + K]
        if _sum > max_sum:
            max_sum = _sum

    return max_sum

def getSmallestSubarray(arr, S):
    """Find the smallest subarray whose sum is equal or greater than a given value S.

    Arguments:
    arr -- an array of positive numeric values
    S -- a positive numeric value

    Outputs:
    return the size of the subarray
    
    """
    w1 = 0 # window start
    min_window = math.inf
    _sum = 0
    # w2: window end
    for w2 in range(0, len(arr), 1):
        _sum += arr[w2]
        while _sum >= S:
            window = w2 - w1 + 1
            if window < min_window:
                min_window = window
            _sum = _sum - arr[w1]
            w1 += 1
    return min_window

def getLongestSubstring(string, K):
    """Find the longest substring which has no more than K distinct letters
    """
    # if the length of string is less than K, return string's length
    if len(string) <= K:
        return len(string)
    # consider lower case strings only
    if not string.islower():
        string = string.lower()
    
    w1 = 0
    max_window = 0
    # list indexed by the hash of the letter
    hashTable = [0 for i in range(26)]
    # hash function: ASCII(letter) - ASCII('a')
    hashFunction = lambda l: ord(l) - ord('a')
    distinct = 0
    for w2 in range(len(string)):
        window = w2 - w1 + 1
        if hashTable[hashFunction(string[w2])] == 0:
            distinct += 1
        hashTable[hashFunction(string[w2])] += 1
        if window > max_window and distinct <= K:
            max_window = window
        while distinct > K:
            hashTable[hashFunction(string[w1])] -= 1
            if hashTable[hashFunction(string[w1])] == 0:
                distinct -= 1
            w1 += 1
    return max_window

def getFruitBasketsWeight(fruits):
    """
    """
    w1 = 0
    baskets = {}
    for w2 in range(len(fruits)):
        if fruits[w2] in baskets:
            baskets[fruits[w2]] += 1
        else:
            baskets[fruits[w2]] = 1
        while len(baskets) > 2:
            baskets[fruits[w1]] -= 1
            if baskets[fruits[w1]] == 0:
                baskets.pop(fruits[w1])
            w1 += 1
    return sum(baskets.values())

def getUniqueLongestSubString(string):
    """
    """
    strDict = {}
    length = 0
    maxLength = 0
    for w2 in range(len(string)):
        if not string[w2] in strDict:
            length += 1
            if length > maxLength:
                maxLength = length
            strDict[string[w2]] = 1
        else:
            length = 1
            strDict.clear()
            strDict[string[w2]] = 1
    return maxLength

def getLongestSameCharSubString(string, K):
    """with no more than K replacements.
    """
    w1 = 0
    maxLength = 0
    charsDict = {}
    charFrequency = 0
    for w2 in range(len(string)):
        if string[w2] not in charsDict:
            charsDict[string[w2]] = 0
        charsDict[string[w2]] += 1
        # charFrequency is determined by the letter under investigation, string[w2]
        charFrequency = max(charFrequency, charsDict[string[w2]])
        if w2 - w1 + 1 - charFrequency > K:
            charsDict[string[w1]] -= 1
            # to consider all possibilities, w1 is incremented by 1 when the window size gets bigger than K
            w1 += 1
        # maxLength depends on the controlled window size, w2 - w1 + 1 - charFrequency
        maxLength = max(maxLength, w2 - w1 + 1)
    return maxLength

def getLongestSubArrayWithOnes(arr, K):
    """
    """
    w1, onesCount, maxLength = 0, 0, 0
    for w2 in range(len(arr)):
        if arr[w2] == 1:
            onesCount += 1
        if w2 - w1 + 1 -onesCount > K:
            if arr[w1] == 1:
                onesCount -= 1
            w1 += 1
        maxLength = max(maxLength, w2 - w1 + 1)
    return maxLength

def findPermutation(string, pattern):
    """Problem challenge 1
    """
    w1, count, = 0, 0

    patternDict = {}
    for char in pattern:
        if char not in patternDict:
            patternDict[char] = 0
        patternDict[char] += 1

    for w2 in range(len(string)):
        if string[w2] in patternDict:
            count += 1
        if w2 - w1 + 1 > len(pattern):
            if string[w1] in patternDict:
                count -= 1
            w1 += 1
        if count == len(pattern):
            return True
    return False

def findStringAnagrams(string, pattern):
    """Problem challenge 2
    """
    w1, count = 0, 0
    indices_list = []
    freqDict = {}
    
    patternDict = {}
    for char in pattern:
        if char not in patternDict:
            patternDict[char] = 0
        patternDict[char] += 1
    
    for w2 in range(len(string)):
        if string[w2] in patternDict:
            if string[w2] not in freqDict:
                freqDict[string[w2]] = 0
            if freqDict[string[w2]] == 0:
                count += 1
            freqDict[string[w2]] += 1
        if w2 - w1 + 1 > len(pattern):
            if freqDict[string[w1]] == 1:
                count -= 1
            freqDict[string[w1]] -= 1
            w1 += 1
        if count == len(pattern):
            indices_list.append(w1)
    return indices_list

def findSubString(string, pattern):
    """Problem challenge 3
    """
    w1, count = 0, 0
    result_list = []
    freqDict = {}
    for letter in pattern:
        freqDict[letter] = 0
    
    for w2 in range(len(string)):
        if string[w2] in freqDict:
            freqDict[string[w2]] += 1
            if freqDict[string[w2]] == 1:
                if count == 0:
                    w1 = w2
                count += 1
            else:
                if freqDict[string[w1]] == 1:
                    count -= 1
                freqDict[string[w1]] -= 1
                w1 += 1
        if string[w1] in freqDict:
            if freqDict[string[w1]] > 1:
                freqDict[string[w1]] -= 1
                w1 += 1
        else:
            w1 += 1
        if count == len(pattern):
            result_list = string[w1:w2 + 1]
            return result_list
    return result_list

def findWordsConcat(string, words):
    """Problem challenge 4
    """
    w1, count = 0, 0
    indices_list = []
    wordLen = len(words[0])
    wordsDict = {word: 1 for word in words}
    freqWordDict = {}
    for w2 in range(wordLen - 1, len(string), wordLen):
        word = string[w2 - wordLen + 1:w2 + 1]
        if word in wordsDict:
            if word not in freqWordDict:
                freqWordDict[word] = 0
            if freqWordDict[word] == 0:
                count += 1
            freqWordDict[word] += 1
        if w2 - w1 + 1 > len(words) * wordLen:
            word = string[w1: w1 + wordLen]
            if freqWordDict[word] == 1:
                count -= 1
            freqWordDict[word] -= 1
            w1 += wordLen
        if count == len(words):
            indices_list.append(w1)
    return indices_list

def main():
    result = findWordsConcat("catfoxcat", ["cat", "fox"])
    print("The result is: " + str(result))

main()