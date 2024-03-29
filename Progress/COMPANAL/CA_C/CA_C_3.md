
- [複素微分](#複素微分)
  - [実数値関数と複素微分](#実数値関数と複素微分)
- [整関数](#整関数)
- [留数計算](#留数計算)
  - [零点](#零点)
  - [テクニック](#テクニック)
- [複素線積分](#複素線積分)
  - [簡単な線積分](#簡単な線積分)
  - [実関数の広義積分値](#実関数の広義積分値)
  - [有理関数 $P(x)/Q(x)$ の広義積分](#有理関数-pxqx-の広義積分)
  - [多項式 $P(x)$](#多項式-px)
  - [無限級数](#無限級数)




# 複素微分

## 実数値関数と複素微分

・実数値関数 $f(z)=u(x,y)$、$u$が微分可能とする。このとき、$u_x(x,y)=u_y(x,y)=0$となる点で微分可能で、それ以外の点で微分不可能

---

# 整関数

<dl><dt>

・$f:\bm{C}\to\bm{C}$ とする。
このとき、整関数 $f$：
$$f\text{ は }\bm{C}\text{ 上正則}$$
<br>

</dt><dd>

- $\bm{C}$ 上有界な整関数 $f:\bm{C}\to\bm{C}$ とする。
このとき、$f$ は定数関数。

</dd></dl>

---

# 留数計算

## 零点

・$f(z)=1+z^n$
→零点：$z=e^{i\frac{\pi}{n}},...,e^{i\frac{(2n-1)\pi}{n}}$

## テクニック
・$a$が$f$の$n$次の極ならば、$Res(f,a,n)=\frac{1}{(n-1)!}\lim_{z\to a}\frac{d^n}{dz^{n-1}}[(z-a)^nf(z)]$

・関数$f$が正則関数の分数形で表されるとき：$f(z)=\frac{f_1(z)}{f_2(z)}$　
このとき、$z_0$が$f_2$の$n$次の零点かつ$f_1$の正則点ならば、$z_0$は$n$次の極

    ・f_2のm次の極ならば、z_0はn+m次の極

---

・$$f(z)=\frac{\sin z}{z^{2k}}\ (k>0)$$
$Res (f,0,2k)=\frac{(-1)^k}{(2k-1)!}$

---

・$$f(z)=\frac{1}{z^2(z-1)^3}$$
→$Res(f,0,2)=-3,\quad Res(f,1,3)=3$ 

---

・$$f(z)=\frac{z}{\sin z}$$

→$Res(f,n\pi,1)=(-1)^nn\pi\quad (n\neq0)$

---
---
---

# 複素線積分

    ・正則関数の積分は経路によらない！

## 簡単な線積分

・$f(z)=\frac{1}{z-a},\quad z(t)=a+re^{it}$ とする。
このとき、$f$ は $\bm{C}-\{a\}$ 上正則で、
$$\int_Cf(z)dz=2\pi i$$

---

## 実関数の広義積分値

・$$\int_{0}^{\infty}\frac{\sin x}{x}dx=\pi/2$$

    ・sinc関数

→$\oint_{長方形}\frac{e^{iz}}{z}=0$による

→留数定理を使うと失敗する！

    ・そもそも広義積分の定義が極限だから、零点を回避することになる

→この積分は絶対収束でないが、収束する

---

・$\int_{0}^{2\pi}\log(1-2r\cos t+r^2)dt=\begin{cases}
0 & (0\le r\le1)  \\
4\pi\log r & (1<r) \\
\end{cases}$

    ・0~πまでの積分値の2倍
- $\int_0^{\pi/2}\log\sin\theta d\theta=-\frac{\pi}{2}\log2$


---

## 有理関数 $P(x)/Q(x)$ の広義積分

・$\deg P+2\le\deg Q$かつ$Q(x)$が実軸上に零点を持たないとき

    ・仮定から広義積分が収束する

→上半平面 $H=\{x+yi\ |\ x\in\bm{R},\ y>0\}$ 内の相異なる $Q(x)$ の零点を $a_1,...,a_n$ とおくと、$\int_{-\infty}^{\infty}R(x)dx=2\pi i\sum\mathrm{Res}(R,a_j)$



→
$$\int_{0}^{\infty}\frac{x^{m-1}}{1+x^n}=\quad\frac{\pi}{n\sin(m\pi/n)}(0<m<n{は自然数})$$

    

→$\int_{-\infty}^{\infty}\frac{1}{1+x^6}=\frac{2\pi}{3},\ \int_{0}^{\infty}\frac{1}{1+x^3}=\frac{2\pi}{3\sqrt{3}},\ \int_{-\infty}^{\infty}\frac{1}{1+x^2}=\pi$ 

    ・最後のはtan^{-1}のこと

## 多項式 $P(x)$

## 無限級数

・$z\to z_0\neq0$ならば、$|1-(\frac{z_0}{z})^n|=0$
・級数$f(z)$が収束円板上の点$z_0$で収束するならば、$f(z_0)=\lim_{z\to z_0} f(z)$（円板内から近づける）

    ・原点からじゃないやつはめんどくさそう、でもたぶん成り立つ