import pandas as pd
import os
from pprint import pprint as dump

path = os.getcwd() + '\\123.csv'
df = pd.read_csv(path, encoding='utf-8', engine='python', error_bad_lines=False, sep=';', comment='#')
data_str = pd.DataFrame.to_string(df)
# wind = data['DD'].mean()

f = open('228.txt', 'a')
# asd = data_str.split('\n')
f.write(data_str)
f.close()

# dump( type(data) )

