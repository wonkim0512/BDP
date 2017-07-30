# built-in function
for idx, name in enumerate(["A", "B", "C"]):
    print(idx, name)

# what 'eval' do?
print(eval("3"))
print(eval('1+2'))

# id(object)
a = 5
print(id(a))
print(id(5))
b = a
print(id(b))

# max and min are also applicable to 'string'.
print(max("abcde"))
print(min("fsflkcsfninfq"))

# sorted & sort
a = [3,1,2]
b = sorted(a)
print('a =', a) # there is no return from sorted(list)
print('b =',b)

result = a.sort()
print(a)
print(result)

sen = 'dlqkfnsif'
c = sorted(sen)
print(sen)
print(c)
d = sorted(sen, reverse = True)
print(d)

# reversed() : 'built-in' function
seqString = 'Python'
print(list(reversed(seqString)))

seqTuple = ('')

# reverse() : 'method' included in list.  alist.method()
a = [1,2,4,2,3,1]
a.reverse()
print(a)

# isinstance
print(isinstance(3, int))
print(isinstance('abc', str))

class Person():
    pass

a = Person()
print(isinstance(a, Person))

# round()
print(round(82.1239812, 6))

# slice()
sentence = 'abcdefg'
s = slice(4)
t = slice(1, len(sentence), 2)
print(sentence[s])
print(sentence[t])

# lambda function
a = lambda x, y : x * y
print(a(3, 4))
print(a('abc',3))
#print(a('ab','cs'))

alist = [-1, -8, 3, -4, 2, 5, -7]
sorted_list_square = sorted(alist, key = lambda x: x*x)
print(sorted_list_square)

# map
items = [1,2,3,4]
squared = list(map(lambda x : x**2, items))
print(squared)

# fiter
smaller = list(filter(lambda x: x<3, items))
print(smaller)

# reduce
#result = list(reduce(lambda x: )) # from functools import reduce
#print(result)

# map() advanced
def multiply(x):
    return x*x

def add(x):
    return x+x

func = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), func))
    print(value)

# two_times : dumb way
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number *2)
    return result

result = two_times([1,2,3,4])
print(result)

# two_times : pythonic
def two_times(x): # if you didnt define this function again, it will make an error, because former one expects you input list.
    return x*2
result = list(map(two_times, [1,2,3,4]))
print(result)

# two_times : more pythonic
result = list(map(lambda x: x*2, [1,2,3,4]))
print(result)
