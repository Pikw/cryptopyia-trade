
# coding: utf-8

# In[1]:

#   Used inf cron ewery hour without grath
#
#-----------------------
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta    
#%matplotlib inline
# print (pd.__name__, pd.__version__)


# In[2]:

cid = '4909' # BTC/USDT #4327 # ZEC/BTC 1261 # PAC/DTC 5662 # ETH/BTC 5760 # ETH/USDT
hid = '2' # hours is
path = 'https://www.cryptopia.co.nz/api/GetMarketHistory/' + cid + '/' + hid
r = requests.get(path) #; r 
#print('---------------END----------------')

# In[3]:

df = json_normalize(json.loads(r.text)['Data'])
# print (df['Amount'].max())
# print (df['Amount'].mean())
# print (df.info)
# print (df.describe())
# print (df.index)


# In[4]:

# анализ запроса
# print (dkow) # сейчас время
dfrom = datetime.fromtimestamp(df.tail(1)['Timestamp']) # время первой сделки в датафрейме 
dto = datetime.fromtimestamp(df.iloc[1]['Timestamp']) # время последней сделки 
dkow = datetime.now() - timedelta(hours=3) # время сейчас с учетом отставания 3 часа
print (dkow - dto) # отставание последних данных
print (dto - dfrom) # за сколько данные смотри hid


# In[5]:

newdf = df; newdf['Inbtc'] = newdf['Price'] * newdf['Amount'] # новый столбец цена в BTC
newdf['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s') # перевод даты
print ('--------------TO-----------------')
print (newdf.iloc[1]['Timestamp']) # начальное время
print ('-------------FROM----------------')
print (newdf.tail(1)['Timestamp'])
print('---------------END----------------')


# In[6]:

# Way One Last DATA
newindex = newdf.set_index(df['Timestamp'])
dfnew = newindex.resample('1Min').agg({'Price': 'mean', 'Amount': 'sum', 'Inbtc': 'sum', 'Total': 'sum'})# .head()
# dfnew['Price'].plot(color='blue',grid=True, secondary_y=True)
# dfnew['Total'].plot(color='gray',grid=True)
# plt.show()


# In[7]:

# загружаем нашу базу 
dfload = pd.DataFrame.from_csv(path='data.csv')
#dfload.tail()#)#.index)
#print (dfnew.tail())#.index)


# In[8]:

dfcc = pd.concat([dfload, dfnew]) # ; dfcc.tail() # сливаем


# In[9]:

# dfcc['Price'].plot(color='blue',grid=True, secondary_y=True)
# dfcc['Total'].plot(color='gray',grid=True)
# plt.show()


# In[10]:

dfcc.to_csv(path_or_buf='data.csv')


# In[11]:

print('-------- Last DATA Hour --------')
print(dfcc.tail(1).index)
print('-------- Last DATA Hour --------')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



