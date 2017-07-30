# 10B 3~12
def func_m3(n):
    for i in range(1, n+1):
        print(*list(range(int(1 + i*(i-1)/2), int(1 + i*(i-1)/2 + i))), sep = " ")

    for i in range(n-1, 0, -1):
        print(*list(range(int(1 + i*(i-1)/2), int(1 + i*(i-1)/2)+i)), sep = " ")

func_m3(3)
func_m3(4)
func_m3(0)
func_m3(1)
print("*"*20)

def func_m4(n):

    for i in range(1,n+1):
        print(*list(range(int(1+i*(i-1)/2),int(1+i*(i-1)/2)+i)),sep=' ')
    for i in range(n-1,0,-1):
        print(*sorted(list(map(lambda y: (n*(n+1))//2+y,list(map(lambda x: (n*(n-1))//2+1-x,list(range(int(1+i*(i-1)/2),int(1+i*(i-1)/2)+i))))))),sep=' ')

func_m4(3)
func_m4(0)
func_m4(1)
print("*"*20)

def func_m5(matrix):
   for row in matrix:
      print(sum (row))

func_m5([[1,0], [0, 1]])
func_m5([[1,2,3], [4,5,6]])
func_m5([[1], [2], [3], [4]])
print("*"*20)

def func_m6(matrix):
   return sum(list(map(lambda x: sum(x),matrix)))

print(func_m6([[1,0], [0, 1]]))
print(func_m6([[1,2,3], [4,5,6]]))
print(func_m6([[1], [2], [3], [4]]))
print("*"*20)

def func_m7(matrix):
   from functools import reduce
   product=1
   for row in matrix:
      product*=reduce(lambda x,y: x*y, row)
   return product

print(func_m7([[1,0], [0, 1]]))
print(func_m7([[1,2,3], [4,5,6]]))
print(func_m7([[1], [2], [3], [4]]))
print("*"*20)

def func_m8(matrix):
   for row in matrix:
      print(*list(filter(lambda x: x%2,row)))

func_m8([[1,0], [0, 1]])
func_m8([[1,2,3], [4,5,6]])
func_m8([[1], [2], [3], [4]])
print("*"*20)

def func_m9(mat1,mat2):
    return([list(map(lambda x: x[0]+x[1], zip(mat1[rowNum],mat2[rowNum]))) for rowNum in range(len(mat1))])

print(func_m9([[1,0], [0,1]], [[1,0], [0,1]]))
print("*"*20)


def func_m10(mat1, mat2):
    return[ [ sum([mat1[mat1row][mat1col] * mat2[mat1col][mat2col] for mat1col in range(len(mat1[0]))])
    for mat2col in range(len(mat2[0])) ] for mat1row in range(len(mat1))]

print(func_m10([[1,0], [0,1]], [[1,0], [0,1]]))
print(func_m10([[1,2,3], [4,5,6]], [[-1, -1],[-1, -1], [-1, -1]]))
print("*"*20)

def func_m11(mtx):
    for i in range(len(mtx)):
        comparison = [1 if j == i else 0 for j in range(len(mtx[i]))]
        if mtx[i] != comparison:
            return False
    return True

print(func_m11([[1]]))
print(func_m11([[1,0,0], [0,1,0], [0,0,1]]))
print(func_m11([[1,0,0], [0,1,5], [0,0,1]]))
print("*"*20)

def func_m12(row,col):
   return [[((i> 0)+(i+1< row)+ (j> 0)+(j+1< col)) for j in range(0,col)] for i in range(0,row)]

print(func_m12(4,4))
print(func_m12(5,1))
print(func_m12(2,2))
