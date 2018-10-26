import numpy as np
import scipy


def int_nn_bias(shape):
##Shape is an array of lenght=number of layers of nn
    count=0
    weights=[]
    for size in shape:
        lweights=np.zeros(size)
        weights.append(lweights)
        count+=count
    return weights
print (int_nn_bias([1,2,1]))
