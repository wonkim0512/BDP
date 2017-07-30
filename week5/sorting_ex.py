def _partition(mylist, start, end):
    count = 0
    pos = start
    for i in range(start, end):
        count += 1
        if mylist[i] < mylist[end]:
            mylist[i], mylist[pos] = mylist[pos], mylist[i]
            pos += 1
    mylist[pos], mylist[end] = mylist[end], mylist[pos]
    return pos, count

def _quicksort(mylist, start, end):
    count = 0
    if start < end:
        pos, count = _partition(mylist, start, end)
        count += _quicksort(mylist, start, pos - 1)
        count += _quicksort(mylist, pos + 1, end)
    return count

def quicksort(mylist, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(mylist) - 1
    return _quicksort(mylist, start, end)


import random
import math
random_100 = [random.randint(-100, 100) for i in range(100)]
count = quicksort(random_100)
print(random_100, count)
print(math.log(100) * 100)
