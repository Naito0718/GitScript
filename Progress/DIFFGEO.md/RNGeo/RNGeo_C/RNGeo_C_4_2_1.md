
- [$R^3$ での正則曲面](#r3-での正則曲面)
  - [種々の基本量](#種々の基本量)
    - [ガウス枠](#ガウス枠)



# $R^3$ での正則曲面

・開集合 $U\sub\bm{R}^2$、$C^2$ 同相写像 $p:U\to\bm{R}^3$ とする。
このとき、$p_u,p_v$ は一次独立。

    ・定義域内でp_u,p_vのどっちかが0になったらダメ。rankで測る。

<dl><dt>




</dt><dd>




<br>

- 

</dd></dl>

---

## 種々の基本量

・正則曲面 $p:\bm{R}^2\to\bm{R}^3$ とする。

---

### ガウス枠



<dl><dt>

・開集合 $\Omega\sub\bm{R}^2$、正則曲面 $p:\Omega\to\bm{R}^3$ とする。
このとき、
$$E=p_u\cdot p_u,\ \ F=p_u\cdot p_v,\ \ G=p_v\cdot p_v\\\ \\
\nu=\frac{p_u\times p_v}{|p_u\times p_v|}\\\ \\
L=p_{uu}\cdot\nu,\ \ M=p_{uv}\cdot\nu,\ \ N=p_{vv}\cdot\nu\\\ \\
I=\begin{pmatrix}
E & F \\
F & G \\
\end{pmatrix},\ \ \mathcal{I}=\begin{pmatrix}
L & M \\
M & N \\  
\end{pmatrix}\\\ \\
A=I^{-1}\mathcal{I}\\\ \\
K=\frac{LN-M^2}{EG-F^2},\ \ H=\frac{EN-2FM+GL}{2(EG-F^2)}\\\ \\$$
と定めると、$\nu,A$ はwell-defined。ここで、$I$ を第一基本行列、$\mathcal{I}$ を第二基本行列、$A$ をワインガルテン行列、$K$ をガウス曲率、$H$ を平均曲率という。
<br>

</dt><dd>

- 
$$I=(p_u,p_v)^T(\nu_u,\nu_v),\ \ \mathcal{I}=-(p_u,p_v)^T(\nu_u,\nu_v)\\\ \\$$

    ・内積じゃなくて行列。
<br>

- 
$$\nu\cdot\nu_u=0,\ \nu\cdot\nu_v=0\\\ \\
(\nu_{u},\nu_v)=-(p_u,p_v)A\\\ \\$$

    ・内積じゃなくて行列。
<br>

- $p_{x^ix^j}=\Gamma^a_{ij}p_{x^a}+X_{ij}\nu$ と定める。
このとき、
$$X_{ij}=\mathcal{I}_{ij}\\\ \\
I_{ka}\Gamma^a_{ij}=p_{x^k}\cdot p_{x^ix^j}$$
ここで、下の式においては、常に $E,F,G$ およびその偏微分で書けることが分かる。
<br>

- $\mathcal{F}=(p_u,p_v,\nu)\in GL(3,\bm{R})$ とする。
このとき、
$$\mathcal{U}_i=\begin{pmatrix}
\Gamma^1_{i1} & \Gamma^1_{i2} & -A^i_1  \\
\Gamma^2_{i1} & \Gamma^2_{i2} & -A^i_2  \\
\mathcal{I}_{i1} & \mathcal{I}_{i2} & 0\\
\end{pmatrix}$$ と定める。
このとき、
$$\frac{\partial\mathcal{F}}{\partial }$$

<br>
    ・A^i_jでj行i列。これ混合テンソル？

</dd></dl>

---




