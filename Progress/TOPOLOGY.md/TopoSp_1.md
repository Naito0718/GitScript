- [位相空間](#位相空間)
  - [演算](#演算)
  - [基本近傍系](#基本近傍系)
    - [連続性と基本近傍系](#連続性と基本近傍系)
  - [開基](#開基)
  - [準開基](#準開基)
  - [稠密性](#稠密性)
  - [可算公理](#可算公理)
    - [第二可算](#第二可算)
    - [第一可算](#第一可算)
    - [可分](#可分)
  - [Lindelof空間](#lindelof空間)
  - [分離公理](#分離公理)
    - [$T1$](#t1)
    - [Hausdorff空間](#hausdorff空間)
    - [正則空間](#正則空間)
    - [正規空間](#正規空間)
  - [連結性](#連結性)
  - [連続性](#連続性)
  - [開写像](#開写像)
- [部分空間](#部分空間)
  - [写像](#写像)
  - [閉包](#閉包)
  - [保たれる位相的性質](#保たれる位相的性質)
    - [コンパクト性](#コンパクト性)
    - [局所コンパクト性](#局所コンパクト性)
    - [局所コンパクトHausdorff性](#局所コンパクトhausdorff性)
- [直積位相空間](#直積位相空間)
  - [位相](#位相)
  - [直積位相の性質](#直積位相の性質)
  - [連続写像](#連続写像)
- [フィルター](#フィルター)
        - [フィルターの性質](#フィルターの性質)
- [ネット](#ネット)
  - [前順序集合](#前順序集合)
  - [ネット](#ネット-1)
    - [ネットの性質](#ネットの性質)
  - [ネットの収束と堆積](#ネットの収束と堆積)
  - [位相的性質とネット](#位相的性質とネット)
  - [始位相](#始位相)
  - [第一可算空間と点列](#第一可算空間と点列)
    - [点列による特徴づけ](#点列による特徴づけ)
    - [点列コンパクト](#点列コンパクト)






# 位相空間

    ・開集合の和集合は非可算無限でよい

## 演算

 ・$\overline{A\cup B}=\overline{A}\cup\overline{B},\quad\overline{A\cap B}\subset \overline{A}\cap\overline{B}$

 - $\bigcup_{\lambda}\overline{A}_{\lambda}\subset\overline{\bigcup_{\lambda} A_{\lambda}}$

        ・左辺は閉集合とは限らない

 ---

・$(A\cap B)^i=A^i\cap B^i,\quad A^i\cup B^i\subset(A\cup B)^i$

- 開集合 $U\sub X$、$A\sub X$ とする。
このとき、$$U\cap A=\phi\Rightarrow U\cap\overline{A}=\phi$$


---

## 基本近傍系

・基本近傍系 $\mathcal{N}_F(x)$ が与えられているとする。
 このとき、
 $O\in\mathcal{O}\iff \forall x\in O{に対して、}\exist U_x\in\mathcal{N}_F(x){であって、}U_x\subset O$

 - 位相空間 $X$ に対して、
$$\mathcal{N}_F(x)\text{が基本近傍系}\\\ \\
\iff\begin{cases}
U\in\mathcal{N}_F(x)\Rightarrow x\in U    \\
U,V\in\mathcal{N}_F(x)\Rightarrow\exist W\in\mathcal{N}_F(x);\ W\subset U\cap V \\
U\in\mathcal{N}_F(x),y\in U\Rightarrow\exist V\in\mathcal{N}_F(y);V\subset U\\
\end{cases}$$

       ・基本近傍系の要素は開集合。

---

### 連続性と基本近傍系

<dl><dt>

・位相空間 $X,Y$、基本近傍系 $\mathcal{U}_X(x),\ \mathcal{U}_Y(y)$ とする。

</dt><dd>

- $$\forall x\in X,\ \forall U\in\mathcal{U}_Y(f(x))\text{ に対して、}\exist V\in\mathcal{U}_X(x)\text{ であって、}\\
f(V)\sub U\\\ \\
\iff f\text{ は連続}\\\ \\$$

- $$\forall x\in X,\ \forall V\in\mathcal{U}_X(x)\text{ に対して、}\exist U\in\mathcal{U}_Y(f(x))\text{ であって、}\\
U\sub f(V)\\\ \\
\iff f\text{ は開写像}$$


</dd></dl> 


---

## 開基

 ・第二可算空間はLindelof空間。

    ・任意の開被覆に対して可算個の部分被覆を取れる。

 - 第二可算空間は可分。

 ---

## 準開基

 ・位相 $\mathcal{O}$ に対して、
 準開基 $\mathcal{J}$ ：
 $$\forall O\in\mathcal{O},\ \forall x\in O\ {に対して、}\\\ \\
 \exist J_1,...,J_n\in\mathcal{J}\ {であって、}x\in J_1\cap...J_n\ {かつ}\ J_1\cap...\cap J_n\subset O$$

 - 準開基 $\mathcal{J}$ に対して、
 $$\mathcal{B}=\{J_1\cap...\cap J_n\ |\ n\in\bm{N},\ J_i\in\mathcal{J}\}$$は開基。

       ・有限個の共通部分。

 ---

## 稠密性

 ・高々可算な集合 $M$ であって、$\overline{M}=X$

    ・部分集合なら不等号。

 - $A\subset X$ が可分ならば、$\overline{A}$ も可分。

 - 可分な集合列 $A_{n}$ に対して、
 $\bigcup_{n}A_{n}$ は可分。


---

・可分な位相空間 $X$、位相空間 $Y$、連続写像 $f:X\to Y$ とする。
このとき、$f(X)$ は可分。

- 位相空間 $X$、Hausdorff空間 $Y$、$\overline{M}=X$ なる部分集合 $M$、$f(x)=g(x)\ (\forall x\in M)$ なる連続関数 $f,g:X\to Y$ とする。
 このとき、$$f=g$$

 ---

・可分かつ第一可算$\Rightarrow$第二可算。

---

## 可算公理

### 第二可算

・位相空間 $X$ に対して、
第二可算：$X$ は高々可算な開基を持つ。

- 第二可算$\Rightarrow$可分かつLindelof空間


- 可分かつ第一可算$\Rightarrow$第二可算

---

### 第一可算

・位相空間 $X$ に対して、
第一可算：$X$ は各点で高々可算な基本近傍系を持つ。

---

### 可分

・位相空間 $X$ に対して、
可分：$\exist \text{ 高々可算な集合 }A\sub X\text{ であって }X=\overline{A}$ 

---

## Lindelof空間

・位相空間 $X$ に対して、
Lindelof空間：任意の開被覆 $X=\bigcup \mathcal{U}$ に対して、高々可算な部分被覆 $\mathcal{U}_0\sub\mathcal{U}$ が存在する。$X=\bigcup\mathcal{U}_0$$

---

## 分離公理

### $T1$

・位相空間 $X$ に対して、
$T_1$：$$\forall x\in X\text{ に対して、}\{x\}\text{ は閉集合}$$

- 位相空間 $X$ に対して、
$X\text{ は }T_1\iff \forall x\in X\text{ に対して、}\bigcap\{N\ |\ N\text{ は }x\text{ の近傍 }\}=\{x\}$

---

### Hausdorff空間

<dl><dt>

・Hausdorff空間 $X$、コンパクト集合 $A\sub X$ とする。

</dt><dd>

- $A$ は $X$ の閉集合。
<br>

- $x\in A^c$ とする。
このとき、
$$\exist\text{ 開集合 }U,V\sub X\text{ であって、}x\in U,\ A\sub V,\ U\cap V=\phi\\\ \\$$

- コンパクト集合 $A,B\sub X$、$A\cap B=\phi$ とする。
このとき、$$\exist\text{ 開集合 }U,V\sub X\text{ であって、}A\sub U,\ B\sub V,\ U\cap V=\phi$$


</dd></dl>

---

### 正則空間

・正則空間 $X$ ：$$\begin{cases}
 T_1    \\
 {閉集合}\ F,\ x\in F^c\  {に対して、}\ x\in U,\ F\subset V,\ U\cap V=\phi\  {なる開集合}\  U,V {が存在する。}      \\
 \end{cases}$$ 

- 位相空間 $X$ に対して、
$X$ が正則空間$\iff x\in X, U\in\mathcal{N}(x)$ に対して、$x\in V\subset\overline{V}\subset U$ なる開近傍 $V$ が存在する。
<br>

- 正則空間$\Rightarrow$Hausdorff空間

---

---

### 正規空間

---

## 連結性

 ・連結な空間：
 $X=O_1\cup O_2,\ O_1\cap O_2=\phi$ なる開集合が存在するならば、
 $O_1=\phi$ または $O_2=\phi$

    ・連結集合のときは、 「A⊂O_1∪O_2,A∩O_1∩O_2=φ、A∩O_1,A∩O_2が共に空でない」 でもよい
    ・空集合は連結でないとする

 - $x\in X$ に対して、一点集合 $\{x\}$ は連結

 - 連結な集合族 $A_{\lambda}\subset X$ であって、$A_{\lambda}\cap A_{\lambda'}\neq\phi$ とする。
 このとき、$\bigcup A_{\lambda}$ は連結。
 - 連結部分集合 $A\subset X$ に対して、
 $A\subset B\subset\overline{A}$ なる $B\subset X$ は連結。

---

 ・連結成分：同値関係 $$x\sim y\iff \exist\ {連結な集合}\ A {であって、} x,y\in A$$ による同値類。

 - $x$ の連結成分 $C(x)$ は $x$ を含む最大の連結部分集合。

 - 連結成分は閉集合。

---

 ・連結な位相空間 $X$、位相空間 $Y$、連続写像 $f:X\to Y$ について、$f(X)$ は連結。

---

## 連続性


 ---
## 開写像



 ---

# 部分空間

## 写像

・位相空間 $X,Y$、部分空間 $A\subset X$、 連続写像 $f:X\to Y$ とする。
このとき、$$f|_A:A\to Y$$は連続写像。

- 包含 $i:A\to X$ は連続写像。

## 閉包

・位相空間 $X$、部分空間 $A\sub X$、$B\sub A$ とする。
このとき、$$\overline{B}_{A}=\overline{B}\cap A$$

    ・Aでの閉包とXでの閉包。

---

## 保たれる位相的性質

 → 第一可算、第二可算、可分
 - $T_1$、ハウスドルフ、正則、正規

 ---

 ・距離空間の部分空間

 →距離 $d$を $W$ 上に制限しただけ

 →$W$ 上の開球：$B(x,r)\cap W$

 ---

### コンパクト性

・位相空間 $X$、$A,K\sub X$ とする。
このとき、
$$K\text{ は }A{ の相対位相でコンパクト}\iff K\text{ は }X\text{ でコンパクト}$$

---

### 局所コンパクト性

・局所コンパクト空間 $X$、閉集合 $F\sub X$ とする。
このとき、$F$ は局所コンパクトな部分空間。

### 局所コンパクトHausdorff性

・局所コンパクトHausdorff空間の開集合は、局所コンパクトHausdorff空間。

    ・別に閉集合も局所コンパクトHausdorff

---
---
---

# 直積位相空間

## 位相

・位相

    位相を定義する開基：各射影の全共通部分、非可算個、可算無限個なら有限和
    有限個のとき、（各射影空間の開集合の直積）=（位相を定義する開基）

<dl><dt>

・$X,Y$ の基本近傍系 $\mathcal{N}_{F;X}(x),\ \mathcal{N}_{F;Y}(x)$ が与えられているとする。
このとき、$$\mathcal{N}_{F;X\times Y}(x,y)=\{U\times V\ |\ U\in\mathcal{N}_{F;X}(x),V\in\mathcal{N}_{F;Y}(y)\}$$ は直積空間 $X\times Y$ の基本近傍系をなす。

</dt><dd>

- 射影 $p:X\times Y\to X$ は連続全射な開写像。

- $A\sub X,B\sub Y$ とする。
このとき、 $$\overline{A\times B}=\overline{A}\times\overline{B}$$

- 
$$(A\times B)^C=(A^C\times Y)\cup(X\times B^C)\\\ \\
(A_1\times A_2)\cap(B_1\times B_2)=(A_1\cap B_1)\times(A_2\cap B_2)$$


</dd></dl> 


---

## 直積位相の性質

・第二可算

    ・可算個の第二可算直積空間は第二可算

・ハウスドルフ

    ・有限個の直積空間はハウスドルフ

・コンパクト空間の族 $X_{\lambda}$ に対して、
 $\Pi_{\lambda}X_{\lambda}$ はコンパクト空間。

・位相空間の族 $X_{\lambda}$ に対して、
 $\Pi_{\lambda}X_{\lambda}$ が連結空間$\iff X_{\lambda}$ は連結。

---

・局所コンパクト空間　$X,Y$ に対して、
$X\times Y$ は局所コンパクト。

・完備距離空間 $X,Y$ に対して、
$X\times Y$ は完備距離空間。

---

## 連続写像

・位相空間 $X_1,X_2,Y_1,Y_2$、連続写像 $f_i:X_i\to Y_i$ とする。
このとき、$$f:X_1\times X_2\to Y_1\times Y_2,\quad f(x_1,x_2)=(f_1(x_1),f_2(x_2))$$は連続写像。

- 同相な位相空間 $X_1\cong Y_1,X_2\cong Y_2$ に対して、
$$X_1\times X_2\cong Y_1\times Y_2$$

---

・位相空間 $X_1,...,X_n,Y$、連続写像 $g_i:X_i\to Y$ とする。
このとき、
$$f:X_1\times...\times X_n\to Y\\\ \\
f(x_1,...,x_n)=(x_1,...,g(x_i),...,x_n)$$は連続。

    ・固定も含む。
    ・各成分固定した奴が連続でも、全体が連続とは限らない！！！

- 位相空間 $X_1,...,X_n,Y$、$x_j\in X_j\ \ (j\neq i)$ とする。
このとき、
$$f:X_i\to X_1\times...X_n\\\ \\
f(x_i)=(x_1,...,x_i,...,x_n)$$は連続。
 

---
---
---

# フィルター

 ・集合 $X$ に対して、
 フィルター $\mathcal{F}\subset 2^X$：
 $$X\in\mathcal{F},\ \phi\notin \mathcal{F}\\\ \\
 \forall F_1,F_2\in\mathcal{F}\ {に対して、} F_1\cap F_2\in\mathcal{F}\\\ \\
 \forall F\in\mathcal{F},\forall F\subset G\subset X\ {に対して、}G\in\mathcal{F}$$

 - 集合 $X$、フィルター $\mathcal{F},\mathcal{G}$ に対して、
 細分、両立：
 $$\mathcal{F}\subset\mathcal{G}\\\ \\\ \forall F\in\mathcal{F},\forall G\in\mathcal{G}\ {に対して、}F\cap G\neq\phi\\\ \\$$

 - 集合 $X$、フィルター $\mathcal{U}$ に対して、
  超フィルター $\mathcal{U}$：$$\forall A\subset X\text{ に対して、}A\in\mathcal{U}\text{ または }A^c\in\mathcal{U}\\\ \\
  \iff(\forall )F\cup G\in\mathcal{U}\text{ に対し、}F\in\mathcal{U}\text{ または }G\in\mathcal{U}\\\ \\
  \iff\mathcal{U}\text{ は自分以外の細分を持たない}$$

       ・非単項超フィルター、自由超フィルター：単項でない超フィルター
    
 ---
##### フィルターの性質

 ・ フィルターは有限交叉性を持つ。

 ・任意のフィルターに対して、その細分となる超フィルターが存在する。

    ・極大性
    ・フィルターFの細分全体は帰納的順序集合

 ---
 ---
 ---

# ネット

## 前順序集合

・集合 $\Lambda$、$\lambda\in \Lambda$ とする。
このとき、前順序集合 $(\Lambda,\le)$：$$\lambda\le\lambda,\quad\lambda_1\le\lambda_2,\ \lambda_2\le\lambda_3\Rightarrow\lambda_1\le\lambda_3$$

・前順序集合 $(\Lambda,\le)$ が有向：
$$\forall\lambda_1,\lambda_2\ {に対して、}\exist\lambda\ {であって、}\lambda_1\le\lambda,\ \lambda_2\le\lambda$$

---

## ネット

<dl><dt>

・集合 $X$、有向集合 $(\Lambda,\le)$ とする。
このとき、ネット： $x_{\lambda}:\Lambda\to X$

    ・有向集合を添え字集合とする写像。
    ・有向集合が自然数 N なら点列。
<br>

</dt><dd>

- 集合 $X$、有向集合 $(\Lambda,\le_{\lambda}),\ (M,\le_\mu)$、ネット $x_{\lambda}:\Lambda\to X$、$\phi:M\to\Lambda$ とする。
このとき、部分ネット $(x_{\phi(\mu)})_{\mu\in M}$：
$$(x_{\phi(\mu)})_{\mu\in M}:M\to X\text{であって},\\\ \\
\forall\lambda\in\Lambda\ {に対して、}\exist\mu_0\in M\ {であって、}\\
\forall\mu\ge\mu_0\Rightarrow\phi(\mu)\ge\lambda\text{ を満たす。}$$

      ・自然数の部分列はk(1)<k(2)<k(3)...で定義される。
      ・点列の部分ネットは部分列とは限らない。
<br>

- 集合 $X$、$A\sub X$、有向集合 $(\Lambda,\le)$、ネット $(x_{\lambda})$ とする。
このとき、eventually in, frequently in：
$$\mathrm{EV}:\ \exist\lambda_0\in\Lambda\ {であって、}\forall\lambda\ge\lambda_0\Rightarrow x_{\lambda}\in A\\\ \\
\mathrm{FR}:\ \forall\lambda\in\Lambda\ {に対して、}\exists\lambda_0\ge\lambda\ {であって、}x_{\lambda_0}\in A\\\ \\$$

- 集合 $X$、有向集合 $(\Lambda,\le)$、ネット $(x_{\lambda})$ とする。
このとき、普遍ネット $x_{\lambda}$：
$$\forall A\subset X\ {に対して、}\\\ \\
x_{\lambda}\  \text{is eventually in}\  A\text{ または }x_{\lambda}\text{ is frewuently in }A^c$$

      ・普遍部分ネット：ネットの部分ネットで、普遍性を持つもの。（元のネットは普遍でなくてよい）

</dd></dl>

---
 
### ネットの性質

・集合 $X$、$X$ のネット $x_{\lambda}$、集合の逆包含関係による有向集合 $\mathcal{B}$ とする。
このとき、
$$\forall B\in \mathcal{B}\text{ に対して } x_{\lambda}\text{ is frequently in }B\Rightarrow\\\ \\
\exist\text{部分ネット } x_{\phi(\mu)}\text{ であって、}\forall B\in\mathcal{B}\text{ に対して}\\
x_{\phi(\mu)}\text{ is eventually in } B$$
<br>

- 任意のネットに対して、普遍部分ネットが存在する。

      ・以下のネットに対するフィルター参照。

---

・集合 $X$、$X$ のネット $(x_{\lambda})$ とする。
このとき、ネット $(x_{\lambda})$ に対するフィルター $\mathcal{F}_{x_{\lambda}}$：
$$\mathcal{F}_{x_{\lambda}}\text{ はフィルターであって、} F\in \mathcal{F}_{x_{\lambda}}\Rightarrow x_{\lambda}\text{ is frequently in }F\\\ \\$$


- $X\in\mathcal{F}_{x_{\lambda}}$
<br>

- ネットに対するフィルター全体は、帰納的順序集合。
つまり、極大フィルターが存在する。

---

## ネットの収束と堆積

    ・fは連続⇔xに収束する任意のネットx_λに対して、ネットf(x_λ)はf(x)に収束する

<dl><dt>

・位相空間 $X$、$X$ のネット $(x_{\lambda})$、$x\in X$ とする。
このとき、収束点、堆積点 $x$：
$$\text{収}:\forall V\in\mathcal{N}(x)\text{ に対して、}x_{\lambda}\text{ is eventually in }V\\\ \\
\text{堆}:\forall V\in\mathcal{N}(x)\text{ に対して、}x_{\lambda}\text{ is frequentry in }V\\\ \\$$

</dt><dd>

- 位相空間 $X$、$X$ のネット $(x_{\lambda})$、$x\in X$ とする。
このとき、
$$x\text{ は }x_{\lambda}\text{ は堆積点}\\\ \\
\iff \exist\text{ 部分ネット }x_{\phi(\mu)}\text{ であって、}x\text{ は }x_{\phi(\mu)}\text{ の収束点}\\\ \\$$

- 位相空間 $X$、$A\sub X$、$x\in X$ とする。
このとき、
$$x\in\overline{A}\\\ \\
\iff\exist\text A{ のネット }x_{\lambda}\text{ であって、}x\text{ は }x_{\lambda}\text{ の収束点}\\\ \\$$

- 位相空間 $X,Y$、$x\in X$、$f:X\to Y$ とする。
このとき、
$$f\text{ は }x\text{ で連続}\\\ \\
\iff\forall\text x\text{ に収束する }X{ のネット }x_{\lambda}\text{ に対して、}\\
f(x)\text{ は }Y\text{ のネット }f(x_{\lambda})\text{ の収束点}$$

</dd></dl>

---

## 位相的性質とネット

 ・位相空間 $X$ に対して、
 $X$ はハウスドルフ空間$\iff$任意の収束するネット $x_{\lambda}$ に対し、収束値が一意的

 --- 

## 始位相

    ・直積位相の一般化
    ・準開基を定めてる

 ・空でない集合 $X$、添え字付けられた位相空間と写像の族 $(Y_j,\mathcal{O}_j),\ f_j:X\to X_j$ に対して、
 $(f_j:X\to X_j)_{j\in J}$ から誘導される始位相： $$\left\{\bigcap_{i=1}^n f_{j_i}^{-1}(U_i)\ |\ n\in\bm{N},j_0,...,j_n\in J,U_i\in\mathcal{O}_{j_i}\right\}$$の要素の和集合で表される集合全体 

 - 各 $f_j$が連続になるような最弱の位相
 - 始位相 $(f_j:X\to X_j)_{j\in J}$ が入った集合 $X$ に対して、
  $x_{\lambda}\to x\iff f_j(x_{\lambda})\to f_j(x)\ (\forall j)$

 ---

## 第一可算空間と点列

 ・$x\in X$が可算な基本近傍系を持つならば、
 $$\forall V\in\mathcal{N}(x)\text{ に対して、}\exist n\in\bm{N}\text{ であって、}\\\ \\
 B_n\subset V,\quad B_{n+1}\subset B_{n}$$
 を満たす $x$ の近傍列 $B_n$ が存在する

 ---

### 点列による特徴づけ

 ・第一可算空間 $X$、点列 $x_n\subset X$、$x\in X$ に対して、
 $x$ は $x_n$ の堆積点$\iff x_n$ の部分列で $x$ に収束するものが存在する

 - 第一可算空間 $X$、$A\subset X$、$x\in X$ に対して、
 $x\in\overline{A}\iff x$ に収束する $A$　の点列が存在する
 <br>

 - 第一可算空間 $X$、位相空間 $Y$、$f:X\to Y$、$x\in X$ に対して、
 $f$は連続$\iff x$ に収束する任意の点列 $x_n$ に対して、$f(x_n)$ は $f(x)$ に収束する

 ---

### 点列コンパクト

・位相空間 $X$ に対して、
 点列コンパクト：$X$ の任意の点列 $x_n$ が収束する部分列を持つ。

・位相空間 $X$ に対して、
Lindelof空間：$X$ の任意の開被覆 $X=\bigcup U_{\lambda}$ が高々可算個の部分被覆を持つ：$X=\bigcup U_n$

- 第二可算空間はLindelof空間

- 点列コンパクトなLindelof空間は、コンパクト

- 第一可算なコンパクト空間は、点列コンパクト

- 第二可算空間$X$に対して、
 $X$がコンパクト$\iff X$が点列コンパクト

---
---
---

