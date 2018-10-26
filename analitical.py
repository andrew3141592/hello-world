import numpy as np
import scipy


def int_nn_bias(shape):
##Shape is an array of lenght=number of layers of nn
    count=0
    bias=[]
    for size in shape:
        lweights=np.zeros(size)
        bias.append(lweights)
        count+=count
    return bias

def fully_conected_network(shape):
    count=0
    weights=[]
    for size in shape:
        
        if count>0.:
            lweights=np.zeros((size,size_pre))
            weights.append(lweights)
        count=count+1
        
        size_pre=size
        
    return weights
shape=[3,2,1,3]
print int_nn_bias(shape)
print fully_conected_network(shape)
