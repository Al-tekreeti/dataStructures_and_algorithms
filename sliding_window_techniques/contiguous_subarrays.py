import math
import copy

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

def max_sub_array_of_size_k(k, arr):
    """
    Using fixed sliding window (version2)
    """
    if k >= len(arr):
        return sum(arr)
    
    max_sum, index1, index2 = 0, 0, k
    for iteration in range(len(arr) - k + 1):
        s = sum(arr[index1:index2])
        if s > max_sum:
            max_sum = s

        index1 += 1
        index2 += 1
    
    return max_sum

def getSubarrayMaxSum(arr, K):
    """ Identify and evaluate the biggest sum of a subarray of a specific size K (version1)

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

def longest_substring_with_k_distinct(str, k):
    """Find the longest substring which has no more than K distinct letters (version 2). The time complexity for the outer for loop is O(N), where N is the length of str. For the while loop, the maximum number of distinct letters cannot exceed N (the distance between index1 and index2 as well). Therefore, in one iteration of the for loop, while loop will execute for N-k iterations, and for the remaining N-1 for loop iterations, the while loop will execute once. Hence, O(N + 1 * (N - k) + (N - 1) * 1) = O(3N - k - 1) = O(N), giving that N >> k for most cases.
    """
    index1 = 0
    longest_ss = 0
    char_dict = {}
    for index2 in range(len(str)):
        if str[index2] in char_dict:
            char_dict[str[index2]] += 1
        else:
            char_dict[str[index2]] = 1
        
        while len(char_dict.keys()) > k and index1 <= index2:
            char_dict[str[index1]] -= 1
            if char_dict[str[index1]] == 0:
                char_dict.pop(str[index1])
            index1 += 1

        if index2 - index1 + 1 > longest_ss:
            longest_ss = index2 - index1 + 1
    
    return longest_ss

def getLongestSubstring(string, K):
    """Find the longest substring which has no more than K distinct letters (version1)
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

def fruits_into_baskets(fruits):
    """version2
    """
    max_fruit_number = 0
    index1 = 0
    fruits_dict = {}
    for index2 in range(len(fruits)):
        if fruits[index2] in fruits_dict:
            fruits_dict[fruits[index2]] += 1
        else:
            fruits_dict[fruits[index2]] = 1  
        
        while len(fruits_dict.keys()) > 2 and index1 <= index2:
            fruits_dict[fruits[index1]] -= 1
            if fruits_dict[fruits[index1]] == 0:
                fruits_dict.pop(fruits[index1])
            index1 += 1
        
        if sum(fruits_dict.values()) > max_fruit_number:
            max_fruit_number = sum(fruits_dict.values())

    return max_fruit_number

def getFruitBasketsWeight(fruits):
    """version1
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

def no_repeat_substring(string):
    """
    """
    chars_dict = {}
    longest_ss, index1 = 0, 0
    for index2 in range(len(string)):
        if string[index2] in chars_dict:
            chars_dict[string[index2]] += 1
        else:
            chars_dict[string[index2]] = 1

        while chars_dict[string[index2]] > 1 and index1 <= index2:
            chars_dict[string[index1]] -= 1
            if chars_dict[string[index1]] == 0:
                chars_dict.pop(string[index1])
            
            index1 += 1

        if len(chars_dict.keys()) > longest_ss:
            longest_ss = len(chars_dict.keys())

    return longest_ss

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

def length_of_longest_substring(str, k):
    """version 2
    """
    # no need to run the algorithm if str is shorter than k
    if k >= len(str):
        return len(str)

    index1, longest_ss, to_be_replaced = 0, 0, 0
    chars_dict = {}

    for index2 in range(len(str)):
        if str[index2] in chars_dict:
            chars_dict[str[index2]] += 1
        else:
            chars_dict[str[index2]] = 1

        to_be_replaced = sum(chars_dict.values()) - max(chars_dict.values())

        while to_be_replaced > k and index1 <= index2:
            chars_dict[str[index1]] -= 1
            if chars_dict[str[index1]] == 0:
                chars_dict.pop(str[index1])
            index1 += 1
            to_be_replaced = sum(chars_dict.values()) - max(chars_dict.values())
        
        if sum(chars_dict.values()) > longest_ss:
            longest_ss = sum(chars_dict.values())
    
    return longest_ss

def getLongestSameCharSubString(string, K):
    """with no more than K replacements (version 1).
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

def length_of_longest_substring_with_ones(arr, k):
    """
    version2
    """
    if len(arr) <= k:
        return len(arr)
    
    index1, longest_sa = 0, 0
    ones_zeros_dict = {}
    for index2 in range(len(arr)):
        if arr[index2] in ones_zeros_dict:
            ones_zeros_dict[arr[index2]] += 1
        else:
            ones_zeros_dict[arr[index2]] = 1
        
        while 0 in ones_zeros_dict and ones_zeros_dict[0] > k and index1 <= index2:
            ones_zeros_dict[arr[index1]] -= 1
            if ones_zeros_dict[arr[index1]] == 0:
                ones_zeros_dict.pop(arr[index1])
            index1 += 1

        if sum(ones_zeros_dict.values()) > longest_sa:
            longest_sa = sum(ones_zeros_dict.values())
    
    return longest_sa


def getLongestSubArrayWithOnes(arr, K):
    """
    version1
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

def find_permutation3(string, pattern):
    """
    version3: using fixed sliding window
    """
    if len(string) < len(pattern):
        return False

    def str_to_dict(str):
        _dict = {}
        for l in str:
            if l in _dict:
                _dict[l] += 1
            else:
                _dict[l] = 1
        return _dict

    pattern_dict = str_to_dict(pattern)
    permut_dict = {}
    index1, index2 = 0, len(pattern) - 1
    for iteration in range(len(string) - len(pattern) + 1):
        if iteration == 0:
            permut_dict = str_to_dict(string[index1:index2 + 1])
        else:# update permut_dict by adding one letter to the right of the window
            if string[index2] in permut_dict:
                permut_dict[string[index2]] += 1
            else:
                permut_dict[string[index2]] = 1

        if pattern_dict == permut_dict:
            return True
        # update permut_dict by removing one letter to the left of the window after shifting one position
        permut_dict[string[index1]] -= 1
        if permut_dict[string[index1]] == 0:
            permut_dict.pop(string[index1])
        
        index1 += 1
        index2 += 1

    return False

def find_permutation2(string, pattern):
    """
    version 2
    """ 
    if len(string) < len(pattern):
        return False

    pattern_dict, permut_dict = {}, {}
    index1 = 0
    # create a dict for pattern
    for letter in pattern:
        if letter in pattern_dict:
            pattern_dict[letter] += 1
        else:
            pattern_dict[letter] = 1

    for index2 in range(len(string)):
        if string[index2] in pattern_dict:# the letter exists in pattern
            if string[index2] in permut_dict:# exists in permutation dict too
                if pattern_dict[string[index2]] > permut_dict[string[index2]]:
                    permut_dict[string[index2]] += 1
                else:# if pattern_dict[letter] = permut_dict[letter], reinitialize
                    permut_dict = {}
                    permut_dict[string[index2]] = 1
            else:
                permut_dict[string[index2]] = 1
        else:
            permut_dict = {}
        
        while string[index2] in pattern_dict and index2 - index1 + 1 > len(pattern):# this while loop can be replaced by an if clause, but kept like this to promote the developed template so far for sliding window
            index1 += 1

        if pattern_dict == permut_dict:# assuming index2 - index1 + 1 = pattern length
            return True

    return False

def findPermutation(string, pattern):
    """Problem challenge 1 (version 1)
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

def find_string_anagrams(str, pattern):
    """
    version2: using fixed sliding window
    """
    anagrams_list = []
    if len(pattern) > len(str):
        return anagrams_list
    
    def str_to_dict(string):
        _dict = {}
        for l in string:
            if l in _dict:
                _dict[l] += 1
            else:
                _dict[l] = 1
        return _dict
    # initializations
    pattern_dict = str_to_dict(pattern)
    anagram_dict = {}
    index1, index2 = 0, len(pattern) - 1

    for iteration in range(len(str) - len(pattern) + 1):
        if iteration == 0:
            anagram_dict = str_to_dict(str[index1:index2 + 1])
        else:# update anagram_dict after shifting the window (right)
            if str[index2] in anagram_dict:
                anagram_dict[str[index2]] += 1
            else:
                anagram_dict[str[index2]] = 1
        
        if anagram_dict == pattern_dict:
            anagrams_list.append(index1)
        # update anagram_dict after shifting the window (left)
        anagram_dict[str[index1]] -= 1
        if anagram_dict[str[index1]] == 0:
            anagram_dict.pop(str[index1])
        
        index1 += 1
        index2 += 1
    
    return anagrams_list
        

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

def find_substring(str, pattern):
    """Problem challenge 3 (version2): using variable sliding window
    """
    if len(pattern) > len(str):
        return ""
    
    pattern_dict, ss_dict = {}, {}
    smallest_ss = ""
    index1 = 0

    for l in pattern:
        if l in pattern_dict:
            pattern_dict[l] += 1
        else:
            pattern_dict[l] = 1
    
    for index2 in range(len(str)):
        if str[index2] in pattern_dict:
            if str[index2] in ss_dict:
                if ss_dict[str[index2]] < pattern_dict[str[index2]]:
                    ss_dict[str[index2]] += 1
                else:
                    ss_dict = {}
                    ss_dict[str[index2]] = 1
                    index1 = index2
            else:
                ss_dict[str[index2]] = 1

        if ss_dict == pattern_dict:
            if len(smallest_ss) > len(str[index1:index2 + 1]) or smallest_ss == "":
                smallest_ss = str[index1:index2 + 1]

            ss_dict[str[index1]] -= 1
            if ss_dict[str[index1]] == 0:
                ss_dict.pop(str[index1])
            index1 += 1
            # while loop inside
            while index1 <= index2 and str[index1] not in ss_dict:
                index1 += 1

    return smallest_ss

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

def find_word_concatenation(str, words):
    """
    problem challenge 4 (version 2): using fixed sliding window
    time complexity: O(NM/K) where N is the length of str, M # of words, K is the word length.
    space complexity: O(M)
    """
    if len(words) * len(words[0]) > len(str):
        return []

    indices_list = []
    index1, index2 = 0, len(words[0]) - 1
    first_index = None
    words_dict = dict.fromkeys(words, 0) 
    first_found_flag = False

    for iteration in range(len(str) // len(words[0])):
        # 
        if str[index1:index2 + 1] in words:
            if words_dict[str[index1:index2 + 1]] == 0:
                words_dict[str[index1:index2 + 1]] = 1
                if not first_found_flag:
                    first_index = index1
                    first_found_flag = True
            else:
                first_index += len(words[0])
                
        else:
            if first_found_flag:
                words_dict = dict.fromkeys(words, 0) 
                first_found_flag = False
                first_index = None

        index1 = index1 + len(words[0])
        index2 = index2 + len(words[0])

        if sum(words_dict.values()) == len(words):
            indices_list.append(first_index)
            words_dict[str[first_index:first_index + len(words[0])]] = 0
            first_index += len(words[0])
    
    return indices_list

def findWordsConcat(string, words):
    """Problem challenge 4 (version 1)
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
    #result = findWordsConcat("catfoxcat", ["cat", "fox"])
    #print("The result is: " + str(result))
    print(find_word_concatenation("dogcatdogcatfoxcatdog", ["cat", "fox", "dog"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

main()