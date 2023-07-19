"""
長さ$L,L1,L2,L3$の棒、重さ$W1,W2$の質点が、
------------
-        -
 -     W2
   W1-

のようにして釣り合っているとする


"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import dsolve
import scipy.sparse.linalg as spla
from mpl_toolkits.mplot3d import Axes3D

N=3
n=N*N
eps=1e-3
deriv=np.zeros([n,n],float)
f=np.zeros(n,float)
x=np.array([0.5,0.5,0.5,0.5,0.5,0.5,1.,1.,1.])  #初期推定値

L=np.array([3.0,4.0,4.0])
Labove=8.0
W=np.array([10.0,20.0])



def F(x,f): #関数f
  f[0]=0; f[1]=0  #初期化

  for _ in range(N):
    f[0]+=L[_]*x[_+N]
    f[1]+=L[_]*x[_]
    f[2*N+_]=x[_]**2+x[_+N]**2-1

  for _ in range(N-1):
      f[2+_]=x[N+_]*x[2*N+j]-x[N+_+1]*x[2*N*_*1]
      f[2+_+N]=x[_]*x[2*N+j]-x[_+1]*x[2*N*_*1]-W[_]

  f[0]-=L

  return f

def dFi_dXj(x,deriv,n): #ヤコビアン
  h=1.0e-4
  for _ in range(n):
    temp=x[_]
    x[_]+=h/2
    F(x,f)
    for _2 in range(n): deriv[_2,_]=f[_2] #ヤコビ行列のための準備
    x[_]=temp
  
  for _ in range(n):
    temp=x[_]
    x[_]-=h/2
    F(x,f)
    for _2 in range(n): deriv[_2,_]=(deriv[_2,_]-f[_2])/h #ヤコビ行列生成
    x[_]=temp

  return deriv

for _ in range(1,100):
  Rate


