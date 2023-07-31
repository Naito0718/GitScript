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
- [三章](#三章)
  - [有限加法的測度](#有限加法的測度)
        - [半集合代数、有限加法族、単調族、σ-有限性](#半集合代数有限加法族単調族σ-有限性)
        - [有限加法的測度、σ-加法的測度、σ-有限測度](#有限加法的測度σ-加法的測度σ-有限測度)
        - [Caratheodory外測度](#caratheodory外測度)
        - [Tonelliの定理、Fubiniの定理](#tonelliの定理fubiniの定理)
- [四章](#四章)
  - [複素数値測度での積分](#複素数値測度での積分)
        - [複素数値測度](#複素数値測度)
        - [実数値測度とHahn分解](#実数値測度とhahn分解)
        - [実数値測度とJordan分解](#実数値測度とjordan分解)
        - [絶対連続とRadon-Nikodymの定理、Radon-Nikodym微分](#絶対連続とradon-nikodymの定理radon-nikodym微分)
        - [複素数値測度に対する全変動とその積分](#複素数値測度に対する全変動とその積分)
- [五章](#五章)
  - [局所コンパクト空間 $X$ 上のRadon測度](#局所コンパクト空間-x-上のradon測度)
        - [Radon測度](#radon測度)
        - [Radon汎関数とRiesz-Markov-角谷の表現定理](#radon汎関数とriesz-markov-角谷の表現定理)
        - [第二可算性とRadon測度](#第二可算性とradon測度)
- [六章](#六章)
  - [Lebesgue測度](#lebesgue測度)
- [七章](#七章)
  - [Bochner積分](#bochner積分)


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

・可測関数$f^{-1}(\forall E_2)\in\mathfrak{M}_1$（↔連続関数）

→可測関数の合成は可測関数

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

# 三章

## 有限加法的測度

##### 半集合代数、有限加法族、単調族、σ-有限性

・半集合代数$\mathcal{I}$

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

# 四章

## 複素数値測度での積分

##### 複素数値測度
$$\bm{\nu:\mathfrak{M}\to\bm{C}}$$

・定義

    ・任意の非交叉列に対してν(∪)=∑(ν)

・性質

    ・φで0
    ・互いに交わらない有限個の可測集合について、ν(∪)=∑(ν)
    ・任意の単調増加列に対して、ν(∪)=lim(ν)
    ・任意の単調減少列に対して、ν(∪)=lim(ν)

・密度関数を持つ測度$\mu_f(E)=\int_E fd\mu$

    ・fが非負値可測関数なら、μ_fは測度
    ・fが実数値可積分関数なら、実数値測度
    ・fが複素数値可積分関数なら、複素数値測度

---

##### 実数値測度とHahn分解

・実数値測度$\nu$に関する非負な集合$P:\nu(E\cap P)\ge0(\forall E\in\mathfrak{M})$

    ・非正も同様
    ・非負な集合列E_nの合併∪E_nも非負

・実数値測度$\nu:\mathfrak{M}\to\bm{R}$の性質

    ・任意の可測集合Eと任意のε>0に対して、B⊂Aかつν(B)≧ν(A)かつν(E)≧-ε(∀E∈M,E⊂B)を満たす可測集合Pが存在する
    ・任意の可測集合Eに対して、νについて非負かつν(P)≧ν(A)を満たす可測集合Pが存在する
    ・sup(ν(E))は有限

・実数値測度$\nu:\mathfrak{M}\to\bm{R}$に対して、$X$の可測分割$P,N$でそれぞれ非負、非正であるものが存在する（Hahn分解）

    ・N=P^c

---

##### 実数値測度とJordan分解

・互いに特異な測度、または互いに特異な複素数値測度$\mu_1⊥\mu_2$

    ・可測分割A_1,A_2で、任意の可測集合Eに対してμ(E)=μ(E∩A_1)かつμ(E)=μ(E∩A_2)を満たすものが存在する

・実数値測度$\nu:\mathfrak{M}\to\bm{R}$に対して、有限測度（∞含まない）$\nu_+,\nu_-$の互いに特異な組で、$\nu=\nu_++\nu_-$を満たすものがただ一つ存在する（Jordan分解）

    ・Hahn分解A_+,A_-を用いてν_±(E)=±ν(E∩A_±)が成り立つ（Eは任意の可測集合）

---

##### 絶対連続とRadon-Nikodymの定理、Radon-Nikodym微分

・測度$\mu$に対して絶対連続な測度、または複素数値測度$\nu<<\mu$

    ・μで零集合ならνでも0 （定義）
    ・μ_fはμに対して絶対連続

・$(X,\mathfrak{M},\mu)$を有限測度空間、$\nu$を有限測度とすると、$\mu$-可積分な非負値可積分関数$f:X\to[0,\infty)$と有限測度$\lambda$で$\nu=\mu_f+\lambda$かつ$\lambda\perp\mu$を満たすものが存在する（Radon-Nikodymの定理）

    ・σ-有限測度空間、σ-有限な測度、非負値可測関数、σ-有限測度（可積分かはわからない）
    ・σ-有限測度空間、実数値測度、実数値可積分関数、実数値測度
    ・σ-有限測度空間、複素数値測度、複素数値可積分関数、複素数値測度

・$\sigma-$有限測度空間に対するRadon-Nikodym微分$f$

    ・σ-有限測度νがμに対して絶対連続ならば、μ-可測な非負値関数であってν=μ_fを満たすものが存在する
    ・実数値測度νがμに対して絶対連続ならば、μ-可積分な実数値関数であってν=μ_fを満たすものが存在する
    ・複素数値測度νがμに対して絶対連続ならば、μ-可積分な複素数値関数であってν=μ_fを満たすものが存在する
    ・f_1,f_2が共にνのμに対するRadon-Nikodym微分ならば、a.e.でf_1=f_2

---

##### 複素数値測度に対する全変動とその積分

・複素数値測度$\nu$に対する全変動$|\nu|:\mathfrak{M}\to[0,\infty]$

    ・|ν|(E)=sup(∑|ν(E_j)| E_jはEの有限可測分割) （定義）
    ・測度空間におけるμ-可積分関数fに対して、|μ_f|=μ_|f|
    ・複素数値測度νの全変動|ν|は有限測度で、複素数値測度νはその全変動|ν|に対して絶対連続
    ・実数値測度の全変動|μ|=μ_+ +μ_- （Jordan分解）

・複素数値測度$\nu$による積分$\int_X fd\nu=\int_X fhd|\nu|$

    ・hはνの|ν|に対するRadon-Nikodym微分で、a.e.|h|=1、|ν|-可積分
    ・fは|ν|-可積分


・$\mu_f$による積分$\int_Xgd\mu_f=\int_Xfgd\mu$

    ・非負値可測関数f:→[0,∞]、非負値可測関数g:→[0,∞]
    ・μ-可積分関数f、|μ_f|-可積分関数g（このとき、複素数値可測関数gに対して、gがμ_f-可積分⇔fgがμ-可積分）
    ・複素数値測度νと|ν|-可積分関数f、|ν_f|-可積分関数g、ν_fと複素数値測度νに関する積分（このとき、複素数値可測関数gに対して、gが|ν_f|-可積分⇔fgが|ν|-可積分）

---

# 五章

## 局所コンパクト空間 $X$ 上のRadon測度

・コンパクト集合$K$に対して、
$$K\prec f\iff f\in C_c(X),\ f:X\to[0,1],\ f(x)=1\ (\forall x\in K)$$

- 開集合 $U$に対して、
$$f\prec U\iff f\in C_c(X),\ f:X\to[0,1],\ suppf\subset U$$

- $K\subset U$なるコンパクト集合$K$と開集合$U$に対して、
$$K\prec f\prec U\iff f\in C_c(X),\ f:X\to[0,1],\ f(x)=1\ (\forall x\in K),\ suppf\subset U$$

- 任意の$K\subset U$なるコンパクト集合$K$と開集合$U$に対して、$K\prec f\prec U$なる$f$が存在する

        ・Urysohn

・開集合 $U_1\subset U_2$ に対して、
$f\prec U_1\Rightarrow f\prec U_2$

・コンパクト集合　$K_1\subset K_2$ に対して、
$K_2\prec f\Rightarrow K_1\prec f$

---

##### Radon測度
$$\bm{\mu:\mathfrak{B}_X\to[0\to\infty]}$$

・定義：局所コンパクトHausdorff空間 $X$ としたとき、

- 任意のコンパクト集合$K$に対して、$\mu(K)<\infty$

- $$\mu(E)=\inf\{\mu(V)\ |\ E\subset V{なる開集合}\}$$

        ・外部正則性

- $\mu(E)<\infty$または $E$ が開集合の時、
$$\mu(E)=\sup\{\mu(K)\ |\ K\subset E{なるコンパクト集合}\}$$

      ・内部正則性

---

・局所コンパクトHausdorff空間$X$、Radon測度 $\mu$ とする。

- $f\in C_c(X)\Rightarrow f$ は $\mu$-可積分
- 開集合 $V$ に対して、$$\mu(V)=\sup\{\int fd\mu\ |\ f\prec V\}$$
- コンパクト集合 $K$ に対して、$$\mu(K)=\inf\{\int fd\mu\ |\ K\prec f\}$$

---

##### Radon汎関数とRiesz-Markov-角谷の表現定理

・Radon汎関数：線形汎関数 $\Lambda: C_{c,\bm{R}}\to\bm{R}$ であって、$$\Lambda(f)\ge0\quad(f:0\to[0,\infty))$$

- $f(x)\le g(x)\ (\forall x\in X)$ なる $f,g\in C_{c,\bm{R}}$ に対して、 $\Lambda(f)\le\Lambda(g)$

        ・単調性

---

・局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda$ とする。

- $$\mu_0:\mathcal{O}_X\to[0,\infty],\quad\mu_0(V)=\sup\{\Lambda(f)\ |\ f\prec V\}$$


- $$\mu^*:2^X\to[0,\infty],\quad \mu^*(E)=\inf\{\mu_0(V)\ |\ E\subset V\in\mathcal{O}_X\}$$
 
- $$\mathfrak{M}_f=\{E\in2^X\ |\ \mu^*(E)<\infty,\ \mu^*(E)=\sup\{\mu^*(K),\ \forall{コンパクト集合} K\subset E\}\}$$　

- $\mathfrak{M}=\{E\in 2^X\ |\ E\cap K\in\mathfrak{M}_f\ (\forall {コンパクト集合}K )\}$

---

・$\mu^*(\phi)=\mu_0(\phi)=0$ で、 $\mu^*,\mu_0$は単調：$E\subset F\Rightarrow \mu_0(E)\subset \mu_0(F),\ \mu^*(E)\subset \mu^*(F)$
- $\mu^*$ は $\mu_0$ の拡張
- $\mu_0$ は劣 $\sigma$-加法的：任意の開集合列 $U_n$ に対して、 $\mu_0(\bigcup U_n)\le\sum \mu_0(U_n)$
- $\mu^*$は劣 $\sigma$-加法的：任意の集合列 $E_n$ に対して、 $\mu^*(\bigcup E_n)\le\sum \mu^*(E_n)\\\ \\$


・コンパクト集合 $K$ に対して、 $K\in\mathfrak{M}_f$ かつ
$\mu^*(K)=\inf\{\Lambda f\ |\ K\prec f\}=\inf\{\Lambda f\ |\ f\in C_{c,+}(X),\ f|_{K}=1\}$

    ・C_{c,+}は台がコンパクトな連続で、実数値かつ非負ってこと

- 開集合 $V$ に対して、
$$\mu^*(V)=\sup\{\mu^*(K)\ |\ \forall{コンパクト集合}K\subset V\}$$したがって、$\mu^*(V)<\infty\Rightarrow V\in\mathfrak{M}_f\\\ \\$


・非交叉列 $E_n\in\mathfrak{M}_f$ に対して、
$\mu^*(\bigcup E_n)=\sum\mu^*(E_n)$
さらに、$\mu^*(\bigcup E_n)<\infty$ ならば、$\bigcup E_n\in\mathfrak{M}_f\\\ \\$

・$\forall E\in\mathfrak{M}_f,\forall\epsilon>0$ に対して、
$K\subset E\subset V$ かつ $\mu^*(K-V)<\epsilon$ を満たすコンパクト集合 $K$、開集合 $V$ が存在する
- $\mathfrak{M}$は$\sigma$-加法族であって、$\mathfrak{B}_X\subset\mathfrak{M}_f$
- $\mathfrak{M}_f=\{E\in\mathfrak{M}\ |\ \mu^*(E)<\infty\}\\\ \\$

・$\mu:\mathfrak{B}_X\ni B\to\mu^*(B)\in[0,\infty]$
はRadon測度
- $\Lambda(f)=\int fd\mu$

    ・右辺はC_c,+以外の関数にも拡張できる！

---

・局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda$ とする。
このとき、
$$\Lambda(f)=\int fd\mu$$を満たすRadon測度 $\mu$ がただ一つ存在する

    ・Riesz-Markov-角谷の表現定理

---

##### 第二可算性とRadon測度

・$\sigma$-コンパクト：位相空間 $X$ に対して、
$$X=\bigcup K_n$$ を満たすコンパクト集合列 $K_n$ が存在する

- 第二可算空間は $\sigma$-コンパクト

---

・$\sigma$-コンパクトな局所コンパクトHausdorff空間 $X$、Radon測度 $\mu:\mathfrak{B}_X\to[0,\infty]$ とする。

- $\forall B\in\mathfrak{B}_X,\epsilon>0$ に対して、$$F\subset B\subset U,\quad \mu(U-F)<\epsilon$$ なる閉集合 $F$、開集合 $U$ が存在する  
<br>       


- $\forall B\in\mathfrak{B}_X$ に対して、
$\mu(B)=\sup\{\mu(K)\ |\ \forall{コンパクト集合}K\subset B\}$

---

・第二可算局所コンパクトHausdorff空間 $X$、Borel測度 $\mu:\mathfrak{B}_X\to[0,\infty]$ とする。
このとき、$\mu(K)<\infty\ (\forall{コンパクト集合}K)$ ならば、$\mu$ はRadon測度


---
---
---

# 六章

## Lebesgue測度



---
---
---

# 七章

## Bochner積分