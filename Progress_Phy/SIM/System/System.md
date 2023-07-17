# 数値解析的な力学系

## 釣り合い

##### $n+2$本の棒、$n+1$本の糸、$n$個の質点

    ・形状は(3String2point3stick.py)参照

・解くべき方程式
$$x=\begin{pmatrix}\sin\theta_1 \\ \vdots \\ \sin\theta_1 \\ \cos\theta_1 \\ \vdots \\ \cos\theta_n \\ T_1 \\ \vdots \\ T_n\end{pmatrix},
\quad f(x)=\begin{pmatrix}\sum L_ix_{n+i}-L \\ \sum L_ix_i \\ \vdots \\ x_{n+j}x_{2n+j}-x_{n+j+1}x_{2n+j+1} \\ \vdots \\ x_{j}x_{2n+j}-x_{j+1}x_{2n+j+1}-W_j \\ \vdots \\ x_i^{2}+x_{n+i}^2-1 \\ \vdots\end{pmatrix}=0\\\ \\
(-\pi/2\le\theta_i\le\pi/2,\ i=1,...,n,\ j=1,...,n-1)$$

→後半の$f$は $x_{n+1}^2-\sqrt{1-x_i^2}$ とすると定義域の情報も含む

---

・ニュートンラフソン法

---

・バックトラッキング

---

