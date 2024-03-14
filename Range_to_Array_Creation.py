# Problem: Explore np.arange and np.linspace for array creation, explaining key differences, inclusivity of endpoints,
# step size control, and when to use each. 

# np.arange():
#     np.arange() generates an array of evenly spaced values within a given range.
#     Syntax: np.arange(start, stop, step)
#     Parameters:
#   start: Start of the interval (inclusive).
#   stop: End of the interval (exclusive).
#   step: Step size between values.
#   Endpoint inclusivity: The stop value is not included in the array.
#   Step size control: You can specify the step size between values.
# Example)-
import numpy as np
arr=np.arange(0,10,2)
print(arr)

# np.linspace():
# np.linspace() generates an array of evenly spaced values over a specified interval.
# Syntax: np.linspace(start, stop, num)
# Parameters:
# start: Start of the interval.
# stop: End of the interval.
# num: Number of samples to generate.
# Endpoint inclusivity: By default, both the start and stop values are included in the array. You can control inclusivity using the endpoint parameter (default is True).
# Step size control: The step size is automatically determined based on the number of samples (num) and the interval.
# Example:

arr1=np.linspace(0,10,8)
print(arr1)

# Key Differences:

# np.arange() allows you to specify the step size directly, while np.linspace() determines the step size automatically based on the number of samples.
# In terms of inclusivity of endpoints, np.arange() excludes the stop value, while np.linspace() includes both start and stop values by default (but can be controlled using the endpoint parameter).