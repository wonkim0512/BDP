# Tuple
t1 = ()
t2 = (1,2,3,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

print(t2)
print(t3)
print(t5)
# del t2[0] #  tuple doesn't support item deletion

L = ("spam", "Spam", "SPAM")
print(L)
print(L[1:])
print(L[-1])

# cmp(t3, L) # python2
print(len(L))
new_tuple = tuple([1,2,3,4,5]) # converts a list into tuple.
print(new_tuple)




# Set
s = set([2,3,4,5,5])
print(s)
print(3 in s)
print(7 in s)
for x in range(7):
    if x not in s:
        print(x)

empty_set = set()
print(empty_set) # set()
s = set(['cat', 'cow', 'dog'])
print(s)

s = set("wahoo")
print(s) # the set of characters which make the string. not multiset

s = set([1,2,'kim'])
print(s)

#s1 = set([1,2,[3,4]])
#s1 = set([4,5,set([5,10])])
#print(s1)


# Sets are very efficient
# 0. preliminaries
import time
n = 1000

# 1. create a list [2,4,6,...n] then check for membership among [1,2,3,4,..,n] in that list.
a = list(range(2, n+1, 2))
print("Using a list", end = "")
start = time.time()
count = 0
for x in range(n+1):
    if x in a:
        count += 1

end = time.time()
elapsed1 = end - start
print("count", count, " and time = {} seonds".format(elapsed1))

# 2. repleat, using a set
print("Using a set", end="")
start = time.time()
s = set(a)
count = 0
for x in range(n+1):
    if x in s:
        count += 1

end = time.time()
elapsed2 = end - start
print("count", count, " and time = {} seonds".format(elapsed2))
print("With n = {}, sets ran about {} times faster than lists".format(n, elapsed1/elapsed2))

s = {2,3,2,4,3}
print(len(s))
t = s.copy()
s.add(10)
print("t=",t, ",s=",s)

s.pop()
print("s=", s)
t.clear()
print(t)



# Dictionary
count = dict()
while True:
    n = int(input("Enter an integer (0 to end):")) # the output of input is always string.
    if n == 0:
        break

    else:
        if n in count:
            count[n] += 1

        else:
            count[n] = 1

    print("I have seen", n, "a total of", count[n], "time(s).")
print("Done")

a = {'Economics': ['econ101', 'econ102', 'econ301'], 'Computer Science': ['cs101', 'cs401'],
'Political Science': ['ps101', 'ps203']}
print(a)
