
- [指数関数 $exp$](#指数関数-exp)
  - [簡単な関係式](#簡単な関係式)
  - [$R$ 上の $exp$](#r-上の-exp)
    - [逆関数](#逆関数)
- [三角関数 $sin,cos$](#三角関数-sincos)
  - [簡単な関係式](#簡単な関係式-1)
    - [零点](#零点)
  - [展開](#展開)
    - [テイラー展開（多項式展開）](#テイラー展開多項式展開)
  - [$R$ 上の $sin,cos$](#r-上の-sincos)
- [$R$ 上のinv $tan$](#r-上のinv-tan)
- [双曲線関数 $sinh,cosh$](#双曲線関数-sinhcosh)
  - [$R$ 上の $sinh,cosh$](#r-上の-sinhcosh)



# 指数関数 $exp$

## 簡単な関係式

・$$\forall l\in\bm{N}\text{ に対して、}i^l=e^{i\frac{l\pi}{2}}$$

---

## $R$ 上の $exp$

### 逆関数

|**$Exp_SinCos-1-1$** |
|:-|

$x>0$ とする。
このとき、$$y\in\bm{R}\text{ がただ一つ存在して、}x=e^y$$
ここで、
$$\log:(0,\infty)\to\bm{R}\\\ \\
\log(x)=\text{ 上記の }y$$
となる関数、すなわち、$\exp$ の実数範囲における逆関数を $\log$ とする。([Log参照](Progress\COMPANAL\CA_C\Log\Log_1.md))

>qed,解析入門1,p.195（杉浦）


<br>

---

# 三角関数 $sin,cos$

## 簡単な関係式

・$$\sin\left(x-\frac{l\pi}{2}\right)=\frac{1}{2i}(e^{ix}-(-1)^le^{-ix})\quad (l=0,1,...,\ x\in\bm{R})$$

・$$\frac{1}{2}\int_{0}^{\pi}\sin^n\theta=\frac{1}{2}\int_0^n\cos^n\theta=\int_0^{\pi/2}\sin\theta^n\\\ \\
=\begin{cases}
\frac{n-1}{n}...\frac{2}{3} & (n{奇数})  \\
\frac{n-1}{n}...\frac{1}{2}\frac{\pi}{2} & (n{偶数}) \\
\end{cases}$$

- $z=x+iy$ とすると、
$$\cos z=\cos x\cosh y+i\sin x\sinh y\\\ \\
|\cos z|=\cos^2x+\sinh^2y$$
特に、これは実数のときと整合する。

      ・虚実分解。

### 零点

・$$\{z\in\bm{C}\ |\ \sin z=0\}=\pi\bm{Z}\\\ \\
\{z\in\bm{C}\ |\ \cos z=0\}=\frac{\pi}{2}\bm{Z}$$
であって、零点は共にすべて一次。

---

## 展開

### テイラー展開（多項式展開）

・$x=a$ での展開：
常に可能で、$f(x)=f(a)+f'(a)(x-a)+...$

    ・いつもの形に代入するわけにはいかない。展開してからまとめるとよい。

---

## $R$ 上の $sin,cos$

・$\forall x\text{ に対して、}\sin x\le |x|$
特に、$\sin x$ は $L=1$ でリプシッツ連続。

---

# $R$ 上のinv $tan$

・$x,y\in\bm{R}-\{0\}$ とする。
このとき、
$$\arctan(-x)=-\arctan(x),\quad\arctan\frac{y}{x}+\arctan\frac{x}{y}=\frac{\pi}{2}\\\ \\$$



# 双曲線関数 $sinh,cosh$

## $R$ 上の $sinh,cosh$

・$\cosh x\ge1\ \ (\forall x\in\bm{R})$ であって、$x<0$ で単調減少、$x=0$ で最小値 $\cosh0=1$、$x>0$ で単調増加。

- $$\lim_{x\to\pm\infty}\cosh x=\infty$$

- $\cosh (-x)=\cosh x$ 。よって、偶関数。

---

・$\sinh x$ は狭義単調増加関数で、$x=0$ のとき $\sinh x=0$

 - $$\lim_{x\to\infty}\sinh x=\infty,\quad\lim_{x\to-\infty}\sinh x=-\infty$$

- $\sinh (-x)=-\sinh x$ 。よって、奇関数。 
