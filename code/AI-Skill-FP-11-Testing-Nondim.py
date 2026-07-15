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
import dill 





# amount of work needed to improve skill
ws = 2


# time scale for w
#a = 0.01
# time scale for s
b = 0.01
# time scale for P 
g = 0.01



#sai = 1.3*smax



# productivity skill threshold
#sp = smax/3
sp = 0.7
#sp = 1.2*smax



# Motivation Array
#Ms = np.array([Pmax/2, Pmax/2])
M = 1/2
#sais = np.array([1.5*smax,1.5*smax])
wss = [0.6, 0.9]


# sai, sp
param1 = np.array([[0.5, 0.8],[0.5, 0.2],[0.5, 0.75],[1.25, 0.75]])

#M =1







# function for ODE
def fun(t,y):
  dwdt =  y[0]*(1-y[0])*(M-y[2]) # equation for dw/dt
  dsdt = b*(y[0]-ws)*(1-y[1])*y[1] # equation for ds/dt
  dPdt = g*((y[1]-sp)*y[0]+ ((sai-sp))*(1-y[0]))*(1-y[2])*y[2] # equation for dP/dt
  return [dwdt, dsdt, dPdt] # return array for dw/dt ds/dt


tspan = [0,15000]


paramshape= np.shape(param1)

# fig, axs = plt.subplots(len(wss), paramshape[0])
# for i in range(paramshape[0]):
#     sai,sp= param1[i]
#     for j in range(len(wss)):
#         ws =wss[j]
#         print(ws)
#         w0 = ws
#         s0 = (sp-(1-ws)*sai)/ws
#         print(s0)
#         P0 = M
#         y0 = [w0, s0, P0]
#         y0 = y0 +10*np.array([-np.random.uniform(-0.01,0.01), -np.random.uniform(0,0.01),np.random.uniform(-0.01,0.01)])
#         sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
#         [w,s,P] = sol.y
#         t1 = sol.t
#         axs[i, j].plot(t1,w,t1,s,'-.',t1,P,'--')
#         axs[i, j].set_ylim([-0.1,1.1])
#         if i == 0:
#             axs[i, j].set_xticklabels([])
#         axs[i, j].set_title(f"$s_{{ai}}$ = {sai}, $s_{{P}}$ = {sp}, $w_{{s}}$ = {ws}")
#         if i == paramshape[0]-1 and j == len(wss)-1:
#             plt.legend(["$w_D$","$s_{ID}$","$P$"])



fig, axs = plt.subplots(2,2)
for i in range(paramshape[0]):
    sai,sp= param1[i]
    ws =0.6
    w0 = ws
    s0 = (sp-(1-ws)*sai)/ws
    P0 = M
    y0 = [w0, s0, P0]
    

    if s0 ==0:
        y0 = y0 +10*np.array([np.random.uniform(-0.01,0.01), np.random.uniform(0,0.01),np.random.uniform(-0.01,0.01)])
    elif s0 ==1.0:
        y0 = y0 +10*np.array([np.random.uniform(-0.01,0.01), np.random.uniform(-0.01,0),np.random.uniform(-0.01,0.01)])
    else:
        y0 = y0 +10*np.array([np.random.uniform(-0.01,0.01), np.random.uniform(-0.01,0.01),np.random.uniform(-0.01,0.01)])
    sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
    [w,s,P] = sol.y
    t1 = sol.t
    print(int(np.mod(i/2,2)))
    axs[np.mod(i,2), int(np.mod(i/2,2))].plot(t1,w,t1,s,'-.',t1,P,'--')
    axs[np.mod(i,2), int(np.mod(i/2,2))].set_ylim([-0.1,1.1])
    if np.mod(i,2)==0:
        axs[np.mod(i,2), int(np.mod(i/2,2))].set_xticklabels([])
    axs[np.mod(i,2), int(np.mod(i/2,2))].set_title(f"$s_{{ai}}$ = {sai}, $s_{{P}}$ = {sp}, $w_{{s}}$ = {ws}")
    if i == paramshape[0]-1:
        plt.legend(["$w_D$","$s_{ID}$","$P$"])






#fig = plt.figure(figsize=(12, 10))
#subplots = [fig.add_subplot(2, 2, i + 1, projection='3d') for i in range(4)]



#for i, ax in enumerate(subplots):
#    i2 = np.mod(i,2)
#    j2 = np.mod(i+1,2)
#    ws =wss[i2]
#    sai= sais[j2] 
#    
#    w0 = wd*(sai-sp)/(sai-smax)
#    if w0 > wd or w0 < 0:
#        print("Impossible Initial Condition")
#        print(w0)
#    s0 = smax
#    P0 = M
#    y0 = [w0, s0, P0]
#    y0 = y0 +100*np.array([np.random.uniform(0,0.01), -np.random.uniform(0,0.01),np.random.uniform(0,0.01)])
#    sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
#    [w,s,P] = sol.y
#    t1 = sol.t
#    ax.plot(w,s,P,label='Phase Curve')
#    ax.legend()


#plt.tight_layout()
#plt.show()

