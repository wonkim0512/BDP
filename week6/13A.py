# 21
def f21(tree):
    if tree == []:
        return 0
    return 1 + max(f21(tree[1]), f21(tree[2]))

print(f21([]))
print(f21([1,[],[]]))
print(f21([1,[1,[],[]],[]]))
print("*"*20)

# f22
def f22(tree):
    if tree == []:
        return 0
    return 1 + f22(tree[1]) + f22(tree[2])

print(f22([]))
print(f22([1,[],[]]))
print(f22([1,[1,[],[]],[]]))
print("*"*20)

# 23
def f23(tree):
    if tree == []:
        return 0
    return tree[0] + f23(tree[1]) + f23(tree[2])

print(f23([]))
print(f23([1,[],[]]))
print(f23([1,[1,[],[]],[]]))
print("*"*20)

# 24
def f24(tree):
    if tree == []:
        return
    f24(tree[1])
    print(tree[0])
    f24(tree[2])

f24([])
f24([1,[],[]])
f24([1,[1,[],[]],[]])
print("*"*20)

# 24_1
def f24_1(tree):
    if tree == []:
        return
    f24(tree[2])
    print(tree[0])
    f24(tree[1])

f24_1([])
f24_1([1,[],[]])
f24_1([1,[1,[],[]],[]])
print("*"*20)

# 25
def f25(tree):
    if tree == []:
        return -1

    if tree[1] == [] and tree[2] == []:
        return tree[0]
    return f25(tree[1])

print(f25([]))
print(f25([1,[],[]]))
print(f25([1,[1,[],[]],[]]))
print("*"*20)
