# 1
def f1(nums, target):
    if nums == []:
        return 0

    if nums[0] == target:
        return 1 + f1(nums[1:], target)

    else:
        return f1(nums[1:], target)

print(f1([0,1,0,4,2,0], 0))

# 2
def f2(nums):
    if nums == []:
        return []

    return [nums[0]] * 2 + f2(nums[1:])


print(f2([1,2,3]))

# 3
def f3(nums, k):
    if not nums:
        return k == 0
    return f3(nums[1:], k - nums[0])

print(f3([1,2,3], 6))
print(f3([1,2,3], 5))

# 4
def f4(str1, str2):
    if str1 == "" and str2 == "":
        return True

    if str1 and str2: # it is important
        if str1[0] == str2[-1]:
            return f4(str1[1:], str2[:-1])

    return False

print(f4("abc","cba"))
print(f4("abc","abc"))
print(f4("abc","dcba"))
print(f4("abc","cb"))
print(f4("",""))

# 5
def f5(nums):
    unique = list(set(nums))
    for num in unique:
        nums.remove(num)

    return sorted(list(set(nums)))


print(f5([1,2,3,2,1]))
print(f5([1,2,3,2,2,4]))


def f5(nums):
    count = dict()
    if nums != []:
        for num in nums:
            if num in count:
                count[num] += 1

            else:
                count[num] = 1
        return sorted([num for num in count if count[num]>1])
    return []

print(f5([1,2,3,2,1]))
print(f5([1,2,3,2,2,4]))
print(f5([]))

def f5(nums):
    from collections import Counter
    cntr = Counter(nums)
    #print(cntr)
    return sorted([key for key in cntr.keys() if cntr[key] > 1])


print(f5([1,2,3,2,1]))
print(f5([1,2,3,2,2,4]))
print(f5([]))

def f5(nums):
    seen = set()
    seenAgain = set()
    for num in nums:
        if num in seen:
            seenAgain.add(num)
        seen.add(num)
    return sorted(seenAgain)

print(f5([1,2,3,2,1]))
print(f5([1,2,3,2,2,4]))
print(f5([]))

# 6
def f6(nums):
    count = {}
    for num in set(nums):
        count[num] = nums.count(num)
    return count

print(f6([2,5,3,4,6,4,2,4,5]))

def f6(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    return count

def f6_1(nums):
    count_dict = f6(nums)
    maxValue_key = 0
    maxValue = list(count_dict.values())[0] # temporary
    for key, value in count_dict.items():
        if maxValue < value:
            maxValue = value
            maxValue_key = key
    return maxValue_key

print(f6_1([2,5,3,4,6,4,2,4,5]))

# 7
def f7(nums_dict):
    result = {}
    valueLst = list(nums_dict.values())
    for value in list(set(valueLst)):
        result[value] = valueLst.count(value)

    return result

letters = {1: 'a', 2: 'b', 3: 'a'}
print(f7(letters))
