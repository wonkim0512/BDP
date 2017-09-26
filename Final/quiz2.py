import pickle
import threading
import numpy as np
import pandas as pd
import collections

# pickle
content = {1: 'Python', 2: "you need"}

with open("test.txt", 'wb') as f:
    pickle.dump(content, f)

with open("test.txt", "rb") as file:
    python = pickle.load(file)
    print(python)


# threading
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


# numpy

print(np.full((3, 3), 7))

a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
print(a+b)
print(a*b)


# pandas

sales_stats = {'visitors': [43,32],
               'revenue': [44,23]}

df = pd.DataFrame(sales_stats, index = ["a", "b"]) # set_index is used to make a column to the index.
print(df)
print(df.loc['a'])


# collections

c = collections.Counter('gallahad')
print(c)

c = collections.Counter(cats=4, dogs=2)
print(c)