import copy
import time

lst = [1,2,3]
alias = lst
shallow = copy.copy(lst)

print(lst)
print(alias)
print(shallow)
print("After changing value")

lst[2] = 10
print(lst)
print(alias)
print(shallow)
print("*"*30)
##################################################################
lst = [[1,2,3],[4,5,6]]
alias = lst
shallow = copy.copy(lst)
deep = copy.deepcopy(lst)
print(lst)
print(alias)
print(shallow)
print(deep)
print("After changing value")
lst[0][0] = 10
print(lst)
print(alias)
print(shallow)
print(deep)
print("*"*30)
##############################################################
lst = [1,[4,5,6]]
a = lst
s = copy.copy(lst)
d = copy.deepcopy(lst)
lst[1][2] = 100
print(lst, a, s, d)

####################################################################

aset = set(list(range(1000)))
alist = list(range(1000))

# set
start = time.clock()
999 in aset
end =  time.clock()
print(end - start)

# list
start = time.clock()
999 in alist
end =  time.clock()
print(end - start)
# sets are more efficient than lists
