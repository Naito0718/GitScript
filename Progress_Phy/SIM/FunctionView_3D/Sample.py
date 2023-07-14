import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


Xmin=-5.; Xmax=5.; Npoints=500  #定義域と分割数
x=np.linspace(Xmin,Xmax,500) 
y=np.linspace(Xmin,Xmax,500) 
X,Y=np.meshgrid(x,y)

def func(x, y): #関数の定義
    return np.sin(x) * np.cos(y)

print("\n Now doing the plotting thing,look for Figure 1 on desktop")

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_wireframe(X,Y,func(X,Y),)  
xlabel = ax.set_xlabel("X-axis [N]")
ylabel = ax.set_ylabel("Y-axis [N]")
zlabel = ax.set_zlabel("Z-axis [N]"); 
plt.title('f(x,y) vs x,y')

plt.show()






