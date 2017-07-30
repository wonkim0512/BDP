# 1
def count_matches(alist, value):
    if alist == []:
        return 0
    if alist[0] == value:
        return 1 + count_matches(alist[1:], value)
    else:
        return count_matches(alist[1:], value)

print(count_matches([0,1,0,4,2,0], 0))
print(count_matches(['a','b','c'], 1))
print(count_matches([], "a"))
print("*"*20)

def count_matches(some_list, value): # TA's code
    if len(some_list) < 2:
        if len(some_list) == 0:
            return 0

        elif some_list[0] == value:
            return 1

        else:
            return 0

    return count_matches([some_list[0]], value) + count_matches(some_list[1:],value)

print(count_matches([0,1,0,4,2,0], 0))
print(count_matches(['a','b','c'], 1))
print(count_matches([], "a"))
print("*"*20)


# 2
def double_each(nums):
    alist = []
    if nums == []:
        return []
    else:
        return [nums[0]]*2 + double_each(nums[1:])

print(double_each([1,2,3]))
print(double_each([]))
print("*"*20)

def double_each(some_list): # TA's code
    if len(some_list) == 0:
        return []
    else:
        return [some_list[0]*2 + double_each(some_list[1:])]

# 3
def sums_to(nums, k):
    if not nums:
        return k == 0
    return sums_to(nums[1:], k - nums[0])

print(sums_to([1,2,3], 6))
print(sums_to([1,2,3], 5))
print(sums_to([],1))
print("*"*20)

# my pool code
def sums_to(nums, k):
    if nums == []:
        return False

    if nums[0] + sums_to(nums[1:], k) == k:
        return True

'''
def sums_to(nums , n):
  if len(nums) == 0:
    return n == 0
  else:
    m = nums[0]
    nums.pop(0)
    return sums_to(nums, (n-m))

print(sums_to([2,3], 5))
'''

# 4
def is_reverse(str1, str2):
    if str1 == "" and str2 == "":
        return True

    if  str1 and str2: # important!
        if str1[0] == str2[-1]:
            return is_reverse(str1[1:], str2[:-1])
    return False

print(is_reverse("abc", "cba"))
print(is_reverse("abc", "abc"))
print(is_reverse("abc", "dcba"))
print(is_reverse("abc", "bc"))
print(is_reverse("", ""))
print(is_reverse("abcd", "dcba"))
print("*"*20)

def is_reverse(str1, str2): # TA's code
    if len(str1) != len(str2):
        return False
    if len(str1) == 0  and len(str2) == 0:
        return True
    if str1[0] == str2[-1]:
        return is_reverse(str1[1:], str2[:-1])
    else:
        return False

print(is_reverse("abc", "cba"))
print(is_reverse("abc", "abc"))
print(is_reverse("abc", "dcba"))
print(is_reverse("abc", "bc"))
print(is_reverse("", ""))
print(is_reverse("abcd", "dcba"))
print("*"*20)

# 5
def sort_repeated(nums):
    dict1 = {}
    for num in nums:
        if num in dict1:
            dict1[num] += 1

        else:
            dict1[num] = 1

    keys_larger = [key for key in dict1.keys() if dict1[key]>1]
    return sorted(keys_larger)

print(sort_repeated([1,2,3,2,1]))
print(sort_repeated([1,2,3,2,2,4]))
print(sort_repeated(list(range(100))))
print("*"*20)

def repeats(L): # TA's code
    seen = set()
    seenAgain = set()
    for element in L:
        if element in seen:
            seenAgain.add(element)
        seen.add(element)
    return sorted(seenAgain) # 'sorted' transforms dict to list automatically.

print(repeats([1,2,3,2,1]))
print(repeats([1,2,3,2,2,4]))
print(repeats(list(range(100))))
print("*"*20)

# 6
# using no get().
def make_Dict_number(alist):
    adict = {}
    for key in set(alist):
        adict[key] = alist.count(key)
    return adict

'''
def make_Dict_number(alist): # TA's code
    counts = {}
    for item in alist:
        counts[item] = counts[item] + 1 if item in counts else 1
    return counts
'''

def mostFrequent(alist):
    adict = make_Dict_number(alist)
    max_value = max(adict.values())
    for key, value in adict.items():
        if value == max_value:
            print(key, end = " ")
    print()

nums = [2,5,3,4,6,4,2,4,6,2]
print(make_Dict_number(nums))
mostFrequent(nums)
print("*"*20)

# using get()
def make_Dict_number(alist):
    counts = {}
    for item in alist:
        counts[item] = counts.get(item, 0) + 1 # default is set as 0.

    return counts

def mostFrequent(alist):
    max_value = None
    max_count = 0
    counts = dict()
    for element in alist:
        count = 1 + counts.get(element, 0)
        counts[element] = count

        if count > max_count:
            max_count = count
            max_value = element
    return max_value

nums = [2,5,3,4,6,4,2,4,6,2]
print(make_Dict_number(nums))
mostFrequent(nums)
print("*"*20)

# 7
def histogram(adict):
    if adict == {}:
        return None

    dict1 = {}
    for letter in set(adict.values()):
        dict1[letter] = list(adict.values()).count(letter)

    return dict1

letters = {1:"a", 2:"b", 3:"c", 4:"a", 5:"b", 6:"a"}
print(histogram(letters))
print("*"*20)

def histogram(letters):
    ans = {}
    valueLst = list(letters.values())
    for i in range(0, len(letters)):
        ans[valueLst[i]] = valueLst.count(valueLst[i])
    return ans

letters = {1:"a", 2:"b", 3:"c", 4:"a", 5:"b", 6:"a"}
print(histogram(letters))
print("*"*20)
