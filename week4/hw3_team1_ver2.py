#1
def f1(list): 
    if list:
        return list[0]+f1(list[1:])
    else:
        return 0
    
    
#2    
def f2(n): #even or odd function
    if n==1: #base case
        return 1
    elif n%2==0: #even
        return 1+f2(n//2) #"1" means one step+
    else: #odd
        return 1+f2(3*n+1) #"1" means one step+
    
	
#3		
def f3(lst):
    if lst:
        print(lst[-1])
        f3(lst[:-1])

    else: # actually we don't need it
        return 


#4
def f4(A):
	if A ==[]:
		return
	if A[0] % 2==1 :
		print(A[0]*3)
		return f4(A[1:])
	if A[0] % 2==0 :
		return f4(A[1:])

	    
#5
def f5(lst):
    if lst:
        if lst[-1] % 2 == 0:
            print(lst[-1])
            f5(lst[:-1])

        else:
            print(lst[-1]*3)
            f5(lst[:-1])

           
# 6
def f6(A):
    if A==[]:
        return []
    if type(A[0])!=list :
        return [A[0]]+f6(A[1:])
    if type(A[0])==list :
        return f6(A[0])+f6(A[1:])

	
# 7
def f7(n):
    if n == 0:
        return 2

    if n == 1:
        return 1

    return f7(n-1) + f7(n-2)


#8
def f8(s):
    if s=="":
        return True
    if s[0]==s[-1]:
        return f8(s[1:-1])
    else:
        return False


# 9
def f9(n):
    if n == 0 or n == 1:
        return 1

    return n * f9(n-1)


#10
def f10(A):
    if A==[]:
        return 0
    else :
        return 1+f10(A[1:])

    
#11
def f11(lst):
    if lst == []:
        return None # confirm

    elif len(lst) == 1:
        return lst[0]

    else:
        return f11(lst[1:])
    

# 12
def f12(n):
    if n > 0:
        print(n)
        return f12(n-1)
    

# 13
def f13(n):
    n //= 10
    if n > 0:
        return 1 + f13(n)

    else:
        return 1


#14
def f14(alist):
    if alist == []:
        return None

    elif alist[0] % 2 != 0:
        return alist[0]
    else:
        return f14(alist[1:])


#15
def f15(lst):
    if len(lst) == 0:
        return 0

    if lst[0] % 2 == 0:
        return f15(lst[1:]) # when a = [1], then a[1:] = []

    else:
        return lst[0] + f15(lst[1:])


# 16
def f16(a):
	if a==[]:
		return []
	else:
		if a[0]%2==1:
			return [a[0]]+f16(a[1:])
		else:
			return f16(a[1:])


# 17
def f17(lst): # secind to last
    if len(lst) == 2:
        return lst[0]
    else:
        return f17(lst[1:])


#18
def f18(a,b): 
    if(b==0): #base case: remainder is 0: one divides the other one
        return a #the one that divided
    else:
        return f18(b,a%b)

			    	
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

		
		
