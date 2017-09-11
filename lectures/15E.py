for i in {1,3,5}: # set is also iterable.
    print(i)

iterables = [1,2,3]
iterator = iter(iterables)
print(next(iterator))
print(iterator.__next__())

def gen():
    yield 10
    yield 20
    yield 30

g = gen()
print(next(g))
print(next(g))

for i in gen():
    print(i)

print(gen())
