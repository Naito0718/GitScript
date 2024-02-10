
- [Buchner可測関数](#buchner可測関数)
  - [Bochner可測関数の性質](#bochner可測関数の性質)
- [準Bochner可測単関数](#準bochner可測単関数)
  - [測度空間上の性質 $P(μ)$](#測度空間上の性質-pμ)
    - [Bochner可測関数の $P(μ)$ 性から従う性質](#bochner可測関数の-pμ-性から従う性質)
  - [Bochner可測関数の単関数近似](#bochner可測関数の単関数近似)
- [Banach空間値 $L^p$ 関数](#banach空間値-lp-関数)
  - [Banach空間値 $L^p$ 関数のBochner可測単関数近似](#banach空間値-lp-関数のbochner可測単関数近似)
  - [Hilbert空間値 $L^2$ 関数](#hilbert空間値-l2-関数)


# Buchner可測関数

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$f:X\to B$ とする。
このとき、Bochner可測関数 $f$：
$$f(X)\text{ は可分であって、}\forall \phi\in B^{\vee}\text{ に対して、}\phi\circ f:X\to\bm{R,C}\text{ が可測}\\\ \\$$

- 可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$f:X\to B$ とする。
このとき、Bochner可測単関数 $f$：
$$f(X)\text{ は有限集合であって、}\forall \phi\in B^{\vee}\text{ に対して、}\phi\circ f:X\to\bm{R,C}\text{ が可測}$$
明らかに、Bochner可測単関数はBochner可測関数。
<br>

</dt><dd>

- $b\in B$ とする。
このとき、
$$f_b:X\to B\\\ \\
f_b(x)=b$$
と定めると、$f_b$ はBochner可測単関数。
<br>

- $f:X\to B$ とする。
このとき、
$$f\text{ はBochner可測単関数}\\\ \\
\iff\exist b_1,...,b_n\in B,\ \exist\text{ 有限可測分割 }E_1,...,E_n\subset\mathfrak{M}\text{ であって、}
f=\sum_{i=1}^n\chi_{E_i}b_i$$

</dd></dl>

---

## Bochner可測関数の性質

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、Bochner可測関数 $f,g:X\to B$ とする。
<br>

</dt><dd>

- 可測関数 $h:X\to\bm{R,C}$ とする。
このとき、$f+g,hf$ はBochner可測関数。
<br>

- $g_0:X\to B$ に各点収束 $\lim_{n\to\infty}f_n(x)=f(x)$ するBochner可測関数列 $f_n:X\to B$ とする。
このとき、$g_0$ はBochner可測関数。
<br>

- $\|f\|:X\to[0,\infty)$ は可測関数。
<br>

</dd></dl>

---

# 準Bochner可測単関数

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$f:X\to B$、$E\in\mathfrak{M}$ とする。
このとき、$f$ が $E$ 上準Bochner可測単関数：
$$\forall\epsilon\text{ に対して、}\exist\text{ 有限可測分割 }E_1,...,E_n\in\mathfrak{M}\text{ であって、}\forall x,y\in E_i\text{ に対して、}\|f(x)-f(y)\|<\epsilon\\\ \\$$
ここで、$f$ は$\forall\text{ 可測集合 }F\in\mathfrak{M},\ F\sub E$ 上で準可測単関数。
<br>

</dt><dd>

・可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$E\in\mathfrak{M}$、$E$ 上準Bochner可測単関数 $f:X\to B$ とする。
このとき、
$$\forall\epsilon>0\text{ に対して、}\exist\text{ Bochner可測単関数 }s:X\to B\text{ であって、}\\\ \\
\forall x\in X\text{ に対して、}\|f(x)-s(x)\|<\epsilon\text{ かつ }\|s(x)\|\le\|f(x)\|,\\\ \\
\forall x\in E^c\text{ に対して、}s(x)=0\\\ \\$$

- 可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$E\in\mathfrak{M}$、$E$ 上準Bochner可測単関数である関数列列 $f_n:X\to B$ とする。
このとき、
$$f_n\text{ は関数 }f:X\to B\text{ に一様収束}\\\ \\
\Rightarrow f\text{ は }E\text{ 上準Bochner可測単関数}$$

</dd></dl>

---

## 測度空間上の性質 $P(μ)$

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、$f:X\to B$ とする。
このとき、$f$ が性質 $P(\mu)$ を満たす：
$$\mu(E)<\infty\text{ なる }\forall E\in\mathfrak{M},\ \forall\epsilon>0\ {に対して、}\\\ \\
\exist F\in\mathfrak{M}\ {であって、}\\\ \\
F\subset E,\ \mu(E-F)<\epsilon,\ f\ {は}\ {F}\ {上準可測単関数}\\\ \\$$ 
明らかに、Bochner可測単関数は $F=E$ 上で準可測単関数、すなわち性質 $P(\mu)$ を満たす。
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$ 、Bochner可測関数 $f:X\to B$ とする。
このとき、$f$ は性質 $P(\mu)$ を満たす。

---

### Bochner可測関数の $P(μ)$ 性から従う性質

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、Bochner可測関数 $f:X\to B$ とする。
このとき、
$$\mu(E),\infty\text{ なる }\forall E\in\mathfrak{M}\text{ に対して、}\exist\text{ 非交叉列 }(F_n)\sub\mathfrak{M}\text{ であって、}\\\ \\
\mu(E-\bigcup F_n)=0,\ \forall n\in\bm{N}\text{ に対して、}F_n\sub E\text{ かつ }f\text{ は }F_n\text{ 上で準可測単関数}$$

---

## Bochner可測関数の単関数近似

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、Bochner可測関数 $f:X\to B$ とする。
このとき、
$$\exist\text{ Bochner可測単関数列 }s_n:X\to B\text{ であって、}\\\ \\
\forall n\in\bm{N},\ \forall x\in X\text{ に対して、}\|s_n(x)\|\le\|f(x)\|\\\ \\
\lim_{n\to\infty}s_n(x)=f(x)\quad(\mu-a.e.)$$ 

---

# Banach空間値 $L^p$ 関数

    ・そもそもBochner可測関数ならL^1？

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$ とする。
このとき、Bochner可測関数全体 $$\mathcal{L}(X,\mathfrak{M},B)$$は $\bm{R,C}$ 上ベクトル空間。
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、Bochner可測関数全体 $\mathcal{L}(X,\mathfrak{M},B)$ とする。
このとき、同値関係と演算：
$$f\sim g\iff f(x)=g(x)\quad (\mu-a.e.)\\\ \\
[f]+[g]=[f+g],\quad \alpha[f]=[\alpha f]$$はwell-defined。
この同値関係によって、$\bm{R,C}$ 上ベクトル空間 $L(X,\mathfrak{M},B,\mu)$ を定義する。
<br>

</dt><dd>

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$p\in[1,\infty)$、$f\in L(X,\mathfrak{M},B,\mu)$ とする。
このとき、$$\|f\|_{p}=\left(\int\|f(x)\|^pd\mu\right)^{\frac{1}{p}}\\\ \\
\|f\|_{\infty}=\inf\Big\{\alpha\in[0,\infty)\ |\ \mu\Big((\alpha<\|f(x)\|)\Big)=0\Big\}\quad({右辺が空なら}\ \infty)$$
と定めると、$\|\cdot\|_p,\|\cdot\|_{\infty}$ は共に $L(X,\mathfrak{M},B,\mu)$ 上のノルム。
<br>

- $$[f]=[g]\Rightarrow \|f\|_{p}=\|g\|_{p},\ \|f\|_{\infty}=\|g\|_{\infty}\\\ \\$$

- $$L^{p}(X,B)=\{f\in L(X,B)\ |\ \|f\|_{p}<\infty\}\\\ \\
L^{\infty}(X,B)=\{f\in L(X,B)\ |\ \|f\|_{\infty}<\infty\}$$ 
は共に $\bm{R,C}$ 上Banach空間

</dd></dl> 

---

## Banach空間値 $L^p$ 関数のBochner可測単関数近似

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、$p\in[1,\infty)$、$f\in \mathcal{L}^p(X,B)$ とする。
このとき、
$$\forall\text{ Bochner可測単関数 }s:X\to B,\quad s(x)=\sum\chi_{E_i}(x)b_i\text{ に対して、}\\\ \\
s\in \mathcal{L}^p(X,B),\quad\mu(E_i)<\infty$$ 
であって、
$$\exist\text{ Bochner可測単関数列 }s_n:X\to B\text{ であって、}\\\ \\
\|s_n(x)\|\le\|f(x)\|\ (\forall n\in\bm{N},\forall x\in X)\\\ \\
\lim_{n\to\infty}\|f-s_n\|_{p}=0$$

---

## Hilbert空間値 $L^2$ 関数

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Hilbert空間 $\mathcal{H}$、$f,g\in L^2(X,\mathcal{H})$ とする。
このとき、$$\phi:X\to\bm{R,C},\quad\phi(x)=(f(x),g(x))\\\ \\
(f,g)_2=\int_{X} (f(x),g(x))d\mu$$
と定めると、$\phi$ は可測関数であって、
$$\int_X|\phi(x)|d\mu\le\|f\|_2\|g\|_2$$
を満たす。すなわち、$(f,g)_2$ はwell-definedな$L^2(X,\mathcal{H})$ 上の内積。

