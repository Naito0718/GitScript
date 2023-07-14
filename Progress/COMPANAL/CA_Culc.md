# 複素関数の具体例、計算例



## 複素微分

・実数値関数$f(z)=u(x,y)$、$u$が微分可能とする。このとき、$u_x(x,y)=u_y(x,y)=0$となる点で微分可能で、それ以外の点で微分不可能

## 留数計算

##### テクニック
・$a$が$f$の$n$次の極ならば、$Res(f,a,n)=\frac{1}{(n-1)!}\lim_{z\to a}\frac{d^n}{dz^{n-1}}[(z-a)^nf(z)]$

・関数$f$が正則関数の分数形で表されるとき：$f(z)=\frac{f_1(z)}{f_2(z)}$　
このとき、$z_0$が$f_2$の$n$次の零点かつ$f_1$の正則点ならば、$z_0$は$n$次の極

    ・f_2のm次の極ならば、z_0はn+m次の極

---

$$f(z)=\frac{\sin z}{z^{2k}}\ (k>0)$$
$Res (f,0,2k)=\frac{(-1)^k}{(2k-1)!}$

---

$$f(z)=\frac{1}{z^2(z-1)^3}$$
$Res(f,0,2)=-3,\quad Res(f,1,3)=3$ 

---

$$f(z)=\frac{z}{\sin z}$$

$Res(f,n\pi,1)=(-1)^nn\pi\quad (n\neq0)$

## 多項式 $P(x)$

## 無限級数 $\sum c_nz^n$

・$z\to z_0\neq0$ならば、$|1-(\frac{z_0}{z})^n|=0$
・級数$f(z)$が収束円板上の点$z_0$で収束するならば、$f(z_0)=\lim_{z\to z_0} f(z)$（円板内から近づける）

    ・原点からじゃないやつはめんどくさそう、でもたぶん成り立つ