import numpy as np

layer1_inputs = np.array([[3, 1, 4], [6, -2, 1.5]])
layer1_weights = np.array([[2, -5, 0.6], [4, 0.2, 1.2], [0.25, -3, 2.2]])
layer1_biases = np.array([2.5, 3, 1.2])

layer1_output = np.dot(layer1_inputs, layer1_weights.T) + layer1_biases

print(layer1_output)

layer2_weights = np.array([[2.1, 0.56, -2.5], [2, -1.9, 4.1]])
layer2_biases = np.array([-2.5, 0.92])

layer2_output = np.dot(layer1_output, layer2_weights.T) + layer2_biases

print(layer2_output)
