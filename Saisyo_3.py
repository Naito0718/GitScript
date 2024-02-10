"""
最小二乗法

"""


import numpy as np
import matplotlib.pyplot as plt

blockx = np.array([1/(1394+273),1/(1404+273),1/(1393+273),1/(1434+273)])
blocky_0 = np.array([0.00299*blockx[0]*blockx[0],0.00208*blockx[1]*blockx[1], 0.00173*blockx[2]*blockx[2],0.00144*blockx[3]*blockx[3]]) 

blocky=np.log10 (blocky_0)

def least_squares(x,y):
    n=len(x)
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    xy_mean=np.mean(x*y)
    x_squared_mean=np.mean(x**2)

    numerator=xy_mean-x_mean*y_mean
    denumerator=x_squared_mean-x_mean**2
    a=numerator/denumerator

    b=y_mean-a*x_mean

    return a,b

a,b=least_squares(blockx,blocky)

print(f"a={a},b={b}")
print(f"よって、φ={-a*1.380658e-23/(1.60217733e-19*np.log10(np.e))},A={pow(10,b)}")
fx=a*blockx +b

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(blockx, blocky, ".",color="k", label="data plot")
ax.plot(blockx, fx, color="red", label="y=15160.2246...x-18.1814...")
ax.set_xlim(np.min(blockx)-np.abs(np.min(blockx)/100),np.max(blockx)+np.abs(np.max(blockx)/100))
ax.set_ylim(np.min(blocky)-np.abs(np.min(blocky)/100),np.max(blocky)+np.abs(np.max(blocky)/100))
ax.set_xlabel("/temperature[1/K]")
ax.set_ylabel("log_10(saturation current/temperature^2)[log_10 (A/K^2)]")
ax.legend(loc="upper left")
plt.savefig('plot_DOSOwave.pdf', transparent=True, bbox_inches ='tight')
plt.show()

#a=15160.224464176355,b=-18.1814993003969
#よって、φ=-3.0081317362465607,A=6.584164905827999e-19

