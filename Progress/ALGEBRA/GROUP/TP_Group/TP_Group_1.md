
- [位相群の基本的な性質](#位相群の基本的な性質)
  - [定義](#定義)
    - [簡単な連続写像](#簡単な連続写像)
    - [集合の演算](#集合の演算)
  - [単位元周りの基本近傍系](#単位元周りの基本近傍系)
  - [連続準同型写像](#連続準同型写像)
  - [剰余空間](#剰余空間)
    - [連続な断面](#連続な断面)
      - [局所断面](#局所断面)
    - [等質集合としての剰余空間](#等質集合としての剰余空間)
    - [剰余群](#剰余群)
- [連続な群作用](#連続な群作用)
  - [基本的な性質](#基本的な性質)
  - [関数への作用](#関数への作用)
  - [等質集合](#等質集合)



# 位相群の基本的な性質 

## 定義

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
$$\overline{A}\ \overline{B}\sub\overline{AB},\quad\overline{A}^{-1}=\overline{A^{-1}}$$

---

### 簡単な連続写像

・位相群 $G$ に対して、
$$L_g,R_g,J,A_g:G\to G\\\ \\
L_g(x)=gx\\\ \\
R_g(x)=xg\\\ \\
J(x)=x^{-1}\\\ \\
A_g(x)=gxg^{-1}$$は同相写像。

- $$(L_g)^{-1}=L_{g^{-1}},\quad A_{g}=L_{g}\circ R_{g^{-1}}\\\ \\$$

- 位相空間 $X$、位相群 $G$、連続写像 $f,g:X\to G$ とする。
このとき、$fg,f^{-1}:X\to G$ は連続写像。
<br>

      ・定数写像なので、gfとかも連続。
<br>

---

### 集合の演算

<dl><dt>

・位相群 $G$、部分集合 $A_1,A_2,B\sub G$ とする。</dt><dd>

- $$(A_1\cap A_2)B=(A_1B\cap A_2B),\ (A_1\cup A_2)B=(A_1B\cup A_2B)\\\ \\
(A_1\cap A_2)^{-1}=(A_1)^{-1}\cap (A_2)^{-1},\ (A_1\cup A_2)^{-1}=(A_1)^{-1}\cup (A_2)^{-1}\\\ \\$$

- 集合族 $A_{\lambda}$、$B_{\lambda}$ に対して、
$$\bigcup A_{\lambda}\bigcup B_{\rho}=\bigcup_{(\rho,\lambda)}A_{\lambda}B_{\rho}\\\ \\
\bigcap A_{\lambda}\bigcap B_{\rho}\sub\bigcap_{(\rho,\lambda)}A_{\lambda}B_{\rho}\\\ \\$$
 
      ・共通部分の方は、有限個でもだめそう。


</dd></dl>

---

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
- 閉集合 $F$、コンパクト集合 $K$ に対して、$FK$ は閉集合。
</dd></dl>

---

<dl><dt>

・位相群 $G$、コンパクト集合 $K_1,K_2\sub G$ とする。

</dt><dd>

- $K_1K_2$ はコンパクト集合。

      ・K_1×K_2のコンパクト性による。

</dd></dl>


---

## 単位元周りの基本近傍系

<dl><dt>

・位相群 $G$、単位元周りの基本近傍系 $\mathcal{N}(e)$ とする。</dt><dd>

- $g\in G$ に対して、$$\{gN\ |\ N\in\mathcal{N}(e)\}$$は $g$ の基本近傍系。
したがって、位相群 $G$ の位相は、単位元 $e$ 周りの基本近傍系によって一意的に決定される。
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

- 任意の単位元 $e$ の開近傍 $U_{\lambda}$ に対して、ある $e$ の開近傍 $U_{\mu},U_{\nu}$ が存在して、
$$U_{\mu}U_{\mu},\ U_{\nu}^{-1}U_{\nu}\sub U_{\lambda}$$
特に、任意の単位元 $e$ の開近傍 $U_{\lambda}$ に対して、ある $e$ の対称開近傍 $U_{\rho,i}^{-1}=U_{\rho,i}$ が存在して、
$$U\supset U_{\rho,1}\supset U_{\rho,2}U_{\rho,2}\supset U_{\rho,3}U_{\rho,3}U_{\rho,3}U_{\rho,3}...$$
<br>

- 任意の単位元 $e$ の開近傍 $U_{\lambda}$、部分集合 $A\sub G$ に対して、ある $e$ の開近傍 $U_{\mu}$ が存在して、
$$\overline{U_{\mu}H}\sub U_{\lambda}H$$

---

## 連続準同型写像

<dl><dt>

・位相群 $G_1,G_2$、準同型写像 $\rho:G_1\to G_2$ とする。
このとき、$\rho$ が $e\in G_1$ で連続ならば、$\rho$ は $G_1$ で連続。
<br>

</dt><dd>

- 位相群 $G_1,G_2$、全射な開準同型写像 $\rho:G_1\to G_2$ とする。
このとき、
$$\psi:G_1/\ker\rho\to G_2\\\ \\
\psi\circ\pi=\rho$$を満たすような位相群の同型写像がただ一つ存在する。

      ・別にImρで置き換えても成り立つ。
      ・開であることに注意。
      ・群と位相。

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
$$\Psi\circ(1\times\pi)=\pi\circ P\quad(P\text{ は }G\text{ で積を取る写像})$$を満たす。
特に、$T_g:G/H\to G/H$ は 
$$T_g(T_h(x))=T_{gh}(x)\\\ \\
T_e(x)=x\\\ \\
\forall x,y\in G/H\text{ に対して、}\exist g\in G\text{ であって、}\\T_g(x)=y$$ を満たす同相写像。 
<br>

- $G$ の単位元周りの基本近傍系 $\{U_{\lambda}\}$ に対して、
$$\{\pi(U_{\lambda})\}$$ は $G/H$ の単位元 $\pi(e)$ 周りの基本近傍系。
<br>

- $H$ が閉部分群ならば、$G/H$ は正則空間。
<br>

      ・基本、閉部分群だけを考える。

</dd></dl>

---

・位相群 $G$、部分群 $H$、$a\in G$ とする。
このとき、
$$f_a:G/H\to G/H\\\ \\
f_a(X)=aX$$
と定めると、これは同相写像。

---

### 連続な断面

・位相群 $G$、部分群 $H\sub G$、射影 $p:G\to G/H$ とする。
このとき、連続な断面 $s:G/H\to G,\ p\circ s=1$ が存在すれば、
$$G\cong (G/H)\times H\ (\text{同相})$$

---

#### 局所断面

・位相群 $G$、部分群 $H\sub G$、射影 $p:G\to G/H$ とする。
このとき、連続な局所断面 $s$：
$$\exist\text{ 開近傍}U\in\mathcal{N}([e]),\ \exist \text{ 連続写像 }s:U\to G\text{ であって、}\\\ \\
p\circ s=1$$

      ・リー群とその閉部分群に対して、常に局所断面が存在する？群と位相p.181
<br>

- 位相群 $G$、部分群 $H\sub G$、射影 $p:G\to G/H$、局所断面 $s:U\to G$ とする。
このとき、$(G,G/H,p,H;H)$ は主ファイバー空間であって、
自明化：
$$U_{a}=aU,\quad\phi_a(X,h)=as(a^{-1}X)h\\\ \\
g_{ab}(x)=s_a(x)^{-1}s_b(x)$$

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

・位相群 $G$、正規部分群 $N$、剰余群 $G/N$ とする。
また、積を取る写像 $P:G\times G\to G,\ \overline{P}:G/N\times G/N\to G/N$、逆元を取る写像 $J:G\to G,\ \overline{J}:G/N\to G/N$ とする。
このとき、$\overline{P},\ \overline{J}$ は連続で、
$$\overline{P}\circ (\pi\times \pi)=\pi\circ P\\\ \\
\overline{J}\circ\pi=\pi\circ J$$満たす。
よって、閉正規部分群 $N$ に対して、$G/N$ は位相群。

    ・閉正規部分群のみを考える。

</dt><dd>

- 射影 $\pi$ は連続で全射な、開な準同型写像。


</dd></dl>

---


# 連続な群作用

## 基本的な性質

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


- $x\in X$、$p:G\to X,\ p(g)=gx$、$x$ の等方群 $G_x$ とする。
このとき、連続な断面 $s:X\to G,\ p\circ s=1$ が存在するならば、
$$G\cong X\times G_x\ (\text{同相})$$また、
$$s(gx)x=gx\ (\forall g\in G)$$ が成り立っている。
<br>

      ・同相を与える写像は、位相空間論の射影と断面のときと同じ。
<br>

- 軌道空間 $X/G$ とする。
このとき、
$$p:X\to X/G\\\ \\
p(x)=G(x)=Gx$$ は連続全射な開写像。また、$A\sub X$ に対して、
$$AG=p^{-1}(p(A))$$

      ・G(x)=Gxと書ける。


</dd></dl>

---

## 関数への作用

・位相群 $G$、位相空間 $X$、$f:G\to X$ とする。
このとき、
$$L_gf,R_gf:G\to X\\\ \\
L_gf(h)=f(g^{-1}h),\quad R_gf(h)=f(hg)$$
とすると、これは群作用。

・位相群 $G$、位相空間 $X$、連続写像 $f:G\to X$ とする。
このとき、$L_gf,R_gf$ は連続写像。


---

## 等質集合

<dl><dt>

・位相群 $G$、位相空間 $X$、連続な群作用 $\Psi:G\times X\to X$ とする。
このとき、等質空間 $X$：推移的な作用

</dt><dd>




</dd></dl>


---
---
---




