# 10B Python Looping and Matrix Practice with Sophistication
# 1
def f1(n):
    for i in range(1, n+1):
        print(*list(range(1, i+1)), sep = " ")
f1(5)
f1(0)
f1(1)
print("*"*20)

#2
def f2(n):
    for i in range(1, n+1):
        print(*list(range(int(1 + i*(i-1)/2), int(1+i*(i-1)/2 + i))), sep = " ")
f2(3)
f2(1)
f2(5)
print("*"*20)

# 3
def f3(n):
    for i in range(1, n+1):
        print(*list(range(int(1 + i*(i-1)/2), int(1 + i*(i-1)/2 + i))), sep = " ")

    for i in range(n-1, 0, -1):
        print(*list(range(int(1 + i*(i-1)/2), int(1 + i*(i-1)/2)+i)), sep = " ")

f3(3)
f3(4)
f3(0)
f3(1)
print("*"*20)

'''
# 4
def f4(n):
    for num in range(1, n**2 + 1):
        print(num, end = "")
        print()

f4(3)
f4(0)
f4(1)
print("*"*20)
'''

# 5
def f5(mtx):
    for row in mtx:
        print(sum(row))

f5([[1,0], [0, 1]])
f5([[1,2,3], [4,5,6]])
f5([[1], [2], [3], [4]])
print("*"*20)


# 6
def f6(mtx):
    result = 0
    for row in mtx:
        result += sum(row)
    return result

print(f6([[1,0], [0, 1]]))
print(f6([[1,2,3], [4,5,6]]))
print(f6([[1], [2], [3], [4]]))
print("*"*20)

# 7
def f7(mtx):
    from functools import reduce
    prod = 1
    for row in mtx:
        prod *= reduce(lambda x, y: x*y, row)

    return prod

print(f7([[1,0], [0, 1]]))
print(f7([[1,2,3], [4,5,6]]))
print(f7([[1], [2], [3], [4]]))
print("*"*20)

# 8
def f8(mtx):
    for row in mtx:
        alist = [num for num in row if num % 2 != 0]
        print(*alist, sep = " ")

f8([[1,0], [0, 1]])
f8([[1,2,3], [4,5,6]])
f8([[1], [2], [3], [4]])
print("*"*20)


# 9
def f9(mtx1, mtx2):
    result = []
    for i in range(len(mtx1)):
        result.append(list(map(lambda x:sum(x), list(zip(mtx1[i], mtx2[i])))))

    return result

def f9(mat1,mat2):
    return([list(map(lambda x: x[0]+x[1],
    zip(mat1[rowNum],mat2[rowNum]))) for rowNum
    in range(len(mat1))])

print(f9([[1,0], [0,1]], [[1,0], [0,1]]))
print("*"*20)

'''
# 10
def f10(mtx1, mtx2):


print(f10([[1,0], [0,1]], [[1,0], [0,1]]))
print(f10([[1,2,3], [4,5,6]], [[-1, -1],[-1, -1], [-1, -1]]))
print("*"*20)
'''

# 11
def f11(mtx):
    for i in range(len(mtx)):
        comparison = [1 if j == i else 0 for j in range(len(mtx[i]))]
        if mtx[i] != comparison:
            return False
    return True

print(f11([[1]]))
print(f11([[1,0,0], [0,1,0], [0,0,1]]))
print(f11([[1,0,0], [0,1,5], [0,0,1]]))

# 12 Pythonic!
def f12(row,col):
	return [[((i> 0)+(i+1< row)+ (j> 0)+(j+1< col)) for j in range(0,col)] for i in range(0,row)]
