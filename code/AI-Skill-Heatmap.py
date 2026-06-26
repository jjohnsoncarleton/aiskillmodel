# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:40:32 2026

@author: jjohnson16

This is code testing the numerical thresholds

For stability of fixed points.

Testing Motivation against AI skill.

Need heat maps for skill, productivity, and work hours

TO DO:
    
Need to test the specific fixed points individually!!! 

(Showing stable and stable manifolds)



"""

# data stuff
import numpy as np
import matplotlib.pyplot as plt

# ode function
from scipy.integrate import solve_ivp
# timer
import time

# Parameters





# amount of work needed to improve skill
ws = 2
# make skill (s^*)
smax = 1
# work hours in day
wd = 10
# Max amount of productivity
Pmax = 10

# time scale for w
a = 0.01
# time scale for s
b = 0.01
# time scale for P 
g = 0.01



#sai = 1.3*smax


# Initial amount work
w0 = 9*wd/10

# Initial amount of skill
s0 = 9*smax/10

# productivity skill threshold
#sp = smax/3
sp = smax/2
#sp = 1.2*smax


# Initial amount of productivity
P0 = 9*Pmax/10


# number of Ms
n = 40
# Motivation Array
Ms = np.linspace(-0.5*Pmax, Pmax*1.5,n)

# number of ais
k = 10
# skill of ai array
sais = np.linspace(0.05, smax*1.1,k)



# Initial Condition
y0 = [w0, s0, P0]

# function for ODE
def fun(t,y):
  dwdt =  a*y[0]*(wd-y[0])*(M-y[2]) # equation for dw/dt
  dsdt = b*(y[0]-ws)*(smax-y[1])*y[1] # equation for ds/dt
  dPdt = g*((y[1]-sp)*y[0]+ ((sai-sp))*(wd-y[0]))*(Pmax-y[2])*y[2] # equation for dP/dt
  return [dwdt, dsdt, dPdt] # return array for dw/dt ds/dt


wavgarray = np.zeros([n,k])
wstdarray = np.zeros([n,k])
savgarray = np.zeros([n,k])
sstdarray = np.zeros([n,k])
Pavgarray = np.zeros([n,k])
Pstdarray = np.zeros([n,k])

tspan = [0, 5000]

# For timing purposes, start the timer
start = time.time()
for i in range(n):

    # Motivation
    M =Ms[i]
    for j in range(k):
        sai =sais[j]
        sol = solve_ivp(fun, tspan, y0, method = 'RK45',atol=1e-10,rtol=1e-8) 
        t1 = sol.t
        y1 = sol.y
        w = y1[0]
        s = y1[1]
        P = y1[2]
        wavgarray[i,j] = np.average(w[t1>max(tspan)/3])
        wstdarray[i,j] = np.std(w[t1>max(tspan)/3])
        savgarray[i,j] = np.average(s[t1>max(tspan)/3])
        sstdarray[i,j] = np.std(s[t1>max(tspan)/3])
        Pavgarray[i,j] = np.average(P[t1>max(tspan)/3])
        Pstdarray[i,j] = np.std(P[t1>max(tspan)/3])
        print(i*k+j+1)

# End the timer
end = time.time()
# Print run time
print(end-start)


fig1=plt.figure(1)
plt.imshow(wavgarray.T, extent=[min(Ms), max(Ms), min(sais), max(sais)],origin='lower', interpolation='nearest', aspect='auto')
plt.plot([Pmax, Pmax],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([0, 0],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([min(Ms), max(Ms)],[sp, sp],'k:',linewidth=3)
plt.xlabel('Motivation $M$')
plt.ylabel('Skill of AI $s_{ia}$')
plt.title('Average Working Hours $w_{ID}$')
plt.colorbar()
plt.show()


fig2=plt.figure(2)
plt.imshow(wstdarray.T, extent=[min(Ms), max(Ms), min(sais), max(sais)],origin='lower', interpolation='nearest', aspect='auto')
plt.plot([Pmax, Pmax],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([0, 0],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([min(Ms), max(Ms)],[sp, sp],'k:',linewidth=3)
plt.xlabel('Motivation $M$')
plt.ylabel('Skill of AI $s_{ia}$')
plt.title('Standard Deviation of Working Hours $w_{ID}$')
plt.colorbar()
plt.show()




fig3=plt.figure(3)
plt.imshow(savgarray.T, extent=[min(Ms), max(Ms), min(sais), max(sais)],origin='lower', interpolation='nearest', aspect='auto')
plt.plot([Pmax, Pmax],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([0, 0],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([min(Ms), max(Ms)],[sp, sp],'k:',linewidth=3)
plt.xlabel('Motivation $M$')
plt.ylabel('Skill of AI $s_{ia}$')
plt.title('Average Skill $s_{ID}$')
plt.colorbar()
plt.show()


fig4=plt.figure(4)
plt.imshow(sstdarray.T, extent=[min(Ms), max(Ms), min(sais), max(sais)],origin='lower', interpolation='nearest', aspect='auto')
plt.plot([Pmax, Pmax],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([0, 0],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([min(Ms), max(Ms)],[sp, sp],'k:',linewidth=3)
plt.xlabel('Motivation $M$')
plt.ylabel('Skill of AI $s_{ia}$')
plt.title('Standard Deviation of Skill $s_{ID}$')
plt.colorbar()
plt.show()



fig5=plt.figure(5)
plt.imshow(Pavgarray.T, extent=[min(Ms), max(Ms), min(sais), max(sais)],origin='lower', interpolation='nearest', aspect='auto')
plt.plot([Pmax, Pmax],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([0, 0],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([min(Ms), max(Ms)],[sp, sp],'k:',linewidth=3)
plt.xlabel('Motivation $M$')
plt.ylabel('Skill of AI $s_{ia}$')
plt.title('Average Productivity $P$')
plt.colorbar()
plt.show()


fig6=plt.figure(6)
plt.imshow(Pstdarray.T, extent=[min(Ms), max(Ms), min(sais), max(sais)],origin='lower', interpolation='nearest', aspect='auto')
plt.plot([Pmax, Pmax],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([0, 0],[min(sais), max(sais)],'r:',linewidth=3)
plt.plot([min(Ms), max(Ms)],[sp, sp],'k:',linewidth=3)
plt.xlabel('Motivation $M$')
plt.ylabel('Skill of AI $s_{ia}$')
plt.title('Standard Deviation of Productivity $P$')
plt.colorbar()
plt.show()


fig1.savefig("Average_Working_Hours.pdf")
fig1.savefig("Average_Working_Hours.png")
fig2.savefig("STD_Working_Hours.pdf")
fig2.savefig("STD_Working_Hours.png")
fig3.savefig("Average_Skill.pdf")
fig3.savefig("Average_Skill.png")
fig4.savefig("STD_Skill.pdf")
fig4.savefig("STD_Skill.png")
fig5.savefig("Average_Productivity.pdf")
fig5.savefig("Average_Productivity.png")
fig6.savefig("STD_Productivity.pdf")
fig6.savefig("STD_Productivity.png")


np.save("wavgarray.npy",wavgarray)
np.save("wstdarray.npy",wstdarray)
np.save("savgarray.npy",savgarray)
np.save("sstdarray.npy",sstdarray)
np.save("Pavgarray.npy",Pavgarray)
np.save("Pstdarray.npy",Pstdarray)
