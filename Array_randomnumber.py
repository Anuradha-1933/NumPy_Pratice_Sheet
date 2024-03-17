# Problem: Create functions for arrays filled with zeros, ones, or custom values, allowing optional shape specification
# and handling invalid inputs. 


import numpy as np

def zeros(shape=(1,), dtype=float):
    try:
        return np.zeros(shape, dtype=dtype)
    except TypeError:
        print("Invalid input for shape. Shape must be a tuple.")
        return None

def ones(shape=(1,), dtype=float):
    try:
        return np.ones(shape, dtype=dtype)
    except TypeError:
        print("Invalid input for shape. Shape must be a tuple.")
        return None

def custom_values(value, shape=(1,), dtype=None):

    try:
        return np.full(shape, value, dtype=dtype)
    except TypeError:
        print("Invalid input for shape. Shape must be a tuple.")
        return None
print("Zeros array:")
print(zeros((3, 4), dtype=int))

print("\nOnes array:")
print(ones((2, 3, 2)))

print("\nCustom values array:")
print(custom_values(5, (2, 3), dtype=float))

print("\nInvalid input handling:")
print(zeros("invalid_shape"))
