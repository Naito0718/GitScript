"""
最小二乗法

"""


import numpy as np
import matplotlib.pyplot as plt

blockx = np.array([1,2,3,4,5])
blocky = np.array([3,5,7,9,11])    

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




#a=2.0,b=1.0

