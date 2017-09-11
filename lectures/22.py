import collections

# Counter
c = collections.Counter()
print(c)
c = collections.Counter("gallahad")
print(c)
c = collections.Counter({'red':4, "blue":2})
print(c)
c = collections.Counter(cats = 4, dogs = 2)
print(c)

# unless collections, it is inconvenient
c = {}
def addCounter(obj):

    if obj not in c:
        c[obj] = 1

    else:
        c[obj] += 1

for ch in 'aaabbccd':
    addCounter(ch)

print(c)

# deque
d = collections.deque('abcdef')
print(d, len(d), d[0], d[-1])
d.append('hello'); print(d)
d.appendleft('good bye!'); print(d)
d.remove('d'); print(d)

d.pop(); print(d)
d.popleft(); print(d)
d.rotate(2); print(d)
d.rotate(-2); print(d)

# OrderedDict
adict = {"James": 1, "David": 3, "Dave": 2}
print(adict)

od_key = collections.OrderedDict(sorted(adict.items(), key = lambda x:x[0]))
print(od_key)
