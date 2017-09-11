import os
import sys
import threading
import time


print(os.name)
print(os.environ)
print(os.environ['PATH'])
print(os.getcwd())
print(os.listdir())
os.chdir('tkinter')
print(os.getcwd())
print(os.listdir())
print(os.listdir('..'))


f = os.popen('dir')
print(f.read()) # dir 결과가 나옴.


print(os.path.isfile('/home/snu/BD')) # folder -> False
print(os.path.isfile('/home/snu/print')) # file -> True
print(os.path.isdir('/home/snu/BD')) # True
print(os.path.isdir('/home/snu/BD/BDP')) # True
deep = os.path.join('/home/snu/BD/BDP', 'lectures')
print(deep)
print(os.path.isdir(deep))


print(sys.path)
print(sys.argv)
print(sys.argv[0])


import glob

print(glob.glob("/home/snu/BD/*"))

pyFiles = glob.glob("/home/snu/BD/BDP/*.py")
for file in pyFiles:
    print(file)


print(os.system('dir'))
import shutil
shutil.copy('20.py', 'new20.py')
print(os.system('dir'))

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
#shutil.copytree('tkinter', 'new') #tkinter 안에 있는 모든 것들 new라는 폴더에 복사생성.



'''
x = 0
def inc():
     global x
     for i in range(1000000):
             x += 1

def dec():
     global x
     for i in range(1000000):
             x -= 1

t1 = threading.Thread(target = inc)
t2 = threading.Thread(target = dec)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)


def say(msg):
    while True:
        time.sleep(1)
        print(msg)

for msg in ['you', 'need', 'python']:
    t = threading.Thread(target = say, args = (msg, ))
    t.daemon = True
    t.start()

for i in range(30):
    time.sleep(0.5)
    print(i)
'''