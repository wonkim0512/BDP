for i in {1,3,5}: # set is also iterable.
    print(i)

iterables = [1,2,3]
iterator = iter(iterables)
print(next(iterator))
print(iterator.__next__())
