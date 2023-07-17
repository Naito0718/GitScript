"""
#線形合同法

def Rander(r,N):
    M=2**(48); c=11; a=273673163155 #パラメータ

    x=r
    rand=np.array([])

    for i in range (N):
        x=(a*x+c)%M
        X=x/M   #[0,1]に正規化
        #Y=A+(B-A)*X    #区間[A,B]
        rand=np.append(rand,X)

    return rand

x=Rander(14.3,100)
i=np.linspace(0,100,100)
k=np.array([])

for p in range (100):
    q=np.random.rand()
    k=np.append(k,q)

print("\n Now doing the plotting thing,look for Figure 1 on desktop")

sisuu=9 #モーメントの次数

print(f"\n自作関数の次モーメント{sum(x**sisuu)/100}")   #独立；1/(k+1)+O(1/\√N)ぐらいになってれば一様かつランダム
print(f"\nnp.randomの1次モーメント{sum(k**sisuu)/100}") #独立

fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(i, x,'-',lw=2)  #-は点をつないで描画、lwは線の幅
ax2.plot(i, k,'-',lw=2,color="b")  #-は点をつないで描画、lwは線の幅
plt.xlabel('i'); plt.ylabel('random'); plt.title('rondom vs i')
plt.grid(True)  #格子生成
plt.show()
print(x)


"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# ランダムウォークのステップ数を指定
num_steps = 1000

def _update(frame, x, y, z, sc):
    """グラフを更新するための関数"""
    if not sc:  # 最初のフレームの場合にscが空ならグラフィックスオブジェクトを作成
        sc.append(ax.scatter([], [], [], c='b', marker='o', s=20))

    # データを更新 (追加) する
    xstep = np.random.choice([-1, 1])
    ystep = np.random.choice([-1, 1])
    zstep = np.random.choice([-1, 1])

    if len(x) == 0:
        x.append(0)
        y.append(0)
        z.append(0)
    elif len(x) == num_steps:
        print(x[len(x) - 1], y[len(y) - 1], z[len(z) - 1])
    else:
        x.append(x[len(x) - 1] + xstep)
        y.append(y[len(y) - 1] + ystep)
        z.append(z[len(z) - 1] + zstep)

    # 新しい3Dグラフィックスオブジェクトを作成して再描画する
    sc[0].remove()  # 最初のフレーム以降は前のフレームのグラフィックスオブジェクトを削除
    sc[0] = ax.scatter(x, y, z, c='b', marker='o', s=20)

    return sc

# 描画領域
fig = plt.figure(figsize=(10, 6))
x = []
y = []
z = []
ax = fig.add_subplot(111, projection='3d')

# 最初の3Dグラフィックスオブジェクト用の空のリスト
sc = []

params = {
    'fig': fig,
    'func': _update,
    'fargs': (x, y, z, sc),
    'interval': 10,
    'frames': np.linspace(0, num_steps, num_steps),
    'repeat': False,
}
anime = animation.FuncAnimation(**params)

# グラフを表示する
plt.show()


