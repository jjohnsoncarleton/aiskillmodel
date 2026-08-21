# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:40:32 2026

@author: jjohnson16

This is code testing the numerical thresholds

For stability of fixed points.

This tests FP 5 stability

Need to test cases:
    
1. M < 0, wd < ws (unstable)
2. M <0, wd > ws (unstable)
3. M <0, wd = ws (unstable)
4. M = 0, wd < ws (unstable)
5. M = 0, wd > ws (unstable)
6. M = 0, wd = ws (unstable)
7. M >0, wd < ws (stable)
8. M >0, wd > ws (unstable)
9. M >0, wd = ws (unstsable)


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
ws = 1/2


# time scale for s
b = 1
# time scale for P 
g = 1



#sai = 1.3*smax



# productivity skill threshold
sp = 1/2




# Motivation Array
Ms = np.array([-0.25,0.25])
#sais = np.array([sp/2,3*sp/2])
wss = [1/2, 3/2]

M =1



# skill of ai array
sai = 3*sp/2


# FP 1
w0 = 1
s0 = 0
P0 = 0
y0 = [w0, s0, P0]
y0 = y0 +np.array([-np.random.uniform(0,0.1), np.random.uniform(0,0.1),np.random.uniform(0,0.1)])

# function for ODE
def fun(t,y):
  dwdt =  y[0]*(1-y[0])*(M-y[2]) # equation for dw/dt
  dsdt = b*(y[0]-ws)*(1-y[1])*y[1] # equation for ds/dt
  dPdt = g*((y[1]-sp)*y[0]+ ((sai-sp))*(1-y[0]))*(1-y[2])*y[2] # equation for dP/dt
  return [dwdt, dsdt, dPdt] # return array for dw/dt ds/dt


tspan = [0,1000]

fig, axs = plt.subplots(len(Ms), len(wss), layout="constrained")
for i in range(len(Ms)):
    M =Ms[i]
    for j in range(len(wss)):
        ws= wss[j]
        sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
        [w,s,P] = sol.y
        t1 = sol.t
        axs[i, j].plot(t1,w,t1,s,'-.',t1,P,'--')
        if i == 0:
            axs[i, j].set_xticklabels([])
        axs[i, j].set_title(f"M = {M}, $w_{{s}}$ = {ws}", fontsize=12)
        if j == len(wss)-1:
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


fig.savefig("FP5_Nondim_Stability.pdf")
fig.savefig("FP5_Nondim_Stability.eps",format='eps')
fig.savefig("FP5_Nondim_Stability.png")
