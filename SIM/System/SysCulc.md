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

## ばね

##### 変位$x$が大きいとき

・ポテンシャル：$V(x)=\frac{1}{2}kx^2(1-\frac{2}{3}\alpha x)$

→$F_k(x)=-kx(1-\alpha x)$

    ・αx<<1なら調和振動子

→$x<1/\alpha$である限り復元力が働く

→解くべき方程式：
$$\frac{dy}{dt}=\begin{pmatrix}y_1 \\ -\frac{k}{m}y_0(1-\alpha y_0)\end{pmatrix}$$

---

##### べき乗ポテンシャル $V(x)=\frac{1}{p}kx^p\quad(p{は偶数})$

・$F_k(x)=-kx^{p-1}$

→常に復元力が働くことになる

→$p$が大きいほど井戸型ポテンシャルに近くなる（反射みたいになる）

→解くべき方程式：
$$\frac{dy}{dt}=\begin{pmatrix}y_1 \\ -\frac{k}{m}y_0^{p-1}\end{pmatrix}$$

---

## 熱力学シミュレーション、ファインマン経路積分

・イジング鎖

・メトロポリス法

・ワン-ランダウ法

・ファインマン経路積分

---

## 分子運動シミュレーション

・ベルレ法、速度ベルレ法

---

## 熱伝導方程式

## 弦と膜

## 波束、電磁波

##### 二次元導体板に外部から電流を流す

→

・解くべき方程式：



## 衝撃波とソリトン

## 流体力学

## 量子力学の積分方程式


