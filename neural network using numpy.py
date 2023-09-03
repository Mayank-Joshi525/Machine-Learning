#!/usr/bin/env python
# coding: utf-8

# In[11]:


# neural network using numpy 

import numpy as np

# Define sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Define sigmoid derivative for backpropagation
def sigmoid_derivative(x):
    return x * (1 - x)

# Input data (features)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Target labels
y = np.array([[0], [1], [1], [0]])

# Seed random numbers for reproducibility
np.random.seed(42)

# Initialize weights randomly with mean 0
input_layer_size = 2
hidden_layer_size = 3
output_layer_size = 1

# Initialize weights randomly with mean 0
weights_input_hidden = np.random.uniform(-1, 1, (input_layer_size, hidden_layer_size))
weights_hidden_output = np.random.uniform(-1, 1, (hidden_layer_size, output_layer_size))

# Learning rate
learning_rate = 0.1

# Number of training iterations
num_iterations = 10000

# Training loop
for iteration in range(num_iterations):
    # Forward propagation
    hidden_layer_input = np.dot(X, weights_input_hidden)
    hidden_layer_activation = sigmoid(hidden_layer_input)
    
    output_layer_input = np.dot(hidden_layer_activation, weights_hidden_output)
    output_layer_activation = sigmoid(output_layer_input)
    
    # Compute error
    error = y - output_layer_activation
    
    # Backpropagation
    d_output = error * sigmoid_derivative(output_layer_activation)
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_activation)
    
    # Update weights
    weights_hidden_output += hidden_layer_activation.T.dot(d_output) * learning_rate
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate

# Test the trained model
test_data = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
predicted_output = sigmoid(np.dot(sigmoid(np.dot(test_data, weights_input_hidden)), weights_hidden_output))

print("Predicted Output:")
print(predicted_output)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




