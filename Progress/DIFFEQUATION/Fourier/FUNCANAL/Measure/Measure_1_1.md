- [測度論の基礎](#測度論の基礎)
  - [σ-加法族](#σ-加法族)
  - [可測関数](#可測関数)
    - [可測性と生成 $σ$-加法族](#可測性と生成-σ-加法族)
  - [Borel集合族](#borel集合族)
    - [Borel写像](#borel写像)
- [実数値可測関数](#実数値可測関数)
  - [拡張実数](#拡張実数)
    - [演算](#演算)
    - [$σ$-加法族](#σ-加法族-1)
    - [［$-∞,∞$］値可測関数](#-値可測関数)
      - [可測関数の演算](#可測関数の演算)
  - [$R,C,R^n$値関数](#rcrn値関数)
  - [可測関数のなすベクトル空間](#可測関数のなすベクトル空間)
    - [可測関数の可測単関数近似](#可測関数の可測単関数近似)
- [測度](#測度)
  - [測度の基本的な性質](#測度の基本的な性質)
    - [測度の細かい性質](#測度の細かい性質)
  - [測度の演算](#測度の演算)


# 測度論の基礎

## σ-加法族

・集合 $X$、部分集合 $\mathfrak{M}\sub 2^X$ とする。
このとき、$\sigma$-加法族 $\mathfrak{M}$：
$$X\in\mathfrak{M}\\\ \\
\forall E\in\mathfrak{M}\text{ に対して、}E^C\in\mathfrak{M}\\\ \\
\forall\text{ 点列 }(E_n)\sub\mathfrak{M}\text{ に対して、}\bigcup E_n\in\mathfrak{M}$$
ここで、$(X,\mathfrak{M})$ を可測空間、$E\in\mathfrak{M}$ を可測集合という。
<br>

- 可測空間 $(X,\mathfrak{M})$、$E,F\in\mathfrak{M}$、点列 $(E_n)\sub\mathfrak{M}$ とする。
このとき、
$$\phi,\ \ \bigcap E_n\in\mathfrak{M}\\\ \\
E\cap F,\ E\cup F,\ E/F\in\mathfrak{M}$$

---

・集合 $X$、$\sigma$-加法族の族 $(\mathfrak{M}_{\lambda})\sub2^X$ とする。
このとき、$\bigcap\mathfrak{M_i}$ は $\sigma$-加法族。
<br>

    ・和集合は無理
<br>

- 集合 $X$、部分集合 $\mathcal{I}\sub 2^X$ とする。
このとき、
$$\sigma(\mathcal{I})=\bigcap\{\mathfrak{M}\ |\ \mathfrak{M}\text{ は }X\text{ 上の }\sigma\text{-加法族で、}\mathcal{I}\sub\mathfrak{M}\}$$
と定めると、これは $\mathfrak{I}$ を含む最小の $X$ 上の $\sigma$-加法族。

      ・別に2^Xもσ加法族なので、空ではない。

---

## 可測関数

・可測空間 $(X,\mathfrak{M}_X),\ (Y,\mathfrak{M}_Y)$、$f:X\to Y$ とする。
このとき、可測関数 $f$：
$$\forall E\in \mathfrak{M}_Y\text{ に対して、}f^{-1}(E)\in\mathfrak{M}_X\\\ \\$$

    ・連続関数の定義に近い

- 可測関数 $f,g$ とすると $f\circ g$ は可測関数。

---

### 可測性と生成 $σ$-加法族

・可測空間 $(X,\mathfrak{M}_X),\ (Y,\mathfrak{M}_Y)$、$f:X\to Y$ とする。
このとき、
$$\mathfrak{M}_Y=\sigma(\exist\ \mathcal{I}_Y)\text{ であって、}\\\ \\
\forall I\in \mathcal{I}_Y\text{ に対して }f^{-1}(I)\in\mathfrak{M}_X$$
ならば、$f$ は可測関数。

---

## Borel集合族

・位相空間 $(X,\mathcal{O})$ とする。
このとき、Borel集合族 $\mathfrak{B}$：
$$\mathfrak{B}=\sigma(\mathcal{O})$$

---

### Borel写像

・連続関数はBorel写像。


---
---
---

# 実数値可測関数 

## 拡張実数

<dl><dt>

$$[-\infty,\infty]=\mathbb{R}\cup\{-\infty,\infty\}\\\ \\$$ とし、
$$\infty\le\infty,\ -\infty\le-\infty\\\ \\
\forall x\in\bm{R}\text{ に対して、}-\infty< x<\infty$$とする。
このとき、$[-\infty,\infty]$ は全順序集合。
00<br>

    ・一点コンパクト化ではない。
    ・区間もa,bが±∞取ることを許す。
<br>

</dt><dd>

- $-\infty,\infty$ は $[-\infty,\infty]$ の最大、最小値。
<br>

- 空でない部分集合 $A\sub[-\infty,\infty]$ とする。このとき、$A$ は上限、下限を持つ。

</dd></dl>

---

### 演算

・
$$x+\infty=\infty,\quad x-\infty=-\infty\\\ \\
0\infty=0(-\infty)=0\\\ \\
x\neq0\text{ に対して、}|x|\infty=\infty,\ |x|(-\infty)=-\infty\\\ \\
-(-\infty)=\infty\\\ \\
x\neq0\text{ に対して、}0^{|x|}=0,\ \infty^{|x|}=\infty$$

    ・可換だから、積も負数で定義されてる。
    ・別に積とか累乗は∞でもいい。
<br>

- 族 $(x_j)\sub [0,\infty]$ とする。
このとき、総和 $\sum_{j\in J}x_j$：
$$\sum_{j\in J}x_j=\sup_{F\in\mathcal{F}_J}\sum_{j\in F}x_j\in[0,\infty]$$
これは $\bm{R}$ における総和の定義と整合する。

      ・実数Rの有界な単調増加ネットは上限に収束する。（今有界は外してよい）


---

### $σ$-加法族

<dl><dt>

・
$$\mathcal{B}_{[-\infty,\infty]}=\sigma(\{[a,b],(a,b),(a,b],[a,b)\ |\ \forall a,b\in[-\infty,\infty]\})$$
と定める。
<br>

</dt><dd>

- $$\mathfrak{B}_{[-\infty,\infty],\bm{R}}=\mathfrak{B}_{\bm{R}}$$
すなわち、相対 $\sigma$-加法族と $\bm{R}$ のBorel集合族は一致する。
<br>

</dd></dl>

---

### ［$-∞,∞$］値可測関数

・可測空間 $(X,\mathfrak{M})$、$f:X\to[-\infty,\infty]$ とする。
このとき、
$$f\text{ は可測}\\\ \\
\iff\forall a\in\bm{R}\text{ に対して、}(a<f)\in\bm{R}\iff\forall a\in\bm{R}\text{ に対して、}(a\le f)\in\bm{R}\\\ \\
\iff\forall a\in\bm{R}\text{ に対して、}(a>f)\in\bm{R}\iff\forall a\in\bm{R}\text{ に対して、}(a\ge f)\in\bm{R}\\\ \\$$

    ・まあ別に∞区間は考えなくてもいい。
<br>

- 可測空間 $(X,\mathfrak{M})$、$f:X\to[-\infty,\infty]$ とする。
このとき、
$$f_{\pm}:X\to[0,\infty]\\\ \\
f_+(x)=\max\{f(x),0\},\quad f_-(x)=\max\{-f(x),0\}$$
と定めると、
$$f(x)=f_+(x)-f_-(x),\quad|f(x)|=f_+(x)+f_-(x)$$
ここで、$f_{\pm}$ を非負、非正部分という。
<br>

- 可測空間 $(X,\mathfrak{M})$、可測関数 $f,g:X\to[-\infty,\infty]$ とする。
このとき、
$$(f<g),\ (f\le g),(f=g)\in\mathfrak{M}$$

---

#### 可測関数の演算

    ・積はない。

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、可測関数列 $f_i:X\to[-\infty,\infty]$ とする。
<br>

</dt><dd>

- $\alpha f,\ \text{定義できる時の}f_1+f_2$ は可測関数。
<br>

- $\max\{f_1,...,f_n\},\ \min\{f_1,...,f_n\}$ は可測関数。
<br>

- $\sup_{i\in\bm{N}}f_i,\ \inf_{i\in\bm{N}}f_i$ は可測関数。
<br>

      ・各点に対して常に定義可能なので、well-defined。
<br>

- $f_{+},\ f_{-},\ \forall \alpha>0\text{ に対しての }|f|^{\alpha}$ は可測関数。
<br>

- 可測関数列 $f_n:X\to[-\infty,\infty]$ とする。
このとき、
$$g(x)=\lim_{n\to\infty}[\sup_{k\ge n }f_k(x)],\quad h(x)=\lim_{n\to\infty}[\inf_{k\ge n }f_k(x)]$$は可測。特に、各点収束可測関数列 $f_n:X\to[-\infty,\infty]$ に対して、$\lim_{n\to\infty}f_n$ も可測。
<br>

      ・上極限と下極限。それぞれ単調減少、単調増加なので、inf(sup)、sup(inf)である。

</dd></dl>

---

## $R,C,R^n$値関数

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、$f:X\to\bm{R}^N$ とする。
このとき、
$$f\text{ は可測}\iff \text{すべての成分 }f_i\text{ は可測}$$

    ・複素数値でも実、複素成分の可測性と同値。
<br>

</dt><dd>

- 可測関数 $f,g:X\to\bm{C}$ とする。
このとき、$fg$ は可測。
<br>

- $E\in\mathfrak{M}$、指示関数 $\chi_E:X\to \bm{R}$ とする。
このとき、$\chi_E$ は可測。
<br>

      ・可測集合の指示関数は可測。

</dd></dl>

---

## 可測関数のなすベクトル空間 

・可測空間 $(X,\mathfrak{M})$ とする。
このとき、
$$\mathcal{L}(X,\mathfrak{M})=\{f:X\to\bm{C}\ |\ f{は可測}\}$$
は $\bm{C}$ 上ベクトル空間。
<br>

- $$\mathcal{S}(X,\mathfrak{M})=\mathrm{span}\{\chi_E |\ E\in\mathfrak{M}\}$$
と定めると、これは $\bm{C}$ 上ベクトル空間で、
$$\mathcal{S}(X,\mathfrak{M})=\{f:X\to\bm{C}\ |\ f\text{ は可測かつ、}f(X)\text{ は有限集合}\}$$
ここで、$\mathcal{S}(X,\mathfrak{M})$ の元を可測単関数という。

---

### 可測関数の可測単関数近似

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、可測関数 $f:X\to[0,\infty]$ とする。
このとき、$$f_n(x)=\sum_{k=1}^{n2^n}\frac{k-1}{2^n}\chi_{\frac{k-1}{2^n}\le f\le\frac{k}{2^n}}(x)+n\chi_{n\le f}(x)$$
と定める。
<br>

</dt><dd>

- $f_n\in\mathcal{S}(X,\mathfrak{M})\\\ \\$

- $\forall x\in X\text{ に対して、}f_n(x)\text{ は単調増加列}\\\ \\$

- $f(x)=\sup_{n\in\bm{N}} f_n(x)$

</dd></dl>

---
---
---


# 測度

このとき、測度 $\mu$：
$$\mu(\phi)=0,\\\ \\
\forall\text{ 非交叉列 }(E_n)\sub\mathfrak{M}\text{ に対して、}\mu\left(\bigcup E_n\right)=\sum\mu(E_n)$$

---

・可測空間 $(X,\mathfrak{M})$ とする。
このとき、可測分割：
$$\exist\text{ 非交叉な集合族 }(E_j)\sub\mathfrak{M}\text{ であって、}X=\bigcup E_j\\\ \\$$

・測度空間 $(X,\mathfrak{M},\mu)$、$N\in\mathfrak{M}$ とする。
このとき、$\mu$-零集合 $N$：$\mu(N)=0$
<br>

・測度空間 $(X,\mathfrak{M},\mu)$ とする。
このとき、$\mu$-a.e.$x\in X$で$P(x)$が成り立つ：$$\exists \mu\text{-零集合 }N\in\mathfrak{M}\text{ であって、}\forall x\in X-N\text{ に対して }P(x)\text{ が成り立つ}$$

---

## 測度の基本的な性質

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$ とする。
<br>

</dt><dd>

- 
$$\forall\text{ 非交叉な集合 }E_1,...,E_n\in\mathfrak{M}\text{ に対して、}\\\ \\
\mu\left(\bigcup_{i=1}^nE_i\right)=\sum_{i=1}^n\mu(E_i)\\\ \\$$

- $$\forall\ E,F\in\mathfrak{M},\ E\sub F\text{ に対して、}\\\ \\
\mu(E)\sub\mu(F)\\\ \\
\mu(E)<\infty\text{ ならば、}\mu(F-E)=\mu(F)-\mu(E)\\\ \\$$

- $$\forall\text{ 集合列 }(E_n)\sub\mathfrak{M}\text{ に対して、}\\\ \\
\mu\left(\bigcup E_n\right)\le\sum\mu(E_n)\\\ \\$$

      ・任意の有限個の可測集合に対しても、この不等式が成り立つ。

<br>

- $$\forall\text{ 単調増加集合列 }(E_n)\sub\mathfrak{M},\ E_{n}\sub E_{n+1}\text{ に対して、}\\\ \\
\mu\left(\bigcup E_n\right)\le\sup_{n\in\bm{N}}\mu(E_n)\\\ \\
\forall\text{ 単調減少集合列 }(E_n)\sub\mathfrak{M},\ E_{n}\sup E_{n+1},\ \mu(E_1)<\infty\text{ に対して、}\\\ \\
\mu\left(\bigcap E_n\right)\le\inf_{n\in\bm{N}}\mu(E_n)\\\ \\$$

</dd></dl>

---

### 測度の細かい性質

・測度空間 $(X,\mathfrak{M},\mu)$、集合列 $(E_n)\sub\mathfrak{M}$ とする。
このとき、
$$\mu(\overline{\lim}E_n)\ge\overline{\lim}\mu(E_n)\\\ \\
\mu\left(\bigcup A_n\right)<\infty\Rightarrow\mu(\underline{\lim}E_n)\le\underline{\lim}\mu(E_n)$$
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、$E_1,E_2\in\mathfrak{M}$、対称差 $E_1\Delta E_2=(E_1-E_2)\cup (E_2-E_1)$ とする。
このとき、$$\mu(E_1\Delta E_2)=0\Rightarrow\mu(E_1)=\mu(E_2)$$


---

## 測度の演算

・可測空間 $(X,\mathfrak{M})$、測度 $\mu_1,\mu_2:\mathfrak{M}\to[0,\infty]$、$\alpha_1,\alpha_2\ge0$とする。
このとき、$\alpha_1\mu_1+\alpha_2\mu_2$ は測度。

- 可測空間 $(X,\mathfrak{M})$、測度列 $\mu_n:\mathfrak{M}\to[0,\infty]$、非負点列 $\alpha_n\ge0$とする。
このとき、$$\sum \alpha_n\mu_n$$ は測度。





