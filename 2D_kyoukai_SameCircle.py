"""
二次元導体に外部電流を印加した時


"""




import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

def jacobi_poisson_solver(tol=1e-6, max_iter=1000):
    """
    ヤコビ法を用いて二次元Poisson方程式を解く関数

    :rho: 与えられた関数rho(x, y)のnumpy配列
    :tol: 収束判定の許容誤差
    :max_iter: 最大反復回数
    :return: 解φ(x, y)のnumpy配列
    """

    # 境界条件：非斉次項はなし
    """同心な2つの円板、外側接地、内側10V"""
    omega=1.0

    phi = np.zeros((N, N))

    for _ in range(0,N):
        for _2 in range(N):
            if R1*R1<=(_*h-o1[0])**2+(_2*h-o1[1])**2<=r2*r2 :
                phi[_,_2]=(V1+V2)/2

            elif (_*h-o1[0])**2+(_2*h-o1[1])**2<R1*R1 :
                phi[_,_2]=V1
            else :
                phi[_,_2]=V2

    nx=N; ny = N

    phi_new = np.zeros((nx, ny))

    #反復開始
    for _ in range(max_iter):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                phi_new[i, j] = (1-omega)*phi[i,j]+omega*0.25 * (phi[i + 1, j] + phi_new[i - 1, j] + phi[i, j + 1] + phi_new[i, j - 1] )

        #境界条件
        for _ in range(0,N):
            for _2 in range(N):
                if (_*h-o1[0])**2+(_2*h-o1[1])**2<=R1*R1 :
                    phi_new[_,_2]=V1

                elif r2*r2<(_*h-o1[0])**2+(_2*h-o1[1])**2 :
                    phi_new[_,_2]=V2

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
"""同心な2つの円板、外側接地、内側10V"""
o1=[L/2,L/2]; r1=2.0; R1=2.5; V1=10
o2=[L/2,L/2]; r2=7.6; R2=8.1; V2=0    #中心、半径、電圧

# ヤコビ法でPoisson方程式を解く
start_time = time.time()

sol = jacobi_poisson_solver()

end_time = time.time(); elapsed_time = end_time - start_time; print(f"計算時間: {elapsed_time}秒")
"""
199
計算時間: 84.79103565216064秒
"""

#グラフの描画

x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111)

# 等高線を描画
levels = np.linspace(np.min(sol), np.max(sol), 21)
contour = ax.contour(X, Y, sol, levels=levels, cmap='viridis')

# 円を描画
circle = plt.Circle((o1[0], o1[1]), R1, color='blue', fill=False)  # 円を生成
ax.add_artist(circle)  # 円をグラフに追加
  
circle2 = plt.Circle((o2[0], o2[1]), r2, color='blue', fill=False)  
ax.add_artist(circle2)  

# カラーバーを表示
plt.colorbar(contour)

plt.grid()
plt.draw()
plt.show()