import matplotlib.pyplot as plt
import numpy as np

Xmin=-5.; Xmax=5.; Npoints=500  #定義域と分割幅
DeIx=(Xmax-Xmin)/Npoints 
x=np.arange(Xmin,Xmax,DeIx) #数列生成,np.linespase()では分割数を指定できる
y=np.sin(x)*np.sin(x*x) #関数の指定

print(f'arange=>x[0],x[1],x[max]={x[0]:.2f}, {x[1]:.2f}, {x[len(x)-1]:.2f}')
print(f'arange=>y[0],y[1],y[499]={y[0]:.2f}, {y[1]:.2f}, {y[len(x)-1]:.2f}')
print("\n Now doing the plotting thing,look for Figure 1 on desktop")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y,'-',lw=2)  #-は点をつないで描画、lwは線の幅
plt.xlabel('x'); plt.ylabel('f(x)'); plt.title('f(x) vs x')
plt.text(-1.75,0.75,'MatPlotLib Example')   #指定した座標に文字列
plt.grid(True)  #格子生成
plt.show()






