
- [積分 $I(f)$](#積分-if)
  - [Bochner積分](#bochner積分)
  - [Bochner積分とLebesgue積分](#bochner積分とlebesgue積分)
- [Bochner積分の性質](#bochner積分の性質)
  - [Bochner-Lebesgue優収束定理](#bochner-lebesgue優収束定理)
  - [Bochner-Fubiniの定理](#bochner-fubiniの定理)



# 積分 $I(f)$

<dl><dt>

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、$f\in \mathcal{L}^1(X,B)$ とする。
このとき、$$I(f):B^{*}\to\bm{C,R}\\\ \\
I(f)(\phi)=\int_X\phi(f(x))d\mu $$
と定めると、
$$\|I(f)\|<\|f\|_{1},\quad |I(f)(\phi)|\le\|\phi\|\|f\|_1\quad(\forall\phi\in B^*)$$
であって、
$$I(\alpha f+\beta g)(\phi)=\alpha I(f)(\phi)+\beta I(g)(\phi)\\\ \\
I(f)(\alpha\phi+\beta\psi)=\alpha I(f)(\phi)+\beta I(\psi)$$
が成り立つ。すなわち、$I(f)\in (B^*)^*$
<br>

</dt><dd>

- Bochner可測単関数 $s\in \mathcal{L}^1(X,B),\ s(x)=\sum\chi_{E_i}(x)b_i$ とする。
このとき、
$$I(s)(\phi)=\phi\left(\sum \mu(E_i) b_i\right)$$
よって、$$I(s)\in\iota(B)\\\ \\
(\text{ただし、}\iota:B\to (B^*)^*,\quad\iota(b)(\phi)=\phi(b))$$

</dd></dl> 

---

## Bochner積分

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、$f\in \mathcal{L}^1(X,B)$ とする。
このとき、
$$\text{ある }b_f\in B\text{ がただ一つ存在して、}\\\ \\
I(f)=\iota(b_f)$$
ここで、$b_f$ を $f\in\mathcal{L}^1(X,B)$ の $\mu$ に関するBochner積分といい、
$$b_f=\int_Xfd\mu$$
と書く。明らかに、
$$\forall\phi\in B^*\text{ に対して、}\phi\left(\int_Xfd\mu\right)=\int_X\phi(f(x))d\mu$$
<br>

- $\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$ とする。
このとき、
$$\psi:L^1(X,B)\to B\\\ \\
\psi(f)=\int_Xfd\mu$$
と定めると、これは線形写像。

---

## Bochner積分とLebesgue積分

・可測空間 $(X,\mathfrak{M})$、$f:X\to B$ とする。
このとき、
$$f\text{ はBochner可測 }\iff f\text{ は可測}$$
であって、
$$\int_Xfd\mu\quad(\text{Bochner})=\int_Xfd\mu\quad(\text{Lebesgue})$$
すなわち、Banach空間 $\bm{C,R}$ におけるBochner積分は、Lebesgue積分と整合する。
<br>

    ・線形汎関数の値域が自分自身であることによる。

---

# Bochner積分の性質

<dl><dt>

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$f\in \mathcal{L}^1(X,B)$ とする。
<br>

</dt><dd>

- $$\left\|\int_X fd\mu\right\|=\sup_{\|\phi\|=1}\left|\int_X\phi(f(x))\right|d\mu\le\int_X\|f\|d\mu\\\ \\$$

- 有界線形作用素 $T\in B(B,C)$ とする。
このとき、$T\circ f\in\mathcal{L}^1(X,B)$ であって、
$$T\left(\int_X fd\mu\right)=\int_XT(f(x))d\mu\\\ \\$$

- 
$$\int_X f(x)d\mu\in\overline{\mathrm{span}f(X)}$$

</dd></dl> 

---

## Bochner-Lebesgue優収束定理

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{R,C}$ 上Banach空間 $B$、Bochner可測関数列 $f_n:X\to B$ とする。
このとき、
$$(1):f_n\text{ は各点収束極限 }\lim f_n(x)=f(x)\in B\ (\forall x\in X)\text{ を持ち、}\\\ \\
(2):\exist\text{ 非負値な }h\in\mathcal{L^1}(X,B)\text{ であって、}\forall n\in\bm{N},\forall x\in X\text{ に対して、 }\|f_n(x)\|\le h(x)\\\ \\
\Rightarrow f,f_n\in\mathcal{L^1}(X,B)\text{ であって、}
\int_X fd\mu=\lim_{n\to\infty}\int_Xf_nd\mu\\\ \\$$

    ・hは実数値関数。

---

## Bochner-Fubiniの定理

<dl><dt>

・$\sigma$-有限測度空間 $(X_i,\mathfrak{M}_i,\mu_i)\ \ (i=1,2)$、$\bm{R,C}$ 上Banach空間 $B$、$f\in\mathcal{L^1}(X_1\times X_2,B)$ とする。
また、$i\neq j$ とし、
$$N_i=\left\{x_i\in X_i\ |\ \int_{X_j}\|f(x_1,x_2)\|d\mu_j(x_j)=\infty\right\}\\\ \\
F_i:X_i\to B\\\ \\
F_i(x_i)=\begin{dcases}
\int_{X_j}f(x_1,x_2)d\mu_j & (x_i\in X/N_i)    \\
0  &  (x_i\in N_i)  \\
\end{dcases}$$
と定める。
<br>

</dt><dd>

- $N_i$ は $\mu_i$-零集合。
<br>

- $x_2\in X_2$ とする。
このとき、$$g:X_1\to B\\\ \\
g(x_1)=f(x_1,x_2)$$
と定めると、$g\in\mathcal{L}^1(X_1,B)$
<br>

      ・Bochner可測関数fに対しては、gはBochner可測。
<br>

- $F_i\in\mathcal{L^1}(X_i,B)$ であって、
$$\int_{X_i}F_id\mu=\int_{X_1\times X_2}f(x_1,x_2)d\mu_1\otimes\mu_2$$
すなわち、積分順序を入れ替えてよい。

</dd></dl> 





