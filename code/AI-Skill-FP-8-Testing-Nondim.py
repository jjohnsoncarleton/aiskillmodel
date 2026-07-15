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

# Parameters





# amount of work needed to improve skill
ws = 2
# make skill (s^*)
smax = 4
# work hours in day
wd = 6
# Max amount of productivity
Pmax = 10

# time scale for w
a = 0.01
# time scale for s
b = 0.01
# time scale for P 
g = 0.01



#sai = 1.3*smax







# Motivation Array
Ms = np.array([0.5,1.25])
sps = np.array([1/2,3/2])
wss = [1/2, 3*1/2]




# skill of ai array
sai = 1/4


# FP 1
w0 = 1
s0 = 1
P0 = 1
y0 = [w0, s0, P0]
y0 = y0 +np.array([-np.random.uniform(0,0.1), -np.random.uniform(0,0.1),-np.random.uniform(0,0.1)])

# function for ODE
def fun(t,y):
  dwdt =  y[0]*(1-y[0])*(M-y[2]) # equation for dw/dt
  dsdt = b*(y[0]-ws)*(1-y[1])*y[1] # equation for ds/dt
  dPdt = g*((y[1]-sp)*y[0]+ ((sai-sp))*(1-y[0]))*(1-y[2])*y[2] # equation for dP/dt
  return [dwdt, dsdt, dPdt] # return array for dw/dt ds/dt



tspan = [0,4000]


sp = sps[0]
fig, axs = plt.subplots(len(Ms), len(wss))
for i in range(len(Ms)):
    M =Ms[i]
    for j in range(len(wss)):
        ws= wss[j]
        sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
        [w,s,P] = sol.y
        t1 = sol.t
        axs[i, j].plot(t1,w,t1,s,t1,P)
        axs[i, j].set_ylim([-0.1,1.1])



#plt.ylabel("Function Values")
plt.show()


sp = sps[1]
fig2, axs2 = plt.subplots(len(Ms), len(wss))
for i in range(len(Ms)):
    M =Ms[i]
    for j in range(len(wss)):
        ws= wss[j]
        sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
        [w,s,P] = sol.y
        t1 = sol.t
        axs2[i, j].plot(t1,w,t1,s,t1,P)




#plt.ylabel("Function Values")
plt.show()


#fig2 =plt.figure()
#for i in range(len(Ms)):
   # M =Ms[i]
    #for j in range(len(sais)):
     #   sai= sais[j]
    #    sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
   #     [w,s,P] = sol.y
  #      t1 = sol.t
  #      axs2 = fig2.add_subplot(9,i+1,j+1,projection='3d')
 #       axs2.plot(w,s,P,label='Phase Curve')
       #axs2.legend()


#plt.show()


