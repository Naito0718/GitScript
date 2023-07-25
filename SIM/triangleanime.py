import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#三角形の内部判定

def sign (p,q,r):

    return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

 
def InTriangle (o, p,q,r):

 
    b1 = sign(o, p, q) < 0.0
    b2 = sign(o, q, r) < 0.0
    b3 = sign(o, r, p) < 0.0
 
    return ((b1==b2) and (b2==b3))

###

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

###


def jacobi_poisson_solver(tol=1e-6, max_iter=1000):

    omega=2 #SOR

    phi = np.zeros((N, N))

    for _ in range(0, N):
        for _2 in range(N):
            if InTriangle([_2*h, _*h], [trix[0], triy[0]], [trix[1], triy[1]], [trix[2], triy[2]]) == True:
                phi[_, _2] = Vt

            elif (0 <= _2*h <= 1.5 and 0 <= _*h <= 17.5) or (0 <= _2*h <= 19 and 18.5 <= _*h <= 20):
                phi[_, _2] = Vs
            else:
                phi[_, _2] = (Vt + Vs) / 2

    nx = N
    ny = N

    phi_new = np.zeros((nx, ny))

    # 反復ごとの解を保存するリスト
    solutions = [phi.copy()]

    # 反復処理
    for _ in range(max_iter):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                if InTriangle([h*j, h*i], [trix[0], triy[0]], [trix[1], triy[1]], [trix[2], triy[2]]) == True:
                    phi_new[i, j] = Vt

                elif (0 <= h*j <= 1.5 and 0 <= h*i <= 17.5) or (0 <= h*j <= 19 and 18.5 <= h*i <= 20):
                    phi[i, j] = Vs

                else:
                    phi_new[i, j] = (1-omega)*phi[i,j]+omega*0.25 * (phi[i + 1, j] + phi_new[i - 1, j] + phi[i, j + 1] + phi_new[i, j - 1])

        # 反復ごとの解を保存
        solutions.append(phi_new.copy())

        diff = np.max(np.abs(phi_new - phi))
        if diff < tol:
            break

        phi = np.copy(phi_new)

    print(_)
    return solutions

# 以下はアニメーション部分のコード

# ドメインを作成
x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

# ヤコビ法を実行して解を取得
solutions = jacobi_poisson_solver()

# 解のリストを2次元配列に変換
solutions_2d = np.array(solutions)

# グラフを描画するための初期設定
fig, ax = plt.subplots()
plot = ax.imshow(solutions_2d[0], cmap='jet', origin='lower', extent=[0, L, 0, L])
plt.colorbar(plot)
ax.set_title("Iteration 0")
ax.set_xlabel("x")
ax.set_ylabel("y")

# グラフを更新する関数
def update(iteration):
    ax.imshow(solutions_2d[iteration], cmap='jet', origin='lower', extent=[0, L, 0, L])
    ax.set_title(f"Iteration {iteration}")

# アニメーションの作成
animation = FuncAnimation(fig, update, frames=len(solutions), interval=200)

# グラフを表示
plt.show()