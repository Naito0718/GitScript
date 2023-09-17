- [一章：四元数体 $H$](#一章四元数体-h)
  - [基本的な性質](#基本的な性質)
    - [定義](#定義)
    - [演算](#演算)
      - [特殊な性質](#特殊な性質)
  - [位相](#位相)
    - [右加群性](#右加群性)
  - [実数$R$との関係](#実数rとの関係)
  - [$H^n$](#hn)
    - [位相](#位相-1)
      - [右加群性](#右加群性-1)
  - [$M(n,H)$](#mnh)
    - [位相的性質](#位相的性質)
    - [具体的な性質](#具体的な性質)
    - [一般線形群 $GL(n,H)$](#一般線形群-glnh)
      - [位相的性質](#位相的性質-1)
    - [$H^n$ との関係](#hn-との関係)
      - [$H^n$ の内積](#hn-の内積)
      - [$G(n,H)$](#gnh)
      - [表現](#表現)
    - [トレース Tr](#トレース-tr)
  - [球面 $S^n$](#球面-sn)
    - [$Sp(n)=G(n,H)$ からの作用](#spngnh-からの作用)
  - [射影空間 $HP$](#射影空間-hp)
    - [定義](#定義-1)
    - [射影空間の位相](#射影空間の位相)
    - [射影直線](#射影直線)
  - [Cayley数](#cayley数)
- [二章：位相線形空間としての $M(n,C)$](#二章位相線形空間としての-mnc)
  - [位相的性質](#位相的性質-2)
  - [指数写像](#指数写像)
    - [単位元の近傍](#単位元の近傍)
    - [$1$ パラメータ部分群](#1-パラメータ部分群)
  - [内積と古典群](#内積と古典群)
- [三章：位相群としての $GL(n,C)$](#三章位相群としての-glnc)
  - [位相的性質](#位相的性質-3)
  - [特殊線形群 $SL(n,C)$](#特殊線形群-slnc)
  - [実一般線形群 $GL(n,R)$](#実一般線形群-glnr)
- [四章：エルミート行列 $H(n)$ と準代数群](#四章エルミート行列-hn-と準代数群)
  - [位相的性質](#位相的性質-4)
  - [性質](#性質)
    - [次元、固有値](#次元固有値)
    - [指数写像](#指数写像-1)
  - [正値エルミート行列](#正値エルミート行列)
    - [位相的性質](#位相的性質-5)
    - [性質](#性質-1)
    - [極分解](#極分解)
  - [対角エルミート行列](#対角エルミート行列)
- [反射行列](#反射行列)
  - [性質](#性質-2)
- [直交群 $O(n)$](#直交群-on)
  - [位相的性質](#位相的性質-6)
    - [位相幾何的性質](#位相幾何的性質)
  - [球面 $S^n$ との関係](#球面-sn-との関係)
  - [射影空間 $RP$ との関係](#射影空間-rp-との関係)
  - [$SO(n)$ との関係](#son-との関係)
    - [$n=1$](#n1)
    - [$n=2$](#n2)
    - [$n=4$](#n4)
    - [$n=8$](#n8)
- [複素直交群 $O(n,C)$](#複素直交群-onc)
        - [位相的性質](#位相的性質-7)
- [ユニタリ群 $U(n)$](#ユニタリ群-un)
  - [位相的性質](#位相的性質-8)
    - [位相幾何的性質](#位相幾何的性質-1)
  - [性質](#性質-3)
    - [球面 $S^n$ との関係](#球面-sn-との関係-1)
    - [射影空間との関係](#射影空間との関係)
    - [$SU(n)$ との関係](#sun-との関係)
    - [交代Hermite行列との関係](#交代hermite行列との関係)
  - [具体的な $n$](#具体的な-n)
    - [$n=1$](#n1-1)
    - [$n=2$](#n2-1)
- [特殊直交群$SO(n)$](#特殊直交群son)
  - [位相的性質](#位相的性質-9)
    - [位相幾何的性質](#位相幾何的性質-2)
  - [性質](#性質-4)
  - [球面 $S^n$ との関係](#球面-sn-との関係-2)
  - [交代行列との関係](#交代行列との関係)
  - [具体的な $n$](#具体的な-n-1)
    - [$n=1$](#n1-2)
    - [$n=2$](#n2-2)
      - [簡単な指数行列](#簡単な指数行列)
    - [$n=3$](#n3)
    - [$n=4$](#n4-1)
    - [$n=8$](#n8-1)
- [特殊ユニタリ群 $SU(n)$](#特殊ユニタリ群-sun)
  - [位相的性質](#位相的性質-10)
    - [位相幾何的性質](#位相幾何的性質-3)
  - [球面 $S^n$ との関係](#球面-sn-との関係-3)
  - [具体的な $n$](#具体的な-n-2)
    - [$n=1$](#n1-3)
    - [$n=2$](#n2-3)
- [一般Lorentz群$O(n-1,1)$](#一般lorentz群on-11)
        - [$R$上ベクトル空間$V$における正則対称双一次形式$B$](#r上ベクトル空間vにおける正則対称双一次形式b)
        - [$n=4$（Lorentz群）](#n4lorentz群)
- [シンプレクティック群 $Sp(n)$](#シンプレクティック群-spn)
  - [位相的性質](#位相的性質-11)
  - [性質](#性質-5)
    - [球面 $S^n$ との関係](#球面-sn-との関係-4)
    - [射影空間との関係](#射影空間との関係-1)
    - [交代Hermite行列との関係](#交代hermite行列との関係-1)
  - [具体的な $n$](#具体的な-n-3)
    - [$n=1$](#n1-4)





# 一章：四元数体 $H$

## 基本的な性質

### 定義

・定義：任意の $x\in\bm{H}$ に対して、$$x=a1+bi+cj+dk\quad (a,b,c,d\in\bm{R})$$ とただ一通りに表される。

---

### 演算

・演算：
 $$i^2=j^2=k^2=-1\\\ \\
 ij=-ji=k,\ jk=-kj=i,\ ki=-ik=j\\\ \\
 1x=x1=x\\\ \\
 (a1)i=i(a1)=ai,\ (a1)j=j(a1)=aj,\ (a1)k=k(a1)=ak$$

 - 和は可換で結合法則、積は結合法則と分配法則

       ・積は可換でない。

---

・$x=a+bi+cj+dk$ に対して、
共役、実部：
$$x^*=a-bi-cj-dk\\\ \\
\mathrm{Re}(x)=a$$

- $x,y\in\bm{H}$ に対して、
$$(x+y)^*=x^*+y^*,\quad (xy)^*=y^*x^*\\\ \\
\mathrm{Re}(xy)=\mathrm{Re}(yx)$$

      ・積は対合演算になってる

---

#### 特殊な性質

・$$\forall \lambda\in \bm{H}\text{ に対して }\overline{\lambda}\ \overline{\alpha}+\alpha\lambda=\overline{\lambda}\ \overline{\beta}+\beta\lambda\iff\alpha=\beta$$

    ・複素数、実数でも成り立つ。

---

## 位相

    ・結局R^4と同じ。

・$\bm{H}$ は $\bm{R}$ 上 $4$ 次元ベクトル空間。

- 内積：$(x,y)=a_1a_2+b_1b_2+c_1c_2+d_1d_2$
<br>

- ノルム：$\|x\|=\sqrt{xx^*}=\sqrt{x^*x}=\sqrt{a^2+b^2+c^2+d^2}$
<br>

- $\|xy\|=\|x\|\|y\|$
<br>

- $x$ の逆元：$$\frac{x^*}{\|x\|^2}$$

- 距離：$\|x-y\|$


---

・明らかに $\bm{R}^4\sim\bm{H}\ (\text{同相})$

- $\bm{H}$ は $\bm{R}$ 上Hilbert空間。すなわち、$\bm{R}$ 上単位的 $C^*$-環。

      ・係数が実数の指数行列とかは問題ない。

---

### 右加群性

・$\bm{H}$ は $2$ 次元 $\bm{C}$-右加群。

- 基底：$1,j$

---

・$\bm{H}$ は $1$ 次元 $\bm{H}$-右加群。

- 内積 $(x,y)=\overline{x}y$

---

## 実数$R$との関係

・$x\in\bm{H}$ に対して、
$x\in \bm{R}\iff x^*=x\iff\forall y\in H\text{ に対して }xy=yx$



---

## $H^n$

### 位相

・$\bm{H}^n$ は $4n$ 次元 $\bm{R}$ 上ベクトル空間。

・距離：$$\|x-y\|=\sqrt{\sum\|x_i-y_i\|}$$であって、これは完備。

---

#### 右加群性

・$\bm{H}$ は $2n$ 次元 $\bm{C}$-右加群。

    ・別に左C-加群でもあるが、C上ベクトル空間ではない。

- 基底：$e_i=(0,...,0,1,0,...,0),\ f_i=(0,...,0,j,0,...,0)$

---

・$\bm{H}^n$ は $n$ 次元右 $\bm{H}$-加群。

      ・別に左H-加群でもあるが、H上ベクトル空間ではない。

- 内積：$(x,y)=\sum_i\overline{x_i}y_i$、
正規直交基底：$e_i=(0,...,0,1,0,...,0)$

---

## $M(n,H)$

### 位相的性質

・$M(n,\bm{H})$ は $n^2$ 次元右 $\bm{H}$-加群。

・内積：$(A,B)=\sum_{i,j}\overline{a_{ij}}b_{ij}$

- ノルム？：$\|A\|=\sqrt{(A,A)}$

      ・右ノルムとでも言うのか

- 距離：$$\|A-B\|$$であって、これは完備。

      ・∑|A_n| が収束すれば、∑A_n も収束する。（絶対収束）

- $\bm{R}$ 上Banach単位的ノルム環。

      ・係数が実数の指数行列とかは問題ない。

---

### 具体的な性質 

    ・複素数、実数上でも成り立つ。

・$$\|AB\|\le\|A\|\|B\|\\\ \\
\|A\|,\|B\|\le a\Rightarrow\forall k\ge1\in\bm{N}\text{ に対して、}\|A^k-B^k\|\le ka^{k-1}\|A-B\|$$

- $A\in M(n,\bm{H})$ とする。
このとき、$\|E-A\|<1$ を満たすならば、$A$ は正則であって、逆行列：
$$A^{-1}=E+\sum_{k=1}^{\infty}(E-A)^k$$

      ・別に0からでまとめてもよい

・$F\in M(n,\bm{H})$ とする。
このとき、$$F\text{ がコンパクト}\iff F\text{ は有界閉集合}$$

    ・結局R^nと距離同相

---

### 一般線形群 $GL(n,H)$

・$$i:GL(n-1,\bm{H})\to i(GL(n-1,\bm{H}))\sub GL(n,\bm{H})\\\ \\
i(A)=\begin{pmatrix}
A &  \\
& 1 \\
\end{pmatrix}$$は群同相写像。よって、
$$GL(n-1,\bm{H})\sub GL(n,\bm{H})$$の部分群とみなせる。

    ・G(n,H) でも成り立つ。

- $A\in G(n,\bm{H})$ に対して、
$$A\in G(n-1,\bm{H})\iff Ae_n=e_n$$


---

・$$i:GL(n-1,\bm{H})\times GL(1,\bm{H})\to i(GL(n-1,\bm{H}\times GL(1,\bm{H})))\sub GL(n,\bm{H})\\\ \\
i(A,a)=\begin{pmatrix}
A &  \\
& a \\
\end{pmatrix}$$は群同相写像。よって、
$$GL(n-1,\bm{H}\times GL(1,\bm{H}))\sub GL(n,\bm{H})$$の部分群とみなせる。

    ・G(n,H)×G(1,H) でも成り立つ。

- $A\in GL(n,\bm{H})$ に対して、
$$A\in GL(n-1,\bm{H})\times GL(1,\bm{H})\iff AE_n=E_nA$$

      ・G(n,H)×G(1,H) でも成り立つ。


#### 位相的性質

<dl><dt>

・位相的性質

    ・複素数上、実数上でも成り立つ。

</dt><dd>

- $M(n,\bm{H})$ において、積演算：$AB$ は連続。
<br>

- 点列 $A_n\sub GL(n,\bm{H})$、$\lim A_n=A\in GL(n,\bm{H})$ とする。
このとき、$$\lim A_n^{-1}=A^{-1}$$すなわち、$GL(n,\bm{H})$ は積に関して位相群。
<br>

- $GL(n,\bm{H})$ は $M(n,\bm{H})$ の開集合。したがって、局所コンパクトHausdorff空間。

      ・第二可算でもある。


</dd></dl> 

---

### $H^n$ との関係

---

#### $H^n$ の内積

・$$(Ax,y)=(x,A^{\dag}y)$$が成り立つ。

---

#### $G(n,H)$

    ・結局G(n,H)はH上右加群のG(V)と群同相。 

・$$G(n,H)=\{A\in M(n,H)\ |\ A^{\dag}A=E\}$$は積で群をなす。この群をシンプレティック群 $Sp(n)$ という。

    ・このとき、AA^{☨}=E
    ・加群ではない。

・$A\in M(n,H)$ とする。
このとき、
$$A\in G(n,H)\\\ \\
\iff (x,y)=(Ax,Ay)\ \ (\forall x,y\in H^n)\\\ \\
\iff \|Ax\|=\|x\|\ \ (\forall x\in H^n)\\\ \\
\iff A=(a_1,...,a_n)\text{ とすると、}a_i\text{ は正規直交基底}\\\ \\
\iff A=(a_{ij})\text{ とすると、}\sum \overline{a_{ik}}a_{jk}=\delta_{ij}$$

    ・複素数、実数上でも成り立つ。

---

#### 表現

・$\bm{H}$-右加群 $\bm{H}^n$、$A\in GL(n,\bm{H})$ とする。
このとき、$A\$

---

### トレース Tr

・$A=(a_{ij})\in M(n,H)$ に対して、$Tr(A)=\sum a_{ii}$

- エルミート行列 $H\in H_{\bm{H}}(n)$、シンプレクティック行列 $A\in Sp(n)$ に対して、
$$\mathrm{Tr}(X)=\mathrm{Tr}(A^{-1}XA)$$

      ・Tr(AB)=Tr(BA)は成り立たない。


---

## 球面 $S^n$

・$$S_H^n=\{\alpha\in H^{n+1}\ |\ \|\alpha\|=1\}$$と定めると、明らかに
$$S_H^{n-1}\cong S^{4n-1}\ (\text{距離同相})$$

    ・複素球面でも同様。

---

### $Sp(n)=G(n,H)$ からの作用

    ・複素数上、実数上でも同様に成り立ち、その時はSO(n),SU(n)でもまったく同様に成り立つ。

・
$$\mu:G(n,\bm{H})\times S_{\bm{H}}^{n-1}\to S_{\bm{H}}^{n-1}\\\ \\
\mu(A,x)=Ax$$は連続な群作用で、効果的で推移的に働く。

- $e_n$ の等方群 $G_{e_n}=G(n-1,\bm{H})$
  
---

## 射影空間 $HP$

    ・実数、複素数でもまったく同様に成り立つ。

### 定義

<dl><dt>

・$x,y\in H^n\backslash\{0\}$ とする。
このとき、$$x\sim y\iff\exist a\in H\text{ であって、}y=xa$$は同値関係。
このとき、射影空間 $$HP_{n-1}=(H^n\backslash\{0\})/\sim$$と定める。
<br>

</dt><dd>

- $A\in M(n,\bm{H})$ とする。
このとき、
$$A^{\dag}=A,\ A^2=A,\ \mathrm{Tr}A=1\\\ \\
\iff\exist B\in Sp(n)\text{ であって、}A=BE_nB^{\dag}\quad(E_n\text{ は $(n,n)$ だけ $1$ の行列})\\\ \\$$

- $$HP(n-1)=\{A\in M(n,\bm{H})\ |\ A^{\dag}=A,\ A^2=A,\ \mathrm{Tr}A=1\}$$と定める。
このとき、
$$f:H^n\backslash\{0\}\to HP(n-1)\\\ \\
f(x)=\frac{1}{\|x\|^2}(x_i\overline{x}_j)$$と定めると、これはwell-definedで全射。
さらに、$$x\sim y\iff f(x)=f(y)$$なので、全単射 $$\tilde{f}:HP_{n-1}\to HP(n-1)$$を誘導する。
<br>

- $HP(n-1)$ は距離空間。よって、射影空間は距離空間と言える。


</dd></dl> 

---

### 射影空間の位相

    ・複素数、実数上でも成り立つ。

・$x,y\in S_{\bm{H}}^{n-1}$ とする。
このとき、$$x\sim y\iff \exist a\in H,\ |a|=1\text{ であって、}y=xa$$は同値関係。 

- 上記の同値関係において、
$$S_{\bm{H}}^{n-1}/\sim\ \cong HP_{n-1}\ (\text{同相})$$特に、$HP_{n-1}$ は弧状連結でコンパクト。
<br>

- $$HP_{n-1}\cong HP(n-1)\ (\text{同相})$$よって、射影空間は弧状連結なコンパクトHausdorff空間。

--- 

・
$$\mu:S_{\bm{H}}^{n-1}\times S_{\bm{H}}^0\to S_{\bm{H}}^{n-1}\\\ \\
\mu(x,a)=xa$$ によって、位相群 $S_{\bm{H}}$ は $S_{\bm{H}}^{n-1}$ に連続に作用する。
<br>

- このとき、軌道空間 $S_{\bm{H}}/S_{\bm{H}}^{0}$ は、上記の同値関係による同値類の集合に等しい。$$S_{\bm{H}}/S_{\bm{H}}^{0}=S_{\bm{H}}/\sim$$




---

### 射影直線

---

## Cayley数

---
---
---


# 二章：位相線形空間としての $M(n,C)$

      ・実数R上の有限次元ベクトル空間で、結合法則、可換性を仮定せず体をなすものは、R,C,Hと8元数に限る
      ・結局可換でないと行列式も定義されない

## 位相的性質

・ノルム：$$\|\alpha\|=\sqrt{\sum|a_{ij}|^2}$$

- 明らかに $\bm{R}^{2n^2}\cong M(n,\bm{C})$ で線形同相。

      ・実数ならn^2、四元数なら4n^2

- $M(n,\bm{C})$ はBanach単位的 $*$-環

        ・ノルムが異なるので、有界線形作用素 B(H) で考えているわけではない
        ・C*まで言える？

 ---

・行列式写像：$\det:M(n,\bm{C})\to\bm{C}$ は連続

- 小行列式写像：$M(n,\bm{C})\to M(n,\bm{C}),\quad\alpha\mapsto\tilde{\alpha}$ は連続

・転置、共役、転置共役写像：$^T,\ \bar\ ,\ ^{\dag}:M(n,\bm{C})\to M(n,\bm{C})$ は線形連続。

- 転置積、転置共役積；$trat,dagt:gg^T,gg^{\dag}$ は連続。

・$\sigma\in GL(n,\bm{C})$ に対して、
$$M(n,\bm{C})\to M(n,\bm{C}),\quad\alpha\mapsto\sigma^{-1}\alpha\sigma$$ は線形連続。

---

・局所コンパクト空間。

・弧状連結。

---

## 指数写像  

    ・四元数体上の行列でも、detと転置と固有値以外は成り立つ。

<dl><dt>

・$$\exp:M(n,\bm{C})\to M(n,\bm{C})$$ は連続。

    ・基本、一般の Banach単位的 C,R 上代数でも成り立つ。

</dt><dd>

- $$\exp0_n=1_n\\\ \\
\exp\alpha^T=(\exp\alpha)^T,\quad \exp(\sigma^{-1}\alpha\sigma)=\sigma^{-1}(\exp\alpha)\sigma,\quad \exp\overline{\alpha}=\overline{\exp\alpha}\\\ \\$$

- $[\alpha,\beta]=0\Rightarrow\exp(\alpha+\beta)=\exp\alpha\exp\beta$

      ・交換子。
      ・級数の積のこと。

- $\exp\alpha\in GL(n,\bm{C})$ であって、
$$(\exp\alpha)^{-1}=\exp(-\alpha)\\\ \\$$

- $\det\exp\alpha=e^{\mathrm{Tr}\alpha}$

      ・0でない。
      ・固有値で示される。

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

# 三章：位相群としての $GL(n,C)$

## 位相的性質

 ・相対距離：$d(\alpha,\beta)=\|\alpha-\beta\|$

    ・別にα-β∊GL(n,C)でなくてもよい

- 逆元：$\alpha\mapsto\alpha^{-1}$ は連続
  <br>

 ・行列式写像：
 $$\det:GL(n,\bm{C})\to C^{\times}$$は準同型写像

---

・局所コンパクト空間。

- $\bm{C}^{*}=GL(1,\bm{C})$

・連結であって、$GL(n,\bm{C})=\det^{-1}\{z\in\bm{C}\ |\ z\neq0\}$

---

## 特殊線形群 $SL(n,C)$

・特殊線形群：$SL(n,\bm{C})=\ker\det\quad(\det:GL(n,\bm{C})\to C^{\times})$

<dl><dt>

・位相的性質

</dt><dd>

- $M(n,\bm{C})$ の閉集合で、$GL(n,\bm{C})$ の閉部分群かつ正規部分群。
<br>

- 第二可算な局所コンパクトHausdorff空間。
<br>

- $\det:GL(n,\bm{C})\to C^{*}$ は連続全射な群準同型。
すなわち、$$GL(n,\bm{C})/SL(n,\bm{C})\to \bm{C}^{*}$$ を誘導する。 

      ・実数上でも成り立つ。


</dd></dl> 

 ---

## 実一般線形群 $GL(n,R)$

 ・$GL(n,\bm{R})\subset GL(n,\bm{C})$ は閉部分群。

---
---
---

# 四章：エルミート行列 $H(n)$ と準代数群

## 位相的性質

・$H(n)$ は $M(n,\bm{R,C,H})$ の閉集合。

---

## 性質

### 次元、固有値

<dl><dt>

・$$H(n)=\{A\in M(\bm{R,C,H})\ |\ A^{\dag}=A\}$$は $\bm{R}$ 加群。ここで、$H(n)$ の元をエルミート行列という。

    ・C,H加群ではない。

</dt><dd>

- $$\dim H_{\bm{R}}(n)=\frac{n(n+1)}{2},\quad\dim H_{\bm{C}}(n)=n^2,\\\ \\
\dim H_{\bm{H}}(n)=n(2n-1)$$特に、対角成分はすべて実数。
さらに、距離空間として $\bm{R}^{\dim H(n)}$ と同型である。

      ・n+k(n(n-1)/2)

- $$\forall A\in H(n)\text{ に対して、}\exist\lambda\in\bm{R},\exist x\in\bm{R,C,H}^n\backslash\{0\}\text{ であって、}\\\ \\
Ax=\lambda x\\\ \\$$

      ・四元数体Hでは、エルミート行列以外の固有値は定義できない。（っぽい）

- $$\forall A\in H(n)\text{ に対して、}\exist X\in G(n,\bm{R,C,H})\text{ であり }\\\ \\
\text{さらに }\lambda_1,...,\lambda_n\in\bm{R}\text{ が順序を除いてただ一つ存在して、}\\\ \\
X^{-1}AX=\begin{pmatrix}
\lambda_1 & \\
 & \ddots & \\
 & & \lambda_n\\
\end{pmatrix}\\\ \\
\mathrm{Tr}(X^k)=\sum_{i=1}^n\lambda_i^k\quad(k=1,...,n)$$が成り立つ。


</dd></dl> 

---

### 指数写像

・$A\in G(n,\bm{R,C,H}),\ X\in H(n)$ とする。
このとき、
$$A\exp X=\exp X\ A$$ならば、
$$AX=XA\\\ \\$$

- $$\exp:H(n)\to H_+(n)$$は同相写像。したがって、$\bm{R}^{\dim H(n)}$ と同相。



---

## 正値エルミート行列

### 位相的性質

・$H_+(n)$ は $GL(n,\bm{R,C,H})$ の閉集合。

---

### 性質

<dl><dt>

・エルミート行列 $A\in H(n)$ に対して、
正値エルミート行列 $A$：固有値がすべて $>0$
ここで、正値エルミート行列全体を $H_{+}(n)$ と書く。

    ・別にR上のベクトル空間ではない。

</dt><dd>

- $H_+(n)\sub GL(n)$
<br>

- エルミート行列 $A\in H(n)$ とする。このとき、
$$A\in H_{+}(n)\\\ \\
\iff\exist B\in H_+(n)\text{ であって、}A=B^2\\\ \\
\iff\forall x\in \bm{R,C,H}\text{ に対して、}(Ax,x)>0\\\ \\$$

- $P,Q\in H_+(n)$ とする。
このとき、$$P^n=Q^n\ (n=1,2,...)\iff P=Q$$

- 
$$f:H_+(n)\to H_+(n)\\\ \\
f(P)=\sqrt{P}=\exp\left(\frac{1}{2}\log P\right)$$ はwell-definedで連続。

</dd></dl> 

--- 

### 極分解

・$A\in GL(n,\bm{R,C,H})$ とする。
このとき、$$\exist! U\in G(n,\bm{R,C,H}),\ \exist! P\in H_+(n)\text{ であって、} H=UP$$ 

    ・一意的に成り立つ。

- 
$$f:G(n,\bm{R,C,H})\times H_+(n)\to GL(n,\bm{R,C,H})\\\ \\
f(u,P)=UP$$は同相写像。




---

## 対角エルミート行列

<dl><dt>

・対角エルミート行列：$DH(n)=\{A\in H(n)\ |\ A\text{ は対角行列 }\}$
<br>

</dt><dd>

- $$DH(n)=\{A\in M(n,\bm{R})\ |\ A\text{ は対角行列 }\}$$

- $$\exp:DH(n)\to DH_+(n)$$ は同相写像。
<br>

- 点列 $D_n\sub DH(n)$ とする。
このとき、$\exp D_n$ が $GL(n,\bm{R,C,H})$ 内に収束するならば、：$\lim \exp D_n=P\in GL(n,\bm{R,C,H})$
$D_n$ は収束し、
$$P\in DH_+(n),\ \lim D_n=D\in DH(n),\ P=\exp D$$


</dd></dl> 


---
---
---

# 反射行列

## 性質

<dl><dt>

・$a\in S_{\bm{R,C,H}}^{n-1}$、$D\in M(n,\bm{R,C,H})$ とする。
このとき、$a$ に関する反射行列 $D$：
$$Da=-a\\\ \\
\forall x\in (\bm{R,C,H})^n\text{ に対して、}(x,a)=0\Rightarrow Dx=x\\\ \\$$

</dt><dd>

- 


</dd></dl> 


---

# 直交群 $O(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=trat^{-1}(I)\cap GL(n,\bm{R})$

・コンパクト集合

---

### 位相幾何的性質

・$O(n)$ は $2$ つの弧状連結成分を持ち、単位元 $E$ を含む方が $SO(n)$ である。

---

## 球面 $S^n$ との関係

・
$$p:O(n)\to S^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$O(n)/O(n-1)\cong S^{n-1}\ (\text{同相})$$

---

## 射影空間 $RP$ との関係

・
$$f:O(n)\to RP_{n-1}\\\ \\
f(A)=AEA^{T}$$と定める。
このとき、次の同相が誘導される。
$$O(n)/(O(n-1)\times S^0)\cong RP(n-1)$$

---

## $SO(n)$ との関係

・$$O(n)/SO(n)\cong S^0=\{-1,1\}\ (\text{群同相})$$

- $$O(n)\cong S^{0}\times SO(n)\ (\text{同相})$$

---

### $n=1$

・明らかに$$O(1)\cong S^0=\{-1,1\}$$

    ・別にO(1)も{-1,1}。

### $n=2$

 ・$O(2)=\left\{\begin{pmatrix}
      \\
      \\
 \end{pmatrix}\ |\ \theta\in[)\right\}$

---

### $n=4$

・$$O(4)\cong S^3\times O(3)\ (\text{同相})$$

    ・？群と位相、p.108

### $n=8$

・$$O(8)\cong S^7\times O(7)\ (\text{同相})$$


# 複素直交群 $O(n,C)$

##### 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n,\bm{C})=trat^{-1}(I)$

---
---
---

# ユニタリ群 $U(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$U(n)=dagt^{-1}(I)$

・コンパクト集合、すなわち $GL(n,\bm{C})$ の有界閉集合

---

### 位相幾何的性質

・$U(n)$ は弧状連結。

---

## 性質

<dl><dt>

・$$\forall A\in U(n)\text{ に対して、}\exist X\in U(n)\text{ であって、}\\\ \\
X^{-1}AX=\begin{pmatrix}
\ddots\\
& e^{i\theta_i}  \\
& & \ddots
\end{pmatrix}\quad(\theta_i\in\bm{R})$$

    ・固有値のこと。エルミート行列の話ではない。

</dt><dd>

- 上記に加えて、
$$\alpha=\begin{pmatrix}
i\theta_1 &  \\
& \ddots \\
& & i\theta_m \\
\end{pmatrix}$$と定めると、
$$\exp\alpha=X^{-1}AX$$したがって、
$$u:I\to U(n)\\\ \\
u(A)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

### 球面 $S^n$ との関係

・
$$p:U(n)\to S_{\bm{C}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$U(n)/U(n-1)\cong S^{2n-1}$$4

---

### 射影空間との関係

・
$$f:U(n)\to CP{n-1}\\\ \\
f(A)=AEA^{\dag}$$と定める。
このとき、次の同相が誘導される。
$$U(n)/(U(n-1)\times S^2)\cong HP(n-1)\ (\text{同相})$$

---

### $SU(n)$ との関係

・$$U(n)/SU(n)\cong S^1\ (\text{ 群同相})$$


---

### 交代Hermite行列との関係

・交代Hermite行列 $A\in M(n,\bm{C})$ とする。
このとき、$\exp A\in U(n)$


---


<dl><dt>

・$$U(n)\cong S^1\times SU(n)\ (\text{同相})$$

    ・群同相ではない。

</dt><dd>

- 行列式：$|\det U|=1$
<br>

- $U\in U(n)$ とする。
このとき、$$U=e^{i\frac{\alpha}{n}}U',\quad(\det U=e^{i\alpha})$$とおくと、$U'\in SU(n)$


</dd></dl> 

---

## 具体的な $n$

### $n=1$

・明らかに$$U(1)\cong S_C^1\cong S^2$$

---

### $n=2$

・$A=\begin{pmatrix}
a & -\bar{c}    \\
c & \bar{a}    \\
\end{pmatrix}\quad(|a|^2+|b|^2=1)$

---
---
---


# 特殊直交群$SO(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=trat^{-1}(I)\cap \det^{-1}(1)$

・コンパクト集合、すなわち $U(n)$ の閉集合。

---

### 位相幾何的性質

・$SO(n)$ は弧状連結。

---

## 性質

<dl><dt>

・$$\forall A\in SO(n)\text{ に対して、}\exist X\in O(n)\text{ であって、}\\\ \\
X^{-1}AX=\begin{pmatrix}
A_1 &  \\
& \ddots \\
& & A_m \\
& & & (1)\\
\end{pmatrix}\quad A_i=\begin{pmatrix}
\cos\theta_i & -\sin\theta_i  \\
\sin\theta_i & \cos\theta_i \\
\end{pmatrix}\\\ \\(\theta_i\in\bm{R},\ \ (1):\text{ $n$ が偶数のときは消えて、奇数なら $1$})$$

    ・XはSO(n) の元に取れるらしい？、群と位相

</dt><dd>

- 上記に加えて、
$$\alpha=\begin{pmatrix}
\alpha_1 &  \\
& \ddots \\
& & \alpha_m \\
& & & (0)\\
\end{pmatrix}\quad \alpha_i=\begin{pmatrix}
0 & \theta_i  \\
\theta_i & 0 \\
\end{pmatrix}\\\ \\((0):\text{ $n$ が偶数のときは消えて、奇数なら $0$})$$と定めると、
$$\exp\alpha=X^{-1}AX$$したがって、
$$u:I\to SO(n)\\\ \\
u(A)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

---

## 球面 $S^n$ との関係

・
$$p:SO(n)\to S^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$SO(n)/SO(n-1)\cong S^{n-1}$$

---

## 交代行列との関係

・交代行列 $A\in M(n,\bm{R})$ とする。
このとき、$$\exp A\in SO(n)$$

    ・Hermiteだと対角は実数なだけだからSUではない。

---

## 具体的な $n$

### $n=1$

・$SO(1)=\{1\}$

---

### $n=2$

・$$SO(2)\cong S^1\text{同相}$$

    ・群同相？

---

#### 簡単な指数行列

・
$$A=\begin{pmatrix}
0 & -\theta \\  
\theta & 0 \\
\end{pmatrix}\quad(\theta\in\bm{R})$$とする。
このとき、
$$\exp A=\begin{pmatrix}
\cos\theta & -\sin\theta \\  
\sin\theta & \cos\theta \\
\end{pmatrix}\in SO(2)$$

---

### $n=3$

・直交座標系の間の変換$\bar{x}=Ax$に対して、
$$A=\begin{pmatrix}
\cos\alpha_1 & \cos\beta_1 & \cos\gamma_1    \\
\cos\alpha_2 & \cos\beta_2 & \cos\gamma_2 \\
\cos\alpha_3 & \cos\beta_3 & \cos\gamma_3  \\
\end{pmatrix},\quad(\alpha_i,\beta_i,\gamma_i{はそれぞれ軸の方位角})$$
と書ける

→$A\in SO(3)$
→高次元でも同じ式が成り立つ

    ・高次元でも角度は定義できる

---

・$A\in SO(3)$を指定する$3$つの実数

→回転軸が$z$軸となす角 $\theta$ と方位角 $\phi$、回転角 $\phi'$

---

・

---

### $n=4$

・$SO(4)=SO(\bm{H})$

    ・？群と位相、p.108

・$$SO(4)\cong S^3\times SO(3)\ (\text{同相})$$

      ・？

### $n=8$

・$$SO(8)\cong S^7\times SO(7)\ (\text{同相})$$

---
---
---

# 特殊ユニタリ群 $SU(n)$

## 位相的性質

・$GL(n,\bm{C})$ の閉部分群であって、$O(n)=dagt^{-1}(I)\cap \det^{-1}(1)$

・コンパクト集合

---

### 位相幾何的性質

・$SU(n)$ は弧状連結。

---

## 球面 $S^n$ との関係

・
$$p:SU(n)\to S_{\bm{C}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$SU(n)/SU(n-1)\cong S^{2n-1}$$

---

## 具体的な $n$

### $n=1$

・$SU(1)=\{1\}$

---

### $n=2$

・$A=\begin{pmatrix}
a & -\bar{c}    \\
c & \bar{a}    \\
\end{pmatrix}\quad(|a|^2+|b|^2=1)$
と書ける

- $SU(2)\cong S^3\text{同相}$

    ・群同相？

---
---
---

# 一般Lorentz群$O(n-1,1)$

##### $R$上ベクトル空間$V$における正則対称双一次形式$B$



---

##### $n=4$（Lorentz群）



---
---
---

# シンプレクティック群 $Sp(n)$

・$Sp(n)=\{A\in M(n,\bm{H})\ |\ AA^{\dag}=E\}$

## 位相的性質

・$GL(n,\bm{H})$ の閉部分群であって、$Sp(n)=dagt^{-1}(I)$

- コンパクト集合。

---

## 性質

<dl><dt>

・$$\forall A\in Sp(n)\text{ に対して、}\exist X\in Sp(n)\text{ であって、}\\\ \\
X^{-1}AX=\begin{pmatrix}
\ddots\\
& e^{i\theta_i}  \\
& & \ddots
\end{pmatrix}\quad(\theta_i\in\bm{R})$$

    ・固有値のこと。エルミート行列の話ではない。
    ・？、群と位相、付録

</dt><dd>

- 上記に加えて、
$$\alpha=\begin{pmatrix}
i\theta_1 &  \\
& \ddots \\
& & i\theta_m \\
\end{pmatrix}$$と定めると、
$$\exp\alpha=X^{-1}AX$$したがって、
$$u:I\to Sp(n)\\\ \\
u(A)=\exp (tX\alpha X^{-1})$$ は単位元 $E$ と $A$ を結ぶ道。


</dd></dl> 

---

### 球面 $S^n$ との関係

・
$$p:Sp(n)\to S_{\bm{H}}^{n-1}\\\ \\
p(A)=Ae_{n}$$と定める。
このとき、次の同相が誘導される。
$$Sp(n)/Sp(n-1)\cong S^{4n-1}$$

### 射影空間との関係

・
$$f:Sp(n)\to HP{n-1}\\\ \\
f(A)=AEA^{\dag}$$と定める。
このとき、次の同相が誘導される。
$$Sp(n)/(Sp(n-1)\times S^3)\cong HP(n-1)\ (\text{同相})$$

---

### 交代Hermite行列との関係

・交代Hermite行列 $A\in M(n,\bm{H})$ とする。
このとき、$\exp A\in Sp(n)$


## 具体的な $n$

### $n=1$

・明らかに$$Sp(1)\cong S_H^1\cong S^3$$