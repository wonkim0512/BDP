def first_perfect_square(alist):
    for idx, val in enumerate(alist):
        if val == 0:
            return idx
        elif val ** (1/2) - int(val**(1/2)) == 0:
            return idx
    return -1

print(first_perfect_square(list(range(5))))
print(first_perfect_square([2,4,6,8,10,12]))
print(first_perfect_square([6,8,10,12,9]))
print(first_perfect_square([1,1]))
print(first_perfect_square([42]))
print(first_perfect_square([]))
print("*"*20)

def num_perfect_squares(nums):
    count = 0
    for num in nums:
        if (num == 0) or (num**(1/2) - int(num**(1/2)) == 0):
            count += 1
    return count

print(num_perfect_squares([]))
print(num_perfect_squares([0]))
print(num_perfect_squares([0,1]))
print(num_perfect_squares(list(range(10))))
print(num_perfect_squares([3]*10))
print("*"*20)


# it does not work for string case.
'''
def second_largest_best(nums):
    the = second = float('-inf')
    count = 0
    for num in nums:
        count += 1
        if num > second:
            if num >= the:
                the, second = num, the
            else:
                second = num
    return second if count>=2 else None

print(second_largest_best([20,67,3,2.6,7,74,2.8,90.8,52.8,4,3,2,5,7]))
print(second_largest_best([10,7,10]))
print("*"*20)
'''

'''
def second_largest(nums):
    the, sec = 0, 0
    if nums[0] > nums[1]:
        the, sec = nums[0], nums[1]
    else:
        the, sec = nums[1], nums[0]

    for num in nums:
        if num > sec:
            if num >= the:
                the, sec = num, the
            else:
                sec = num
    return sec
'''

def second_largest(nums):
    it = iter(nums)
    sec, the = sorted((next(it), next(it)))

    for num in it:
        if num > sec:
            if num >= the:
                the, sec = num, the
            else:
                sec = num

    return sec

print(second_largest([3,-2,10,-1,5]))
print(second_largest([-2,1,1,-3,5]))
print(second_largest([1,2,3,3]))
print(second_largest(['alpha', 'gamma','beta','delta']))
print("*"*20)
