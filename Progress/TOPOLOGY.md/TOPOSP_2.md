
- [局所コンパクトHausdorff空間](#局所コンパクトhausdorff空間)
        - [Urysohnの補題](#urysohnの補題)
        - [一点コンパクト化](#一点コンパクト化)
- [コンパクト空間](#コンパクト空間)
  - [ネットによる特徴づけ](#ネットによる特徴づけ)
  - [コンパクト集合から定まるコンパクト集合](#コンパクト集合から定まるコンパクト集合)
  - [コンパクト集合と集積点](#コンパクト集合と集積点)
  - [連続写像](#連続写像)
- [コンパクトHausdorff空間](#コンパクトhausdorff空間)
- [距離空間 $X$](#距離空間-x)
  - [位相的性質](#位相的性質)
    - [等長写像](#等長写像)
    - [有界性](#有界性)
  - [局所コンパクト性](#局所コンパクト性)
  - [全有界、完備性](#全有界完備性)
    - [コンパクト距離空間の性質](#コンパクト距離空間の性質)
  - [一様連続、一様収束](#一様連続一様収束)
  - [Baireのカテゴリ定理](#baireのカテゴリ定理)



# 局所コンパクトHausdorff空間

・局所コンパクト空間 $X$：$\forall x\in X$は閉包がコンパクトな開近傍を持つ。

- 局所コンパクトHausdorff空間 $X$、$x\in X$ とする。
このとき、一点集合 $\{x\}$ はコンパクト。
<br>

- コンパクト集合 $K\subset X,x\in K^c$ に対して、
 $$x\in U,K\subset V,U\cap V=\phi$$を満たす開集合 $U,V $が存在する。
 <br>

- $K\subset U$ なるコンパクト集合 $K$ と開集合 $U$ に対して、$$K\subset V\subset\overline{V}\subset U$$なる閉包がコンパクトな開集合 $V$ が存在する。

      ・一点とその開近傍でもよい。

<br>

---

・$X$ は正則空間。

    ・閉集合で上と似たようなことができる！

- $X=\bigcup F_n$ となる閉集合列 $F_n$ に対して、
$F_{n_0}^i\neq\phi$ を満たす $n_0$ が存在する。

      ・Baireのカテゴリ定理

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

## ネットによる特徴づけ

  ・$X$を位相空間とすると、
  $X$がコンパクト空間 $\iff X$ の任意のネットは堆積点を持つ$\iff$ $X$ の任意のネットは収束する部分ネットを持つ $\iff$  $X$の任意の普遍ネットは収束する。

---

・位相空間 $X$ とする。
このとき、
$X$ がコンパクト$\iff$ 有限交叉性を持つ閉集合族 $F_{\lambda}$ に対して、$\bigcap F_{\lambda}\neq\phi$

    ・任意に有限個持ってきたとき、共通部分が空でない

---

## コンパクト集合から定まるコンパクト集合

・コンパクト集合の部分閉集合はコンパクト集合

- 有限個の和集合はコンパクト

      ・共通部分はコンパクトでない

---

## コンパクト集合と集積点

・コンパクト空間 $X$、無限集合 $A\sub X$ とする。
このとき、$A$ は少なくとも一つ集積点を持つ。

    ・xを含む任意の開集合が、少なくとも一つxと異なる点を持つ。

---

## 連続写像

・位相空間 $X,Y$、コンパクト集合 $K\subset X$、連続写像 $f:X\to Y$ とする。
このとき、$f(K)\subset Y$ はコンパクト集合

- コンパクト空間 $X$、Hausdorff空間 $Y$、$f:X\to Y$とする。
このとき、$f$ が連続全単射ならば、同相写像である。

---
---
---

# コンパクトHausdorff空間

 ---

# 距離空間 $X$

## 位相的性質

・正則空間

- 第一可算で、$B(x,1/n)$ が基本近傍系
<br>

- 可分 $\iff$ 第二可算
  
### 等長写像

・距離空間 $X,Y$、全単射 $f:X\to Y$ とする。
このとき、等距離写像：
$$d(x,y)_X=d(f(x),f(y))_Y$$等距離写像が存在すれば、
$$X\cong Y\ (\text{同相})$$

    ・同相だけでは完備性などが保たれない。

---

### 有界性

・距離空間 $X$、$A\sub X$ とする。
このとき、$A$ が有界：
$$\exist r>0,\exist x_0\in X\text{ であって、}\forall a\in A\text{ に対して }d(a,x_0)<r$$

---

## 局所コンパクト性

・距離空間 $X$ に対して、
$$\forall\text{ 有界閉集合 }A\subset X\text{ がコンパクト}\Rightarrow X\text{ は局所コンパクト}$$

    ・割と自明。

---

## 全有界、完備性

・全有界：$\forall n\in\bm{N}$に対し、有限個の $x_{n,1},...,x_{n,m}\in X$が存在して、$X=B(x_{n,1},1/n)\cup...\cup B(x_{n,m},1/n)$

    ・全有界空間は有界。

・部分集合の直径：$d(A)=\sup\{d(x,y)\ |\ x,y\in A\}$

- 全有界な距離空間は可分

---

・距離空間 $X$、収束列 $x_n$ とする。
このとき、$x_n$ はCauchy列

---

・距離空間$X$に対して、
$X$はコンパクト$\iff$$X$は点列コンパクト$\iff$$X$は全有界かつ完備

---

### コンパクト距離空間の性質

<dl><dt>

・コンパクト距離空間 $X$ とする。
<br>

</dt><dd>

- 位相空間 $Y$、開被覆 $X=\bigcup U_{\lambda}$、連続写像 $f:X\to Y$ とする。
このとき、$$\exist\delta>0\text{ であって、}d(x-y)<\delta\Rightarrow\exist\lambda\text{ であって } f(x),f(y)\in U_{\lambda}$$

      ・ちょっと一様連続っぽい

</dd></dl>

---

## 一様連続,一様収束

・一様連続関数 $f:X_{d_X}\to Y_{d_Y}$
$$\forall\epsilon>0{に対して、}\exist\delta>0{であって}d_X(x_1,x_2)<\delta\Rightarrow d_Y(f(x_1),f(x_2))$$

    ・δがxによらない

・一様収束ネット列 $f_{\lambda}:X\to Y_d,\quad\lim f_{\lambda}=f$
$$\forall\epsilon>0{に対して}\exist\lambda_0\in\Lambda{であって、}\lambda\ge\lambda_0\Rightarrow d(f_{\lambda}(x),f(x))<\epsilon\quad(\forall x\in X)$$

    ・Xはただの集合

・一様Cauchy関数列 $f_n:X\to Y_d\quad(X{は集合},Y{は完備距離空間})$
$$\forall\epsilon>0{に対して}\exist n_0\in\bm{N}{であって、}n,m\ge n_0\Rightarrow d(f_n(x),f_m(x))<\epsilon\quad(\forall x\in X)$$


 -  一様連続ならば連続

---

・コンパクト距離空間 $(X,d_X)$、距離空間 $(Y,d_Y)$、連続関数  $f:X\to Y$ に対して、$f$ は一様連続

- 位相空間 $X$、距離空間 $(Y,d_Y)$、$f$ に一様収束する連続関数ネット列 $f_{\lambda}:X\to Y$ とする。
このとき、$f$ は連続
<br>

- 集合 $X$、完備距離空間 $(Y,d_Y)$、一様Cauchy関数列 $f_{n}:X\to Y$ とする。
このとき、$f_n$ はある関数 $f:X\to Y$ に一様収束する

---

### コンパクト一様収束

・位相空間 $X$、距離空間 $Y$、関数ネット列と関数 $f_{\lambda},f:X\to Y$ とする。
このとき、$f$ にコンパクト一様収束：
$$\forall\text{ コンパクト集合 }K\sub X\text{ に対して、}f_{\lambda} \text{ が }f\text{ に一様収束}$$

---

## Baireのカテゴリ定理

・完備距離空間 $X$、$X$ で稠密な開集合列 $V_n\subset X$ とする。
このとき、$\bigcap V_n$ は $X$ において稠密。

    ・Baireのカテゴリ定理

- 完備距離空間 $X$、$X=\bigcup_n F_n$ を満たす閉集合列 $F_n\subset X$ とする。
このとき、$\exist n\in\bm{N}$ であって、$F_n^{\circ}\neq\phi$ 

---