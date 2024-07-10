import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
print(data)

print('-' * 20)

lst1 = ['1' if lst[i] == 'robot' else '0' for i in range(20)]
data = data.rename(columns={'whoAmI': 'human'})
data.loc[data['human'] == 'human', 'human'] = 1
data.loc[data['human'] == 'robot', 'human'] = 0
data['robot'] = lst1
print(data)