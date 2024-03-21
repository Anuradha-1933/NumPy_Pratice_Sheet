# from numpy import random

# x = random.normal(size=(3, 3))

# print(x)

# Matplotlib  is a plotting library for the Python programming language
# import matplotlib
# print(matplotlib.__version__)
# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# draw a line where number and their square of relation are shown
# (1,20)
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.arange(1,21)
# y=np.arange(1,21)**2
# plt.plot(x,y, 'o')
# plt.scatter(x,y)
# plt.show()

# multiple points
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints=np.array([1,4,5,6])
# ypoints=np.array([3,9,7,8])
# plt.plot(xpoints,ypoints)
# plt.show()

# Default X-point 
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([2,7,8,9])
# plt.plot(ypoints,marker='*')
# plt.show()

#  line style
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linestyle = 'dashed')
# plt.show()

# line coloring
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([2,7,6,1,8])
# plt.plot(ypoints,c='red')
# plt.show()

# line width
# import matplotlib.pyplot as plt
# import numpy as np
# ypoints=np.array([2,7,6,1,8])
# plt.plot(ypoints,lw='10.5')
# plt.show()

# multiple line 
# import matplotlib.pyplot as plt
# import numpy as np
# y1=np.array([2,7,6,1,8])
# y2=np.array([2,5,4,6,3])
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x1=np.array([0,9,4,5,7])
# x2=np.array([3,5,7,1,2])
# y1=np.array([2,7,6,1,8])
# y2=np.array([2,5,4,6,3])
# plt.plot(x1)
# plt.plot(x2)
# plt.plot(y1)
# plt.plot(y2)
# plt.show()

# Label 
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([2,4,6,8,10,12,14,16])
# y=np.array([3,6,9,12,15,18,21,24])
# plt.plot(x,y)
# plt.xlabel('X-axis')
# plt.ylabel('y-axis')
# plt.show()

# LABEL-title 
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([2,4,6,8,10,12,14,16])
# y=np.array([3,6,9,12,15,18,21,24])
# plt.plot(x,y)
# plt.title("My Graph")
# plt.xlabel('X-axis')
# plt.ylabel('y-axis')
# plt.show()

# lebel-color and font 
# import numpy as np
# import matplotlib.pyplot as plt
# x=np.array([4,3,2,6])
# y=np.array([4,7,3,8])
# font1={"family":"serif","color":"pink","size":25}
# plt.title("function", fontdict=font1,loc="right")
# plt.xlabel("x-axis",fontdict=font1)
# plt.ylabel("y-axis",fontdict=font1)
# plt.plot(x,y)
# plt.show()

# Grid 
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([3,6,5,7])
# y=np.array([5,6,4,3])
# plt.title("Funvtion")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.plot(x,y)
# plt.grid()
# plt.grid(axis='y')
# plt.grid(color="purple",linestyle="-",linewidth="3.5")
# plt.show()

# Subplot
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([3,4,5,7])
# y=np.array([5,6,7,8])
# plt.subplot(1,1,1)
# plt.plot(x,y)

# x=np.array([3,6,9,10])
# y=np.array([5,6,7,8])
# plt.subplot(2,1,2)
# plt.plot(x,y)

# x=np.array([3,6,8,9])
# y=np.array([5,6,9,10])
# plt.subplot(3,1,3)
# plt.plot(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.title("My shop")
# plt.subplot(1, 2, 1)
# plt.plot(x,y)
#plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])
# plt.title("My adv")
# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.suptitle("My function")
# plt.show()

# Scatter plots
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])
# plt.scatter(x,y)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([3,5,8,9])
# y=np.array([6,7,8,9])
# plt.scatter(x,y,color='pink')
# x=np.array([3,2,4,5])
# y=np.array([4,6,7,9])
# plt.scatter(x,y,color='green')
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])
# plt.scatter(x, y, c=colors)
# plt.show()

# size
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([4,5,6,7])
# y=np.array([4,5,6,7])
# colors = np.array(["red","green","blue","yellow"])
# sizes=np.array([40,20,70,90])
# plt.scatter(x,y,c=colors,s=sizes,alpha=0.5)
# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.randint(100,size=(100))
# y=np.random.randint(100,size=(100))
# colors=np.random.randint(100,size=(100))
# sizes=10*np.random.randint(100,size=(100))
# plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap='nipy_spectral')
# plt.colorbar()
# plt.show()

# BAR 
# import matplotlib.pyplot as plt
# import numpy as np
# x=["A","B","C","D"]
# y=[1,2,3,4]
# plt.bar(x,y)
# plt.show()

# BARH created with horizontal
# import matplotlib.pyplot as plt
# import numpy as np
# x=["A","B","C","D"]
# y=[8,6,4,2]
# plt.barh(x,y,color="purple")
# plt.bar(x,y,width=0.1)
# plt.barh(x,y,height=0.2)
# plt.show()

# Histogram
# import matplotlib.pyplot as plt
# import numpy as np
# x=np.random.normal(20,40,30)
# plt.hist(x)
# plt.show()

# Pie chart
import matplotlib.pyplot as plt
import numpy  as np
x=np.array([34,8,4,1])
plt.pie(x)
plt.show()





