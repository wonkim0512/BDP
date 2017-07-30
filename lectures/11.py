'''
f = open('f.txt', 'w')
for i in range(1, 11):
    if i not in [1,2,3]:
        f.write("This is {} th line\n".format(i))
    if i == 1:
        f.write("This is {} st line\n".format(i))

    if i == 2:
        f.write("This is {} nd line\n".format(i))

    if i ==3:
        f.write("This is {} rd line\n".format(i))

f.close()

f = open('f.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open('f.txt', 'r')
while True:
    line = f.readline()
    print(line)
    if not line:
        break
f.close() # why does two above have one line term.

f = open('f.txt', 'r')
content = f.read()
print(content)
f.close()

f = open('f.txt', 'r')
lines = f.readlines()
print(lines) # list
f.close()

f = open('f.txt', 'r')
line = f.readline()
print(line)
f.close()
'''
import csv
with open('f.txt', 'w+') as csvFile:
    f_writer = csv.writer(csvFile)
    a = [1, 2, 3]
    f_writer.writerow(a)


with open('f.txt', 'r+') as csvFile:
    f_reader = csv.reader(csvFile)
    for row in f_reader:
        print(row)

# exception handling
try:
    x = 5 +'a'

#except:
except TypeError: # if you have other except condition, you have to show it clearly
    print("What the hell?")

except ZeroDivisionError:
    print("Study Mathematics, bro!")


finally:
    print("Thank you, though.")

########################################
try:
    x = 5 +'a'

except ZeroDivisionError:
    print("Study Mathematics, bro!")
'''
else:
    print("I don't know...") # what I did wrong?
'''
finally:
    print("Thank you, though.")
