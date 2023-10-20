"""
二次元導体に外部電流を印加した時


"""




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

#三角形の内部判定

def sign (p,q,r):

    return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

 
def InTriangle (o, p,q,r):

 
    b1 = sign(o, p, q) < 0.0
    b2 = sign(o, q, r) < 0.0
    b3 = sign(o, r, p) < 0.0
 
    return ((b1==b2) and (b2==b3))

#ヤコビ法

def jacobi_poisson_solver(tol=1e-2, max_iter=1000):
    """
    ヤコビ法を用いて二次元Poisson方程式を解く

    :tol: 収束判定の許容誤差
    :max_iter: 最大反復回数
    :return: 解のnumpy配列
    """

    # 境界条件：非斉次項はなし
    """三角形10V、二枚の接地された長方形"""

    omega=1 #SOR

    phi = np.zeros((N, N))

    for _ in range(0,N):
        for _2 in range(N):
            if InTriangle([_2*h,_*h],[trix[0],triy[0]],[trix[1],triy[1]],[trix[2],triy[2]])==True:
                phi[_,_2]=Vt

            elif ( 0<= _2*h <=1.5 and 0<= _*h <=17.5 )or (0<= _2*h <=19 and 18.5<= _*h <=20) :
                phi[_,_2]=Vs
            else :
                phi[_,_2]=(Vt+Vs)/2

    nx=N; ny = N

    phi_new = np.zeros((nx, ny))

    #反復開始
    for _ in range(max_iter):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                if InTriangle([h*j,h*i],[trix[0],triy[0]],[trix[1],triy[1]],[trix[2],triy[2]])==True:
                    phi_new[i,j]=Vt

                elif ( 0<= h*j <=1.5 and 0<= h*i <=17.5 )or (0<= h*j <=19 and 18.5<= h*i <=20) :
                    phi[i,j]=Vs

                else :
                    phi_new[i, j] = (1-omega)*phi[i,j]+omega*0.25 * (phi[i + 1, j] + phi_new[i - 1, j] + phi[i, j + 1] + phi_new[i, j - 1])
        diff = np.max(np.abs(phi_new - phi))
        if diff < tol:
            break

        phi = np.copy(phi_new)
    
    print(_)
    return phi

# 定数

L=20  #全体の正方形領域の一辺
N=200  #分割数
h=L/N   #分割幅

# 境界条件：非斉次項はなし
# 三角形の3つの頂点の座標
trix = [11.5, 11.2 + h, 9]
triy = [10.4, 9, 10.5+2*h]; Vt=10   #電位

# 長方形
rect1=[0, 0]  # 左下隅の座標
width1 = 1.5      # 幅
height1 = 17.5     # 高さ   

rect2=[0, 18.5]  # 左下隅の座標
width2 = 19      # 幅
height2 = 1.5     # 高さ

Vs=0    #接地


# ヤコビ法でPoisson方程式を解く
start_time = time.time()

sol = jacobi_poisson_solver()

end_time = time.time(); elapsed_time = end_time - start_time; print(f"計算時間: {elapsed_time}秒")
"""
999
計算時間: 133.11729383468628秒
"""

#グラフの描画

x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111)

# 等高線を描画
contour = ax.contour(X, Y, sol, levels=np.arange(0,11), cmap='viridis')
contour.clabel(fmt='%1.1f', fontsize=14)

# 三角形を描画
triangle = plt.Polygon(np.column_stack((trix, triy)), edgecolor='red', fill=False)
ax.add_patch(triangle)

# 長方形を描画
rectangle1 = plt.Rectangle((rect1[0],rect1[1]), width1, height1, edgecolor='red', facecolor='none')
ax.add_patch(rectangle1)

rectangle2 = plt.Rectangle((rect2[0],rect2[1]), width2, height2, edgecolor='red', facecolor='none')
ax.add_patch(rectangle2)

# カラーバーを表示
plt.colorbar(contour)

plt.grid()
plt.draw()
plt.show()