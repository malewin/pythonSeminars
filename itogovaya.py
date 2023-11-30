import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
data_list = list(data['whoAmI'])
for i in range(len(data_list)):
    if data_list[i] == 'robot':
        data_list[i] = 0
    else:
        data_list[i] = 1
print(data_list)