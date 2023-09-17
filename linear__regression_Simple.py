#!/usr/bin/env python
# coding: utf-8

# In[6]:


data = [(1, 8), (2, 16), (3, 24), (4, 36), (5, 40)]


# In[7]:


sum_x = 0
sum_y = 0
sum_xy = 0
sum_x_squared = 0


# In[8]:


for x, y in data:
    sum_x += x
    sum_y += y
    sum_xy += x * y
    sum_x_squared += x ** 2


# In[9]:


n = len(data)
slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
intercept = (sum_y - slope * sum_x) / n


# In[10]:


print(f"Equation of the line: y = {slope:.2f}x + {intercept:.2f}")

