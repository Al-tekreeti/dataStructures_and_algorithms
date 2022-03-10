from math import ceil, fmod, sqrt
def isValidSudoku(board):
    N = len(board)
    
    for r in range(N):
        row_table = 0
        for c in range(N):
            if board[r][c] == '.':
                continue
            if row_table & (1 << int(board[r][c])):
                return False
            else:
                row_table |= 1 << int(board[r][c])
    
    for c in range(N):
        column_table = 0
        for r in range(N):
            if board[r][c] == '.':
                continue
            if column_table & (1 << int(board[r][c])):
                return False
            else:
                column_table |= 1 << int(board[r][c])
    
    for s in range(N):
        square_table = 0
        for r in range(3*(s//3), 3*(s//3) + 3):
            for c in range(3*(s%3), 3*(s%3) + 3):
                if board[r][c] == '.':
                    continue
                if square_table & (1 << int(board[r][c])):
                    return False
                else:
                    square_table |= 1 << int(board[r][c])
    
    return True

def reverse(x: int) -> int:
        
    max_limit = pow(2, 31) - 1
    min_limit = -pow(2, 31)
    rev_x = 0
    while x != 0:
        if rev_x < min_limit / 10 or rev_x > max_limit / 10:
            return 0
        rev_x *= 10
        if rev_x < min_limit - x % 10 or rev_x > max_limit - x % 10:
            return 0
        rev_x += int(fmod(x, 10))
        x = ceil(x/10) if x < 0 else x//10
    
    return rev_x

def countPrimes(n):
    # recursive with no memorization (time exceede)
    if n <= 2:
        return 0
    
    def isPrime(k):
        for p in range(2, int(sqrt(k)) + 1):
            if k % p == 0:
                return 0
        return 1
        
    
    return countPrimes(n-1) + isPrime(n-1)

def isValid(s: str) -> bool:
    lst = [s[i] for i in range(len(s))]
    
    def helper(lst, pref):
        if len(lst) == 0 and len(pref) == 0:
            return True
        if len(lst) == 0 and len(pref) != 0:
            return False
        if lst[0] in [')', ']', '}']:
            if len(pref) == 0:
                return False
            if pref[-1] == '(' and lst[0] != ")" or pref[-1] == '[' and lst[0] != "]" or pref[-1] == '{' and lst[0] != "}":
                return False 
            return helper(lst[1:], pref[:len(pref)-1])
        else:
            return helper(lst[1:], pref[:len(pref)] + [lst[0]])
    
    return helper(lst, [])

if __name__ == "__main__":
    
    """
    board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]
    print(isValidSudoku(board))
    """
    #print(reverse(123))
    #print(countPrimes(10))
    print(isValid("{[]}"))
    