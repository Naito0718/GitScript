import numpy as np
import matplotlib.pyplot as plt

def jacobi_poisson_solver(rho, tol=1e-6, max_iter=1000):
    """
    ヤコビ法を用いて二次元Poisson方程式を解く関数

    :param rho: 与えられた関数ρ(x, y)のnumpy配列
    :param tol: 収束判定の許容誤差
    :param max_iter: 最大反復回数
    :return: 解φ(x, y)のnumpy配列
    """
    nx, ny = rho.shape
    phi = np.zeros((nx, ny))  # 初期値を0として初期化
    phi_new = np.zeros((nx, ny))

    for _ in range(max_iter):
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                phi_new[i, j] = 0.25 * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1] - h*h*rho[i, j])

        diff = np.max(np.abs(phi_new - phi))
        if diff < tol:
            break

        phi = np.copy(phi_new)

    return phi

# 定数

L=10  #全体の正方形領域の一辺
N=100  #分割数
h=L/N   #分割幅

# 非斉次項
rho = np.zeros((N, N))
rho[N // 2, N // 2] = 1.0  # 中心に点電荷を置く

# ヤコビ法でPoisson方程式を解く
sol = jacobi_poisson_solver(rho)

x = np.linspace(0, L, N)
y = np.linspace(0, L, N)
X, Y = np.meshgrid(x, y)

fig = plt.figure()
ax = fig.add_subplot(111)

# 等高線を描画
contour = ax.contour(X, Y, sol, levels=20, cmap='viridis')

# カラーバーを表示
plt.colorbar(contour)

plt.grid()
plt.draw()
plt.show()