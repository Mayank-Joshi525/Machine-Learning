#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas



# In[14]:


df = pandas.read_csv("data.csv")


# In[15]:


X = df[['Weight', 'Volume']]
y = df['CO2']



# In[16]:


from sklearn import linear_model



# In[17]:


regr = linear_model.LinearRegression()
regr.fit(X, y)


# In[19]:


predictedCO2 = regr.predict([[2300, 1300]])
print(predictedCO2)


# In[ ]:




