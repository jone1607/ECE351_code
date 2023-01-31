# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 13:47:55 2023

@author: jedjj
"""

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({ 'font.size' :  14})

steps = 1e-2
t = np.arange(0,10+steps, steps)

print('number of elements: len(t) =', len(t), '\nFirst Element: t[0] =',
      t[0], '\nlast Element: t[len(t)-1] =', t[len(t)-1])

            
def u(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c= (1e-2)*i 
        if c < 0:
            
            y[i] = 0
            
        if c > 0:
                
            y[i] = .5*c
        if c>3:
            y[i] = 8
        if c > 6:
            y[i] = 18-2*c
    return y

def one(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c= (1e-2)*i 
        if c > 0:
            
            y[i] = (2*c)-2
            
        if c > 3:
                
            y[i] = 8
        if c>6:
            y[i] = 7-0.5*c
        if c > 9:
            y[i] = 0
    return y


            
def example1(t):
    y = np.zeros(t.shape)
    
    for i in range(len(t)):
        x= (1/4)*i 
        if x < 0:
            
            y[i] = 0
            
        if x > 0:
                
            y[i] = .5*x
        if x>3:
            y[i] = 8
        if x > 6:
            y[i] = 18-2*x
           
    return y 

def two(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c= (1e-2)*i 
        if c < 0:
            
            y[i] = 0
            
        if c > 0:
                
            y[i] = .5*c
        if c>3:
            y[i] = 8
        if c > 6:
            y[i] = 18-2*c
    return y

t = np.arange(0, 10 + steps, steps)
y = u(t)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t) with Good Resolution')
plt.title('plot for lab 2')

t = np.arange(0, 10 + 0.25, 0.25)
y= example1(t)

plt.subplot(2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t) with poor resolution')
plt.xlabel('t')
plt.show()


t = np.arange(0, 10 + steps, steps)
y = example1(t)
plt.figure(figsize = (10, 10))
plt.subplot (3, 1, 3)
plt.plot(-t, y)
plt.grid()
plt.ylabel('y(t) reflected')
plt.title('plot for lab 2')


t = np.arange(0, 10 + steps, steps)
y = two(t)
plt.figure(figsize = (15, 10))
plt.subplot (2, 1, 2)
plt.plot(-t-4, y)
plt.grid()
plt.ylabel('y(t) time shift(-4)')
plt.title('plot for lab 2')

t = np.arange(0, 10 + steps, steps)
y = two(t)
plt.figure(figsize = (15, 10))
plt.subplot (2, 1, 2)
plt.plot(t+4, y)
plt.grid()
plt.ylabel('y(t) time shift(+4)')
plt.title('plot for lab 2')


t = np.arange(0, 10 + steps, steps)
y = two(t)
plt.figure(figsize = (15, 10))
plt.subplot (2, 1, 2)
plt.plot(t/2, y)
plt.grid()
plt.ylabel('y(t) time scaling(1/2)')
plt.title('plot for lab 2')

t = np.arange(0, 10 + steps, steps)
y = two(t)
plt.figure(figsize = (15, 10))
plt.subplot (2, 1, 2)
plt.plot(t*2, y)
plt.grid()
plt.ylabel('y(t) time scaling (x2)')
plt.title('plot for lab 2')

