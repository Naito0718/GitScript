import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sps
import math
from mpl_toolkits.mplot3d import Axes3D

#級数計算



def func(x): #関数の定義（sin）
    s=x
    an=x
    eps=1.0e-8   #誤差
    n=1    #繰り返す数

    while (np.abs(an)>eps): 
        an=an*(x**2)*(-1)/(2*n*(2*n+1))
        s=s+an
        n+=1

    print(f"とった級数項：{n}")
    return s

#以下計算

x=np.pi   #変数の値、でかすぎるとダメっぽい。。。

print(func(x))