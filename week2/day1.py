# control structure
mail = 0
if mail: # 0 is false, others are true.
    print('mail time')

else:
    print("no mail:(")

print("*"*20)

if 7<= 6:
    print('whaa')

else:
    print("7 is greater than 6")

print("*"*20)

if 0 and 4: # 'false' and 'true' is false
    print("whaa")

print("*"*20)

if not 0:
    print('yep')

print("*"*20)

for i in range(0, 100, 10):
    print i

print("*"*20)

i = 0
while i < 10:
    print i
    i += 1

print("*"*20)

for i in range(30):
    if not i%3:
        continue
    print i

for i in range(30):
    if i%3 ==0:
        continue
    print i

print("*"*20)

x, y = 0, 0
while True:
    print x, y
    x += 1
    y += 2
    if x+y >10:
        break
print x, y

print("*"*20)

def moredata():
    moredata = 'yes'
    sum = 0
    count = 0
    while moredata[0] == 'y':
        x = eval(raw_input('Enter the number:'))
        sum += x
        count += 1
        moredata = raw_input("Do you want more number? Enter yes or no :")
    print 'The avg number of the numbers is', sum/count
moredata()

print("*"*20)

# loop with readline()
def main():
    fileName = "C:/Users/woni/Desktop/" # one / is same with \\
    fileName = fileName + raw_input("What file are the numbers in?:")
    infile = open(fileName+'.txt', 'r') # C:\Users\woni\Desktop\test.txt
    sum = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        sum += eval(line)
        count += 1
        line = infile.readline()
    print 'The avg of the numbers is', sum/count

main()
