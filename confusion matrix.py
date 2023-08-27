#!/usr/bin/env python
# coding: utf-8

# In[32]:


import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()


# In[14]:





# In[15]:





# In[16]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




