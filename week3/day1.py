def sum_matrix(table):
    sum = 0
    for row in range(0, len(table)):
        for col in range(0, len(table[row])):
            sum += table[row][col]

    return sum

table = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print sum_matrix(table)

# dynamic allocation(1)
rows = 3
cols = 2
a = []
for row in range(rows):
    a += [[0]*cols]

print("This is ok. At first:")
print "a = ",a
print "*"*20

# dynamic allocation(2)
a = [ ([0]*cols) for row in range(rows)]

print a
a[0][0] = 42
print a
print "*"*20

# dynamic allocation(3)
def make2dList(rows, cols):
    a = []
    for row in range(rows):
        a += [[0]*cols]
    return a

a = make2dList(rows, cols)
print a
print "*"*20

# getting 2d list dimensions
a = [[2,3,5], [1,4,7]]
rows = len(a)
cols = len(a[0])
for row in range(rows): # in rows
    for col in range(cols): # in cols  why not?
        a[row][col] += 1

print a

# manipulating 2d-array
a = [[1,2,3],[4,5,6]]
row = 1
rowList = a[row]
print(rowList)

col = 1
colList = []
for i in range(len(a)):
    colList += [a[i][col]] # appending?

print(colList)


# prime number generator with python
# dumb version
def IsPrime_dumb(n):
    if n<2:
        return False

    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True

for i in range(1, 100):
    if IsPrime_dumb(i): # True
        print(i)

# clever version.. actually not I did wrongly
def Is_prime(n):
    if n<2:
        return False

    if n % 2 ==0 or n % 3 == 0 or n % 5 ==0 or n % 7 == 0: # Hey Won! what about 2,3,5,7?
        return False

    return True

for i in range(1, 100):
    if Is_prime(i):
        print(i)

# sifting
def sift(lst, k):
    i = 0
    while i < len(lst):
        if lst[i] != None and lst[i] % k == 0:
            lst[i] = None
        i += 1

    return lst

a = [1,2,3,4,5,6,7,8,9,10,11,12]
print sift(a, 3)

'''def sift2(lst, k):
    i = 0
    while i < len(lst):
        if lst[i] % k == 0:
            lst.remove(lst[i])

        else:
            i += 1

    return lst

print sift2(a, 3)'''

# prime checker - better version
def IsPrime_better(n):
    if n<2:
        return False

    if n ==2:
        return False

    if n%2==0:
        return False

    for factor in range(3, n, 2):
        if n%factor == 0:
            return False

    return True

# time checker
import time
start = time.time()
for i in range(1,100):
    if IsPrime_better(i):
        print(i)
end = time.time()
duration = end - start
print duration


# recursive function
def rf_factorial(n):
    if n ==0 or n==1:
        return 1

    return rf_factorial(n-1)*n

print rf_factorial(5)
print rf_factorial(10)

def factorial(n):
    result = 1
    for i in range(1, n+1):
            result *= i

    return result

print(factorial(5))
print(factorial(10))
