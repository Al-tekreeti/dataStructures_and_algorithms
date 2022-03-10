from collections import deque
from random import randrange
import math
import numpy as np

def rotate_by(char, r_factor):
  if char.isnumeric():
    numeric_char = (int(char) + r_factor) % 10
    return f"{numeric_char}"
  else:
    factor = 0
    if char.islower():
      factor = ord("a")
    else:
      factor = ord("A")
    
    alpha_char = ((ord(char) - factor) + r_factor) % 26
    return chr(alpha_char + factor)


def rotationalCipher(input, rotation_factor):
  # Write your code here
  if rotation_factor == 0:
    return input
  
  output = []
  
  for i in range(len(input)):
    if not input[i].isalnum():
      output.append(input[i])
      continue
    output.append(rotate_by(input[i], rotation_factor))
    
  return "".join(output)

def findSignatureCounts(arr):
  # Write your code here
  output = [1] * len(arr)
  
  for i in range(1, len(arr) + 1):
    if i == arr[i-1]:
      continue
    
    tmp = arr[i-1]
    while i != tmp:
      output[i-1] += 1
      tmp = arr[tmp-1]
    
  return output

def min_length_substring(s, t):
  # Write your code here
  # check for corner cases
  
  char_dict = {}
  for i in range(len(s)):
    if s[i] not in char_dict:
      char_dict[s[i]] = [i]
    
    else:
      char_dict[s[i]].append(i)
  
  t_list = []
  for ch in t:
    if ch not in char_dict:
      return -1

    t_list.append(char_dict[ch].pop(0))
    if not char_dict[ch]:
      char_dict.pop(ch)

  return max(t_list) - min(t_list) + 1

def n_take_2(num):
  if num == 1:
    return 1
  return int((num * (num - 1)) / 2)

def numberOfWays(arr, k):
  # Write your code here
  count = 0
  num_dict = {}
  for i in range(len(arr)):
    if arr[i] not in num_dict:
      num_dict[arr[i]] = 0
    num_dict[arr[i]] += 1
  
  for key in num_dict.keys():
    if num_dict[key] > 0 and k - key in num_dict:
      count += n_take_2(num_dict[k - key])
    
      num_dict[key] -= 1
  
  return count

class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here
def reverse_helper(head, start, end):
  pre_start = head
  if start != head:
    while pre_start.next and pre_start.next != start:
      pre_start = pre_start.next
  
  prev, stop = end.next, end.next
  current = start
  while current and current != stop:
    tmp = current.next
    current.next = prev
    prev = current
    current = tmp
    
  if start == head:
    head = prev
  else:
    pre_start.next = prev
    
  return head
  

def reverse(head):
  # Write your code here
  node = head
  nd1, nd2 = None, None
   
  while node:
    if node.data % 2 == 0:
      if nd1 == None:
        nd1 = node 
    else:
      if nd1:
        nd2 = pre_node
        if nd1 != nd2:
          head = reverse_helper(head, nd1, nd2)
        nd1 = None
        nd2 = None
        
    pre_node = node
    node = node.next
    
  if nd1 and not nd2 and nd1 != pre_node:
    head = reverse_helper(head, nd1, pre_node)
  
  return head

def reverse_list(lst):
  new_lst = []
  for elem in reversed(lst):
    new_lst.append(elem)
  return new_lst

def generate_words(given_word):
  # by reversing all possible subwords
  words_lst = []
  for i in range(len(given_word)):
    for j in range(i+1, len(given_word)):
      w = list(given_word[i:j+1])
      for k in range(len(w)//2):
        w[k], w[len(w) - k - 1] = w[len(w) - k - 1], w[k]
      
      words_lst.append(given_word[0:i] + "".join(w) + given_word[j+1:])
  return words_lst

def minOperations(arr):
  # Write your code here
  goal_word = "".join([str(num) for num in sorted(arr)])
  curr_word = "".join([str(num) for num in arr])
  
  seen_words = set()
  queue = deque()
  queue.append((curr_word, 0))
  
  while queue:
    word, count = queue.popleft()
    if word == goal_word:
      return count
    lst_words = generate_words(word)
    for new_word in lst_words:
      if new_word not in seen_words:
        queue.append((new_word, count + 1))
        seen_words.add(new_word)

def reverse_list(lst):
  new_lst = []
  for elem in reversed(lst):
    new_lst.append(elem)
  return new_lst

def minOperations2(arr):
  # Not optimal
  count = 0
  ind1, ind2 = -1, -1
  i = 0
  while i < len(arr):
    if ind1 == -1 and arr[i] != i + 1:
      ind1 = i
    if ind1 != -1 and arr[i] == ind1 + 1:
      ind2 = i
    if ind1 != -1 and ind2 != -1:
      count += 1
      arr[:] = arr[:ind1] + reverse_list(arr[ind1:ind2 + 1]) + arr[ind2 + 1:]
      i = ind1
      ind1, ind2 = -1, -1
      
    i += 1
  
  return count

def search_kth_smallest(arr, k):
  if len(arr) == 0:
    return 
  if len(arr) == 1:
    return arr[0]
  if k > len(arr):
    return None
  
  i = 0
  p = randrange(len(arr))
  arr[i], arr[p] = arr[p], arr[i]
  for j in range(1, len(arr)):
    if arr[j] <= arr[0]:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i], arr[0] = arr[0], arr[i]
  if k - 1 == i:
    return arr[i]
  elif k - 1 < i:
    return search_kth_smallest(arr[:i], k)
  else:
    return search_kth_smallest(arr[i+1:], k - i - 1)

def findMinArray(arr, k):
  # Write your code here
  sorted_arr = sorted(arr)
  index_dict = {}
  for i in range(len(arr)):
    if arr[i] not in index_dict:
      index_dict[arr[i]] = i

  index = None
  for elem in sorted_arr:
    if index_dict[elem] <= k:
      index = index_dict[elem]
      break
     
  """
  index = None
  for j in range(1, len(arr) + 1):
    elem = search_kth_smallest(arr, j)
    if index_dict[elem] <= k:
      index = index_dict[elem]
      break
  """
  while index > 0:
    arr[index-1], arr[index] = arr[index], arr[index-1]
    index -= 1

  return arr

def minOverallAwkwardness(arr):
  # Write your code here
  new_arr = sorted(arr)
  left_lst = []
  right_lst = []
  for i in range(len(new_arr)):
    if i % 2:
      left_lst.append(new_arr[i])
    else:
      right_lst.append(new_arr[i])
  
  left_lst.reverse()
  new_arr[:] = left_lst + right_lst
  
  max_awk = -math.inf
  for i in range(1, len(new_arr)):
    awk_val = abs(new_arr[i] - new_arr[i-1])
    if awk_val > max_awk:
      max_awk = awk_val
    
    if i == len(new_arr) - 1 and abs(new_arr[i] - new_arr[0]) > max_awk:
      max_awk = abs(new_arr[i] - new_arr[0])
  
  return max_awk

def findPositions(arr, x):
  # Write your code here
  queue = deque()
  buffer = deque()
  output = [0] * x
  num_dict = {}
  
  for i in range(len(arr)):
    queue.append(arr[i])
    
    if arr[i] not in num_dict:
      num_dict[arr[i]] = deque()
    
    num_dict[arr[i]].append(i)
  
  iterations = x
  max_elem = None
  max_index = -1

  for i in range(x):
    
    while iterations and queue:
      
      elem = queue.popleft()
      
      if max_elem == None or elem > max_elem:
        max_elem = elem
        max_index = num_dict[elem][0]
      
      if elem > 0:
        
        index = num_dict[elem].popleft()
        if elem - 1 not in num_dict:
          num_dict[elem - 1] = deque()
         
        num_dict[elem - 1].append(index)
        
        if not num_dict[elem]:
          num_dict.pop(elem)

        elem -= 1
      
      buffer.append(elem)
      iterations -= 1
    
    if max_elem > 0:
      max_elem -= 1
    
    while buffer:
      item = buffer.popleft()
      if item == max_elem:
        num_dict[item].remove(max_index)
        if not num_dict[item]:
          num_dict.pop(item)

        output[i] = max_index + 1
        max_elem = None
        max_index = -1
      else:
        queue.append(item)
      
    iterations = x  
  
  return output

def getBillionUsersDay(growthRates):
  # Write your code here
  total = 0
  num_users = pow(10, 9)
  n = len(growthRates)
  p = [1] * n
  rates_array = np.array(growthRates)
  
  lowest_rate = min(growthRates)
  biggest_rate = max(growthRates)
  
  lower = math.floor(math.log(num_users/n)/math.log(biggest_rate))
  upper = math.ceil(math.log(num_users/n)/math.log(lowest_rate))

  while upper - lower > 1:
    middle = lower + math.ceil((upper - lower)/2)
    p_array = np.array(p)
    for _ in range(middle):
      p_array = np.multiply(p_array, rates_array)
      
    total = np.sum(p_array)
    
    if total == num_users:
      return middle
    elif total > num_users:
      upper = middle
    else:
      lower = middle

  if total < num_users:
    return middle + 1

  return middle

def countDistinctTriangles(arr):
  # Write your code here
  tr_set = set()
  for tr in arr:
    tr_set.add(tuple(sorted(tr)))
  
  return len(tr_set)

def canGetExactChange(targetMoney, denominations):
  # Write your code here
  def helper(money, coins):
    if money == 0:
      return 0
    output = []

    for i in range(len(coins)):
      if money >= coins[i]:
        out = helper(money - ((money//coins[i]) * coins[i]), coins[:i] + coins[i+1:])
        output.append(out)
      else:
        output.append(money)
    return min(output)
  return helper(targetMoney, denominations) == 0

def findEncryptedWord(s):
  # Write your code here
  def helper(string):
    n = len(string)
    if n == 0:
      return []
    if n == 1:
      return [string]
    
    return [string[(n - 1)//2]] + helper(string[:(n - 1)//2]) + helper(string[((n - 1)//2) + 1:]) 
  
  output = helper(s)
  return "".join(output)

class Node2: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

def count_of_nodes(root, queries, s):
  # Write your code here
  char_dict = {}
  for i in range(len(s)):
    if s[i] not in char_dict:
      char_dict[s[i]] = deque()
    char_dict[s[i]].append(i+1)
  
  queue = deque()
  output = []
  
  for query in queries:
    count = 0
    u, c = query
    queue.append(root)
    
    while queue:
      node = queue.popleft()
      if node.val == u:
        count += 1
        if queue:
          queue.clear()
        queue.extend(node.children)
        break
        
      queue.extend(node.children)
      
    while queue:
      node = queue.popleft()
      if node.val in char_dict[c]:
        count += 1
        
      queue.extend(node.children)
      
    output.append(count)
    
  return output

if __name__ == "__main__":
    #print(rotationalCipher("Zebra-493", 3))
    #print(findSignatureCounts([1,3,4,2,5]))
    #print(min_length_substring("bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf", "cbccfafebccdccebdd"))
    #print(numberOfWays([1,2,3,4,3], 6))
    """
    node = Node(2)
    node.next = Node(18)
    node.next.next = Node(24)
    node.next.next.next = Node(3)
    node.next.next.next.next = Node(5)
    node.next.next.next.next.next = Node(7)
    node.next.next.next.next.next.next = Node(9)
    node.next.next.next.next.next.next.next = Node(6)
    node.next.next.next.next.next.next.next.next = Node(12)
    reverse(node)
    """
    #print(minOperations([1,2,3,4,5]))
    #print(search_kth_smallest([8,9,11,2,1], 4))
    #print(findMinArray([8,9,11,2,1], 3))
    #print(minOverallAwkwardness([5, 10, 6, 8]))
    #print(findPositions([2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4], 4))
    #print(getBillionUsersDay([1.01, 1.02]))
    #print(countDistinctTriangles([(7, 6, 5), (5, 7, 6), (8, 2, 9), (2, 3, 4), (2, 4, 3)]))
    #print(canGetExactChange(75, [4,17,29]))
    #print(findEncryptedWord("facebook"))
    root_2 = Node2(1)
    root_2.children.append(Node2(2))
    root_2.children.append(Node2(3))
    root_2.children.append(Node2(7))
    root_2.children[0].children.append(Node2(4))
    root_2.children[0].children.append(Node2(5))
    root_2.children[1].children.append(Node2(6))
    print(count_of_nodes(root_2, [(1, 'a'), (2, 'b'), (3, 'a')], 'abaacab'))
    
