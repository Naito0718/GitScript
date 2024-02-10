\newpage

\section{付録}

\subsection{波形データ：同相（逆相、うなりも同様なので省略）}
\begin{lstlisting}[caption=info1,label=fuga]
import numpy as np
import matplotlib.pyplot as plt


DOSOch1 = np.loadtxt("./DOSOch1.txt", comments='!')
DOSOch1_axis1, DOSOch1_value1 = np.loadtxt("./DOSOch1.txt", comments='!', unpack=True)

DOSOch2 = np.loadtxt("./DOSOch2.txt", comments='!')
DOSOch2_axis1, DOSOch2_value1 = np.loadtxt("./DOSOch2.txt", comments='!', unpack=True)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(DOSOch1_axis1, DOSOch1_value1, color="k", label="value of ch1")
ax.plot(DOSOch2_axis1, DOSOch2_value1, color="red", label="value of ch2")
ax.set_xlim(0, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel("time[s]")
ax.set_ylabel("volt[V]")
ax.legend(loc="upper left")
plt.savefig('plot_DOSOwave.pdf', transparent=True, bbox_inches ='tight')
plt.show()
\end{lstlisting}

\subsection{周波数スペクトル：同相（逆相、うなりも同様なので省略）}
\begin{lstlisting}[caption=info3,label=fuga]
import numpy as np
import matplotlib.pyplot as plt
#import math


DOSOch1 = np.loadtxt("DOSOch1.txt", comments='!')
DOSOch1_axis1, DOSOch1_value1 = np.loadtxt("DOSOch1.txt", comments='!', unpack=True)

n=len(DOSOch1_axis1)
w_ch1 = []
F_ch1 = []

h = 0.01
for w in np.arange(0.0,10.0,0.01):
    Re = 0
    Im = 0
    
    for i in range(0,n):
        Re += DOSOch1_value1[i] *np.cos (w * DOSOch1_axis1[i]) * h
        Im += DOSOch1_value1[i] * np.sin (w * DOSOch1_axis1[i]) * h

    F = ( Re**2 + Im**2 ) /(2.0*np.pi**2) 
    w_2=w/(2*np.pi)
    w_ch1.append(w_2)
    F_ch1.append(F)
    

DOSOch2 = np.loadtxt("DOSOch2.txt", comments='!')
DOSOch2_axis1, DOSOch2_value1 = np.loadtxt("DOSOch2.txt", comments='!', unpack=True)

n=len(DOSOch2_axis1)
w_ch2 = []
F_ch2 = []

h = 0.01
for w in np.arange(0.0,10.0,0.01):
    Re = 0
    Im = 0
    
    for i in range(0,n):
        Re += DOSOch2_value1[i] *np.cos (w * DOSOch2_axis1[i]) * h
        Im += DOSOch2_value1[i] * np.sin (w * DOSOch2_axis1[i]) * h

    F = ( Re**2 + Im**2 ) /(2.0*np.pi**2) 
    w_2=w/(2*np.pi)
    w_ch2.append(w_2)
    F_ch2.append(F)
    
m1=np.argmax(F_ch1)
m2=np.argmax(F_ch2)
w_m1=w_ch1[m1]
w_m2=w_ch2[m2]
print('ピーク周波数：f_ch1=',w_m1,'f_ch2=',w_m2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(w_ch1, F_ch1, color="k", label="ch1")
ax.plot(w_ch2, F_ch2, color="red", label="ch2")
ax.set_xlabel("frequence[Hz]")
ax.set_ylabel("amplitude[arb]")
ax.legend(loc="upper left")
plt.legend
plt.savefig('plot_DOSOfourier.pdf', transparent=True, bbox_inches ='tight')
plt.show()
\end{lstlisting}

\subsection{三重対角化関数による対角化}
\begin{lstlisting}[caption=info3,label=fuga]
import numpy as np
from scipy import linalg
a = [0.0,0.0,0.0,0.0,0.0]
b = [1.0,1.0,1.0,1.0]
w, U = linalg.eigh_tridiagonal(a, b)


print('対角化=')
print(np.diag(w))
print('固有ベクトルを横に並べた行列U.T=')
print(U.T)
\end{lstlisting}

\subsection{振り子の時間発展シミュレーション}
\begin{lstlisting}[caption=info3,label=fuga]
import tempfile
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

m=26.8E-3
g=9.8
l=0.48
b=0.1
c=1.89E-4

xi=g/l
eta=c/(m*b*l*l)

a = [-xi-eta,-xi-2*eta,-xi-2*eta,-xi-2*eta,-xi-eta]
b = [eta,eta,eta,eta]
w, U = linalg.eigh_tridiagonal(a, b)

theta_0=np.array([1.0,0.0,0.0,0.0,0.0])
theta=np.zeros(5)
W=np.zeros(5)
T=[]
Th_0=[]
Th_1=[]
Th_2=[]
Th_3=[]
Th_4=[]



for t in np.arange(0.0,30.0,0.1):
    for i in range(4):
        W[i]=np.cos(w[i]*t)
    theta=U@np.diag(W)@U.T@theta_0
    T.append(t)
    Th_0.append(theta[0])
    Th_1.append(theta[1]+2)
    Th_2.append(theta[2]+4)
    Th_3.append(theta[3]+6)
    Th_4.append(theta[4]+8)



fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(T, Th_0,color="k")
ax.plot(T, Th_1, color="r")
ax.plot(T, Th_2, color="b")
ax.plot(T, Th_3, color="g")
ax.plot(T, Th_4, color="y")

ax.set_xlabel("time[s]")
ax.set_ylabel("angle[rad]")
ax.legend(loc="upper left")
plt.legend
plt.savefig('plot_SimuationWave.pdf', transparent=True, bbox_inches ='tight')
plt.show()

\end{lstlisting}
