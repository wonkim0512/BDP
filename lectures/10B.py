def f2(n):
    for i in range(1, n+1):
        print(*list(range(1 + int(i*(i-1)/2), 1 + int(i*(i-1)/2) + i)))

f2(3)
print("*"*20)

def f3(n):
    f2(n)
    for i in range(n-1, 0, -1):
        print(*list(range(1 + int(i*(i-1)/2), 1 + int(i*(i-1)/2) + i)), sep = " ")

f3(3)
print("*"*20)


def f4(n):
    s=sorted(list(range(1,(n**2)+1)),reverse=True)
    [print(*[s.pop() for j in range(n-abs(i-n))]) for i in range(1,2*n)]

f4(4)
print("*"*20)

def f7(mtx):
    from functools import reduce
    prod = 1
    for row in mtx:
        prod *= reduce(lambda x,y: x*y, row)
    return prod

print(f7([[1,0], [0, 1]]))
print(f7([[1,2,3], [4,5,6]]))
print(f7([[1], [2], [3], [4]]))
print("*"*20)

def f8(mtx):
    for row in mtx:
        print(*list(filter(lambda num: num%2 != 0, row)), sep = "\n")

f8([[1,0], [0, 1]])
f8([[1,2,3], [4,5,6]])
f8([[1], [2], [3], [4]])
print("*"*20)

def f9(mtx1, mtx2):
    return [list(map(lambda x: sum(x),zip(mtx1[rowNum], mtx2[rowNum])))
    for rowNum in range(len(mtx1))]

print(f9([[1,0], [0,1]], [[1,0], [0,1]]))
print("*"*20)

def f10(mtx1, mtx2):
    mtx = []
    for i in range(len(mtx1)):
        row = []
        for j in range(len(mtx2[0])):
            element = 0
            for k in range(len(mtx1[i])):
                element += mtx1[i][k] * mtx2[k][j]
            row.append(element)
        mtx.append(row)
    return mtx

print(f10([[1,0],[0,1]], [[1,0], [0,1]]))
print(f10([[1,2,3],[4,5,6]], [[-1,-1], [-1,-1], [-1,-1]]))

def f10(mtx1, mtx2):
    return [[ sum(list(mtx1[i][k] * mtx2[k][j]
    for k in range(len(mtx1[i]))))
    for j in range(len(mtx2[i]))]
    for i in range(len(mtx1))]

print(f10([[1,0], [0,1]], [[1,0], [0,1]]))
print(f10([[1,2,3], [4,5,6]], [[-1, -1],[-1, -1], [-1, -1]]))
print("*"*20)
