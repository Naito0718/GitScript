import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

"""
アダムス法
・特徴
    長所：精度がよい 短所：メモリを食う、不安定
    今の時間、ひとつ前の時間を用いる


"""

#定数の定義

g=9.8   #重力加速度
m=1.0   #質量
ky=0.4   #y軸のばね定数
kx=0.5  #x軸のばね定数

#定数ここまで

#初期値

x_0=0.0
y_0=0.0
vx_0=10.0
vy_0=0.0

#初期値ここまで


t_0=-0.; t_end=10.; Npoints=500  #定義域と分割数
dt=(t_end-t_0)/Npoints  #微小時間


#以下微分方程式

print("\n Now simulating")

t=t_0; x=x_0; y=y_0
vx=vx_0; vy=vy_0

x_ar=np.array([]); y_ar=np.array([])
vx_ar=np.array([]); vy_ar=np.array([])
t_ar=np.array([])

for step in range(Npoints):
    t+=dt
    vy+=-dt*g-ky*y  #速度、運動方程式
    vx+=-kx*x
    y+=vy*dt  #位置
    x+=vx*dt

    x_ar=np.append(x_ar,x); y_ar=np.append(y_ar,y); t_ar=np.append(t_ar,t)
    print(f"{x}")

print("\n Now doing the plotting thing,look for Figure 1 on desktop")

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot(x_ar,y_ar,t_ar)  
xlabel = ax.set_xlabel("X-axis [N]")
ylabel = ax.set_ylabel("Y-axis [N]")
plt.title('y vs x')

plt.show()






