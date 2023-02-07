import numpy as np

a=[1,2,3] #input
b=[4,4,6] #weight

a=np.array([a])
b=np.array([b]).T # perform a traspose operation to turn our row to a column
result=np.dot(a,b)
print(result)

#NB// numpy does not have a dedicated method for both
  # matrix-product and dot-product they all share the .dot() method
#Let’s get back to our inputs and weights — when covering them, 
# we mentioned that we need to
#perform dot products on all of the vectors that consist of both input and 
# weight matrices. As we
#have just learned, that’s the operation that the matrix product performs. 
# We just need to perform
#transposition on its second argument, which is the weights matrix in our case, 
# to turn the row
#vectors it currently consists of into column vectors
import numpy as np
inputs = [[1.0, 2.0, 3.0, 2.5],
 [2.0, 5.0, -1.0, 2.0],
 [-1.5, 2.7, 3.3, -0.8]]
weights = [[0.2, 0.8, -0.5, 1.0],
 [0.5, -0.91, 0.26, -0.5],
 [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]
weights = np.array(weights).T
layer_outputs = np.dot(inputs,weights ) + biases
print('layer output',layer_outputs)

