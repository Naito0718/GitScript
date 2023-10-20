import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def jacobi_poisson_solver(f, dx, dy, tolerance=1e-6, max_iterations=100):
    # ドメインのサイズ
    nx, ny = len(f), len(f[0])

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
                u_new[i][j] = 0.25 * (u[i+1][j] + u[i-1][j] + u[i][j+1] + u[i][j-1] - dx * dy * f[i][j])

        # 反復ごとの解を保存
        solutions.append(u_new.copy())

        # 収束判定
        error = np.max(np.abs(u_new - u))
        if error < tolerance:
            break

        u = u_new

    return solutions

# Poisson方程式の右辺関数f(x, y)を定義
def f(x, y):
    return 2 * (x - 1) * (y - 1)

# ドメインのサイズと格子間隔を設定
nx, ny = 21, 21
dx, dy = 1.0, 1.0


# ドメインを作成
x = np.linspace(0, (nx - 1) * dx, nx)
y = np.linspace(0, (ny - 1) * dy, ny)
X, Y = np.meshgrid(x, y)

# 右辺関数f(x, y)の値を計算
F = f(X, Y)

# ヤコビ法を実行して解を取得
solutions = jacobi_poisson_solver(F, dx, dy)

# グラフを描画するための初期設定
fig, ax = plt.subplots()
plot = ax.imshow(solutions[0], cmap='jet', origin='lower', extent=[0, (nx - 1) * dx, 0, (ny - 1) * dy])
plt.colorbar(plot)
ax.set_title("Iteration 0")
ax.set_xlabel("x")
ax.set_ylabel("y")

# グラフを更新する関数
def update(iteration):
    ax.imshow(solutions[iteration], cmap='jet', origin='lower', extent=[0, (nx - 1) * dx, 0, (ny - 1) * dy])
    ax.set_title(f"Iteration {iteration}")

# アニメーションの作成
animation = FuncAnimation(fig, update, frames=len(solutions), interval=200)

# グラフを表示
plt.show()
