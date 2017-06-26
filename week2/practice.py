def f24(alist):
    max = alist[0]
    max_before = alist[0]
    for num in alist:
        if max < num:
            max_before = max
            max = num

    if max_before != max:
        print max_before

    else:
        alist.remove(max)
        f24(alist)

f24([1,4,3,2,5])
f24([3,2])
f24([3,4])
print "*"*20
