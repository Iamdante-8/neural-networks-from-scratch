#########
#A dot product of two vectors is a sum of products of consecutive vector elements. 
# Both vectors must be of the same size (have an equal number of elements).
#Let’s write out how a dot product is calculated in Python. 
# For it, you have two vectors, which we
# can represent as lists in Python. We then multiply their elements 
# from the same index values and
# then add all of the resulting products. 
# Say we have two lists acting as our vectors:
#########
a = [1,2,3]
b = [2,3,4]

# To obtain the dot product

dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print('The dot product is : ',dot_product)
