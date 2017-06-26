




def f14(A):
    for i in range(1,len(A)+1,1):
        if A[-i] < 0 :
            return (-i+len(A))
			
def f15(a):
	sum=0
	for i in range(len(a)):
		if i%2==0:
			sum=sum+a[i]
	return sum
	
def f16(n):
	for i in range(n):
		print("*"*(n-i))	

		
######번은 빌트인 없이 해보기 
def f17(alist):
    alist = alist[-1:0:-1]#인덱스를 뒤집는다 
    for num in alist:
        if num not in alist[alist.index(num)+1:]:
            print (num)



def f18(n): #재귀함수 
	fact=1
	for i in range(1,n):
		fact=fact*(i+1)
	return fact

	
# 19
def f19(alist):
    for num in alist:
        print( f18(num))	
		
		
# 20
def f20(alist):
	for num in alist:
		for i in range(num, -1, -1):
			if i == 0 :
				print(i,end="\n")
			else :
				print(i,end=" ")



def f21(a,b):
	for i in range(len(b)):
		a[i]=a[i]+b[i]
	return a

	
def f22(n): #2또는 3의 배수 출력
    for i in range(1,n+1):
        if i%2==0 or i%3==0:
            print(i)

def f23(alist):
    max = alist[0][0]
    for i in range(len(alist)):
        for j in range(len(alist[i])):
            if max < alist[i][j]:
                max = alist[i][j]
    print (max)

#24 번은 빌트인 없이 해보기 

def f24(A):
    max=A[0]
    for i in range(len(A)):
        if max < A[i]:
            max=A[i]
    A.remove(max)
    max=0
    for i in range(len(A)):
        if max < A[i]:
            max=A[i]
    print(max)



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
		print(max)










