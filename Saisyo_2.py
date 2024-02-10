"""
最小二乗法

"""


import numpy as np
import matplotlib.pyplot as plt

blockx_0 = np.array([10,20,30])
blocky_0 = np.array([2.77e-4, 6.9e-4, 1.16e-3]) 

blockx=np.log10 (blockx_0) 
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
print(f"よって、a={a},K={pow(10,b)}")


#a=1.313575886819513,b=-4.873187217738655
#よって、a=1.313575886819513,K=1.339099297664582e-05

