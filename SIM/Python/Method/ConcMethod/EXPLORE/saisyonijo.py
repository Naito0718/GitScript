"""
最小二乗法

"""


import numpy as np
import matplotlib.pyplot as plt


block = np.loadtxt("SpringExpC_2_data.txt", comments='!')
blockx, blocky_0 = np.loadtxt("SpringExpC_2_data.txt", comments='!', unpack=True)
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

print(a,b)
fx=a*blockx +b


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(blockx, blocky, ".",color="k", label="data plot")
ax.plot(blockx, fx, color="red", label="approximate curve")
ax.set_xlim(0.0024,0.004 )
ax.set_ylim(3, 5)
ax.set_xlabel("/temperature[1/K]")
ax.set_ylabel("resistance[log_10 Ohm]")
ax.legend(loc="upper left")
plt.savefig('plot_DOSOwave.pdf', transparent=True, bbox_inches ='tight')
plt.show()