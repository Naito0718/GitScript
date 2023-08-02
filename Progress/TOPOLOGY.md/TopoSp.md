- [位相空間](#位相空間)
        - [演算](#演算)
        - [基本近傍系](#基本近傍系)
        - [開基](#開基)
        - [稠密性](#稠密性)
        - [分離公理](#分離公理)
        - [連結性](#連結性)
        - [連続性](#連続性)
        - [開写像](#開写像)
- [部分空間](#部分空間)
        - [写像](#写像)
        - [保たれる位相的性質](#保たれる位相的性質)
        - [コンパクト性](#コンパクト性)
        - [局所コンパクトHausdorff性](#局所コンパクトhausdorff性)
- [直積位相空間](#直積位相空間)
        - [位相](#位相)
        - [直積位相の性質](#直積位相の性質)
        - [写像](#写像-1)
- [ネット](#ネット)
      - [始位相](#始位相)
- [フィルター](#フィルター)
  - [第一可算空間と点列](#第一可算空間と点列)
        - [点列による特徴づけ](#点列による特徴づけ)
        - [点列コンパクト](#点列コンパクト)
- [局所コンパクトHausdorff空間](#局所コンパクトhausdorff空間)
        - [Urysohnの補題](#urysohnの補題)
        - [一点コンパクト化](#一点コンパクト化)
- [コンパクト空間](#コンパクト空間)
        - [ネットによる特徴づけ](#ネットによる特徴づけ)
        - [コンパクト集合](#コンパクト集合)
        - [連続写像](#連続写像)
- [コンパクトHausdorff空間](#コンパクトhausdorff空間)
  - [距離空間 $X$](#距離空間-x)
        - [位相的性質](#位相的性質)
        - [全有界、完備性](#全有界完備性)
        - [一様連続、一様収束](#一様連続一様収束)





# 位相空間

    ・開集合の和集合は非可算無限でよい

##### 演算

・$\overline{A\cup B}=\overline{A}\cup\overline{B},\quad\overline{A\cap B}\subset \overline{A}\cap\overline{B}$

- $\bigcup_{\lambda}\overline{A}_{\lambda}\subset\overline{\bigcup_{\lambda} A_{\lambda}}$

        ・左辺は閉集合とは限らない

---

・$(A\cap B)^i=A^i\cap B^i,\quad A^i\cup B^i\subset(A\cup B)^i$


---

##### 基本近傍系

・基本近傍系 $\mathcal{N}_F(x)$ が与えられているとする。
このとき、
$O\in\mathcal{O}\iff \forall x\in O{に対して、}\exist U_x\in\mathcal{N}_F(x){であって、}U_x\subset O$

- 位相空間 $X$ に対して、
$\mathcal{N}_F(x)$ が基本近傍系
$\iff$$\begin{cases}
U\in\mathcal{N}_F(x)\Rightarrow x\in U    \\
U,V\in\mathcal{N}_F(x)\Rightarrow\exist W\in\mathcal{N}_F(x);\ W\subset U\cap V \\
U\in\mathcal{N}_F(x),y\in U\Rightarrow\exist V\in\mathcal{N}_F(y);V\subset U\\
\end{cases}$

---

##### 開基

・第二可算空間はLindelof空間。

    ・任意の開被覆に対して可算個の部分被覆を取れる。

- 第二可算空間は可分。

---

##### 稠密性

・高々可算な集合 $M$ であって、$\overline{M}=X$

    ・部分集合なら不等号。

- $A\subset X$ が可分ならば、$\overline{A}$ も可分。

- 可分な集合列 $A_{n}$ に対して、
$\bigcup_{n}A_{n}$ は可分。


---

・位相空間 $X$、Hausdorff空間 $Y$、$\overline{M}=X$ なる部分集合 $M$、$f(x)=g(x)\ (\forall x\in M)$ なる連続関数 $f,g:X\to Y$ とする。
このとき、$$f=g$$

---

・可分かつ第一可算ならば、
第二可算である。

---

##### 分離公理


・正則空間 $X$ ：$$\begin{cases}
T_1    \\
{閉集合}\ F,\ x\in F^c\  {に対して、}\ x\in U,\ F\subset V,\ U\cap V=\phi\  {なる開集合}\  U,V {が存在する。}      \\
\end{cases}$$ 

- 位相空間 $X$ に対して、
$X$ が正則空間$\iff x\in X, U\in\mathcal{N}(x)$ に対して、$x\in V\subset\overline{V}\subset U$ なる開近傍 $V$ が存在する。

---

##### 連結性

・連結な空間：
$X=O_1\cup O_2,\ O_1\cap O_2=\phi$ なる開集合が存在するならば、
$O_1=\phi$ または $O_2=\phi$

    ・連結集合のときは、 「A⊂O_1∪O_2,A∩O_1∩O_2=φ、A∩O_1,A∩O_2が共に空でない」 でもよい
    ・空集合は連結でないとする

- $x\in X$ に対して、一点集合 $\{x\}$ は連結

- 連結な集合 $A_1,A_2\subset X$ であって、$A_1\cap A_2\neq\phi$ とする。
このとき、$A_1\cup A_2$ は連結。

---

・連結成分：同値関係 $$x\sim y\iff \exist\ {連結な集合}\ A {であって、} x,y\in A$$ による同値類

---

・連結な位相空間 $X$、位相空間 $Y$、連続写像 $f:X\to Y$ について、$f(X)$ は連結。

---

##### 連続性


---
##### 開写像



---

# 部分空間

##### 写像

位相空間 $X,Y$、部分集合 $A\subset X$ 連続写像 $f:X\to Y$ に対して、
$f|_A:A\to Y$ は連続写像。

---

##### 保たれる位相的性質

→ 第一可算、第二可算、可分
- $T_1$、ハウスドルフ、正則、正規

---

・距離空間の部分空間

→距離 $d$を $W$ 上に制限しただけ

→$W$ 上の開球：$B(x,r)\cap W$

---

##### コンパクト性

・$K$ が相対位相でコンパクトならば、元の位相でもコンパクト

---


##### 局所コンパクトHausdorff性

・局所コンパクトHausdorff空間の開集合は、局所コンパクトHausdorff空間

---
---
---

# 直積位相空間

##### 位相

・位相

    位相を定義する開基：各射影の全共通部分、非可算個、可算無限個なら有限和
    有限個のとき、（各射影空間の開集合の直積）=（位相を定義する開基）

---

・$X,Y$ の基本近傍系 $\mathcal{N}_{F;X}(x),\ \mathcal{N}_{F;Y}(x)$ が与えられているとする。
このとき、$$\mathcal{N}_{F;X\times Y}(x,y)=\{U\times V\ |\ U\in\mathcal{N}_{F;X}(x),V\in\mathcal{N}_{F;Y}(y)\}$$ は直積空間 $X\times Y$ の基本近傍系をなす。

---

##### 直積位相の性質

・第二可算

    可算個の第二可算直積空間は第二可算

・ハウスドルフ

    有限個の直積空間はハウスドルフ

・コンパクト空間の族 $X_{\lambda}$ に対して、
$\Pi_{\lambda}X_{\lambda}$ はコンパクト空間。

・連結空間の族 $X_{\lambda}$ に対して、
$\Pi_{\lambda}X_{\lambda}$ は連結空間。

##### 写像

・位相空間 $X_1,X_2,Y_1,Y_2$、連続写像 $f_i:X_i\to Y_i$ とする。
このとき、$$f:X_1\times X_2\to Y_1\times Y_2,\quad f(x_1,x_2)=(f_1(x_1),f_2(x_2))$$は連続写像。

---

・ 位相空間 $X_1,...,X_n,Y$、連続写像 $f:X_1\times...\times X_n\to Y$ とする。

- 連続写像 $g:X_i\to X_i$ に対して、
$$f'(x_1,...,x_n)=f(x_1,...,g(x_i),...,x_n)$$ は連続。

        ・固定も含む。

---
---
---

# ネット

・前順序集合

    ・反射と推移

・有向集合

    ・任意の2要素に対してでかいやつが存在する

・ネット$x_{\lambda}:\Lambda\to X$

    ・有向集合を添え字集合とする写像
    ・eventually in, frequently in
    ・普遍ネット（普遍的にeventually in）

・ネットに対するフィルター

    ・ネットに対するフィルターは、固有とは限らない2^Xのフィルター
    ・全体集合Xは当てはまる
    ・ネットに対するフィルター全体は帰納的順序集合

・収束点と堆積点（位相空間）

    ・xが収束点↔任意のxの近傍Vでeventually
    ・xが堆積点↔任意のxの近傍Vでfrequently
    ・xがネットの堆積点⇔ネットの部分ネットで、xに収束するものが存在する
    ・xに収束するXの部分集合Aのネットが存在する⇔xはAの閉包に属する
    ・fは連続⇔xに収束する任意のネットx_λに対して、ネットf(x_λ)はf(x)に収束する

・位相的性質とネット

    ・ハウスドルフ空間⇔任意の収束するネットに対し、収束値が一意的
    ・

#### 始位相

    ・直積位相の一般化

・空でない集合 $X,J$、対応 $j\in J,\ (X_j,\mathcal{O}_j),f_j:X\to X_j$に対して、
$$\{\bigcap_{i=1}^n f_{j_i}^{-1}(U_i)\ |\ n\in\bm{N},j_0,...,j_n\in J,u_i\in\mathcal{O}_{j_i}\}$$の要素の合併で表される集合全体 $\mathcal{O}$

- 各 $f_j$が連続になるような最弱の位相
- 始位相 $(f_j:X\to X_j)_{j\in J}$ が入った集合 $X$ に対して、
  $x\to x_{\lambda}\iff f_j(x_{\lambda})\to f_j(x)\ (\forall j)$

---
---
---

# フィルター

・フィルター

    ・X含みφ含まない、共通部分、包含する全部分集合
    ・フィルターは有限交叉性を持つ
    ・細分、両立
    ・フィルターがその部分集合を含むときの、制限と拡大。互いに逆写像。

・両立するフィルター$\iff$$2$つのフィルターは共通の細分を持つ

    ・2つの両立フィルターの和は有限交叉性をもつ
    ・2つの両立フィルターの和から生成されるフィルター=F⋀G、これは共通する最小の細分

・超フィルター$\iff\forall A\subset X$に対して$A\in\mathcal{F}$または$A^c\in\mathcal{F}\iff(\forall )F\cup G\in\mathcal{F}$に対し、$F\in\mathcal{F}$または$G\in\mathcal{G}$

    ・自身以外に細分を持たないフィルター（極大フィルター）
    ・単項でない超フィルターを非単項超フィルター、自由超フィルターという。
    ・任意のフィルターに対しその細分となる超フィルターが存在する。（極大性）
    ・フィルターFの細分全体は帰納的順序集合

---

## 第一可算空間と点列

・$x\in X$が可算な基本近傍系を持つならば、
$x$の任意の近傍 $V$ に対して、$B_n\subset V$ なる $n\in\bm{N}$が存在して、$B_{n+1}\subset B_{n}$
を満たす $x$ の近傍列 $B_n$が存在する

---

##### 点列による特徴づけ

・$x\in X$に対して、
$x$は$x_n$の堆積点$\iff x_n$の部分列で $x$ に収束するものが存在する

→ $A\subset X$に対して、
$x\in\overline{A}\iff x$ に収束する $A$　の点列が存在する

→ 位相空間$Y$、$f:X\to Y$に対して、
$f$は連続$\iff x$ に収束する任意の点列 $x_n$ に対して、$f(x_n)$ は $f(x)$ に収束する

---

##### 点列コンパクト

・点列コンパクト：位相空間$X$の任意の点列 $x_n$ が収束する部分列を持つこと

・Lindelof空間：位相空間 $X$ の任意の開被覆 $X=\bigcup U_{\lambda}$ が高々可算個の部分被覆を持つこと $X=\bigcup U_n$

→
第二可算空間はLindelof空間

→
点列コンパクトなLindelof空間はコンパクト

→
第一可算なコンパクト空間は点列コンパクト

→
第二可算空間$X$に対して、
$X$がコンパクト$\iff X$が点列コンパクト

---
---
---

# 局所コンパクトHausdorff空間

・$\forall x\in X$は閉包がコンパクトな開近傍を持つ

- コンパクト集合 $K\subset X,x\in K^c$ に対して、
$$x\in U,K\subset V,U\cap V=\phi$$を満たす開集合 $U,V $が存在する。
<br>

- $K\subset U$ なるコンパクト集合 $K$ と開集合 $U$ に対して、$$K\subset V\subset\overline{V}\subset U$$なる閉包がコンパクトな開集合 $V$ が存在する。
<br>

---

・$X$ は正則空間。

    ・閉集合で上と似たようなことができる！

- $X=\bigcup F_n$ となる閉集合列 $F_n$ に対して、
$F_{n_0}^i\neq\phi$ を満たす $n_0$ が存在する。

---

##### Urysohnの補題

・$K\subset U$なるコンパクト集合$K$と開集合$U$に対して、$$f:X\to [0,1],\quad f(x)=1\ (\forall x\in K),\quad suppf\subset U$$なる $suppf$がコンパクトな連続関数が存在する

    ・Urysohnの補題

- $K\subset \bigcup_{i=1}^n U_i$なるコンパクト集合$K$と開集合$U_1,...,U_n$に対して、$$f:X\to [0,1],\quad \sum_{j=1}^n f_j=1\ (\forall x\in K),\quad suppf_j\in U_j$$なる $suppf_j$がコンパクトな連続関数$f_1,...,f_n$が存在する

        ・このとき、∑f_j∊[0,1]

---

##### 一点コンパクト化

・$\infty\notin X$に対して、$$\tilde{X}=X\cup\{\infty\},\quad\tilde{\mathcal{O}}=\{U\subset\tilde{X}\ |\ \infty\in U,\ \tilde{X}-U\subset X{はコンパクト}\}\cup\mathcal{O}$$と定める

    ・一点コンパクト化

- $\tilde{\mathcal{O}}$は$\tilde{X}$の位相
- $\mathcal{O}$は$\tilde{\mathcal{O}}$の相対位相
- $\tilde{X}$はコンパクトHausdorff空間

---
---
---

# コンパクト空間

##### ネットによる特徴づけ

・$X$を位相空間とすると、
$X$がコンパクト空間 $\iff X$ の任意のネットは堆積点を持つ$\iff$ $X$ の任意のネットは収束する部分ネットを持つ $\iff$  $X$の任意の普遍ネットは収束する。

---

・位相空間 $X$ とする。
このとき、
$X$ がコンパクト$\iff$ 有限交叉性を持つ閉集合族 $F_{\lambda}$ に対して、$\bigcap F_{\lambda}\neq\phi$

    ・任意に有限個持ってきたとき、共通部分が空でない

---

##### コンパクト集合

・コンパクト集合の部分閉集合はコンパクト集合

- 有限個の和集合はコンパクト

      ・共通部分はコンパクトでない

---

##### 連続写像

・位相空間 $X,Y$、コンパクト集合 $K\subset X$、連続写像 $f:X\to Y$ とする。
このとき、$f(K)\subset Y$ はコンパクト集合

- コンパクト空間 $X$、Hausdorff空間 $Y$、$f:X\to Y$とする。
このとき、$f$ が連続全単射ならば、同相写像である。

---
---
---

# コンパクトHausdorff空間

---

## 距離空間 $X$

##### 位相的性質

・Hausdorff空間

→第一可算で、$B(x,1/n)$ が基本近傍系

→ 
可分 $\iff$ 第二可算

---

##### 全有界、完備性

・全有界：$\forall n\in\bm{N}$に対し、有限個の $x_{n,1},...,x_{n,m}\in X$が存在して、$X=B(x_{n,1},1/n)\cup...\cup B(x_{n,m},1/n)$

・完備：任意のCauchy列が収束列

・部分集合の直径：$d(A)=\sup\{d(x,y)\ |\ x,y\in A\}$

→全有界な距離空間は可分

→距離空間の収束列はCauchy列

---

・距離空間$X$に対して、
$X$はコンパクト$\iff$$X$は点列コンパクト$\iff$$X$は全有界かつ完備

---

##### 一様連続、一様収束

・一様連続関数 $f:X_{d_X}\to Y_{d_Y}$
$$\forall\epsilon>0{に対して、}\exist\delta>0{であって}d_X(x_1,x_2)<\delta\Rightarrow d_Y(f(x_1),f(x_2))$$

    ・δがxによらない

・一様収束ネット列 $f_{\lambda}:X\to Y_d,\quad\lim f_{\lambda}=f$
$$\forall\epsilon>0{に対して}\exist\lambda_0\in\Lambda{であって、}\lambda\ge\lambda_0\Rightarrow d(f_{\lambda}(x),f(x))<\epsilon\quad(\forall x\in X)$$

    ・Xはただの集合

・一様Cauchy関数列 $f_n:X\to Y_d\quad(X{は集合},Y{は完備距離空間})$
$$\forall\epsilon>0{に対して}\exist n_0\in\bm{N}{であって、}n,m\ge n_0\Rightarrow d(f_n(x),f_m(x))<\epsilon\quad(\forall x\in X)$$


→
一様連続ならば連続

---

・コンパクト距離空間 $(X,d_X)$、距離空間 $(Y,d_Y)$、連続関数 $f:X\to Y$に対して、$f$は一様連続

- 位相空間 $X$、距離空間 $(Y,d_Y)$、$f$に一様収束する連続関数ネット列 $f_{\lambda}:X\to Y$ とする。
このとき、$f$は連続
<br>

- 集合 $X$、完備距離空間 $(Y,d_Y)$、一様Cauchy関数列 $f_{n}:X\to Y$ とする。
このとき、$f_n$はある関数$f:X\to Y$に一様収束する

---

    ・Baireのカテゴリ定理

---