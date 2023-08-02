- [一章：群の性質](#一章群の性質)
- [二章：準同型写像](#二章準同型写像)
        - [準同型写像の性質](#準同型写像の性質)
        - [部分群と準同型写像](#部分群と準同型写像)
        - [準同型定理](#準同型定理)
        - [部分群の対応定理](#部分群の対応定理)
        - [同型定理](#同型定理)
        - [準同型の分解](#準同型の分解)
- [三章：元の位数](#三章元の位数)
        - [準同型写像と元の位数](#準同型写像と元の位数)
- [四章：群作用](#四章群作用)
- [五章：共役](#五章共役)


# 一章：群の性質

・$$gAg^{-1}\subset A\ (\forall g)\iff gAg^{-1}=A\ (\forall g)\iff gA=Ag\ (\forall g)\\\ \\
$$

- $$BAB^{-1}\subset A\Rightarrow BA\subset AB\ {かつ}\ AB^{-1}\subset B^{-1}A$$

- $g\in G$ に対して、
$$A=gBg^{-1}\iff B=g^{-1}Ag$$

- $$(AB)^{-1}=B^{-1}A^{-1}$$

---

・部分集合 $H\subset G$ に対して、
$H$ は部分群$\iff H^{-1}\subset H,\ HH\subset H\iff x,y\in H {ならば} x^{-1}y\in H\iff H^{-1}H\subset H$

        ・包含は等号でもよい。

---

・$H_1,H_2\subset G$ を共に部分群とする。
このとき、$H_1\cap H_2$ は $G$ の部分群。

- $H\subset G$ を部分群、$N\subset G$ を正規部分群とする。
このとき、$H\cap N$ は $H$ の正規部分群。
<br>

- $N_1,N_2\subset G$ を共に正規部分群とする。
このとき、$N_1\cap N_2$ は $G$ の正規部分群。

---
---
---

# 二章：準同型写像

##### 準同型写像の性質

・$$\phi(1_{G_1})=1_{G_2},\quad \phi(g^{-1})=\phi(g)^{-1}$$

- $\ker\phi\subset G_1$ は正規部分群、$Im\phi\subset G_2$ は部分群。
<br>

- $\phi_2\circ\phi_1$ は準同型写像
<br>

- 準同型写像 $\phi:G_1\to G_2$ に対して、
$\phi$ は単射$\iff\ker\phi=\{1_{G_1}\}$
<br>

---

・群 $G_1,G_2$、$\langle S\rangle=G_1$ なる部分集合 $S$、準同型写像 $\phi_1,\phi_2:G_1\to G_2$ とする。
このとき、$$\phi_1(g)=\phi_2(g)\ (\forall g\in S)\Rightarrow\phi_1=\phi_2$$

---

- 部分群 $H\subset G$ に対して、
包含写像 $i:H\to G$ は準同型写像
<br>

- 群 $G$、$g\in G$ に対して、
$$\phi:\bm{Z}\to G,\quad\phi(n)=g^{n}$$と定義する。
このとき、$\phi$ は準同型写像

---

##### 部分群と準同型写像

・部分群 $K\subset G_2$ に対して、
$$\ker\phi\subset\phi^{-1}(K)\subset G_1$$ は部分群。

    ・kerのとこは常に成り立つ

- 正規部分群 $K\subset G_2$ に対して、
$\phi^{-1}(K)\subset G_1$ は正規部分群。
<br>

- 全射準同型写像 $\phi$、正規部分群 $K\subset G_2$ に対して、
$G_1/\phi^{-1}(K)\cong G_2/K$
<br>

- 部分群 $H\subset\ker\phi\subset G_1$ に対して、
$\phi(H)=\phi(\ker\phi)=\{1_{G_2}\}$
<br>

- 正規部分群 $H\subset G_1$、全射準同型写像 $\phi:G_1\to G_2$ に対して、
$\phi(H)\subset G_2$ は正規部分群。

---

##### 準同型定理

・群 $G_1,G_2$、準同型写像 $\phi:G_1\to G_2$ に対して、
$$\psi\circ\pi=\phi$$を満たす同型写像 $\psi:G_1/\ker\phi\to Im\phi$ がただ一つ存在する

---

##### 部分群の対応定理

・$G$を群、$N\subset G$を正規部分群とする。
このとき、
$$X=\{H\ |\ N\subset H{であって、}H\subset G{は部分群} \}\subset2^G\\
Y=\{K\ |\ K\subset G/N{は部分群}\}\subset 2^{G/N}$$と定める。
また、自然な射影 $\pi:G\to G/N$ に対して、
$$\phi:X\to Y,\quad\phi(H)=\pi(H)\\
\psi:Y\to X,\quad \psi(K)=\pi^{-1}(K)$$と定める。

---

・$\phi,\psi$の値域は共にwell-defined
- $\phi,\psi$は互いの逆写像である。
- $G/N$ の部分群と $G$ の $N$ を含む部分群は、一対一に対応する。

---

##### 同型定理

・$H\subset G$ を部分群、$N\subset G$ を正規部分群とする。
このとき、$H/(N\cap H)\cong HN/N$

・$N_1\subset N_2\subset G$ を共に正規部分群とする。

- $$\phi:G/N_1\to G/N_2,\quad\phi(xN_1)=xN_2$$ は準同型写像。
- $$(G/N_1)/(N_2/N_1)\cong G/N_2$$

---

##### 準同型の分解

・$G_1,G_2$ を群、$\phi:G_1\to G_2$ を準同型写像、$N\subset G_1$ を正規部分群とする
このとき、
$N\subset\ker\phi\iff\phi=\psi\circ\pi$ を満たす準同型写像 $\psi:G_1/N\to G_2$ が存在する。

---
---
---

# 三章：元の位数

##### 準同型写像と元の位数

・位数 $n$ の元 $g\in G_1$、準同型写像 $\phi:G_1\to G_2$ に対して、
$\phi(g)$ の位数は $n$ の約数

- $g\in G_1$、単射準同型写像 $\phi:G_1\to G_2$ に対して、
$\phi(g)$ の位数は $g$ の位数に等しい。

        ・∞でもよい

---
---
---

# 四章：群作用

---

# 五章：共役