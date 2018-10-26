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

def activation_func(array):
    return

def forward(input,weights,shape):
    if len(input)>shape[0]:
        print "input wrong shape"

    for layer in weights:
        print input
        input=np.matmul(input, layer)

    return input


shape=[3,2,1]

bias= int_nn_bias(shape)
weights= fully_conected_network(shape)
input=np.array([1.,1.,1.])
print forward(input,weights,shape)
