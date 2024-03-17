# Problem: Create functions for arrays with random numbers from uniform and normal distributions, allowing
# shape/sample specification and providing distribution explanations. 

import numpy as np
def uniform_random(shape=(1,2),low=0,high=1):
    return np.random.uniform(low,high,size=shape)
def  normal_random(shape=(1,2),mean=0,std=1):
    return np.random.normal(mean,std,size=shape)

# numpy.random.uniform(low=0.0, high=1.0, size=None) 
# Draw samples from a uniform distribution. 
# Samples are uniformly distributed over the half-open 
# interval [low, high) (includes low, but excludes high). 
# In other words, any value within the given interval is equally likely to be drawn by uniform.
print("Uniform Distribution Function")
print(uniform_random((5,4),low=10,high=20))

#  The normal distribution is symmetrical around its peak. Because of this symmetry,
# the mean of the distribution, often denoted by μ, is at that peak
print("\nNormal Distribution Function")
print(normal_random((3,6),mean=5,std=2))