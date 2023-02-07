import numpy as np
inputs = [1.0, 2.0, 3.0, 2.5]
weights = [0.2, 0.8, -0.5, 1.0]
bias = 2.0
outputs = np.dot(weights, inputs) + bias
print('Dot Notation using NumPy: ',outputs)

# a list of lists basically a matrix
inputs1 = [1.0, 2.0, 3.0, 2.5]
weights1 = [[0.2, 0.8, -0.5, 1],
[0.5, -0.91, 0.26, -0.5],
[-0.26, -0.27, 0.17, 0.87]]
biases1 = [2.0, 3.0, 0.5]
layer_outputs = np.dot(weights1, inputs1) + biases1
print('layered output is:',layer_outputs)

