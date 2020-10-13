def insertion_sort(mlist):
    if len(mlist) <= 1:
        return mlist

    for right in range(1, len(mlist)):
        target = mlist[right]
        for left in range(right):
            if mlist[left] >= target:
                mlist[left+1:right+1] = mlist[left:right]
                mlist[left] = target
                break
    return mlist


testlst = [7,2,4,3,9,6,6]
print(insertion_sort(testlst))
