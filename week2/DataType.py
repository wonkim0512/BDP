# Numeric Data

# String Data
print 'hello' '''sdasda ''' # not a quotation

'''hello
''' #this is multi line quotation

print "I eat %d apples a day." % 3
print "I eat {} apples a day.".format(3)
print "{0} eat(s) {1} {2} a day".format("He" ,2, "bananas")

print "*"*20

print "%-10sjane" % 'hi..'

print "*"*20
a = "Life is too short"
print a.index("t")
#print a.index("w")
print a.replace("Life", "The train")
splited_a_list =  a.split(" ")
print splited_a_list
concatenated_a = "".join(splited_a_list)
print concatenated_a


print ord("A")
print ord('Z')
print ord('a')
print chr(98)

#list Data Type
a = []
# print a.append('a') # None
a.append('a')
print a

b = [1, 2, 3]
print b[:-1] # not include the last

c = ['Life', 'is', 'short', '!']
print " ".join(c)

d = [25, 'pretty']

e = [1, 2, ['Life', 'is']]
b.append(c) # difference between python 2 and 3?
print b

f = [1, 2, ['a', 'b', ["Life", "is"]]]
print f[2][0], f[2][2]
print f[2][2][1]

del f[0]
print f
f.insert(0, [1,2,3])
print f

a = [4,3,6,7,1,10,2]
print sorted(a)
print a
print a.index(7)

print a.pop(4)
print a
a.extend([5,21])
print a

# set
a = {1,2,3,3}
print a

print "*"*20
a = 3
b = a
del a
#print a
print b


c = 4
d = c
print c is d
print c==d

#
import sys
print sys.getrefcount(2) # when a = 2, if del a, then sys.getrefcount reduce 1.
print sys.getrefcount(2021)


a = [1,2,3,4]
while a:
    print a.pop()
