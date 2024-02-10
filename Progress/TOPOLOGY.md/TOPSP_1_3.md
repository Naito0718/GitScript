
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

