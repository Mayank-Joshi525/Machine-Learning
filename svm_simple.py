#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

# Define the SVM training function
def train_svm(X, y, learning_rate=0.01, num_epochs=1000):
    num_samples, num_features = X.shape

    # Initialize weights and bias
    weights = np.zeros(num_features)
    bias = 0

    # Training the SVM using gradient descent
    for _ in range(num_epochs):
        for i in range(num_samples):
            if y[i] * (np.dot(X[i], weights) - bias) >= 1:
                # Correctly classified point, update weights and bias
                weights -= learning_rate * (2 * 1 / num_epochs * weights)
            else:
                # Misclassified point, update weights and bias
                weights -= learning_rate * (2 * 1 / num_epochs * weights - np.dot(X[i], y[i]))
                bias -= learning_rate * y[i]

    return weights, bias

# Define the SVM prediction function
def predict_svm(X, weights, bias):
    # Predict class labels for input data
    linear_output = np.dot(X, weights) - bias
    return np.sign(linear_output)

# Sample data for binary classification (linearly separable)
X = np.array([[1, 2], [2, 3], [3, 4], [5, 5], [4, 3], [6, 4]])
y = np.array([1, 1, 1, -1, -1, -1])

# Train the SVM and get weights and bias
learned_weights, learned_bias = train_svm(X, y, learning_rate=0.01, num_epochs=1000)

# Test the model with new data
new_data = np.array([[2, 2], [4, 4]])
predictions = predict_svm(new_data, learned_weights, learned_bias)

print("Predictions:", predictions)


# In[ ]:





# In[ ]:




