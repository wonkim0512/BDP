def f1(nums):
    count = 0
    for num in nums:
        if num % 2 != 0:
            count += 1
    return count

print(f1([1,2,3,4]))
print(f1([1,2,3,4,5]))


def f1(nums):
    #return list(map(lambda num:num % 2 != 0, nums))
    return len(list(filter(lambda num:num % 2 != 0, nums)))

print(f1([1,2,3,4]))
print(f1([1,2,3,4,5]))
print("*"*20)

def f2(nums):
    print(*list(filter(lambda num:num%2!=0, nums)),sep = "\n")

f2([1,2,3,4])
a = ['a','b','c','d']
print(*a, sep = " ")
print("*"*20)

def f3(nums):
    if not nums:
        return 0

    if nums[0] % 2 != 0:
        return nums[0] + f3(nums[1:])

    else:
        return f3(nums[1:])

print(f3([1,2,3,4]))
print(f3([1,2,3,4,5]))

def f3(nums):
    return sum(filter(lambda num: num%2 != 0, nums))
print(f3([1,2,3,4]))
print(f3([1,2,3,4,5]))
print("*"*20)


def f4(nums):
    sum = 0
    for idx, num in enumerate(nums):
        if num % 2 != 0:
            sum += idx

    return sum
print(f4([1,2,3,4]))
print(f4([1,2,3,4,5]))
print("*"*20)

def f12(lst):
    if not lst:
        return True

    if lst[0] < 0:
        return f12(lst[1:])

    return False

print(f12([]))
print(f12([-1,-2,-3,-4,5]))
print(f12([1,2,3,4,5]))
print(f12([-1,-2,-3]))
print("*"*20)


def f15(nums):
    sum = 0
    for idx, num in  enumerate(nums):
        if idx % 2 == 0:
            sum += num
    return sum
print(f15([1,2,-3]))
print("*"*20)

def f16(n):
    print(*list(map(lambda num: "*"*num, list(range(n, 0, -1)))), sep = "\n")

f16(3)

def f20(matrix):
    for idx, row in enumerate(matrix):
        print(row[idx])

f20([[1,0],[0,1]])
f20([[1,2,3],[4,5,6],[7,8,9]])
f20([[1]])
f20([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
print("*"*20)



def f21(nums):
    import math
    print(*list(map(lambda num: math.factorial(num), nums)), sep = "\n")

f21([1,2,3,4])

def f21(nums):
    import math
    for num in nums:
        print(math.factorial(num))

f21([1,2,3,4])
print("*"*20)

def f22(nums):
    for num in nums:
        print(*list(range(num, -1, -1)), sep = " ")

f22([1,3,5])

def f22(nums):
    for num in nums:
        for i in range(num, -1, -1):
            print(i, end = " ")
        print()

f22([1,3,5])
print("*"*20)

def f23(lst1, lst2):
    return list(map(lambda x: sum(x), zip(lst1,lst2)))

print(f23([], []))
print(f23([1,2,3], [1,2,3]))
print("*"*20)

def f23(lst1, lst2):
    if lst1 == []:
        return lst2

    if lst2 == []:
        return lst1

    lst = []
    for i in range(len(lst1)):
        lst.append(sum(list(zip(lst1, lst2))[i]))
    return lst

print(f23([], []))
print(f23([1,2,3], [1,2,3]))
print("*"*20)

def f24(n):
    print(*list(filter(lambda num: num % 2 == 0 or num % 3 == 0,
    list(range(1,n+1)))), sep = "\n")

f24(10)
f24(15)
print("*"*20)


def f26(nums):
    it = iter(nums)
    second, the = sorted((next(it), next(it)))

    for num in it:
        if num > second:
            if num >= the:
                the, second = num, the
            else:
                second = num
    return second


print(f26([1,4,3,2,5]))
print(f26([3,2]))
print(f26([3,4]))
print("*"*20)


def f27(n):
    return int(str(n)[0])

print(f27(1234))
print(f27(4321))

def f27(n):
    while not n<10:
        n //= 10
    return n

print(f27(1234))
print(f27(4321))
print("*"*20)

def f28(lists):
    print(*list(map(lambda alist: max(alist), lists)), sep = "\n")

f28([[1,2,3],[4,5,6],[7,8,9]])
f28([[3,2,1],[0,-1,-2]])
f28([[1,2,3,4],[1],[34],[2],[3],[56],[67]])


def f28(alist):
    for a in alist:
        print(max(a))

f28([[1,2,3],[4,5,6],[7,8,9]])
f28([[3,2,1],[0,-1,-2]])
f28([[1,2,3,4],[1],[34],[2],[3],[56],[67]])
