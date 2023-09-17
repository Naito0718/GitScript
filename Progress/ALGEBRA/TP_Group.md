
- [位相群](#位相群)
  - [基本的な性質](#基本的な性質)
    - [定義](#定義)
    - [連続写像](#連続写像)
    - [集合の演算](#集合の演算)
  - [単位元周りの基本近傍系](#単位元周りの基本近傍系)
  - [連続写像](#連続写像-1)
  - [剰余空間](#剰余空間)
    - [等質集合としての剰余空間](#等質集合としての剰余空間)
    - [剰余群](#剰余群)
    - [連続な断面](#連続な断面)
  - [連続な群作用](#連続な群作用)
    - [基本的な性質](#基本的な性質-1)
    - [等質集合](#等質集合)
- [不変積分](#不変積分)
- [表現](#表現)
- [位相群の基本群](#位相群の基本群)
- [弧状連結位相群](#弧状連結位相群)
  - [離散部分群 $Γ$](#離散部分群-γ)
- [第二可算局所コンパクト位相群](#第二可算局所コンパクト位相群)
  - [開写像定理](#開写像定理)
  - [群作用](#群作用)
  - [Haar測度](#haar測度)
- [コンパクト群](#コンパクト群)
  - [準同型定理](#準同型定理)
  - [コンパクト部分群](#コンパクト部分群)
  - [群作用](#群作用-1)
    - [推移的な作用](#推移的な作用)
- [リー群](#リー群)



# 位相群

## 基本的な性質 

### 定義

<dl><dt>

・位相群 $G$：</dt><dd>

- $G$ は群。
- $G$ は $T_1$空間。
- $P(g,h)=gh,\quad J(g)=g^{-1}$ が共に連続。 </dd></dl>

---

・$P(g,h),J(g)$ が連続 $\iff Q(g,h)=g^{-1}h$ が連続

- $$\forall U\in \mathcal{N}(xy)\text{ に対して、}\exist V\in\mathcal{N}(x),\exist W\in\mathcal{N}(y)\text{ であって、}\\
VW\sub U\\\ \\
\forall U\in \mathcal{N}(x^{-1})\text{ に対して、}\exist V\in\mathcal{N}(x)\text{ であって、}\\
V^{-1}\sub U\\\ \\$$

- 部分集合 $A,B\sub G$ とする。
このとき、
$$\overline{A}\ \overline{B}\sub\overline{AB},\quad\overline{A}^{-1}\sub\overline{A^{-1}}$$

---

### 連続写像

・位相群 $G$ に対して、
$$L_g,R_g,J,A_g:G\to G\\\ \\
L_g(x)=gx\\\ \\
R_g(x)=xg\\\ \\
J(x)=x^{-1}\\\ \\
A_g(x)=gxg^{-1}$$は同相写像。

- $$(L_g)^{-1}=L_{g^{-1}},\quad A_{g}=L_{g}\circ R_{g^{-1}}$$

---

### 集合の演算

<dl><dt>

・位相群 $G$、開集合 $O\sub G$ とする。</dt><dd>

- $\forall X\sub G$ に対して、$$XO,OX$$は開集合。
- $O^{-1}$ は開集合。</dd></dl>

---

<dl><dt>

・位相群 $G$、閉集合 $F\sub G$ とする。</dt><dd>

- $\forall \text{ 有限集合 }X\sub G$ に対して、$$XO,OX$$は閉集合。
- $F^{-1}$ は閉集合。
<br>

- 閉集合 $F$、コンパクト集合 $K$ に対して、
$$F\cap K=\phi\\\ \\
\Rightarrow\exist U\in\mathcal{U}(e)\text{ であって、}\\
FU\cap KU=\phi$$
- 閉集合 $F$、コンパクト集合 $K$ に対して、$FK$ は閉集合。</dd></dl>

---

## 単位元周りの基本近傍系

<dl><dt>

・位相群 $G$、単位元周りの基本近傍系 $\mathcal{N}(e)$ とする。</dt><dd>

- $g\in G$ に対して、$$\{gN\ |\ N\in\mathcal{N}(e)\}$$は $g$ の基本近傍系。

- 位相群 $G$ の位相は、単位元 $e$ 周りの基本近傍系によって一意的に決定される。
<br>

- $$\bigcap\mathcal{N}(e)=\{e\}\\\ \\
U_1,U_2\in\mathcal{N}(e)\Rightarrow\exist U_3\in\mathcal{N}(e)\text{ であって }U_3\subset U_1\cap U_2\\\ \\
U_1\in\mathcal{N}(e),x\in U_1\text{ に対して、}\exist U_2\in\mathcal{N}(e)\text{ であって　}xU_2\subset U_1\\\ \\
U_1\in\mathcal{N}(e)\text{ に対して、}\exist U_2\in\mathcal{N}(e)\text{ であって } U_2^{-1}U_2\sub U_1\\\ \\
U_1\in\mathcal{N}(e),g\in G\text{ に対して、}\exist U_2\in\mathcal{N}(e)\text{ であって }gU_2g^{-1}\sub U_1$$

- 群 $G$、$e$ を含む部分集合族 $\mathcal{N}(e)$ が上記の $5$ つの性質を満たすとする。
このとき、$G$ は位相群となり、$\mathcal{N}(e)$ は $e$ の基本近傍系となるような $G$ の位相がただ一つ定まる。</dd></dl>

---

・位相群 $G$、$A\subset G$、単位元周りの基本近傍系 $\mathcal{N}(e)$ とする。
このとき、$$\overline{A}=\bigcap AU_{\lambda}=\bigcap \overline{AU_{\lambda}}$$

- 位相群は正則空間。

      ・位相幾何的には完全正則まで言える。

- 任意の単位元 $e$ の開近傍 $U_{\lambda}$ に対して、ある　$e$ の開近傍 $U_{\mu},U_{\nu}$ が存在して、$U_{\mu}U_{\mu},\ U_{\nu}^{-1}U_{\nu}\sub U_{\lambda}$
<br>

- 任意の単位元 $e$ の開近傍 $U_{\lambda}$、部分集合 $A\sub G$ に対して、ある $e$ の開近傍 $U_{\mu}$ が存在して、
$$\overline{U_{\mu}H}\sub U_{\lambda}H$$

---

## 連続写像

<dl><dt>

・位相群 $G_1,G_2$、準同型写像 $\rho:G_1\to G_2$ とする。
このとき、$\rho$ が $e\in G_1$ で連続ならば、$\rho$ は $G_1$ で連続。

</dt><dd>

- 位相群 $G_1,G_2$、全射開準同型写像 $\rho:G_1\to G_2$ とする。
このとき、
$$\psi:G_1/\ker\rho\to G_2\\\ \\
\psi\circ\pi=\rho$$を満たすような位相群の同型写像がただ一つ存在する。

      ・別にImρで置き換えても成り立つ。
      ・開であることに注意。

</dd></dl>


---

## 剰余空間

<dl><dt>

・位相群 $G$、部分群 $H$、剰余空間 $G/H$ とする。 

</dt><dd>

- 射影 $\pi:G\to G/H$ は連続な全射開写像。特に、
$$F\sub G/H\text{ が閉集合}\iff \pi^{-1}(F)\sub G\text{ が閉集合}\\\ \\$$

- $$\Psi:G\times(G/H)\to G/H\\\ \\
\Psi(g,x)=T_gx,\quad(T_g(hH)=ghH)$$ は連続写像で、
$$\Psi\circ(1\times\pi)=\pi\circ P\quad(p\text{ は }G\text{ で積を取る写像})$$を満たす。
特に、$T_g:G/H\to G/H$ は 
$$T_g(T_h(x))=T_{gh}(x)\\\ \\
T_e(x)=x\\\ \\
\forall x,y\in G/H\text{ に対して、}\exist g\in G\text{ であって、}\\T_g(x)=y$$ を満たす同相写像。 
<br>

- $G$ の単位元周りの基本近傍系 $\{U_{\lambda}\}$ に対して、
$$\{\pi(U_{\lambda})\}$$ は $G/H$ の単位元 $\pi(e)$ 周りの基本近傍系。t
<br>

- $H$ が閉部分群ならば、$G/H$ は正則空間。

      ・基本、閉部分群だけを考える。

</dd></dl>

---

### 等質集合としての剰余空間

<dl><dt>

・位相群 $G$、閉部分群 $H\sub G$ とする。
このとき、$\Psi:G\times (G/H)\to G,\ \Psi(g,x)=T_g(x),\ T_g(hH)=(gh)H$ は $G$ から $G/H$ への連続な作用。さらに、この作用は推移的、すなわち $G/H$ は $G$ の等質集合。

    ・別にここは部分群でもいい。

</dt><dd>

- 等方群：$A_{gH}\sub G$、共役部分群 $gHg^{-1}$ に対して、
$$A_{gH}=gHg^{-1}\\\ \\$$

- $$\text{作用が効果的}\\\ \\
\iff H\text{ が }G\text{ の単位元以外の正規部分群を含まない}$$

</dd></dl>

---



### 剰余群


<dl><dt>

・位相群 $G$、正規部分群 $N$、剰余群 $G/N$、積を取る写像 $P:G\times G\to G,\ \overline{P}:G/N\times G/N\to G/N$、逆元を取る写像 $J:G\to G,\ \overline{J}:G/N\to G/N$ とする。
このとき、$\overline{P},\ \overline{J}$ は連続で、
$$\overline{P}\circ (\pi\times \pi)=\pi\circ P\\\ \\
\overline{J}\circ\pi=\pi\circ J$$満たす。
よって、閉正規部分群 $N$ に対して、$G/N$ は位相群。

    ・閉正規部分群のみを考える。

</dt><dd>

- 射影 $\pi$ は連続で全射な、開な準同型写像。


</dd></dl>

---

### 連続な断面

・位相群 $G$、部分群 $H\sub G$、射影 $p:G\to G/H$ とする。
このとき、連続な断面 $s:G/H\to G,\ p\circ s=1$ が存在すれば、
$$G\cong (G/H)\times H\ (\text{同相})$$

    ・群の具体例参照

---

## 連続な群作用

### 基本的な性質

<dl><dt>

・位相群 $G$、位相空間 $X$、群作用 $\Psi:G\times X\to X$ とする。
このとき、$G$ の $X$ への連続な群作用：$\Psi$ が連続。

</dt><dd>

- $T_g:X\to X,\ T_g(x)=gx$ は同相写像。
<br>

- $x\in X,\ g\in G$ とする。$gx$ の近傍 $U\in\mathcal{N}(xg)$ とする。
このとき、
$$\exist A\in\mathcal{N}(x),\ \exist B\in \mathcal{N}(g)\text{ であって、}BA\sub U\\\ \\$$


- $X$ が $T_1$ ならば、等方群 $G_x$ は閉部分群。
<br>


- $x\in X$、$p:G\to X,\ p(x)=gx$、$x$ の等方群 $G_x$ とする。
このとき、連続な断面 $s:X\to G,\ p\circ s=1$ が存在するならば、
$$G\cong X\times G_x\ (\text{同相})$$また、
$$s(gx)x=gx\ (\forall g\in G)$$ が成り立っている。

      ・同相を与える写像は射影と断面のときと同じ。

- 軌道空間 $X/G$ とする
このとき、
$$p:X\to X/G\\\ \\
p(x)=G(x)=Gx$$ は連続全射な開写像。また、$A\sub X$ に対して、
$$AG=p^{-1}(p(A))$$

      ・G(x)=Gxと書ける。


</dd></dl>

---

### 等質集合

<dl><dt>

・位相群 $G$、位相空間 $X$、連続な群作用 $\Psi:G\times X\to X$ とする。
このとき、等質空間 $X$：推移的な作用

</dt><dd>




</dd></dl>


---
---
---

# 不変積分

・

---

# 表現

・位相群 $G$ が有限次元 $K$-加群に群として作用するとする。
このとき、位相群 $G$ による作用：
$$\exist\text{ 基底 }u_i\text{ に対して、}xu_i=\sum u_ja_{ji}(x)\text{ と表すとき、}\\\ \\
a_{ji}:G\to K\text{ が連続}$$

    ・結局 A=(a_ij) でうまく基底に対応する。


# 位相群の基本群

---


# 弧状連結位相群

## 離散部分群 $Γ$

・弧状連結位相群 $G$、離散正規部分群 $\Gamma\sub G$、中心 $Z(G)$ とする。
このとき、
$$\Gamma\sub Z(G)$$



---


# 第二可算局所コンパクト位相群

    ・Hausdorffでもある

## 開写像定理

<dl><dt>

・第二可算局所コンパクト位相群 $G_1$、局所コンパクト位相群 $G_2$、連続全射な群準同型 $f:G_1\to G_2$ とする。

</dt><dd>

- $f$ は開写像。

- $$G_1/\ker f\cong G_2\ (\text{群同相})\\\ \\
\text{群同相：}\phi(x\ker f)=f(x)$$


</dd></dl>


---

## 群作用

・第二可算局所コンパクト位相群 $G_1$ が局所コンパクト空間 $X$ に推移的に作用しているとする。また、$x\in X$、等方群 $G_x$ とする。
このとき、
$$f:G/G_x\to X\\\ \\
f(gG_x)=gx$$は同相写像。

    ・G_xは閉部分群とは限らない。
    ・？群と位相、p,104

## Haar測度

---
---
--- 

# コンパクト群

## 準同型定理

    ・一般の場合には開写像であることが条件だった。

・コンパクト位相群 $G_1$、位相群 $G_2$、連続な全射準同型 $f:G_1\to G_2$ とする。
このとき、
$$\psi:G_1/\ker f\to G_2\\\ \\
\psi\circ\pi=f$$を満たすような位相群の同型写像 $\psi$ がただ一つ存在する。

---

## コンパクト部分群

<dl><dt>

・位相群 $G$、コンパクト部分群 $H$ とする。

</dt><dd>

- 射影 $$p:G\to G/H$$は閉写像。
<br>

- $G/H$ がコンパクトならば、$G$ はコンパクト。

      ・逆は連続像だからいつでも成り立つ。


</dd></dl>

---

## 群作用

<dl><dt>

・コンパクト群 $G$ がHausdorff空間 $X$ に作用しているとする。

</dt><dd>

- 軌道 $G(x)$ はコンパクト。
<br>

- 軌道空間 $X/G$ はコンパクト


</dd></dl>

---

### 推移的な作用

・コンパクト群 $G$ がHausdorff空間 $X$ に推移的に作用しているとする。また、$x\in X$、$x$ の等方群 $G_x$ とする。
このとき、
$$f:G/G_x\to X\\\ \\
f(gG_x)=gx$$は同相写像。

    ・G_xは閉部分群。




---

# リー群


---