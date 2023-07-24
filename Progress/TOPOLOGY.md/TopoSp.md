# 位相空間

・開集合の和集合は非可算無限でよい

##### 稠密性

・連続関数 $f,g:X\to Y$ が $\overline{M}=X$ を満たす集合 $M$ 上で等しく、 $Y$ がHausdorffならば、$f=g$

##### 連結性

## 部分空間

・全空間$X$に対する部分空間$W$において保たれる位相的性質

→ 第一可算、第二可算、可分
→ ハウスドルフ

---

・距離空間の部分空間

→距離 $d$を $W$ 上に制限しただけ

→$W$ 上の開球：$B(x,r)\cap W$

---

## 直積位相空間

・位相

    位相を定義する開基：各射影の全共通部分、非可算個、可算無限個なら有限和
    有限個のとき、（各射影空間の開集合の直積）=（位相を定義する開基）

・第二可算

    可算個の第二可算直積空間は第二可算

・ハウスドルフ

    有限個の直積空間はハウスドルフ

---

## ネット

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

## フィルター

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

## 第一可算空間 $X$ と点列 $(x_n)_{n\in\bm{N}}$

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

## 局所コンパクトHausdorff空間

・$\forall x\in X$は閉包がコンパクトな開近傍を持つ

→ 
コンパクト集合$K\subset X,x\in K^c$に対して、
$$x\in U,K\subset V,U\cap V=\phi$$を満たす開集合$U,V$が存在する

→ 
$K\subset U$なるコンパクト集合$K$と開集合$U$に対して、$$K\subset V\subset\overline{V}\subset U$$なる閉包がコンパクトな開集合$V$が存在する

---

・$K\subset U$なるコンパクト集合$K$と開集合$U$に対して、$$f:X\to [0,1],\quad f(x)=1\ (\forall x\in K),\quad suppf\subset U$$なる $suppf$がコンパクトな連続関数が存在する

    ・Urysohnの補題

→
$K\subset \bigcup_{i=1}^n U_i$なるコンパクト集合$K$と開集合$U_1,...,U_n$に対して、$$f:X\to [0,1],\quad \sum_{j=1}^n f_j=1\ (\forall x\in K),\quad suppf_j\in U_j$$なる $suppf_j$がコンパクトな連続関数$f_1,...,f_n$が存在する

---

・$\infty\notin X$に対して、$$\tilde{X}=X\cup\{\infty\},\quad\tilde{\mathcal{O}}=\{U\subset\tilde{X}\ |\ \infty\in U,\ \tilde{X}-U\subset X{はコンパクト}\}\cup\mathcal{O}$$と定めると定義する

    ・一点コンパクト化

→ $\tilde{\mathcal{O}}$は$\tilde{X}$の位相
→ $\mathcal{O}$は$\tilde{\mathcal{O}}$の相対位相
→ $\tilde{X}$はコンパクトHausdorff空間

---

## コンパクト空間

##### ネットによる特徴づけ

・$X$を位相空間とすると、
$X$がコンパクト空間 $\iff X$ の任意のネットは堆積点を持つ$\iff$ $X$ の任意のネットは収束する部分ネットを持つ $\iff$  $X$の任意の普遍ネットは収束する

##### コンパクト集合

・コンパクト集合の部分閉集合はコンパクト集合

→有限個の和集合はコンパクト

    ・共通部分はコンパクトでない

---

## コンパクトHausdorff空間

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

→
位相空間 $X$、距離空間 $(Y,d_Y)$、$f$に一様収束する連続関数ネット列 $f_{\lambda}:X\to Y$に対して、$f$は連続

→
集合 $X$、完備距離空間 $(Y,d_Y)$、一様Cauchy関数列 $f_{n}:X\to Y$に対して、$f_n$はある関数$f:X\to Y$に一様収束する

---

    ・Baireのカテゴリ定理

---