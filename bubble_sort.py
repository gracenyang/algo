import random


def randomlist(n):
    """returns a list of n random integers in range [0, 1000) """
    nList = []
    for i in range(n):
        nList.append(random.randrange(1000))
    return nList


def bubble_sort(myList):

    if len(myList) <= 1:
        return myList

    for j in range(len(myList)-1, 0, -1):
        exchange = False
        for i in range(j):
            if myList[i] > myList[i+1]:
                myList[i], myList[i+1] = myList[i+1], myList[i]
                exchange = True
        print(myList)
        if not exchange:
            return myList

    return myList


lst = randomlist(15)
customized_lst = [9,1,2,3,4,5]
bubble_sort(customized_lst)


