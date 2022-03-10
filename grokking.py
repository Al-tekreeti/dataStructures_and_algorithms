from typing import List
from collections import deque

def print_perms(string):
    result = []
    letter_count_map = build_freq_table(string)
    print_perms_inner(letter_count_map, "", len(string), result)
    return result


# returns dictionary <string, integer>
def build_freq_table(string):
    letter_count_map = {}
    for letter in string:
        if letter not in letter_count_map:
            letter_count_map[letter] = 0
        letter_count_map[letter] += 1
    return letter_count_map


def print_perms_inner(letter_count_map, prefix, remaining, result):
    # base case Permutation has been completed
    if remaining == 0:
        result.append(prefix)
        return
    # try remaining letter for next char, and generate remaining permutations
    for character in letter_count_map:
        count = letter_count_map[character]
        if count > 0:
            letter_count_map[character] -= 1
            print_perms_inner(
                letter_count_map, prefix + character, remaining - 1, result
            )
            letter_count_map[character] = count
def get_coins(cents):
    """ Iterative solution
    """
    reps = []
    if cents == 0:
        return []
    for q in range(cents//25 + 1):
        for d in range((cents - 25*q)//10 + 1):
            for n in range((cents - 25*q - 10*d)//5 + 1):
                p = cents - (q*25 + d*10 + 5*n)
                if p >= 0 and p <= cents:
                    reps.append([q, d, n, p])
    
    return len(reps)

def coin_combinations(amount, coin_sizes=None):
    """ Recursive solution
    """
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if coin_sizes is None:
        coin_sizes = [25, 10, 5, 1]

    if len(coin_sizes) == 0:
        return 0
    m = len(coin_sizes)
    return coin_combinations(amount, coin_sizes[: m - 1]) + coin_combinations(
        amount - coin_sizes[m - 1], coin_sizes
    )

def get_product(lst):
    """ Compute the product of list elements recursively.
    """
    if len(lst) == 0:
        return 1

    return lst[0] * get_product(lst[1:])

def get_flattened(lst):
    results = []
    flattened(lst, results)
    return results

def flattened(lst, results):
    if type(lst) != list:
        results.append(lst)
        return
    for l in lst:
        flattened(l, results)

def get_capitalized(lst):
    if len(lst) == 0:
        return []
    
    return [lst[0].capitalize()] + get_capitalized(lst[1:])

def change(x, coins=[25, 10, 5, 1]):
    """ Minimum number of change coins for x cents using 25, 10, 5, and 1 cent coins.
    """
    if x == 0:
        return 0
    
    for coin in coins:
        if x - coin >= 0:
            return 1 + change(x - coin, coins)
    
def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) in [0, 1]:
        return len(nums)
    
    i1 = 0
    for i2 in range(1, len(nums)):
        if nums[i1] == nums[i2]:
            continue
        
        i1 += 1
        nums[i1] = nums[i2]
    
    return i1 + 1

def rotate(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or k == 0:
            return nums
        
        nums = nums[k+1:] + nums[:k+1]
        return nums

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 1:
        return 0
    
    char_dict = {}
    for i in range(len(s)):
        if s[i] not in char_dict:
            char_dict[s[i]] = i
        else:
            char_dict[s[i]] = -1
    
    for key in char_dict.keys():
        if char_dict[key] != -1:
            return char_dict[key]
    
    return -1

def strStr(haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        
        if m == 0:
            return 0
        elif m > n:
            return -1
        
        index, i, j = -1, 0, 0
        while i < n and j < m:
            if haystack[i] != needle[j]:
                if index == -1:
                    i += 1
                    
                else:
                    j = 0
                    i = index + 1
                    index = -1
                    
            else:
                if index == -1:
                    index = i
                
                i += 1
                j += 1
        
        if j >= m:
            return index
        else:
            return -1

def longestCommonPrefix(strs: List[str]) -> str:
    n = len(strs)
    if n == 1:
        return strs[0]
    
    s1 = strs.pop()
    s2 = strs.pop()
    for _ in range(n-1):
        s1 = pref_two_strings(s1, s2)
        if len(s1) == 0:
            return ""
        
        if len(strs) > 0:
            s2 = strs.pop()
    
    return s1
    
def pref_two_strings(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    
    i = 0
    shortest_str = min(len(s1), len(s2))
    while i < shortest_str and s1[i] == s2[i]:
        i += 1
    
    return s1[:i]

def romanToInt(s: str) -> int:
    if len(s) == 0:
        return 0
    i = 0
    num = 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    while i < len(s):
        if (i < (len(s) - 1)) and roman_dict[s[i]] < roman_dict[s[i+1]]:
            num += roman_dict[s[i+1]] - roman_dict[s[i]]
            i += 2
            continue
            
        num += roman_dict[s[i]]
        i += 1

        
    return num

def generate(num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

def generate_sequences(seq1, seq2):
    """This is part of the implementation of problem 4.9 in the book cracking the coding interview
    """
    def recurse_helper(s1, s2, prefix):
        if not s1 or not s2:
            return prefix + s1 + s2
        
        out1 = recurse_helper(s1[1:], s2, prefix + s1[0:1])
        out2 = recurse_helper(s1, s2[1:], prefix + s2[0:1])

        if type(out1[0]) != list and type(out2[0]) != list:
            return [out1, out2]
        elif type(out1[0]) == list and type(out2[0]) == list:
            return out1 + out2
        elif type(out1[0]) == list:
            out1.append(out2)
            return out1
        else:
            out2.append(out1)
            return out2
    
    return recurse_helper(seq1, seq2, [])


if __name__ == "__main__":
    #print(print_perms("aaf"))
    #cents = 35
    #print(f"The number of ways of coin representations of {cents} cents are {get_coins(cents)}")
    #print(coin_combinations(35))
    #print(get_product([1, 2, 3, 5, 5, 5]))
    #print(get_flattened([0, [1,2,3], [4,5]]))
    #print(get_capitalized(['foo', 'bar']))
    #print(change(30, coins=[25, 10, 5, 1]))
    #print(removeDuplicates([1,1,2]))
    #print(rotate([1,2,3,4,5,6,7], 3))
    #print(firstUniqChar("aadadaad"))
    #print(strStr("aaaaaaab", "aaaab"))
    #print(longestCommonPrefix(["flower","flow","flight"]))
    #print(romanToInt("MCMXCIV"))
    #print(generate(6))
    print(len(generate_sequences([2,3, 4], [6, 7, 8,9, 10,11, 12])))

    