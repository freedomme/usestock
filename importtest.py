import numpy as np
import pandas as pd
import datetime
from pandas import Series,DataFrame
import matplotlib.pyplot as plt

# datetime.datetime.strftime('')
res = pd.read_csv('E:\\workspace\\usestock\\aa.csv',encoding='GB2312')
print(type(res))
tolist = np.array(res)
mean = res.mean()
std = res.std()
print(type(mean))
print(mean)
print(std)
def normfun(x,mu, sigma):
    pdf = np.exp(-((x - mu)**2) / (2* sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf
x = np.arange(0.0336, 0.1444, 1620)
y = normfun(x, mean, std)
plt.plot(x,y)
# plt.show()
plt.ion()
plt.pause(5)
plt.close()