import numpy as np

a=[1,2,3]

array = np.array([a])

print(array)

b=[1,2,3]
array1=np.expand_dims(np.array(b),axis=0)
print(array1)