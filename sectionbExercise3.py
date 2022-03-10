# -*- coding: utf-8 -*-
"""
@author: María Pérez Martínez
"""

import numpy as np
import matplotlib.pyplot as plt
 
#variable that I change to find the different conditions
n = 0.28

#constant
gamma = 10

#This function represents the Helmholtz free energy divided by T
def F(V):
    
    N = n*V
    
    #Two vectors with 1000 values that go from 0 to N
    Nx = np.linspace(0,N,1000)#x orientation of the rods
    Ny = np.linspace(0,N,1000)#y orientation of the rods
    
    #Command that allows to create two matrices filled with Nx and Ny respectively 
    NX,NY = np.meshgrid(Nx,Ny)
    
    #Creation of a matrix full of ones with 1000 rows and colums
    f = np.ones([1000,1000])
    
    #With the following loop all the rows and columns of the previous matrix are traversed and filled with Helmholzts free energy (divided by T)
    for i in range (0, 1000):
        for j in range (0, int(1000-i)):
            
            f[i,j] = NX[i,j]*np.log(NX[i,j]/V) + NY[i,j]*np.log(NY[i,j]/V)+ (N - NX[i,j] -NY[i,j])*np.log((N-NX[i,j]-NY[i,j])/V)+gamma*(NX[i,j]*NY[i,j]+NY[i,j]*(N-NX[i,j]-NY[i,j])+(N-NX[i,j]-NY[i,j])*NX[i,j])/V
             
    return(f, NX, NY)
    
#In the X, Y and Z axis Nx, Ny and Helmholtz free energy divided by T are plotted respectively
plt.contourf(F(1e10)[1], F(1e10)[2], F(1e10)[0], 20, cmap = 'RdGy')
plt.colorbar()
plt.xlabel(r'$N_x$')
plt.ylabel(r'$N_y$')
plt.title(r'F/T as a function of $N_x$ vs $N_y$')
plt.savefig("fig.pdf")
        