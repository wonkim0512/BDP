import glob
import os

aa='C:'+os.environ['HOMEPATH']
print(aa)
a=aa.split('\\')
print(a)
newa=a[0]
for i in range(1,len(a)):
    newa+='\\\\'+a[i]
print(newa)

g=glob.glob(newa)
print(g)