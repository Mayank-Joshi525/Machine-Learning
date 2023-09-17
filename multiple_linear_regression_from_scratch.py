#!/usr/bin/env python
# coding: utf-8

# In[12]:


# Sample data: (x1, x2, y)
data = [
    (2, 3, 7),
    (3, 4, 11),
    (4, 5, 15),
    (5, 6, 19),
    (6, 7, 23)
]

# Initialize variables
learning_rate = 0.01
num_iterations = 1000

# Initialize coefficients (b0, b1, b2)
b0 = 0.0
b1 = 0.0
b2 = 0.0

# Perform gradient descent
for _ in range(num_iterations):
    gradient_b0 = 0
    gradient_b1 = 0
    gradient_b2 = 0
    
    for x1, x2, y in data:
        y_pred = b0 + b1 * x1 + b2 * x2
        
        gradient_b0 += -(2 / len(data)) * (y - y_pred)
        gradient_b1 += -(2 / len(data)) * x1 * (y - y_pred)
        gradient_b2 += -(2 / len(data)) * x2 * (y - y_pred)
    
    b0 -= learning_rate * gradient_b0
    b1 -= learning_rate * gradient_b1
    b2 -= learning_rate * gradient_b2

# Print the coefficients
print(f"Coefficients: b0 = {b0:.2f}, b1 = {b1:.2f}, b2 = {b2:.2f}")


# In[ ]:





# In[ ]:




