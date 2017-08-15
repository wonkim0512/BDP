def func_f1(lst):
    return len(list(filter(lambda x: x%2==1, lst)))

def func_f2(lst):
    print(*list(filter(lambda x: x%2!=0, lst)), sep = "\n")

def func_f3(lst):
    return sum(filter(lambda x: x%2!=0, lst))

def func_f4(lst):
    return sum(list(map(lambda x: x[0],
    filter(lambda x: x[1] % 2 != 0, enumerate(lst)))))

def func_f5(lst):
    return list(map(lambda x: x**2, lst))

def func_f6(lst):
    lst.sort()
    return lst[-1]

def func_f7(lst):
    return sum(lst)/len(lst)

def func_f8(a,b,n):
    print(*list(filter(lambda x: x % n == 0, list(range(a,b+1)))),sep = '\n')

def func_f9(w, h):
    print(*list(map(lambda x:x * w, ["*" for a in range(h)])), sep = "\n")

def func_f10(n):
      print(*[ '*' * (i+1) for i in range(n) ],sep="\n")

def func_f11(lst):
    if sorted(lst, reverse = True) == lst:
        return True

    else:
        return False

def func_f12(li):
   return all(map(lambda x : x<0,li))

def func_f13(lst, target):
    return list(map(lambda x:x[0], filter(lambda x:x[1] == target, enumerate(lst))))[-1]

def func_f14(lst):
    return list(map(lambda x: x[0], filter(lambda x: x[1]<0, enumerate(lst))))[-1]

def func_f15(lst):
    return sum(map(lambda x:x[1], filter(lambda x: x[0]%2==0, enumerate(lst))))


def func_f16(n):
    print(*list(map(lambda x: x*"*", [num for num in range(n,-1,-1)])), sep = "\n")


def func_f17(lst):
    for num in lst[::-2]:
        print(num)

def func_f18(n):
   import math
   return math.factorial(n)

def func_f19(mtx):
   for row in mtx:
      print(sum(row))

def func_f20(matrix):
   print(*list(map(lambda x: x[1][x[0]],enumerate(matrix))),sep='\n')

def func_f21(a):
   from functools import reduce
   for i in a:
      print(reduce(lambda x,y: x*y, range(1,i+1)))

def func_f22(li): # list[1,3,5]->10 3210 543210
    for i in li:
        print(*list(range(i,-1,-1)),sep=' ')

def func_f23(li1,li2):
    return list(map(lambda x:x[0]+x[1],zip(list1,list2)))

def func_f24(n):
   print(*list(filter(lambda x: x%2==0 or x%3==0, range(1,abs(n)+1))),sep='\n')

def func_f25(li):
    if isinstance(li[0],list):
        return f25(list(map(lambda x: max(x) ,filter(lambda x: len(x) != 0, li))))
    else:
        return max(li)

def func_f26(lst):
    return sorted(lst)[-2]

def func_f27(n):
    return int(str(n)[0])

def func_f28(lst):
    print(*list(map(lambda x: max(x), lst)), sep = "\n")

def func_m1(n):
   for i in range(1,n+1):
      print(*list(range(1,i+1)))

def func_m2(n):
    for i in range(1, n+1):
        print(*list(range(int(1 + i*(i-1)/2), int(1+i*(i-1)/2 + i))), sep = " ")

def func_m3(n):
    for i in range(1, n+1):
        print(*list(range(int(1 + i*(i-1)/2), int(1 + i*(i-1)/2 + i))), sep = " ")

    for i in range(n-1, 0, -1):
        print(*list(range(int(1 + i*(i-1)/2), int(1 + i*(i-1)/2)+i)), sep = " ")


def func_m4(n):

    for i in range(1,n+1):
        print(*list(range(int(1+i*(i-1)/2),int(1+i*(i-1)/2)+i)),sep=' ')
    for i in range(n-1,0,-1):
        print(*sorted(list(map(lambda y: (n*(n+1))//2+y,
        list(map(lambda x: (n*(n-1))//2+1-x,list(range(int(1+i*(i-1)/2),
        int(1+i*(i-1)/2)+i))))))),sep=' ')


def func_m5(matrix):
   for row in matrix:
      print(sum (row))


def func_m6(matrix):
   return sum(list(map(lambda x: sum(x),matrix)))


def func_m7(matrix):
   from functools import reduce
   product=1
   for row in matrix:
      product*=reduce(lambda x,y: x*y, row)
   return product



def func_m8(matrix):
   for row in matrix:
      print(*list(filter(lambda x: x%2,row)))


def func_m9(mat1,mat2):
    return([list(map(lambda x: x[0]+x[1], zip(mat1[rowNum],mat2[rowNum]))) for rowNum in range(len(mat1))])

print(func_m9([[1,0], [0,1]], [[1,0], [0,1]]))
print("*"*20)


def func_m10(mat1, mat2):
    return[ [ sum([mat1[mat1row][mat1col] * mat2[mat1col][mat2col]
    for mat1col in range(len(mat1[0]))])
    for mat2col in range(len(mat2[0])) ]
    for mat1row in range(len(mat1))]


def func_m11(mtx):
    for i in range(len(mtx)):
        comparison = [1 if j == i else 0 for j in range(len(mtx[i]))]
        if mtx[i] != comparison:
            return False
    return True


def func_m12(row,col):
   return [[((i> 0)+(i+1< row)+ (j> 0)+(j+1< col)) for j in range(0,col)]
   for i in range(0,row)]
