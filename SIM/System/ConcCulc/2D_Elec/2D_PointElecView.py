import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

"""
このアニメーションなんか終了できない、反復され続けるし挙動も重くなる？

"""

def jacobi_poisson_solver(rho, dx, tolerance=1e-6, max_iterations=100):
    # ドメインのサイズ
    nx, ny = len(rho), len(rho[0])  #二次元配列の要素数

    # 初期値を0で設定
    u = np.zeros((nx, ny))

    # 反復ごとの解を保存するリスト
    solutions = [u.copy()]

    # 反復処理
    for iteration in range(max_iterations):
        u_new = np.copy(u)

        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                # ラプラシアン演算子を用いて新しい値を計算
                u_new[i][j] = 0.25 * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1] - dx * dx * rho[i][j])

        # 反復ごとの解を保存
        solutions.append(u_new.copy())

        # 収束判定
        error = np.max(np.abs(u_new - u))
        if error < tolerance:
            break

        u = u_new

    return solutions

###

# ドメインのサイズと格子間隔を設定
nx, ny = 21, 21
dx= 1.0


# ドメインを作成
x = np.arange(0, (nx - 1) , dx)
y = np.arange(0, (ny - 1) , dx)
X, Y = np.meshgrid(x, y)

# 非斉次項
rho = np.zeros((len(X), len(Y)))
rho[len(X) // 2, len(Y) // 2] = 1.0  # 中心に点電荷を置く

# ヤコビ法を実行して解を取得
solutions = jacobi_poisson_solver(rho, dx)

###

# グラフを描画するための初期設定
fig, ax = plt.subplots()
plot = ax.imshow(solutions[0], cmap='jet', origin='lower', extent=[0, len(x), 0, len(y)])
plt.colorbar(plot)
ax.set_title("Iteration 0")
ax.set_xlabel("x")
ax.set_ylabel("y")

# グラフを更新する関数
def update(iteration):
    ax.imshow(solutions[iteration], cmap='jet', origin='lower', extent=[0, len(x), 0, len(y)])
    ax.set_title(f"Iteration {iteration}")

# アニメーションの作成
animation = FuncAnimation(fig, update, frames=len(solutions), interval=200)

# グラフを表示
plt.show()