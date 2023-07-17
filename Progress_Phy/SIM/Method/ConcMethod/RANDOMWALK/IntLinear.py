import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# ランダムウォークのステップ数を指定
num_steps = 1000

def _update(frame, x, y, z, line):
    """グラフを更新するための関数"""
    # 現在のグラフを消去する
    line.set_data(x[:frame], y[:frame])
    line.set_3d_properties(z[:frame])

    # データを更新 (追加) する
    xstep = np.random.rand([-1, 1])
    ystep = np.random.choice([-1, 1])
    zstep = np.random.choice([-1, 1])

    if len(x) < num_steps:
        x.append(x[-1] + xstep)
        y.append(y[-1] + ystep)
        z.append(z[-1] + zstep)

    # 座標軸の範囲を自動調整
    ax.set_xlim(min(x) - 1, max(x) + 1)
    ax.set_ylim(min(y) - 1, max(y) + 1)
    ax.set_zlim(min(z) - 1, max(z) + 1)

    return line,

# 描画領域
fig = plt.figure(figsize=(10, 6))
x = [0]
y = [0]
z = [0]
ax = fig.add_subplot(111, projection='3d')

# 線の初期化
line, = ax.plot([], [], [], c='b', marker='o', markersize=4)

params = {
    'fig': fig,
    'func': _update,
    'fargs': (x, y, z, line),
    'interval': 10,
    'frames': num_steps,
    'repeat': False,
}
anime = animation.FuncAnimation(**params)

# 初期の視点を設定
ax.view_init(elev=20, azim=30)

# グラフを表示する
plt.show()
