# tuple
tuple1 = ('spam', 'how', 1, 2)
print(tuple1[1:3])

tuple2 = (1,2,3,4)
# print(cmp(tuple1, tuple2)) -> python2

print(len(tuple2), max(tuple2), min(tuple2))
tuple3 = tuple(range(1,10))
print(tuple3)

# set
s = set()
print(s)

# s[0], s[1] = 'dog', 'cat'
s1, s2 = set('wahoo'), {2,3,4}
print(s1, s2)

s = {}
print(type(s))
s = set()
print(type(s))

s = set([2,4,8])
print(s)
for num in s:
    print(num)

# s = set([1,2,[2,3]]) # unhashable type: 'list'
for num in s:
    print(num)

alist = [1,2,3]
s1 = set(alist)
#s2 = set([alist]) -> unhashable type: 'list'
print(s1)

s = {2,3,2,4,3}
print(len(s))
t = s.copy()
s.add(5)
print(s, t)

s = {12, 13, 31}
print(s.pop())
print(s)

s = {1,2,3,4,5}
#print(s.remove(s.pop()))
print(s.discard(s.pop()))

print({1,2} <= {1}, {1,2}.issubset({1}))

s = {1,2,3,4}
t = {4,5}
print(s.symmetric_difference(t))

t = s^{1,3}
print(s, t)

s = {1,2}
t = {3,4}
s.update(t)
print(s)
s |= {6}
print(s)
