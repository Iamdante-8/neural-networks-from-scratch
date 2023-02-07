inputs = [1, 2, 3] #The input data which passed to attain a desired output
#The weight is what is trained in neural networks
weights = [0.2, 0.8, -0.5]
#The bias is an additional tunable value but is not associated with 
# any input in contrast to the weights.
bias = 2

#This neuron sums each input multiplied by that input’s 
# weight, then adds the bias
output = (inputs[0]*weights[0] +
inputs[1]*weights[1] +
inputs[2]*weights[2] + bias)
print('The output is :',output)

#The output should be 2.3
inputs1 = [1.0, 2.0, 3.0, 2.5]
weights1 = [0.2, 0.8, -0.5, 1.0]
bias1 = 2.0
output1 = (inputs1[0]*weights1[0] +
inputs1[1]*weights1[1] +
inputs1[2]*weights1[2] +
inputs1[3]*weights1[3] + bias1)
print('Output 2 is:',output1)


