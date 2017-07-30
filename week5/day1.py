# 170710
# reduce
from functools import reduce
f = lambda x, y: x if x>y else y
maxi = reduce(f, [47,22,34,54,235,43,233])
print(maxi)

# zip
a, b = [1,2,3,4,5], [5,4,3,2,1]
for x,y in zip(a, b):
    print(x,y)

c = list(zip(a,b))
print(c)

d = 'abc'
e = list(zip(a, d))
print(e)



# File IO
'''
myfile = open("C:/Users/woni/Desktop/text.txt", 'w')
myfile.write("First line\nSecond line")
myfile.close()
myfile = open("C:/Users/woni/Desktop/text.txt", 'a')
myfile.write("\nThird line\nDone.")
myfile.close()
'''
f = open("C:/Users/woni/Desktop/text.txt", 'w')
for i in range(10):
    f.write("{}번째 줄입니디.\n".format(i+1))
f.close()
print("*"*20)

f = open("C:/Users/woni/Desktop/text.txt", 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
f.close()
print("*"*20)

f = open("C:/Users/woni/Desktop/text.txt", 'r')
lines = f.readlines()
print(lines) # return list
for line in lines:
    print(line)
f.close()
print("*"*20)

with open("C:/Users/woni/Desktop/text.txt", 'a') as f:
    f.write("Syntaetic Sugar!!!")

with open("C:/Users/woni/Desktop/pi.txt", 'r') as file_object:
    for line in file_object:
        print(line.rstrip())
        #print(line)

with open("C:/Users/woni/Desktop/csv_practice.csv", 'r') as f:
    content = f.read()
    print(content)


# exception
#x = 3 + "apple"
try:
    x = 3 + 'ham'
#
except TypeError:
    print("Types are not same")

except ZeroDivisionError:
    print("Impossible to be divided by 0")

finally:
    print("Done.")

# raise TypeError("haha")

import math
def main():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a,b,c = eval(input("Please enter the coefficients (a,b,c): "))
        discroot = math.sqrt(b**2 -4*a*c)
        root1 = (-b + discroot)/(2*a)
        root2 = (-b - discroot)/(2*a)
        print("\n The solutions are:", root1, root2)

    except ValueError:
        print("\n No real roots")

main()
