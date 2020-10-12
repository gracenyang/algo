# not using python built-in functions
# Time: O(n^2)
def selection_sort(mlist):
    if len(mlist) <= 1:
        return mlist
    for i in range(len(mlist)-1):
        min_idx = i
        for j in range(i+1, len(mlist)):
            if mlist[min_idx] > mlist[j]:
                min_idx = j
        if i != min_idx:
            mlist[i], mlist[min_idx] = mlist[min_idx], mlist[i]
    return mlist


 # using python built-in functions
 # Time: O(n)
def selection_sort_2(mlist):
    if len(mlist) <= 1:
         return mlist
    
    for i in range(len(mlist)-1):
        if mlist[i] != min(mlist[i:]):
            min_idx = mlist.index(min(mlist[i:]))
            mlist[i], mlist[min_idx] = mlist[min_idx], mlist[i]
    return mlist



testlist = [7, 3, 1, 5, 9, 4]
print(selection_sort_2(testlist))
