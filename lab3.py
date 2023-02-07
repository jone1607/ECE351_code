# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:48:16 2023

@author: jedjj
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

 

plt.rcParams.update({ 'font.size' :  14})

steps = 1e-2
t = np.arange(0,10+steps, steps)
q=1
n=0
def u(t,v):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        
        t= (1e-2)*i
        if t<0:
            y[i] = 0
        if t > r :
            y[i]=1
    return y

def r(t,r):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        a= (1e-2)*i
        
        if a > r:
            y[i]=a-r
    return y

def two(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c= (1e-2)*i 
        if c < 0:
            
            y[i] = 0
            
        if c > 0:
                
            y[i] = c
        if c>3:
            y[i] = 8
        if c > 6:
            y[i] = 18-2*c
    return y



def f1(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c= (1e-2)*i 
        if c < 0:
            
            y[i]= 0
            
        if c > 0:
           
            y[i] = 0
        if c >2:
            y[i]= 1
        if c >9 :
            y[i]=0
            
    return y

def f2(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c= (1e-2)*i 
        if c<0:
            
            y[i]= 0
        if c>0:
            y[i]= (2.71828)**(-c)
        
    return y

def f3(t):
    y = np.zeros(t.shape)
    for i in range(len(t)):
        c = (1e-2)*i
        if c <0:
            y[i]=0
        if c> 2:
            y[i]= 0.5*c-1
        if c>3:
            y[i]= (2-(0.5*c))
        if c>4:
            y[i] = 0
       
    return y

def p2(t):
    y= np.zeros(t.shape)
    for i in range(len(t)):
        c = (1e-2)*i
        if c>4:
          y[i]= c - 4
        if c>5:
            y[i]= 1
        if c>10:
            y[i]=10-0.9*c
        if c>=11:
            y[i] = 0
            
    return y
    
def p3(t):
    y= np.zeros(t.shape)
    for i in range(len(t)):
        c = (1e-2)*i
        if c>2:
          y[i]= (2.71828)**(-c)
        if c>9:
            y[i] =  0
    return y

def p4(t):
    y= np.zeros(t.shape)
    for i in range(len(t)):
        c = (1e-2)*i
        if c>2:
          y[i]= (2.71828)**(-c)
        if c>3:
            y[i]= -1*(2.71828)**(-c)
    return y



t = np.arange(0, 20 + steps, steps)
y = f3(t)
plt.figure(figsize = (10, 10))
plt.subplot (1, 1, 1)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.title('f3(t)')

t = np.arange(0, 20 + steps, steps)
y = f2(t)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.title('f2(t)')

t = np.arange(0, 20 + steps, steps)
y = f1(t)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.title('f1(t)')

t = np.arange(0, 20 + 0.00001, steps)
y = p2(t)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.title('f1**f3')

t = np.arange(0, 20 + 0.00001, steps)
y = p3(t)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.title('f1**f2')

t = np.arange(0, 20 + 0.00001, steps)
y = p4(t)
plt.figure(figsize = (10, 10))
plt.subplot (2, 1, 2)
plt.plot(t, y)
plt.grid()
plt.ylabel('y(t)')
plt.title('f3**f2')