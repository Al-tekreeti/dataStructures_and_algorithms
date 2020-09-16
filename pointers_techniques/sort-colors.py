def sortColors(clrs):
    eq = 0
    smaller = 0
    greater = len(clrs) - 1
    while eq <= greater:
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
