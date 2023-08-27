#!/usr/bin/env python
# coding: utf-8

# In[26]:


import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))
speed=myfunc(10)
print(speed)
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()


# In[14]:





# In[15]:





# In[16]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




