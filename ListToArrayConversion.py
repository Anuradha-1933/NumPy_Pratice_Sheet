# Problem: Convert a Python list to a NumPy array, preserving data types while handling various data types, empty
# lists, and mixed data types. 

import numpy as np
lst=[1,'a',9,True,'b',5]
int1=[]
s=[] #string
b=[] #boolean 
for x in lst:
    if type(x)==int:
        int1.append(x)
    if type(x)==str:
        s.append(x)
    if type(x)==bool:
        b.append(x)
arr1=np.array(int1)
arr2=np.array(s)
arr3=np.array(b)
print(arr1)
print(arr2)
print(arr3)


