import pandas as pd
import codecs
import os
from pprint import pprint as dump
from io import StringIO, BytesIO

path = os.getcwd() + '\\123.csv'
# data = pd.read_csv(path, 'utf-8', engine='python')
data = pd.read_csv(path, encoding='utf-8', engine='python', error_bad_lines=False, sep=';', comment='#')

f = open("1488.txt", "a")
asd = pd.DataFrame.to_string(data)
f.write(asd)
f.close()

# dump( data )