# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:09:50 2023

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


def u(t,r,v): # basic ramp function for use in complicated math
    y = np.zeros(t.shape) 
    for i in range(len(t)):
        
        t= (1e-2)*i
        if t< v:
            y[i] = 0
        if t > r :
            y[i]=1
    return y

def r(t,r): # ramp function for further use
    y = np.zeros(t.shape)
    for i in range(len(t)):
        a= (1e-2)*i
        if a< r:
            y[i] =0
        if a > r:
            y[i]=a-r
    return y

def h1(t,r): # for use in a convolution function
    y = np.zeros(t.shape) 
    for i in range(len(t)):
        tmp = (1e-2)*i
        if tmp < r:
            y[i] = 0
        if tmp > r:
            y[i] = (np.exp(-2*tmp))
        if tmp > 13:
            y[i] = 0
    return y

def h2(t, r):# for use in a convolution function
    y = np.zeros(t.shape) 
    for i in range(len(t)):
        tmp= (1e-2)*i
        if tmp>12:
            y[i] = 1
        if tmp > 16:
            y[i]=0
    return y

def h3(t, r):# for use in a convolution function
    y = np.zeros(t.shape) 
    for i in range(len(t)):
        tmp= (1e-2)*i
        if tmp<r:
            y[i] = 0
        if tmp > r:
            y[i]= (-1)*np.cos(1.5708*tmp)
    return y

def c(t,r):# the convolution with time shift.
    y = np.zeros(t.shape) 
    for i in range(len(t)):
     tmp= (1e-2)*i
     if tmp < r:
        y[i]= 0
     if tmp > r:
         y[i] = 0.5*tmp*np.exp(-2*tmp) * np.sin(1.5708*tmp)
    return y
    
    
    
plt.rcParams.update({ 'font.size' :  14})
steps = 1e-2

t = np.arange(-10, 10 + steps, steps)
y = h1(t,10)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('h1(t)')
plt.show()

t = np.arange(-10, 10 + steps, steps)
y = h2(t,r)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('h2(t)')
plt.show()

t = np.arange(-10, 10 + steps, steps)
y = h3(t,10)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('h3(t)')
plt.show()

t = np.arange(-10, 10 + steps, steps)
y = c(t,12)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.xlabel('t')
plt.title('Convolution of all functions')
plt.show()