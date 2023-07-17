import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import dsolve
import scipy.sparse.linalg as spla
from mpl_toolkits.mplot3d import Axes3D



"""

#連立方程式の解き方(sympyでも可能)
A=np.array([[2,4],[3,5]]) #係数行列、行を入力した
b=np.array([11,15]) #右辺の非斉次項
print(np.linalg.solve(A,b)) #解

"""

"""

#行列コマンド
A=np.arange(9).reshape(3,3) #一次元配列を二次元に、012/345/678、バグりやすい
A=A+1 #各要素に足す
B=A*A   #各要素の掛け算（割り算）
C=np.dot(A,B)   #行列の積

A_0=np.identity(3) #単位行列
A_d=np.diag([2,5,8])    #対角行列
A_f=np.fliplr(np.diag([1,2,3,4])) #反対角行列
AT=A.T  #転置
A_inv=np.linalg.inv(A_0)  #逆行列、.pinvだと存在しなくてもなんか値を返してくれる
detA=np.linalg.det(A)   #行列式
norA=np.linalg.norm(A)  #行列のノルム

A0=np.zeros([3,3])  #全部0、型を指定
A1=np.ones([3,3])   #全部1
A=np.full([3,3],5)  #全部5
A01=np.concatenate([A0,A1],0)   #行方向にくっ付ける、1だと列方向、型に注意

a0=np.zeros(3); a1=np.ones(3)   #ベクトルは横ベクトル
a01=np.stack([a0,a1],1)   #concatenateは次元を増やせない、ただし今回は0なら可能、stackは両対応

B1=np.block([A0,A1])    #横結合
B2=np.block([[A0,A1]])  #縦結合
B3=np.block([[A0,A1,A],[A,A0,A1],[A1,A,A0]]) #複雑な行列


b1=np.block([a0,a1])    #6ーベクトル
b2=np.block([[a0,a1]])  #2*3行列

"""

"""

#疎行列
A=np.diag([1,2,3,4])
As=sps.csr_matrix(A)    #疎行列化、演算は同じ
B=As.A  #復元
C=10*As; D=C+B
sinA=As.sin().A #関数に入れるとき

plt.spy(sinA)   #行列の疎密が分かる
plt.show()

"""

"""

#ソルバー
A1=np.diag([1,2,3,4])
A2=np.fliplr(np.diag([3,4,5,6]))
A=A1+A2
b=np.array([6,7,8,9])
A=sps.csr_matrix(A)

x = dsolve.spsolve(A,b, use_umfpack=False)  #なんかエラー吐く、Aは疎行列
print(x)

x=spla.cg(A,b)  #共役勾配法
print(x)

x=spla.bicg(A,b)    #双共役勾配法
print(x)

x=spla.bicgstab(A,b)    #安定化双共役勾配法
print(x)

"""


