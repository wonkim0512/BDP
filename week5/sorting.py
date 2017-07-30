# 170712 sorting algorithm
import random
import time
import math

# selection sort
def SelectionSort(alist):
    for bottom in range(len(alist)):
        mp = bottom
        for idx in range(bottom + 1, len(alist)):
            if alist[idx] < alist[mp]:
                mp = idx
        alist[bottom], alist[mp] = alist[mp], alist[bottom]

    return alist

# insertion sort
def InsertionSort(alist):
    for i in range(1, len(alist)):
        j = i
        while j > 0 and alist[j-1] > alist[j]:
            alist[j-1], alist[j] = alist[j], alist[j-1]
            j -= 1

    return alist

# bubble sort
def BubbleSort(alist):
    for i in range(len(alist)):
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]

    return alist

# merge sort
def merge(lst1, lst2):
    if lst1 == []:
        return lst2

    if lst2 == []:
        return lst1

    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)

    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

'''
def merge(lst1, lst2):
    idx1, idx2 = 0, 0
    lst = []
    while idx1 < len(lst1) and idx2 < len(lst2):
        if lst1[idx1] <= lst2[idx2]:
            lst.append(lst1[idx1])
            idx1 += 1

        else:
            lst.append(lst2[idx2])
            idx2 += 1

    lst.extend(lst1[idx1:] or lst2[idx2:])
    return lst
'''
def MergeSort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst[:]

    half = len(lst) // 2
    lst1 = lst[:half]
    lst2 = lst[half:]
    newlst1 = MergeSort(lst1)
    newlst2 = MergeSort(lst2)
    newlst = merge(newlst1, newlst2)
    return newlst

'''
# quick sort - my first code
def QuickSort(lst, count = 0):
    if len(lst) > 1:
        pivot_idx = len(lst) // 2
        smaller_nums, larger_nums = [], []

        for idx, num in enumerate(lst):

            if idx != pivot_idx:
                if num < lst[pivot_idx]:
                    smaller_nums.append(num)

                else:
                    larger_nums.append(num)

        count = QuickSort(smaller_nums, count + 1)[1]
        count = QuickSort(larger_nums, count + 1)[1]
        lst[:] = smaller_nums + [lst[pivot_idx]] + larger_nums

    return lst, count

print(QuickSort([1,6,5,2,3,2,76,45,65,4,2,3,1])[0])
print(QuickSort([1,6,5,2,3,2,76,45,65,4,2,3,1])[1])
'''

'''Your post is mistaken on several points:

Big-O ignores constant factors and "small" values of n, where the definition of small can be arbitrarily large. So your math is meaningless.
Your counts are wrong. There's one comparison per loop iteration. You're counting something else.
This is a strange way to count. Just use a global variable.
Try this. Note really you're using twice as many comparisons as this reports. The check that the loop index isn't the pivot could be eliminated with a smarter implementation.
'''
#revised code
count = 0
def QuickSort(lst):
    if len(lst) <= 1:
        return lst
    pivot_idx = len(lst) // 2
    smaller, larger = [], []
    for idx, num in enumerate(lst):
        if idx != pivot_idx:
            global count
            count += 1
            (larger, smaller)[num < lst[pivot_idx]].append(num)
    return QuickSort(smaller) + [lst[pivot_idx]] + QuickSort(larger)

def Run(n):
    lst = [random.randint(0,1000) for r in range(n)]
    QuickSort(lst)
    return count


# time check
def TimeChecker(lst):
    print("Comparison of sorting algorithm with ", len(lst),"elements' list.")
    # 1. sorted
    print("sorted()")
    startTime = time.clock()
    sorted(lst)
    endTime = time.clock()
    elapsedTime = endTime - startTime
    print("The elapesed time for sorted() is", elapsedTime)
    print("*"*20)

    # 2.selection sort
    print("selection sort")
    startTime = time.clock()
    SelectionSort(lst)
    endTime = time.clock()
    elapsedTime = endTime - startTime
    print("The elapesed time for selection sort is", elapsedTime)
    print("*"*20)

    # 3. insertion sort
    print("insertion sort")
    startTime = time.clock()
    InsertionSort(lst)
    endTime = time.clock()
    elapsedTime = endTime - startTime
    print("The elapesed time for insertion sort is", elapsedTime)
    print("*"*20)

    # 4. bubble sort
    print("bubble sort")
    startTime = time.clock()
    BubbleSort(lst)
    endTime = time.clock()
    elapsedTime = endTime - startTime
    print("The elapesed time for bubble sort is", elapsedTime)
    print("*"*20)

    # 5.merge sort
    print("merge sort")
    startTime = time.clock()
    MergeSort(lst)
    endTime = time.clock()
    elapsedTime = endTime - startTime
    print("The elapesed time for merge sort is", elapsedTime)
    print("*"*20)

    # 6. quick sort
    print("quick sort")
    startTime = time.clock()
    QuickSort(lst)
    endTime = time.clock()
    elapsedTime = endTime - startTime
    print("The elapesed time for quick sort is", elapsedTime)
    print("*"*80)


random_100 = [random.randint(-1000, 1000) for i in range(100)]
random_500 = [random.randint(-1000, 1000) for i in range(500)]
random_1000 = [random.randint(-1000, 1000) for i in range(1000)]

TimeChecker(random_100)
TimeChecker(random_500)
TimeChecker(random_1000)

# Comparison Operation times

for alist in [random_100, random_500, random_1000]:
    #print(len(alist)*math.log(len(alist)))
    print("Quick sort operates comparison",Run(len(alist)),
    "times with", len(alist),"elements")


'''
# search
# binary search # try again!
def binarySearch(lst, target):
    lst.sort()
    half = len(lst)//2
    if target == lst[half]:
        return half

    if target < lst[half]:
        return binarySearch(lst[:half], target)

    else:
        return binarySearch(lst[half:], target)

print(binarySearch([1,4,6,2,3,7,8,9,23,32,12], 4))

# binary tree
'''
