# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:32:00 2023

@author: jedjj
"""

import numpy
import scipy.signal
import time



t = 1
print(t)
print("t =",t)
print('t =',t,"seconds")
print('t is now =', t/3,"\n . . . and can be rounded using 'round()'", round(t/3,4));


print(3**2)


list1 = [0,1,2,3]
print('list1:' ,list1)
list2 = [[0] ,[1] , [2], [3]]
print('list2:' , list2)
list3 = [[0,1] ,[2 ,3]]
print('list3:' , list3)
array1 =numpy. array ([0,1,2,3])
print('array1', array1)
array2 = numpy.array ([[0] ,[1], [2] , [3]])
print('array2', array2)
array3 = numpy.array ([[0,1],[2,3]])
print('array3:',array3)


import numpy as np

print(np.pi)

print(np.arange(4), '\n', np.arange(0,2,0.5), '\n', np.linspace(0,1.5,4))



print('1x3:',np.zeros(3))
print('2x2:',np.zeros((2,2)))
print('2x3:',np.ones((2,3)))



import matplotlib.pyplot as plt
steps = 0.1
x = np.arange(-2, 2 +steps,steps)

y1 = x + 2
y2 = x**2

plt.figure(figsize=(12,8))

plt.subplot(3,1,1)
plt.plot(x,y1)
plt.title('sample plots for lab 1')

plt.ylabel('Subplot 1')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(x,y2)

plt.ylabel('subplot 2')
plt.grid(which='both')

plt.subplot(3,1,3)
plt.plot(x,y1,'--r',label = 'y1')

plt.plot(x,y1,'0', label = 'y2')
plt.axis([-2.5, 2.5, -0.5, 4.5])
plt.grid(True)
plt.legend(loc='lower right')
plt.xlabel('x')
plt.ylabel('subplot 3')
plt.show()






