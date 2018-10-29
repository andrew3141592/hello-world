import numpy as np
import scipy


def int_nn_bias(shape):
##Shape is an array of lenght=number of layers of nn
    count=0
    bias=[]
    for size in shape:
        lweights=np.ones(size)
        bias.append(lweights)
        count+=count
    return bias

def fully_conected_network(shape):
    count=0
    weights=[]
    for size in shape:
        
        if count>0.:
            lweights=np.ones((size_pre,size))
            weights.append(lweights)
        count=count+1
        
        size_pre=size
        
    return weights

def sigmoid(x):
    s = 1./(1.+np.exp(-x))
    return s

def activation_func(array):
    return

def forward(input,weights,shape):
    if len(input)>shape[0]:
        print "input wrong shape"

    for layer in weights:
        print input
        input=sigmoid(np.matmul(input, layer))

    return input

def cost_func(test_out,correct_out):
    cost=sum((test_out-correct_out)**2)
    return cost

def gradiant_of_decent(weights,bias,shape,cost,step_size):
    return step

shape=[3,2,1]

bias= int_nn_bias(shape)
weights= fully_conected_network(shape)
input=np.array([1.,1.,1.])

print forward(input,weights,shape)
print cost_func(forward(input,weights,shape),np.array([1.]))
