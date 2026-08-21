# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:40:32 2026

@author: jjohnson16

This is code testing the numerical thresholds

For stability of fixed points.

This tests FP 2 stability

Need to test cases:
    
1. M <Pmax, sai < sp (stable)
2. M <Pmax, sai > sp (unstable)
3. M <Pmax, sai = sp (unstable)
4. M =Pmax, sai < sp (unstable)
5. M =Pmax, sai > sp (unstable)
6. M =Pmax, sai = sp (unstable)
7. M >Pmax, sai < sp (unstable)
8. M >Pmax, sai > sp (unstable)
9. M >Pmax, sai = sp (unstsable)


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
ws = 0.5


# time scale for s
b =1
# time scale for P 
g = 1




# productivity skill threshold

sp = 1/2




# Motivation Array
Ms = np.array([0.75,1,1.25])
sais = np.array([sp/2,sp,3*sp/2])



# FP 1
w0 = 0
s0 = 1
P0 = 1
y0 = [w0, s0, P0] 
y0 = y0+np.array([np.random.uniform(0,0.1), -np.random.uniform(0,0.1),-np.random.uniform(0,0.1)])

# function for ODE
def fun(t,y):
  dwdt =  y[0]*(1-y[0])*(M-y[2]) # equation for dw/dt
  dsdt = b*(y[0]-ws)*(1-y[1])*y[1] # equation for ds/dt
  dPdt = g*((y[1]-sp)*y[0]+ ((sai-sp))*(1-y[0]))*(1-y[2])*y[2] # equation for dP/dt
  return [dwdt, dsdt, dPdt] # return array for dw/dt ds/dt


tspan = [0,1500]

fig, axs = plt.subplots(len(Ms), len(sais), layout="constrained")
for i in range(len(Ms)):
    M =Ms[i]
    for j in range(len(sais)):
        sai= sais[j]
        sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
        [w,s,P] = sol.y
        t1 = sol.t
        axs[i, j].plot(t1,w,t1,s,'-.',t1,P,'--')
        axs[i,j].set_ylim(-0.05,1.05)
        if i < len(Ms)-1:
            axs[i, j].set_xticklabels([])
        axs[i, j].set_title(f"M = {M}, $s_{{ai}}$ = {sai}, $s_{{P}}$ = {sp}", fontsize=9)
        if j == len(sais)-1:
            plt.legend(["$w_D$","$s_{ID}$","$P$"])
        



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




fig.savefig("FP4_Nondim_Stability.pdf")
fig.savefig("FP4_Nondim_Stability.eps",format='eps')
fig.savefig("FP4_Nondim_Stability.png")
