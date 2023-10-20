- [群の性質](#群の性質)
  - [集合の演算](#集合の演算)
- [準同型写像](#準同型写像)
  - [準同型写像の性質](#準同型写像の性質)
        - [部分群と準同型写像](#部分群と準同型写像)
        - [準同型定理](#準同型定理)
        - [部分群の対応定理](#部分群の対応定理)
        - [同型定理](#同型定理)
        - [準同型の分解](#準同型の分解)
- [元の位数](#元の位数)
  - [準同型写像と元の位数](#準同型写像と元の位数)
- [群作用](#群作用)
  - [基本的な性質](#基本的な性質)
  - [種々の空間への作用](#種々の空間への作用)
- [共役](#共役)


# 群の性質

## 集合の演算

・$$gAg^{-1}\subset A\ (\forall g)\iff gAg^{-1}=A\ (\forall g)\iff gA=Ag\ (\forall g)\\\ \\
$$
- $$BAB^{-1}\subset A\Rightarrow BA\subset AB\ {かつ}\ AB^{-1}\subset B^{-1}A\\\ \\$$

- $g\in G$ に対して、
$$A=gBg^{-1}\iff B=g^{-1}Ag\\\ \\$$

- $$(AB)^{-1}=B^{-1}A^{-1}\\\ \\$$

- $$gA\subset B\iff A\subset g^{-1}B$$
        
      ・gは右からかけても同様に成り立つ。

- $$g\bigcup U_{\lambda}=\bigcup gU_{\lambda},\quad g\bigcap_{\lambda}U_{\lambda}=\bigcap gU_{\lambda}$$


---

・部分集合 $H\subset G$ に対して、
$H$ は部分群$\iff H^{-1}\subset H,\ HH\subset H\\\ \\
\iff x,y\in H {ならば} x^{-1}y\in H\iff H^{-1}H\subset H$

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

・群 $G_1,G_2$、準同型写像 $G_1\to G_2$、$x\in G_1,A\sub G_1$ とする。
このとき、
$$f(x)f(A)=f(xA)$$

---
---
---

# 準同型写像

## 準同型写像の性質

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

# 元の位数

## 準同型写像と元の位数

・位数 $n$ の元 $g\in G_1$、準同型写像 $\phi:G_1\to G_2$ に対して、
$\phi(g)$ の位数は $n$ の約数

- $g\in G_1$、単射準同型写像 $\phi:G_1\to G_2$ に対して、
$\phi(g)$ の位数は $g$ の位数に等しい。

      ・∞でもよい

---
---
---

# 群作用

## 基本的な性質

<dl><dt>

・群 $G$、集合 $X$ とする。
このとき、作用：
$$gx\in X\\\ \\
g(hx)=(gh)x\\\ \\
ex=x\\\ \\$$

- 群 $G$ が集合 $X$ に作用する時、
効果的、自由な作用：
$$T_g=id_X\iff g=e\\\ \\
\exist x\in X\text{ であって、}gx=x\iff g=e$$

      ・自由な作用のときは、T_e以外の作用は不動点を持たない。
<br>

</dt><dd>

- $x\in X$、作用 $\Psi:G\times X\to X$、制限 $\Psi_x(g)=gx$ とする。
このとき、等方群：$$G_x=\{g\in G\ |\ gx=x\}=\Psi_x^{-1}(\{x\})$$は $G$ の部分群。

<br>

- $T_g:X\to X,\quad T_g(x)=gx$ と定めると、
$$T_e(x)=x\\\ \\
T_g(T_h(x))=(gh)x\\\ \\
(T_g)^{-1}=T_{g^{-1}}$$ を満たす。特に、$T_g$ は全単射。
<br>

- $G(x)=\{gx\ |\ g\in G\}\sub X$ と定めると、
$$G(x)\cap G(y)\neq\phi\iff G(x)=G(y)\\\ \\
X=\bigcup_{x\in X} G(x)$$が成り立つ。特に、
$$x\sim y\iff \exist g\in G\text{ であって }y=gx$$で同値関係を定めると、$G(x)$ は $x$ の同値類。ここで、$G(x)$ を軌道といい、軌道空間 $X/G$ とする。
<br>

- 等方群 $H_x$ に対して、
$$\text{作用が効果的}\iff\bigcap_{x\in X}H_x=\{e\}\\\ \\$$


</dd></dl>

---

<dl><dt>

・ 群 $G$ が集合 $X$ に作用する時、
推移的な作用：$$\forall x,y\in X\text{ に対して、}\exist g\in G\text{ であって、}\\
gx=y\\\ \\$$

</dt><dd>

- 軌道 $G(x)$ に対して、
$$\text{作用が推移的}\iff X\text{ の軌道がただ一つのみからなる}\\\ \\$$

- 
$$P_x:G\to X\\\ \\
P_x(g)=gx$$は全射。



</dd></dl>

---

## 種々の空間への作用

・群 $G$、環 $R$ 

---

・群 $G$ が $K$-加群 $V$ に集合として作用するとする。
このとき、$K$-加群 $V$ への作用：
$$g(v_1+v_2)=gv_1+gv_2,\quad g(v\alpha)=(gv)\alpha$$
また、$V$ を $G-K$ 加群、$G$ の $K$ 上表現加群という。

    ・有限次元なら表現

- $$V^G=\{v\in V\ |\ gv=v\ (\forall g)\}$$は部分 $K$-加群。

---

# 共役

---

