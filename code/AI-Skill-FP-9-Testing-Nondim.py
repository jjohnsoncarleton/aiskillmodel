# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:40:32 2026

@author: jjohnson16

This is code testing the numerical thresholds

For stability of fixed points.

This tests FP 5 stability

Need to test cases:
    
Testing condition

M>0, wd>ws, smax > sp


"""

# data stuff
import numpy as np
import matplotlib.pyplot as plt

# ode function
from scipy.integrate import solve_ivp
# timer
#import time
#import cmath
#import dill 






# time scale for w
#a = 0.01
# time scale for s
b = 1
# time scale for P 
g = 1



#sai = 1.3*smax



# productivity skill threshold
#sp = smax/3

#sp = 1.2*smax



# Motivation Array
#Ms = np.array([Pmax/2, Pmax/2])
#M = 1/2
#sais = np.array([1.5*smax,1.5*smax])

# sai, sp, ws,M
param1 = np.array([[0.5, 0.25, 0.75,0.5],[0.5, 0.5,0.75,0],[0.5, 0.1,0.1,0]])

#M =1







# function for ODE
def fun(t,y):
  dwdt =  y[0]*(1-y[0])*(M-y[2]) # equation for dw/dt
  dsdt = b*(y[0]-ws)*(1-y[1])*y[1] # equation for ds/dt
  dPdt = g*((y[1]-sp)*y[0]+ ((sai-sp))*(1-y[0]))*(1-y[2])*y[2] # equation for dP/dt
  return [dwdt, dsdt, dPdt] # return array for dw/dt ds/dt


tspan = [0,10000]


paramshape= np.shape(param1)




fig, axs = plt.subplots(1,3, layout="constrained")
for i in range(paramshape[0]):
    sai,sp,ws,M= param1[i]
    w0 = 1-sp/sai
    s0 = 0
    P0 = M
    y0 = [w0, s0, P0]
    print(y0)
    
    perturb = np.array([np.random.uniform(-0.01,0.01), np.random.uniform(0,0.01),np.random.uniform(-0.01,0.01)])
  

    if sp ==sai:
        perturb[0] = np.random.uniform(0,0.01)
    if M == 1:
        perturb[2] = np.random.uniform(-0.01,0)
    if M == 0:
        perturb[2] = np.random.uniform(0,0.01)
        
    y0 = y0 +perturb
    sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
    [w,s,P] = sol.y
    t1 = sol.t
    #print(int(np.mod(i/2,2)))
    axs[i].plot(t1,w,t1,s,'-.',t1,P,'--')
    #axs[i].set_ylim([-0.1,1.1])
    axs[i].set_title(f"$s_{{ai}}$ = {sai}, $s_{{P}}$ = {sp}, $w_{{s}}$ = {ws}, $M$ = {M}",fontsize=7)
    if i == paramshape[0]-1:
        plt.legend(["$w_D$","$s_{ID}$","$P$"])






