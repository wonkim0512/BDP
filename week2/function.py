# function
# def function_name(argument or parameter):

def sum_print(a,b):
    print "The sum of {} and {} is {}".format(a, b, a+b)

sum_print(1,2)

def sum_return(a,b):
    return a+b

result = sum_return(1,2)
print result
# print sum(1,2)  is same.


def say():
    return "Hi!"

print say()


def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print sum(1,2,3,4,5)

# multi way
def sum_mul(choice, *args):
    if choice == "sum":
        result = 0
        for i in args:
            result += i

    else:
        result = 1
        for i in args:
            result *= i

    return result

print sum_mul('sum', 1,2,3,4,5)
print sum_mul('mul', 1,2,3,4,5)

# as tuple
def sum_and_mul(a,b):
    return a+b, a*b

print sum_and_mul(2,3) #it return as tuple


def myFunc(a, b=3): # b is default value now. it consider3 when has no arg input
    return a + b

print myFunc(10)
print myFunc(10, 10)

# local and global
a =1
def square(a):
    return a**2

def square_global(b):
    """express global"""
    global a
    return a**2

print square(4)
print square_global(4) # however we try not to use global variable in the def.

print(square_global.__doc__) # it doesn't show # comments.
