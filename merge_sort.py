def mergeLists(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result += left
    if right:
        result += right
    
    return result


def mergeSort(mlist):
    if len(mlist) <= 1:
        return mlist
    
    mid = len(mlist) // 2
    left, right = mlist[:mid], mlist[mid:]
    left = mergeSort(left)
    right = mergeSort(right)

    return mergeLists(left, right)


testlst = [1,9,3,7,4,5,8,0,6]
print(mergeSort(testlst))