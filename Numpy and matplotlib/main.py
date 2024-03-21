# import numpy
# arr=numpy.array([1,2,3,4])
# print(arr)

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)

# import numpy as np
# print(np.__version__)

# LIST 
# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr)
# print(type(arr))

# TOUPLE
# import numpy as np
# arr=np.array((1,2,3,4))
# print(arr)
# print(type(arr))

# import numpy as np
# arr=np.array(34)
# print(arr)

# import numpy as np

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# import numpy as np

# arr = np.array([1, 2, 3, 4], ndmin=5)

# print(arr)
# print('number of dimensions :', arr.ndim)

# import numpy as np
# arr=np.array([2,3,4,5])
# print(arr[0])

# import numpy as np
# arr=np.array([[2,3,4,5],[3,2,1,5]])
# print(arr[0][1])

# import numpy as np
# arr=np.array([[[2,3,4,5],[3,2,1,5],[2,1,3,2],[1,2,4,2]]])
# print(arr[0,1,2])

# import numpy as np
# arr=np.array([1,3,2,4])
# print(arr[1:2])

# import numpy as np
# arr=np.array([1,3,2,4,6,5,3])
# print(arr[1:5:2])

# import numpy as np
# arr=np.array([1,2,3,4])
# print(arr.dtype)

# import numpy as np

# arr = np.array(['apple', 'banana', 'cherry'])

# print(arr.dtype)

# import numpy as np
# a=np.array([2.3,1.3,1.4])
# newa=a.astype("i")
# print(newa)
# print(newa.dtype)

# import numpy as np
# arr=np.array([[1,2,3,4],[4,5,6,7]])
# print(arr.shape)

# import numpy as np
# arr=np.array([1,2,3,4],ndmin=5)
# print(arr.shape)

# import numpy as np
# arr=np.array([1,2,3,4])
# for x in np.nditer(arr):
#     print(x)

# import numpy as np
# arr=np.array([1,2,3,4])
# for x in np.nditer(arr,flags=["buffered"],op_dtypes="S"):
#     print(x)

import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([4,5,6,7])
arr=np.concatenate((arr1,arr2),axis=0)
print(arr)