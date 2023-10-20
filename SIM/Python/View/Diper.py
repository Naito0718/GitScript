import matplotlib.pyplot as plt
import numpy as np

Xmin=-5; Xmax=5
x0=np.arange(Xmin-1,Xmax+1) #差1の数列
x=np.arange(Xmin,Xmax) #差1の数列
y=np.sin(x)*np.sin(x*x) #関数の指定

errTop=np.abs(np.sin(x))
errBot=np.abs(np.cos(x))

print(f'取ったx軸上の点の数={x[0]}, {x[1]}, {len(x)}')
print(f'yの値の範囲=>y[0],y[1],y[max]={y[0]}, {y[1]}, {y[len(x)-1]}')
print("\n Now doing the plotting thing,look for Figure 1 on desktop")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x0, np.zeros(len(x0)),'-',lw=2)  #y=0の線
ax.plot(x,y,'r')  

ax.errorbar(x,y,[errBot,errTop],fmt='o')

plt.xlabel('x'); plt.ylabel('f(x)'); plt.title('f(x) vs x')
plt.text(-1.75,0.75,'MatPlotLib Example')   #指定した座標に文字列
plt.grid(True)  #格子生成
plt.show()






