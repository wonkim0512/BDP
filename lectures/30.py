import numpy as np
import pandas as pd




df = pd.DataFrame(data = np.array([[1,2,3],[4,5,6],[7,8,9]]), columns = ['a','b','c'])
print(df)

for idx, row in df.iterrows():
    print(idx)
    print(row['a'])