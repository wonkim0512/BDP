# 10A Python Function Practice with Sophistication
# 1
def f1(lst):
    return len(list(filter(lambda x: x%2==1, lst)))

print(f1([1,2,3,4]))
print(f1([1,2,3,4,5]))
print("*"*20)

# 2
def f2(lst):
    print(*list(filter(lambda x: x%2!=0, lst)), sep = "\n")

f2([1,2,3,4])
f2([1,2,3,4,5])
print("*"*20)

# 3
def f3(lst):
    return sum(filter(lambda x: x%2!=0, lst))

print(f3([1,2,3,4]))
print(f3([1,2,3,4,5]))
print("*"*20)

# 4
def f4(lst):
    return sum(list(map(lambda x: x[0],
    filter(lambda x: x[1] % 2 != 0, enumerate(lst)))))

print(f4([1,2,3,4]))
print(f4([1,2,3,4,5]))
print("*"*20)

# 5
def f5(lst):
    return list(map(lambda x: x**2, lst))

print(f5([1,2,3,4]))
print(f5([1,2,3,4,5]))
print("*"*20)

# 6
def f6(lst):
    lst.sort()
    return lst[-1]

print(f6([1,2,3,4,5,7,3,4,2,1]))
print("*"*20)

# 7
def f7(lst):
    return sum(lst)/len(lst)

print(f7([1,2,3,4]))
print(f7([1,2,3,4,5]))
print("*"*20)

# 8
def f8(a,b,n):
    print(*list(filter(lambda x: x % n == 0, list(range(a,b+1)))),sep = '\n')

f8(1,10,2)
f8(1,10,11)
f8(1,10,7)
print("*"*20)

# 9
def f9(w, h):
    print(*list(map(lambda x:x * w, ["*" for a in range(h)])), sep = "\n") # separator

f9(4,5)
print("*"*20)

# 10
def f10(n):
    print(*list(map(lambda x: x*"*", [num for num in range(1,n+1)])), sep = "\n")

f10(3)
print("*"*20)

# 11
def f11(lst):
    if sorted(lst, reverse = True) == lst:
        return True

    else:
        return False

print(f11([]))
print("*"*20)

# 12
def f12(lst):
    lst = list(filter(lambda x: x > 0, lst))
    if lst:
        return False
    return True

print(f12([]))
print(f12([-1,-2,-3,-4,5]))
print(f12([1,2,3,4,5]))
print(f12([-1,-2,-3]))
print("*"*20)

# 13
def f13(lst, target):
    return list(map(lambda x:x[0], filter(lambda x:x[1] == target, enumerate(lst))))[-1]

print(f13([1,2,3], 3))
print(f13([1,2,3,1,2,3],3))
print(f13([1,1,1,1], 1))
print("*"*20)

# 14
def f14(lst):
    return list(map(lambda x: x[0], filter(lambda x: x[1]<0, enumerate(lst))))[-1]

print(f14([1,2,-3]))
print(f14([1,-2,-3,1,-2,-3]))
print(f14([-1,1,1,1]))
print("*"*20)

# 15
def f15(lst):
    return sum(map(lambda x:x[1], filter(lambda x: x[0]%2==0, enumerate(lst))))

print(f15([1,2,-3]))
print(f15([1,-2,-3,1,-2,-3]))
print(f15([-1,1,1,1]))
print("*"*20)

# 16
def f16(n):
    print(*list(map(lambda x: x*"*", [num for num in range(n,-1,-1)])), sep = "\n")

f16(3)
f16(2)
f16(1)
print("*"*20)

# 17
def f17(lst):
    for num in lst[::-2]:
        print(num)

f17([1,2,3,4,5,6])
f17([1,2,3,4])
print("*"*20)

# 18
def f18(n):
    import math
    print(list(map(lambda x: math.factorial(x), [n]))[0])
f18(0)
f18(2)
f18(3)
print("*"*20)

# 19
def f19(mtx):
    for row in mtx:
        print(sum(row))

f19([[1,0],[0,1]])
f19([[1,2,3],[4,5,6]])
print("*"*20)

# 20 # try again!
def f20(mtx):
    for idx in range(len(mtx)):
        print(*list(map(lambda x: x[1][idx],
        filter(lambda x: x[0] == idx, enumerate(mtx)))))

f20([[1,0],[0,1]])
f20([[1,2,3],[4,5,6],[7,8,9]])
f20([[1]])
f20([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
print("*"*20)

# 21
def f21(lst):
    import math
    print(*list(map(lambda x:math.factorial(x), lst)), sep="\n")

f21([])
f21([1,2,3])
f21([1,2,3,4])
print("*"*20)

# 22
def f22(lst):
    for num in lst:
        print(*list(map(lambda x: x, list(range(num, -1, -1)))))

f22([])
f22([1,3,5])
f22([5,3,6,2])
print("*"*20)

# 23
def f23(lst1, lst2):
    return list(map(lambda x: sum(x), zip(lst1, lst2)))

print(f23([1,2,3], [1,2,3]))
print("*"*20)

# 24
def f24(n):
    print(*list(filter(lambda x: x % 2 == 0 or x % 3 == 0,
    list(range(1, n+1)))),sep = "\n")

f24(10)
f24(1)
f24(3)
print("*"*20)

# 25
def f25(lst):
    if isinstance(lst[0], list):
        return f25(list(map(lambda x: max(x), lst)))

    else:
        return max(lst)

print(f25([[1,2,3],[4,5,6],[7,8,9]]))
print("*"*20)

# 26
def f26(lst):
    return sorted(lst)[-2] # lst.sort()???

print(f26([1,4,3,2,5]))
print(f26([3,2]))
print(f26([3,4]))
print("*"*20)

# 27
def f27(n):
    return int(str(n)[0])

print(f27(1234))
print(f27(4321))
print(f27(3))
print("*"*20)

# 28
def f28(lst):
    print(*list(map(lambda x: max(x), lst)), sep = "\n")

f28([[1,2,3],[4,5,6],[7,8,9]])
f28([[3,2,1],[0,-1,-2]])
f28([[1,2,3,4],[1],[34],[2],[3],[56],[67]])
