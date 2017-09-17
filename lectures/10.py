'''
for i in [[], {}, set()]:
    print(type(i), dir(i), end = "")
    print()
'''
print(divmod(7,2))
print(divmod(9,3))

print(eval('1+4/2'))
print(eval("'hi' + 'a'"))

print(max('python'), min('python'))
print(pow(4, 1/2))

s = "nice to meet you! it's really good to see you"
print(s.upper())
print(s.title())
print(s.capitalize())
t = "nice to meet you! it is really good to see you"
print(t.title())

a = [3,2,1,4,3,2,12,3,4]
print(sorted(a))
print(a)
print(sorted(a, reverse = True))

print(sorted(s))
print(set(s))
print(sorted(set(s)))

print(list(reversed(a)))

b = list(a)
print(b)
c= [a]
print(c)
print(round(3.9))

p = 'python'
print(p[slice(1,5,2)])

lst = [1,5,6,2,3]
my_iter = iter(lst)
print(next(my_iter))
print(next(my_iter))

a = lambda x,y: x * y
print(a(3,4))
sum = lambda x,y: x+y
print(sum(1,2))
mylst = [lambda x,y: x+y, lambda x,y:x*y]
print(mylst[0](3,4))

lst = [1,2,3]
squared = list(map(lambda x: x**2, lst))
print(squared)

funcs = [lambda x: x**2, lambda x: x+x]
for i in range(5):
    value = list(map(lambda func: func(i), funcs))
    print(value)

lst = list(map(lambda x: x**2 if x<3 else x-3, [1,2,3,4]))
print(lst)

a = [1,2,3,4,5,6]
b = list(filter(lambda x: x**2 < 10, a))
print(b)

from functools import reduce
result = reduce(lambda x,y: x*y, [1,2,3])
print(result)
