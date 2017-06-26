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


# 25
def f25(n):
    while n > 10:
        n = n // 10
    return (n)

def f26(a):
	for i in range(len(a)):
		b=a[i]
		max=b[0]
		for j in b:
			if j > max:
				max=j
		print max


f26([[1,2,3],[4,5,6],[7,8,9]])
f26([[3,2,1],[0,-1,-2]])
f26([[1,2,3,4],[1],[34],[2],[3],[56],[67]])
