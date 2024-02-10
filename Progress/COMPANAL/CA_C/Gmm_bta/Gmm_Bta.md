
- [ガンマ関数のwell-defined性](#ガンマ関数のwell-defined性)
  - [ガンマ関数の性質](#ガンマ関数の性質)
    - [ガンマ関数の性質 $2$](#ガンマ関数の性質-2)
    - [ガンマ関数のちょっとした性質](#ガンマ関数のちょっとした性質)
  - [スターリング式](#スターリング式)
- [ベータ関数](#ベータ関数)


# ガンマ関数のwell-defined性

<dl><dt>

・$x\in(0,\infty)$ とする。さらに、
$$\gamma_x:(0,\infty)\to\bm{R}\\\ \\
\gamma_x(t)=e^{-t}t^{x-1}$$
として、$\gamma_x\in\mathcal{L}^1(0,\infty)$ であるかを考える。
ここで、
$$\Gamma:(0,\infty)\to\bm{R}\\\ \\
\Gamma(x)=\int_0^{\infty}e^{-t}t^{x-1}dm(t)$$
をガンマ関数という。
<br>

</dt><dd>

・$x\in(0,\infty)$ とし、
$$f,F,G:(0,\infty)\to\bm{R}\\\ \\
f(t)=-e^{-t},\quad F(t)=e^{-t},\quad G(t)=\frac{1}{x}t^x$$
と定めると、$G$ は $(0,\infty)$ 上 $C^1$ であって、$F$ は $f$ の原始関数。さらに、$$F(t)\frac{dG}{dt}(t)=e^{-t}t^{x-1}$$
より、$F(t)\frac{dG}{dt}(t)$ は $(0,\infty)$ 上非負。
<br>

- 
$$fG=-\frac{1}{x}e^{-t}t^x\\\ \\
\frac{d}{dt}\Big[fG(t)\Big]=-\frac{e^{-t}}{x}t^{x-1}(x-t)$$
したがって、
$$\frac{d}{dt}\Big[fG(t)\Big]=0\iff t=x\\\ \\
\lim_{t\to+0}fG(t)=0,\quad\lim_{t\to\infty}fG(t)=0,\quad fG(x)=-x^{x-1}e^{-x}$$
特に、$fG$ は $(0,\infty)$ 上有界で、最小値 $-x^{x-1}e^{-x}$、上限 $0$。
<br>

- 
$$FG=\frac{1}{x}e^{-t}t^x\\\ \\
\frac{d}{dt}\Big[FG(t)\Big]=\frac{e^{-t}}{x}t^{x-1}(x-t)$$
したがって、
$$\frac{d}{dt}\Big[FG(t)\Big]=0\iff t=x\\\ \\
\lim_{t\to+0}FG(t)=0,\quad\lim_{t\to\infty}FG(t)=0,\quad FG(x)=x^{x-1}e^{-x}$$
特に、$FG$ は $(0,\infty)$ 上有界で、最大値 $x^{x-1}e^{-x}$、下限 $0$。
<br>

- 上記より、[部分積分](../../DIFFGEO.md/RNGeo/RNGeo_1_2_2.md) を適用できる。
したがって、$F\frac{dG}{dt}=\gamma_x$ は $(0,\infty)$ 上可積分であって、
$$\int_0^{\infty}\Big[-\frac{1}{x}e^{-t}t^x\Big]dm(t)+\int_0^{\infty}\Big[e^{-t}t^{x-1}\Big]dm(t)=0$$
ここで、この式は $\Gamma(x+1)=x\Gamma(x)$ のことである。

</dd></dl>

---

## ガンマ関数の性質

・$$\Gamma(1)=1,\quad\forall x\in x\text{ に対して、}\Gamma(x)>0\\\ \\$$

- $$\Gamma(x+1)=x\Gamma(x)$$

---

### ガンマ関数の性質 $2$

---

### ガンマ関数のちょっとした性質

・$\lambda>0$、$n\in\bm{N}$ とする。
このとき、
$$\int_0^{\infty}e^{-\lambda t}t^ndm(t)=\frac{n!}{\lambda^{n+1}}\\\ \\$$

    ・n=0の時は普通に積分、n>0の時はガンマ関数使うといい。

---

## スターリング式

・
$$\Gamma(x)=\sqrt{2\pi}x^{x-\frac{1}{2}}e^{-x}e^{\mu(x)}\\\ \\
\mu(x)=\sum_{n\ge0}g(x+n)\\\ \\
g(x)=\left(x+\frac{1}{2}\right)\log\left(1+\frac{1}{x}\right)-1\\\ \\$$

- 
$$\Gamma(x)\sim\sqrt{2\pi}x^{x-\frac{1}{2}}e^{-x}\ \ (x\to\infty)\\\ \\
n!\sim \sqrt{2\pi(n+1)}(n+1)^{n}e^{-n-1}\ \ (n\to\infty)\\\ \\
\log1+...+\log n=\log n!\\
\sim n(\log n-1)=\int_1^n\log xdx-1$$

    ・最初だけ両辺で差取ればε未満になる。

---

# ベータ関数

・
$$B:(0,\infty)\times(0,\infty)\to\bm{R}\\\ \\
B(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}dm(t)$$