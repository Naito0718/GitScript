
- [位相線形空間としての $M(n,C)$](#位相線形空間としての-mnc)
  - [位相的性質](#位相的性質)
    - [基本的な連続写像](#基本的な連続写像)
  - [位相幾何的性質](#位相幾何的性質)
  - [指数写像](#指数写像)
    - [基本的な性質](#基本的な性質)
    - [単位元の近傍](#単位元の近傍)
    - [実解析性](#実解析性)
    - [$1$ パラメータ部分群](#1-パラメータ部分群)
  - [内積と古典群](#内積と古典群)



# 位相線形空間としての $M(n,C)$

    ・実数R上の有限次元ベクトル空間で、結合法則、可換性を仮定せず体をなすものは、R,C,Hと8元数に限る
    ・結局可換でないと行列式も定義されない

## 位相的性質

<dl><dt>

・$$\|\cdot\|:M(n,\bm{C}):\to\bm{R}\\\ \\
\|\alpha\|=\sqrt{\sum|a_{ij}|^2}$$
と定めると、これはノルム。

</dt><dd>

- 明らかに $\bm{R}^{2n^2}\cong M(n,\bm{C})\quad(\bm{R}-\text{加群同型で、同相})$
<br>

      ・実数ならn^2、四元数なら4n^2。
<br>

- $M(n,\bm{C})$ はBanach単位的 $*$-環で、局所コンパクト。
<br>

        ・ノルムが異なるので、有界線形作用素 B(H) で考えているわけではない！
        ・C*まで言える？

</dd></dl>

---

### 基本的な連続写像

<dl><dt>

・行列式写像：$\det:M(n,\bm{C})\to\bm{C}$ は連続写像。
<br>

- 小行列式写像：$M(n,\bm{C})\to M(n,\bm{C}),\quad\alpha\mapsto\tilde{\alpha}$ は連続写像。
<br>

</dt><dd>

・転置、共役、転置共役写像：$^T,\ \bar\ ,\ ^{\dag}:M(n,\bm{C})\to M(n,\bm{C})$ は連続な線形写像。
<br>

- 転置積、転置共役積：
$trat,dagt:trat(\alpha)=\alpha\alpha^T,dagt(\alpha)=\alpha\alpha^{\dag}$ は連続写像。
<br>

- $\sigma\in GL(n,\bm{C})$ に対して、
$$M(n,\bm{C})\to M(n,\bm{C}),\quad\alpha\mapsto\sigma^{-1}\alpha\sigma$$ は連続な線形写像。

</dd></dl>

---

## 位相幾何的性質

・$M(n,\bm{C})$ は弧状連結。

    ・R,H上でも同様。

---

## 指数写像  

    ・四元数体上の行列でも、detと転置と固有値以外は成り立つ。

### 基本的な性質

<dl><dt>

・$$\exp:M(n,\bm{C})\to M(n,\bm{C})$$ は連続写像。

    ・detより上は一般の Banach単位的 C,R 上代数でも成り立つ。

</dt><dd>

- $$\exp0_n=1_n\\\ \\
\exp\alpha^T=(\exp\alpha)^T,\quad \exp(\sigma^{-1}\alpha\sigma)=\sigma^{-1}(\exp\alpha)\sigma,\quad \exp\overline{\alpha}=\overline{\exp\alpha}\\\ \\$$

- $[\alpha,\beta]=0\Rightarrow\exp(\alpha+\beta)=\exp\alpha\exp\beta$
<br>

      ・交換子。
      ・級数の積のこと。
<br>

- $\exp\alpha\in GL(n,\bm{C})$ であって、
$$(\exp\alpha)^{-1}=\exp(-\alpha)\\\ \\$$

- $\det\exp\alpha=e^{\mathrm{Tr}\alpha}$
<br>

      ・0でない。
      ・固有値で示されるので、R上では成り立たない。
<br>

- $$\exp\begin{pmatrix}
c  & * & \dots & * \\
0   \\
\vdots   & & \alpha'\\
0   \\
\end{pmatrix}=
\begin{pmatrix}
e^c  & * & \dots & * \\
0   \\
\vdots   & & \exp\alpha'\\
0   \\
\end{pmatrix}\\\ \\$$特に、上三角行列の指数写像は上三角。
<br>

- $\alpha$ の固有値を $\lambda_i$ とすると、
$\exp\alpha$ の固有値：$\exp\lambda_i$

</dd></dl> 

---

### 単位元の近傍

・$$\exist0_n\text{ の開近傍 }N\sub M(n,\bm{C}),\ 1_n\text{ の開近傍 }U\sub GL(n,\bm{C})\text{ であって、}\\\ \\
\exp:N\to U\text{ によって} N\cong U(\text{ 同相})$$

    ・逆はlog

---

### 実解析性

### $1$ パラメータ部分群

・$\alpha\in M(n,\bm{C})$ とする。
このとき、
$$g_{\alpha}:\bm{R}\to GL(n,\bm{C})\\\ \\
g(t)=\exp(t\alpha)$$は連続な群準同型写像。
ここで、$\mathrm{Im} g_{\alpha}$ を $\alpha$ が定義する $1$ パラメータ部分群といい、
$$\forall t\in\bm{R}\text{ に対して }g_{\alpha}(t)=g_{\beta}(t)\\\ \\
\Rightarrow\alpha=\beta$$

      ・スカラー倍は保存しない。
      ・g(t+s)=g(t)g(s)

- $$g_{\alpha}:I\to GL(n,\bm{C})$$ は単位元 $E$ から $\exp\alpha$ への道。




---

## 内積と古典群

---
---
---