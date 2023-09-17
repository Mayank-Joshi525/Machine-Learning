#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Generate some sample data
np.random.seed(0)
data = np.random.rand(10, 2)

# Perform hierarchical clustering
linked = linkage(data, method='single')  # You can choose a different linkage method (e.g., 'complete', 'average')

# Create a dendrogram
plt.figure(figsize=(10, 5))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Data Points')
plt.ylabel('Distance')
plt.show()


# In[ ]:





# In[ ]:




