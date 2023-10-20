- [一章](#一章)
  - [測度論の基礎](#測度論の基礎)
        - [σ-集合族](#σ-集合族)
        - [可測関数](#可測関数)
        - [Borel集合族](#borel集合族)
- [二章](#二章)
  - [実数値可測関数](#実数値可測関数)
        - [拡張実数](#拡張実数)
        - [$R,C,R^n$値関数](#rcrn値関数)
        - [可測関数のなすベクトル空間](#可測関数のなすベクトル空間)
  - [測度と積分](#測度と積分)
        - [非負値可測単関数の積分](#非負値可測単関数の積分)
        - [非負値可測関数の積分](#非負値可測関数の積分)
        - [実数値可測関数の積分](#実数値可測関数の積分)
        - [複素数値可測関数の積分](#複素数値可測関数の積分)
        - [測度論の基本定理](#測度論の基本定理)
- [有限加法的測度](#有限加法的測度)
  - [半集合代数、有限加法族、単調族、σ-有限性](#半集合代数有限加法族単調族σ-有限性)
        - [有限加法的測度、σ-加法的測度、σ-有限測度](#有限加法的測度σ-加法的測度σ-有限測度)
        - [Caratheodory外測度](#caratheodory外測度)
        - [Tonelliの定理、Fubiniの定理](#tonelliの定理fubiniの定理)


# 一章

## 測度論の基礎

##### σ-集合族

・$\sigma-$加法族 $\mathfrak{M}$ 、可測空間 $(X,\mathfrak{M})$ 、可測集合 $E\in\mathfrak{M}$（↔位相、位相空間、開集合）

    ・全体、補集合、可算和（定義）
    ・φ、可算積、有限和、有限積、引き算∊M

→$\bigcap\mathfrak{M_i}$は非可算でも$\sigma$-加法族

    ・和集合は無理

---

##### 可測関数

・可測関数：$f^{-1}(\forall E_2)\in\mathfrak{M}_1$

    ・連続関数の定義に近い

- 可測関数の合成は可測関数

---

##### Borel集合族

・Borel集合族 $\mathfrak{B}$、Borel集合 $E\in\mathfrak{B}$

    ・位相Oから生成されるσ加法族

・Borel写像 $f$

    ・可測関数と同じ

- 連続関数はBorel写像

・Borel測度：可測空間(Y,B_Y)上の測度

---
---
---

# 二章

## 実数値可測関数 
$$\bm{f:X\to [-\infty,\infty],\mathbb{R},\mathbb{C},\mathbb{R}^N}$$

##### 拡張実数
$$\bm{[-\infty,\infty]=\mathbb{R}\cup\{-\infty,\infty\}}$$

    （複素数の一点コンパクト化ではない）

・順序

    ・全順序性を満たす
    ・最小限：-∞、最大限+∞
    ・任意の空でない部分集合は上限と下限を持つ。

・区間の再定義$[a,b],(a,b),[a,b)$（$\pm\infty$も含む）

・演算

    ・∞とR、-∞とRの可換和、0との可換積、-(-∞)、正数と∞、-∞、負数と∞、-∞の積
    ・0の累乗、∞の累乗

・絶対値$|a|$（$\pm\infty$も含む）

・総和$\sum_{j\in J}x_j=\sup_{F\in\mathcal{F}_J}\sum_{j\in F}x_j\in[0,\infty]$（$J$は空でない集合、$\mathcal{F}_J$は$J$の空でない有限部分集合全体で包含による有向集合）

    ・実数Rの有界な単調増加ネットは上限に収束する（今有界は外してよい）
    ・この定義は一般のノルム空間におけるネットの定義と矛盾しない（実数Rの時も含めて）

---

・Borel集合族$\mathcal{B}_{[-\infty,\infty]}$

→区間（開、閉、半開）を含む集合全体から生成されるσ加法族
→$\sigma(\bm{R})=\mathcal{B}(\bm{R})$
→開区間だけ、閉区間だけ、両半開区間だけでもべつによい（開基による）（拡張実数での閉区間は半開区間だし、どうせ補集合も含まれる）

---

・$[-\infty,\infty]$値関数の可測性

    ・f可測⇔任意の実数aに対し(a<f)が可測集合⇔(a≦f)が可測集合⇔(a>f)が可測集合⇔(a≧f)が可測集合
    ・

・$f_{\pm}:x\mapsto\max\{\pm f(x),0\}\in[0,\infty]$

    ・f=f_+-f_-、|f|=f_+ +f_-
    ・

---

##### $R,C,R^n$値関数

・可測性

    ・それぞれのBorel集合族に対して可測であること
    ・実数Rについては拡張実数[∞-,∞]における可測性と矛盾しない
    ・R^n、複素数Cについては、各成分が可測であることと同値

・可測関数$f:X\to [-\infty,\infty]$における演算

    ・任意実数倍は可測、したがって複素数倍も可測
    ・和は可測（定義できれば）
    ・有限個の可測関数のmax、minは可測
    ・可測関数列のsup、infは可測
    ・f_+、f_-、|f|、|f|^p（pは非負実数）は可測
    ・複素数値関数において、積は可測

- 可測関数列 $f_n:X\to[-\infty,\infty]$ に対して、その上極限、下極限は可測。よって、各点収束先 $f_n\to f$ も可測

---

・指示関数$\chi_E:X\to \mathbb{R}\ (E\subset X)$

    ・可測集合の指示関数は可測

---

##### 可測関数のなすベクトル空間 
$$\bm{\mathcal{L}(X,\mathfrak{M})=\{f:X\to\bm{C}\ |\ f{は可測}\}}$$

・可測単関数のなすベクトル空間
$$\mathcal{S}(X,\mathfrak{M})=span\{\chi_E |\ E\in\mathfrak{M}\}$$

→ $S(X,M)=\{f→\bm{C}は可測かつ、f(X)は有限集合\}$

---

・任意の非負値可測関数 $f:X\to[0,\infty]$ に対し、
$$f_n(x)=\sum_{k=1}^{n2^n}\frac{k-1}{2^n}\chi_{\frac{k-1}{2^n}\le f\le\frac{k}{2^n}}(x)+n\chi_{n\le f}(x)$$
と定義する。（非負値単関数単調増加列近似）

→ $f_n$は可測単関数
→ $f_n$は任意の $x$ に対して単調増加列
→ $f(x)=\sup f_n(x)$

---

## 測度と積分

・集合列

    ・単調増加列、単調減少列、非交叉列

・測度$\mu:\mathfrak{M}\to[0,\infty]$、測度空間

→ $\mu(\phi)=0,\ \mu(\bigcup E_i)=\sum\mu(E_i)\ ({非交叉})$

→非交叉列の有限加法性
→任意列の劣σ加法性
→任意列の劣有限加法性
→任意の単調増加列のsup収束性
→任意の単調減少列のinf収束性（$μ(E_1)<∞$）
→$B⊂A$ ならば、$μ(A-B)=μ(A)-μ(B)$

---

・測度$\mu$の可測集合への制限

→相対σ加法族に対してそのまま測度を用いればよい

---

・可測分割

    ・有限可測分割⇔有限個の非交叉列で、全体集合Xを被覆するもの
    ・可算可測分割⇔可算個の非交叉列で、全体集合Xを被覆するもの

・$\mu-$零集合（$\mu(N)=0, N$は可測）

→ $\mu-$a.e.$x\in X$で$P(x)$が成り立つ$\iff$$\exists N(\mu-{零集合}){であって}\forall x\in X-N{に対して}P(x)$が成り立つ

---

##### 非負値可測単関数の積分

・定義

    ・有限可測分割による指示関数のスカラー倍の和
    ・well-defined（別の表し型でも値が等しい、値が一意的）
    ・正

・性質

    ・非負斉次性
    ・加法線形
    ・単調性

・$g$を非負値可測単関数、$f_n$を非負値可測単関数の単調増加列とし、$g\le\sup f_n$とする。このとき、$\int_X gd\mu\le\sup\int_X f_nd\mu$

---

##### 非負値可測関数の積分
$$\bm{f:X\to[0,\infty]}$$

・定義

    ・非負値可測単関数（≦f）によるsup
    ・非負値可測単関数の定義と整合する
    ・値は一意的、正

・性質

    ・単調性
    ・非負値可測単関数の単調増加列における、積分とsupの交換
    ・非負斉次性
    ・加法線形
    ・非負値可測関数の単調増加列における、積分とsupの交換（単調収束定理）

・$\int_X\infty fd\mu=\infty\int_X fd\mu$（$\sup n$考えればよい）

・$f_n$を非負値可測関数の列とすると、$\int_X\sum_{n\in\bm{N}}f_nd\mu=\sum_{n\in\bm{N}}\int_Xf_nd\mu$

・$\mu$-零集合$N$

    ・非負値可測関数fに対して、fχ_Nの積分は0
    ・非負値可測関数fに対して、積分0⇔μ-a.e.x∊Xでf(x)=0
    ・非負値可測関数fに対して、積分が有限(<∞)⇔μ-a.e.x∊Xでf(x)は有界(<∞)

---

##### 実数値可測関数の積分

・$\mu$-可積分

    ・絶対値とったやつの積分が有限
    ・f_+,f_-の積分がともに有限、可積分であることと同値

・定義$\int_X fd\mu=\int_Xf_+d\mu-\int_Xf_-d\mu\ (f:X\to\bm{R})$

    ・fが非負値可測関数であるときと整合する（f_-=0）

・実数値可測関数空間$\mathcal{L}_{\bm{R}}^1(X,\mathfrak{M},\mu)=\{f\in\mathcal{L}_{\bm{R}}(X,\mathfrak{M})\ |\ f{は}\mu{-可積分}\}$

    ・実数R上ベクトル空間
    ・∫:L→RはR上線形写像（可積分関数に対する積分の線形性）

---

##### 複素数値可測関数の積分

・$\mu$-可積分

    ・絶対値とったやつの積分が有限
    ・Ref,Imfの積分がともに有限、可積分であることと同値

・定義$\int_X fd\mu=\int_X\mathrm{Re} (f)d\mu+i\int_X\mathrm{Im}(f)d\mu\ (f:X\to\bm{R})$

    ・fが実数値関数であるときと整合する

・複素数値可測関数空間$\mathcal{L}^1(X,\mathfrak{M},\mu)=\{f\in\mathcal{L}_{\bm{R}}(X,\mathfrak{M})\ |\ f{は}\mu{-可積分}\}$

    ・複素数C上ベクトル空間
    ・∫:L→CはC上線形写像（可積分関数に対する積分の線形性）
    ・積分不等式

・$\mu$-零集合$N$において、$\mu-a.e.x\in X{で}f(x)=0\iff\int_X |f|d\mu=0\iff {任意の可測集合}E{に対して、}\int_X f\chi_E d\mu=0$

---

##### 測度論の基本定理

・非負値可測関数列 $f_n$ に対して、
$$\int_X\sup_{n\in\bm{N}}\inf_{k\ge n} f_kd\mu\le\sup_{n\in\bm{N}}\inf_{k\ge n} \int_X f_kd\mu$$
<br>

・$f_n$を複素数値可測関数の列とし、$\forall x\in X{で}f=\lim f_n\in\bm{C}$かつ、
非負値可積分関数であって$\forall n\in\bm{N},\forall x\in X{で}|f_n(x)|\le h(x)$を満たすものが存在するとする。
このとき、$f,f_n$は可積分であって、
$$\int_X fd\mu=\lim_{n\to\infty}\int_X f_nd\mu$$

    ・優収束定理

---
---
---

# 有限加法的測度

## 半集合代数、有限加法族、単調族、σ-有限性

・空でない集合 $X$、$\mathcal{I}\sub 2^X$ とする。このとき、半集合代数 $\mathcal{I}$：
$X,\phi\in X\\\ \\
\forall$$

    ・全体Xとφ含む、A,B含めばA∩B含む、A^cは互いに交わらないIの要素の有限和（定義）
    ・半集合代数Iから生成される有限加法族A(I)={互いに交わらないIの要素の有限和}

---

・有限加法族 $\mathcal{F}$

    ・σ加法族の有限和バージョン

→$E,F\in\mathcal{F}\Rightarrow E\cap F,E-F\in\mathcal{F}$

→有限加法族ならば半集合代数

→有限加法族$\mathcal{F}$に対して、$\sigma(\mathcal{F})=\mathcal{M}(A)$

---

・単調族$\mathcal{M}$

    ・M上の任意の単調増加列に対して合併含む
    ・M上の任意の単調減少列に対し共通部分含む

・$\mathfrak{M}$が$\sigma$-集合族$\iff\mathfrak{M}$は有限加法族かつ単調族

・生成される有限加法族$\mathcal{A}(\mathcal{I})$、単調族$\mathcal{M(I)}$

    ・有限加法族：Iを含む有限加法族のすべての交叉
    ・単調族：Iを含む単調族すべての交叉
    ・ともにIを含む最小のもの

---

##### 有限加法的測度、σ-加法的測度、σ-有限測度

・有限加法的測度、$\sigma$-加法的測度$\mu_0:\mathcal{I}\to[0,\infty]\ (\mathcal{I}{は半集合代数})$

    ・φで0、μ(有限個の互いに交わらない和集合)=∑(有限和) （定義）
    ・σ加法性：非交叉列で和集合がIに含まれるならば、μ（非交叉列の無限和）＝Σ(無限和)
    ・μ_0を有限加法的測度とすると、A(I)上の有限加法的測度に一意拡張できる。このときσ加法性も保たれる

・有限加法族$\mathcal{F}$上の有限加法的測度$\mu:\mathcal{F}\to[0,\infty]\ (\mathcal{A}{は有限加法族})$

- $A\subset B$ならば$\mu(A)\le \mu(B)$

- $A_1,...,A_n\subset\mathcal{F}$に対して$\mu(\bigcup A_i)\le\sum\mu(A_i)$

- $\sigma$-加法的測度ならば、集合列 $A_n,\ \bigcup A_n\in\mathcal{F}$ に対して$\mu(\bigcup A_n)\le\sum A_n$

---

・有限加法的測度に対する$\sigma$-有限性

    ・半集合代数Iの列C_nで、Iを被覆しμ(C_n)<∞（n任意）を満たすものが存在すること

---

・$\sigma$-有限測度$\mu:\mathcal{A}\to[0,\infty]\ (\mathcal{A}{は有限加法族})$

    ・Aの非交叉列A_nで、Xを被覆しμ(A_n)<∞（n任意）であるものが存在する
    ・Aの単調増加列A_nで、Xを被覆しμ(A_n)<∞（n任意）であるものが存在する

---

##### Caratheodory外測度
$$\mu^*:2^X\to[0,\infty],\ \mu^*(E)=\inf\{\sum_{n\in\bm{N}}\mu(A_n)\ |\ A_n\subset\mathcal{A},E\subset\bigcup A_n\},\\\ \mathfrak{M}
=\{A\in2^X\ |\ \mu^*(E\cap A)+\mu^*(E\cap A^c)=\mu^*(E),\ \forall E\in2^X\}$$　（$\mathcal{A}$は有限加法族、$\mu$は$\sigma$-加法的測度）

---

・$\mu^*(\phi)=0,\ \mu^*$は単調
・$\mu^*$は劣加法的
・$\mathfrak{M}$は$\sigma$-加法族
・$\mathfrak{M}$の任意の非交叉列$A_n$に対して、$\mu^*(E)=\sum_{n=1}^N\mu^*(E\cap A_n)+\mu^*(E-\bigcup_{n=1}^N A_n)\ (\forall E\in2^X,\forall N\in\bm{N})$
・$\mu^*:\mathfrak{M}\to[0,\infty]$は測度
・$\mathcal{A}\subset\mathfrak{M}$
・$\mu^*$は$\mu$の拡張

---

・$\mathcal{A}$を有限加法族、$\mu:\mathcal{A}\to[0,\infty]$を$\sigma$-加法的測度とする。このとき、$\mu$は$\sigma(\mathcal{A})$上の測度に拡張できる。さらに、$\mu$が$\sigma$-有限ならば拡張は一意的。（拡張定理）

---


##### Tonelliの定理、Fubiniの定理

・直積測度：$$\otimes_{j=1}^N\mu_j:\otimes\mathfrak{M}\to[0,\infty],\quad X_i,\mathfrak{M}_i,\mu_i\ (i=1,...,N){は}\sigma{-有限な測度})$$

- $$μ(E_1×...×E_n)=μ_1(E_1)...μ_N(E_N)$$を満たすものがただ一つ存在する（直積測度）

---

・$(X_i,\mathfrak{M}_i,\mu_i)\ (i=1,...,N)$を$\sigma$-有限な測度空間、$f:X_1\times...\times X_N\to[0,\infty]$を非負値可測関数とする。
このとき、$$\Phi:X_1\times...\times \tilde X_k\times...\times X_N\to[0,\infty],\\\ \\(x_1,...,\tilde x_k,...,x_N)\mapsto\int_{X_k}f(x_1,...,x_k,...,x_N)d\mu_k$$は可測関数である

・$(X_i,\mathfrak{M}_i,\mu_i)\ (i=1,...,N)$を$\sigma$-有限な測度空間、$f:X_1\times...\times X_N\to[0,\infty]$を非負値可測関数、$\tau$を$n$次の置換とする。
このとき、$$\int_{\prod_{k=1}^N X_k}fd\otimes_{j=1}^N\mu_j=\int_{X_{\tau(1)}}\left(...\left(\int_{X_{\sigma(N)}}f(x_1,...,x_N)d\mu_{\sigma(N)}\right)...\right)d\mu_{\sigma(1)}$$

    ・このとき累次積分の各被積分部分は意味を持つ
    ・Tonelliの定理

---

・$(X_1,\mathfrak{M}_1,\mu_1)\ ,(X_2,\mathfrak{M}_2,\mu_2)$を$\sigma$-有限な測度空間、$f\in\mathcal{L}(X_1\times X_2,\mathfrak{M}_1\otimes\mathfrak{M}_2,\mu_1\otimes\mu_2)$とする。

- $N_1=\{x_1\in X_1\ |\ \int_{X_2}|f|d\mu_2=\infty\}$は$\mu_1$-零集合
- $$F_1(x_1)=\begin{cases}
\int_{X_2}|f|d\mu_2 & (x_1\in X_1-N_1) \\
0 & (x_1\in N_1)
\end{cases}$$は$\mu_1$-可積分
- $$\int_{X_1\times X_2}fd(\mu_1\otimes\mu_2)=\int_{X_1}F_1d\mu_1$$

        ・fは複素数値可積分関数
        ・定理は対称に成り立つ

---





