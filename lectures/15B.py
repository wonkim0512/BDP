# alasing, shallow copy, deep copy
import copy

L = [1,2,3]
A = L # aliasing
S = copy.copy(L)
D = copy.deepcopy(L)

for i in [L, A, S, D]:
    print(i)

L[1] = 10
for i in [L, A, S, D]:
    print(i)

# there is no difference between shallow copy and deep copy when the list in one dimension
# however..
L = [[1,2,3], [4,5,6]]
A = L # aliasing
S = copy.copy(L)
D = copy.deepcopy(L)

for i in [L, A, S, D]:
    print(i)

L[0][1] = 10
for i in [L, A, S, D]:
    print(i)
