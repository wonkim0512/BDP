# Homeword 1 by group 1.
#1
def f1(alist):
    count = 0
    for num in alist:
        if num % 2 != 0:
            count += 1

    print count

f1([1,2,3,4])
f1([1,2,3,4,5])
print "*"*20


#2
def f2(alist):
    for num in alist:
        if num % 2 != 0:
            print num

f2([1,2,3,4])
f2([1,2,3,4,5])
print "*"*20


#3
def f3(alist):
    sum = 0
    for num in alist:
        if num % 2 != 0:
            sum += num

    print sum

f3([1,2,3,4])
f3([1,2,3,4,5])
print "*"*20


#4
def f4(alist):
    sum_idx = 0
    idx = 0
    for num in alist:
        if num % 2 != 0:
            sum_idx += idx
        idx += 1
    print sum_idx

f4([1,2,3,4])
f4([1,2,3,4,5])
print "*"*20


#5
def f5(alist):
    squared_lst = [] # make an empty list first to contain the result.
    for num in alist:
        squared_lst.append(num**2)
    print squared_lst

f5([1,2,3,4])
f5([1,2,3,4,5])
print "*"*20


#6   try again not to use built-in function
def f6(alist):
    max = alist[0]
    for num in alist:
        if num > max:
            max = num
    print max

f6([1,2,3,4])
f6([1,2,3,4,5])
print "*"*20


#7
def f7(alist):
    sum = 0
    count = 0
    for num in alist:
        sum += num
        count += 1

    print float(sum) / count

f7([1,2,3,4])
f7([1,2,3,4,5])
print "*"*20


#8
def f8(a, b, n):
    for num in range(a,b+1):
        if num % n == 0:
            print num

f8(1, 10, 2)
f8(1, 10, 7)
print "*"*20


#9 try again!
def f9(width, height):
    for x in range(height):
        print "*"*width

f9(0,1)
f9(10,0)
f9(1,1)
f9(1,2)
f9(5,5)
print "*"*20


#10
def f10(n):
    for i in range(1, n+1):
        print "*"* i

f10(1)
f10(2)
f10(3)
print "*"*20


#11
def f11(alist):
    if len(alist) == 0 or len(alist) == 1:
        return True
    for i in range(len(alist)-1):
        if alist[i] < alist[i+1]:
            return False
    return True

print f11([])
print f11([5,4,3,2,1])
print f11([5,4,3,2,0])
print f11([5,4,5,2])
print "*"*20


#12
def f12(alist):
    for num in alist:
        if num >= 0:
            return False
    return True

print f12([])
print f12([-1,-2,-3,-4,5])
print f12([1,2,3,4,5])
print f12([-1,-2,-3])
print "*"*20


#13
def f13(alist, target):
    target_idx = 0
    for idx in range(len(alist)):
        if alist[idx] == target:
            target_idx = idx
        idx += 1
    print target_idx

f13([1,2,3], 3)
f13([1,2,3,1,2,3], 3)
f13([1,1,1,1], 1)
print "*"*20


# 14
def f14(alist):
    idx = 0
    idx_negative = 0
    for i in alist:
        if i < 0:
            idx_negative = idx
        idx += 1
    print idx_negative

f14([1,2,-3])
f14([1,-2,-3,1,-2,-3])
f14([-1,1,1,1])
print "*"*20


# 15
def f15(alist):
    idx = 0
    sum = 0
    for num in alist:
        if idx % 2 ==0:
            sum += num
        idx += 1
    print sum

f15([1,2,-3])
f15([1,-2,-3,1,-2,-3])
f15([-1,1,1,1])
print "*"*20


# 16
def f16(n):
    for i in range(n, 0, -1):
        print "*" * i

f16(3)
f16(2)
f16(1)
print "*"*20


# 17
def f17(alist):
    alist = alist[::-1]
    idx = 0
    for num in alist:
        if num not in alist[:idx] and num not in alist[idx+1:]:
            print num
        idx += 1

f17([1,2,1,4,1,6])
f17([1,2,1,4])
f17([1])
print "*"*20


#18
def f18(n):
    if n == 0 or n == 1:
        return 1

    else:
        return f18(n-1) * n

print f18(0)
print f18(2)
print f18(3)
print "*"*20


# 19
def f19(alist):
    for num in alist:
        print f18(num)

f19([])
f19([1,2,3])
f19([1,2,3,4])
print "*"*20


# 20                         !!! python 2 and 3 version conflict. !!!
def f20(alist):
    for num in alist:
        for i in range(num, -1, -1):
            print i,


f20([])
f20([1,3,5])
f20([5,3,6,2])
print "*"*20


# 21
def f21(alist1, alist2):
    lst = []
    for i in range(len(alist1)):
        lst.append(alist1[i]+alist2[i])
    print lst

f21([], [])
f21([1,2,3], [1,2,3])
f21([0,0,0], [1,2,3])
print "*"*20


# 22
def f22(n):
    for i in range(1, n+1):
        if i % 2 ==0 or i % 3 ==0:
            print i

f22(10)
f22(1)
f22(3)
print "*"*20


# 23
def f23(alist):
    max = alist[0][0]
    for i in range(len(alist)):
        for j in range(len(alist[i])):
            if max < alist[i][j]:
                max = alist[i][j]
    print max

f23([[1,2,3],[4,5,6],[7,8,9]])
f23([[3,2,1],[0,-1,-2]])
f23([[1,2,3,4],[],[],[56],[67]])
print "*"*20


# 24
def f24(alist):
    max = alist[0]
    max_before = alist[0]
    for num in alist:
        if max < num:
            max_before = max
            max = num

    if max_before != max:
        print max_before

    else:
        alist.remove(max)
        max = alist[0]
        for num in alist:
            if max < num:
                max = num
        print max

f24([1,4,3,2,5])
f24([3,2])
f24([3,4])



def f24_also(alist):
    max = alist[0]
    for num in alist:
        if max < num:
            max = num


f24_also([1,4,3,2,5])
f24_also([3,2])
f24also([3,4])
print "*"*20

# 25
def f25(n):
    while n > 10:
        n = n / 10
    print n

f25(1234)
f25(4321)
f25(3)
print "*"*20


# 26
def f26(alist):
    for i in range(len(alist)):
        max = alist[i][0]
        for j in range(len(alist[i])):
            if max < alist[i][j]:
                max = alist[i][j]
        print max

f26([[1,2,3],[4,5,6],[7,8,9]])
f26([[3,2,1],[0,-1,-2]])
f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]])
