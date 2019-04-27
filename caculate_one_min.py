# 930  959  对应 1-30
# 1000 1059 对应 31-90
# 1100 1059 对应 91-120
# 1300 1359 对应 121-180
# 1400 1459 对应 181 - 240

import numpy as np
import pandas as pd
import datetime
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# datetime.datetime.strftime('')
res = pd.read_csv('G:\\BaiduYunDownload\\20130606\\SH600007.csv',encoding='GB2312')
print(type(res))
# print(res[1])