def sortColors(clrs):
    """ 
        Sort a list of colors. Each color can appears more than once. The colors are encoded using integer numbers to show the required order. For example, red=0, blue=1, and green=2. This is an instance of Dutch national flag problem as defined by Dijkstra.

        Arguments: 
        clrs -- an array of non-negative integer numbers.

        Returns:
        a sorted array.
    """
    # for 3 colors encoded as 0, 1, and 2, we define 3 indices
    eq = 0 # index for color 1
    smaller = 0 # index for color 0
    greater = len(clrs) - 1 # index for color 2

    # if clrs is empty, the condition of the while loop does not hold and the same array is returned
    while eq <= greater:
        if clrs[eq] < 0 or clrs[smaller] < 0 or clrs[greater] < 0:
            print("negative values are not acceptable!")
            return -1

        if clrs[eq] > 2 or clrs[smaller] > 2 or clrs[greater] > 2:
            print("Only 0, 1, and 2 values are acceptable!")
            return -1

        if clrs[eq] == 0:
            temp = clrs[eq]
            clrs[eq] = clrs[smaller]
            clrs[smaller] = temp
            eq += 1
            smaller += 1
        elif clrs[eq] == 2:
            temp = clrs[eq]
            clrs[eq] = clrs[greater]
            clrs[greater] = temp
            greater -= 1
        else:
            eq += 1
    return clrs

if __name__ == "__main__":
    a = [2,2,1,1,0,0,0,0,0,0,0]
    print(f"The sorted array is {sortColors(a)}")
