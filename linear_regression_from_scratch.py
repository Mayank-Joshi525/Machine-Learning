#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as mayank
import numpy as joshi
from scipy import stats


# In[6]:


data = [(1, 8), (2, 16), (3, 24), (4, 32), (5, 40)]
x=[]
y=[]
for i in range(len(data)):
    x.append(data[i][0])
    y.append(data[i][1])
slope,intersecpt,r,p,std_err=stats.linregress(x,y)
# if r=1  -> 100% relation
# r ranges from -1 to 1

# In[7]:


mayank.scatter(x,y)
mayank.show()


# In[8]:


print(r)
print(slope)


# In[ ]:




