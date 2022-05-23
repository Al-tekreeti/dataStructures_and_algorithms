def sherlockAndAnagrams(s):
    # Write your code here
    count = 0
    for w in range(1,len(s)):
        for i in range(0, len(s)):
            d = {}
            if i+w > len(s):
                break
            
            s1 = s[i:i+w]
            for k in range(len(s1)):
                if s1[k] not in d:
                    d[s1[k]] = 0
                d[s1[k]] += 1

            for j in range(i+1, len(s)):
                if j+w > len(s):
                    break
                if is_anagram(dict(d), s[j:j+w]):
                    count += 1
    return count

def sherlockAndAnagrams2(s):
    # Write your code here
    count = 0
    lsubs = generate_substrings(s)
    for i in range(len(lsubs)):
        d = create_dict(lsubs[i])
        for j in range(i+1, len(lsubs)):
            if len(lsubs[i]) != len(lsubs[j]):
                break
            if is_anagram(dict(d), lsubs[j]):
                count += 1
    return count

def is_anagram2(s1, s2):
    d = {}
    for k in range(len(s1)):
        if s1[k] not in d:
            d[s1[k]] = 0
        d[s1[k]] += 1
    
    for j in range(len(s2)):
        if s2[j] not in d or d[s2[j]] == 0:
            return False
        d[s2[j]] -= 1
    return True

def is_anagram(d, s2):
    for j in range(len(s2)):
        if s2[j] not in d or d[s2[j]] == 0:
            return False
        d[s2[j]] -= 1
    return True

def generate_substrings(s):
    subs = []
    for w in range(1, len(s)):
        for i in range(len(s)):
            if i+w > len(s):
                break
            subs.append(s[i:i+w])
    return subs

def create_dict(s):
    d = {}
    for k in range(len(s)):
        if s[k] not in d:
            d[s[k]] = 0
        d[s[k]] += 1
    return d

def surfaceArea(A):
    # Pad the grid width a layer of 0
    # for easier calculation
    a = [[0] * (len(A[0]) + 2)]
    for row in A:
        a.append([0] + row + [0])
    a.append([0] * (len(A[0]) + 2))
    
    # Bottom and top area
    ans = len(A) * len(A[0]) * 2
    
    # Side area is just the sum of differences
    # between adjacent cells. Be careful not to
    # count a side twice.
    for i in range(1, len(a)):
        for j in range(1, len(a[i])):
            ans += abs(a[i][j] - a[i-1][j])
            ans += abs(a[i][j] - a[i][j-1])
    return ans

def surfaceArea2(A):
    """
    The 4 side faces are evaluated by evaluating the max of each row and of each column. The top and down faces are straight forward. The tricky part is how to evaluate the hidden faces.
    """
    # evaluate the base and top faces
    total = len(A) * len(A[0]) * 2
    # evaluate 2 of the side faces
    for row in A:
        total += max(row) * 2
    # evaluate the other 2 side faces and hidden ones
    for c in range(len(A[0])):
        pos = neg = None
        for r in range(len(A)):
            if r > 0 and r < len(A):
                if A[r-1][c] - A[r][c] > 0:
                    pos = A[r-1][c] - A[r][c]
                if A[r-1][c] - A[r][c] < 0 and pos != None:
                    total += min(pos, A[r][c] - A[r-1][c]) * 2

    col_max = A[0]
    for r in range(len(A)):
        pos = neg = None
        for c in range(len(A[0])):
            if A[r][c] > col_max[c]:
                col_max[c] = A[r][c]
            if c > 0 and c < len(A[0]):
                if A[r][c-1] - A[r][c] > 0:
                    pos = A[r][c-1] - A[r][c]
                if A[r][c-1] - A[r][c] < 0 and pos != None:
                    total += min(pos, A[r][c] - A[r][c-1]) * 2

    return total + sum(col_max) * 2

def surfaceArea3(A):
    total = 0
    for r in range(len(A)):
        for c in range(len(A[0])):
            if A[r][c] == 0:
                continue
            total += 4 * A[r][c] + 2
            if r > 0:
                total -= min(A[r-1][c], A[r][c])
            if r < len(A) - 1:
                total -= min(A[r][c], A[r+1][c])
            if c > 0:
                total -= min(A[r][c], A[r][c-1])
            if c < len(A[0]) - 1:
                total -= min(A[r][c], A[r][c+1])
    return total

def matrixRotation2(matrix, t=1):
    n = len(matrix)
    m = len(matrix[0])
    for l in range(min(n//2, m//2)):
        tmp = []

        r = c = l
        count = 0
        while (n - 2*l - 1) * 2 + (m - 2*l - 1) * 2 > count:
            tmp.append(matrix[r][c])
            r, c = linearize(n, m, l, r, c)
            count += 1

        reverse(tmp, 0, len(tmp)-1)
        reverse(tmp, 0, len(tmp) - (t % len(tmp)) - 1)
        reverse(tmp, len(tmp) - (t % len(tmp)), len(tmp) - 1)

        r = c = l
        for item in tmp:
            matrix[r][c] = item
            r, c = linearize(n, m, l, r, c)
    return matrix
    

def linearize(n, m, l, r, c):
    if c < m - l - 1 and r == l:
        c += 1
    elif c == m - l - 1 and r < n - l - 1:
        r += 1
    elif r == n - l - 1 and c > l:
        c -= 1
    elif c == l and r > l:
        r -= 1

    return r, c

def reverse(arr, i, k):
    while i < k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1

def matrixRotation(matrix,r):
    m, n = len(matrix), len(matrix[0])
    b = [[None]*n for _ in range(m)]
    indices = []

    for c in range(min(m,n)//2):
        index = []
        for i in range(c,n-c): index.append((c,i))
        for i in range(c+1,m-1-c): index.append((i,n-1-c))
        for i in range(c,n-c)[::-1]: index.append((m-1-c,i))
        for i in range(1+c,m-1-c)[::-1]: index.append((i,c))
        if not index:
            break
        indices.append(index)

    rotated = []
    for index in indices:
        k = r%len(index)
        rotated.append(index[k:]+index[:k])

    for (x,y) in zip(indices,rotated):
        for ((c,d),(e,f)) in zip(x,y):
            b[c][d] = matrix[e][f]

    return b

def maximizingXor(l, r):
    # Write your code here
    expected_num = l ^ r
    factor = 1
    while True:
        if expected_num & factor == 0:
            if (l ^ factor >= l and l ^ factor <= r) or \
               (r ^ factor >= l and r ^ factor <= r):
                expected_num |= factor
            
        factor = factor << 1
        if factor > r:
            return expected_num

if __name__ == "__main__":
    #print(sherlockAndAnagrams2("kkkk"))
    #print(generate_substrings("cdcd"))
    #print(surfaceArea3([[1,1,1],[1,0,1],[1,1,1]]))
    #print(matrixRotation([[1,2,3,4,5,6],[7,8,9,12,11,12]],5))
    #print(reverse([1,2,3,4,5,6,7,8], 0, 4))
    print(maximizingXor(10, 15))