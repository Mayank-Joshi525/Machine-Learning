import tensorflow as tf
from tensorflow.keras import layers, models

# Define the CNN model
model = models.Sequential()

# Add a convolutional layer with 32 filters, each of size 3x3, and input shape of (28, 28, 1)
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))

# Add a max pooling layer
model.add(layers.MaxPooling2D((2, 2)))

# Add another convolutional layer with 64 filters
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Add another max pooling layer
model.add(layers.MaxPooling2D((2, 2)))

# Flatten the output to feed into a densely connected layer
model.add(layers.Flatten())

# Add a densely connected layer with 64 neurons
model.add(layers.Dense(64, activation='relu'))

# Add an output layer with 10 neurons for 10 classes (assuming it's a classification task)
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Display the architecture of the model
model.summary()
