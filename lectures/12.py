nums = [7,42,6,3,15,12,43,23,11]

# selection sort
def ssort(nums):
    for bottom in range(len(nums)-1):
        the = bottom
        for idx in range(bottom + 1, len(nums)):
            if nums[the] > nums[idx]:
                the = idx
        nums[bottom], nums[the] = nums[the], nums[bottom]
    return nums


#merge sort
def merge(lst1, lst2):
    if lst1 == []:
        return lst2

    if lst2 == []:
        return lst1

    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)

    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

def msort(nums):
    if len(nums) <2:
        return nums[:]

    mid = len(nums) // 2
    lst1 = nums[:mid]
    lst2 = nums[mid:]
    newlst1 = msort(lst1)
    newlst2 = msort(lst2)
    newlst = merge(newlst1, newlst2)
    return newlst

# bubble sort
def bsort(nums): # fill from the right
    for i in range(len(nums)):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# inerstion sort
def isort(nums):
    for i in range(1, len(nums)):
        for j in range(len(nums)):
            while j > 0 and  nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
    return nums

# quick sort
def qsort(nums):
    if len(nums) < 2:
        return nums[:]

    pivot_idx = len(nums) // 2
    smaller, larger = [], []

    for idx, value in enumerate(nums):
        if idx != pivot_idx:
            if value < nums[pivot_idx]:
                smaller.append(value)

            else:
                larger.append(value)

    qsort(smaller)
    qsort(larger)
    return smaller + [nums[pivot_idx]] + larger #list(3) -> 'int' is not iterable

print(ssort(nums))
print(msort(nums))
print(bsort(nums))
print(isort(nums))
print(qsort(nums))
