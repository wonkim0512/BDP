# Recursion Practice
# 1
def f1(lst):
    if len(lst) == 0: # base case
        return 0

    if len(lst) == 1:
        return lst[0]

    return lst[0] + f1(lst[1:])

def f1(lst):
    if lst:
        return lst[0] + f1(lst[1:])

    else:
        return 0

print(f1([1,2,3,4]))
print(f1([]))
print("*"*20)



# 2 difficult
def f2(n):
    if n == 1:
        return 1 # how does it work at last?

    elif n % 2 == 0:
        return f2(n // 2) + 1

    elif n % 2 != 0:
        return f2(3*n + 1) + 1

print(f2(1))
print(f2(6))
print(f2(11))
print(f2(637228127))
print("*"*20)

# 3 while loop is included in recursion itself.
def f3(lst):
    if lst:
        print(lst[-1])
        f3(lst[:-1])
'''
    else: # actually we don't need it
        return lst
'''
f3([1,2,3])
f3([])
f3([3,2,1])
print("*"*20)

# 4
def f4(lst):
    if lst == []:
        return
    if lst[0] % 2 != 0:
        print(lst[0] * 3)
    else:
        pass
    return f4(lst[1:])

def f4(lst):
    if lst:
        if lst[0] % 2 != 0:
            print(lst[0] * 3)
        else:
            pass
        return f4(lst[1:])

f4([1,2,3,4])
f4([2,4])
f4([11,42,63,15])
print("*"*20)

# 5
def f5(lst):
    if lst:
        if lst[-1] % 2 == 0:
            print(lst[-1])
            f5(lst[:-1])

        else:
            print(lst[-1]*3)
            f5(lst[:-1])


f5([1,2,3,4])
f5([2,4])
f5([11,42,64,15])
print("*"*20)


# 6
def f6(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(f6(i))

        else:
            result.append(i)

    return result

print(f6(["baa"]))
print(f6(["baa",[4,True,[10, 5],[1,2,['moo']]],['chirp']]))
print("*"*20)

# 7
def f7(n):
    if n == 0:
        return 2

    if n == 1:
        return 1

    return f7(n-1) + f7(n-2)

print(f7(3))
print(f7(14))
print(f7(0))
print(f7(22))
print("*"*20)

# 8
def f8(s):
    if s == "":
        return True

    elif s[0] == s[-1]:
        f8(s[1:-1]) # i don't need 'return'

    else:
        return False

    return True # i don't need it. when i haer return at elif

print(f8(""))
print(f8('kayak'))
print(f8('penguin'))
print(f8('a'))
print("*"*20)

# 9
def f9(n):
    if n == 0 or n == 1:
        return 1

    return n * f9(n-1)

print(f9(0))
print(f9(1))
print(f9(2))
print(f9(3))
print("*"*20)


# 10
def f10(alist):
    count = 0
    if alist == []:
        return count

    else:
        count = f10(alist[1:]) + 1 # how is it working?

    return count

print(f10([1,2,3]))
print(f10([]))
print(f10([2]))
print("*"*20)

# 11
'''
def f11(lst):
    if lst[1:]:
        f11(lst[1:])

    return lst # not lst[0]
''' # I did wrong.

def f11(lst):
    if lst == []:
        return None # confirm

    elif len(lst) == 1:
        return lst[0]

    else:
        return f11(lst[1:])

print(f11([1,2,3]))
print(f11([]))
print(f11([1]))
print("*"*20)



# 12
def f12(n):
    if n > 0:
        print(n)
        f12(n-1)

f12(3)
f12(0)
f12(1)
print("*"*20)

# 13
def f13(n):
    n //= 10
    if n > 0:
        return 1 + f13(n)

    else:
        return 1

print(f13(9175))
print(f13(34))
print(f13(268))
print(f13(0))
print("*"*20)

# 14
def f14(alist):
    if alist == []:
        return None # difference between return and return None -> same!

    elif alist[0] % 2 != 0:
        return alist[0]
    else:
        return f14(alist[1:])

print(f14([1,2,3]))
print(f14([2,4]))
print(f14([2,4,6,8,10,3]))
print("*"*20)

# 15
def f15(lst):
    if len(lst) == 0:
        return 0

    if lst[0] % 2 == 0:
        return f15(lst[1:]) # when a = [1], then a[1:] = []

    else:
        return lst[0] + f15(lst[1:])

print(f15([1,2,3]))
print(f15([2,4]))
print(f15([1,3,6,9]))
print("*"*20)

# 16
def f16(alist):
    result = []
    if alist == []:
        return result

    elif alist[0] % 2 != 0:
        result.append(alist[0])
        result.extend(f16(alist[1:])) # important. extend, not append

    else:
        return f16(alist[1:])

    return result

print(f16([1,3,5,7]))
print(f16([2,4]))
print(f16([1,2,3,4,5]))
print("*"*20)

# 17
def f17(lst): # secind to last
    if len(lst) == 2:
        return lst[0]
    else:
        return f17(lst[1:])

print(f17([1,2]))
print(f17([1,2,3,4]))
print(f17([1,2,3]))
print("*"*20)


# 18
def f18(a, b):
    if a%b != 0: # i have to consider when b == 0
        return f18(b, a%b)

    return b

print(f18(5,4))
print(f18(40, 60))
print(f18(9, 3))
print("*"*20)

# 19 #merge()
def f19(lst1, lst2):
    if lst1 == []:
        return lst2

    if lst2 == []:
        return lst1

    if lst1[0] > lst2[0]:
        return [lst2[0]] + f19(lst1, lst2[1:])

    else:
        return [lst1[0]] + f19(lst1[1:], lst2)

print(f19([1,2,3],[4,5]))
print(f19([4,5],[1,2,3]))
print(f19([1,3,5], [2,4]))
print(f19([1,2,3],[]))
print(f19([],[1,2,3]))
print(f19([],[]))
print("*"*20)

# 20
def f20(alist): # msort()
    if len(alist) == 0 or len(alist) == 1:
        return alist[:len(alist)] # important. alist[0] -> index error

    half = len(alist)//2
    list1 = alist[:half]
    list2 = alist[half:]
    newlist1 = f20(list1)
    newlist2 = f20(list2)
    newlist = f19(newlist1, newlist2) # when is it implemented?
    return newlist

print(f20([3,2,1]))
print(f20([]))
print(f20([5,3,1,2,4,6]))
