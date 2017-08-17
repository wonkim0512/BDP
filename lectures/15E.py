<<<<<<< HEAD
for i in {1,3,5}: # set is also iterable.
    print(i)

iterables = [1,2,3]
iterator = iter(iterables)
print(next(iterator))
print(iterator.__next__())
=======
# Iterator and Generator

for num in [1,2,3]:
    print(num, end = " ")
print()

for ch in "Hello World!":
    print(ch, end = " ")
print()

for num in {1,2,3,4}:
    print(num, end = " ")
print()

for i in {"a":1, "b":2}:
    print(i, end = " ")
print()


lst = [1,2,3]
it = iter(lst)
print(it)
print(next(it))
print(it.__next__())

# make object of class as Iterator object
class MyCollection(object):
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= self.size:
            return StopIteration

        n = self.data[self.index]
        self.index += 1
        return n

coll = MyCollection()
print(coll)
iter(coll)
print(next(coll))
print(next(coll))

# Generator
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(type(g))
print(next(g))
print(next(g))

for x in gen():
    print(x)

gc = (n**2 for n in range(1, 11))
print(type(gc))
for x in range(5):
    value = next(gc)
    print(value)
for x in gc:
    print(x)
>>>>>>> ecb4187e0d5c15e2e79dfcdac8b86b83fcc85e3a
