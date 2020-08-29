#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Global_Mobility_Report.csv')
data.head(n=3)

uaeData = data[data['country_region'].str.contains('United Arab Emirates')]
uaeData.head(n=5)


# In[15]:


from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode()
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


dataset= uaeData
dataset.describe(include='O')

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataset.iloc[:,10] = le.fit_transform(dataset.iloc[:,10])
dataset.head(2)

X= dataset[['country_region', 'date','retail_and_recreation_percent_change_from_baseline', 'grocery_and_pharmacy_percent_change_from_baseline']]
y= dataset.iloc[:,1]


# In[21]:


train_dataset= pd.DataFrame()
train_dataset['ds'] = pd.to_datetime(X["date"])
train_dataset['y']= X['retail_and_recreation_percent_change_from_baseline']
train_dataset.head(2)

prophet_basic = Prophet()
prophet_basic.fit(train_dataset)

future= prophet_basic.make_future_dataframe(periods=25)
future.tail(2)


# In[28]:


forecast=prophet_basic.predict(future)
fig1 =prophet_basic.plot(forecast)
fig1 = prophet_basic.plot_components(forecast)
from fbprophet.plot import add_changepoints_to_plot
fig = prophet_basic.plot(forecast)
a = add_changepoints_to_plot(fig.gca(), prophet_basic, forecast)


# In[23]:


pro_change= Prophet(changepoint_range=0.9)
forecast = pro_change.fit(train_dataset).predict(future)
fig= pro_change.plot(forecast);
a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)

plt.title('United Arab Emirates: No seasonality included')


# In[25]:


pro_change= Prophet(n_changepoints=20, yearly_seasonality=True)
forecast = pro_change.fit(train_dataset).predict(future)
fig= pro_change.plot(forecast);
a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)

plt.title('United Arab Emirates: Yearly Seasonality Included')


# In[26]:


pro_change= Prophet(n_changepoints=50, daily_seasonality=True)
forecast = pro_change.fit(train_dataset).predict(future)
fig= pro_change.plot(forecast);
a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)

plt.title('United Arab Emirates: Daily Seasonality Included')


# In[27]:


pro_change= Prophet(n_changepoints=50, yearly_seasonality = True, daily_seasonality=True)
forecast = pro_change.fit(train_dataset).predict(future)
fig= pro_change.plot(forecast);
a = add_changepoints_to_plot(fig.gca(), pro_change, forecast)

plt.title('United Arab Emirates: Both Daily and Yearly Seasonality Included')


# In[29]:


prophet_basic.changepoints


# In[ ]:




