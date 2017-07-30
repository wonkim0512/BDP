import math

# 1
def f1(nums):
    import math
    if not nums:
        return -1

    for idx, num in enumerate(nums):
        if num ** (1/2) - int(num ** (1/2)) == 0:
            return idx
    return -1

print(f1([2,4,6,8,10]))

# 2
def f2(nums):
    count = 0
    for num in nums:
        if num < 0:
            continue

        if num ** (1/2) - int(num ** (1/2)) == 0:
            count += 1

    return count

print(f2([-4,-2,0,2,4]))

# 3
def f3(nums):
    it = iter(nums)
    the, second = sorted((next(it), next(it)), reverse = True)

    for num in it:
        if num > second:
            if num >= the:
                the, second = num, the

            else:
                second = num

    return second

print(f3([3,-2,10,-1,5]))
print(f3(['alpha', 'gamma', 'beta', 'delta']))
print(f3([3.1, 3.1]))

# 4 French numbers
