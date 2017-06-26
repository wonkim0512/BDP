# 1
# python 2 and 3 version conflict
def f1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print j,
        print

f1(5)
print("*"*20)

# 2 TA did it with "star list" *list
def f2(n):
    for i in range(1, n+1):
        for j in range(0, i):
            print i+j,
        print

f2(10)
print("*"*20)

#
