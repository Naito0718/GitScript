
- [局所コンパクト空間](#局所コンパクト空間)
- [局所コンパクトHausdorff空間](#局所コンパクトhausdorff空間)
  - [基本的な性質](#基本的な性質)
  - [Urysohnの補題](#urysohnの補題)
  - [一点コンパクト化](#一点コンパクト化)
- [第二可算局所コンパクトHausdorff空間](#第二可算局所コンパクトhausdorff空間)
- [コンパクト空間](#コンパクト空間)
  - [ネットによる特徴づけ](#ネットによる特徴づけ)
  - [コンパクト集合から定まるコンパクト集合](#コンパクト集合から定まるコンパクト集合)
  - [コンパクト集合と集積点](#コンパクト集合と集積点)
  - [連続写像](#連続写像)
- [コンパクトHausdorff空間](#コンパクトhausdorff空間)
- [距離空間 $X$](#距離空間-x)
  - [位相的性質](#位相的性質)
    - [等長写像](#等長写像)
    - [同値な距離](#同値な距離)
    - [有界性](#有界性)
  - [局所コンパクト性](#局所コンパクト性)
  - [全有界,完備性](#全有界完備性)
    - [コンパクト距離空間と全有界性](#コンパクト距離空間と全有界性)
    - [コンパクト距離空間の性質](#コンパクト距離空間の性質)
  - [一様連続,一様収束](#一様連続一様収束)
    - [コンパクト一様収束](#コンパクト一様収束)
  - [Baireのカテゴリ定理](#baireのカテゴリ定理)


# 局所コンパクト空間

・位相空間 $X$ とする。
このとき、局所コンパクト空間 $X$：
$$\forall x\in X\text{ に対して、}\exist\text{ 開近傍 }U\in\mathcal{N}(x)\text{ であって、}\\\ \\
\overline{U}\text{ はコンパクト}$$

---

# 局所コンパクトHausdorff空間

## 基本的な性質

<dl><dt>

・局所コンパクトHausdorff空間 $X$ とする。

</dt><dd>

- $x\in X$ とする。
このとき、一点集合 $\{x\}$ はコンパクト。
<br>

- コンパクト集合 $K\subset X,x\in K^c$ とする。
このとき、
$$\exist\text{ 開集合 }U,V\sub X\text{ であって、}\\\ \\
x\in U,\ K\subset V,\ U\cap V=\phi\\\ \\$$

- $K\subset U\sub X$ なるコンパクト集合 $K$、開集合 $U$ とする。
このとき、$$\exist\text{ 開集合 }V\sub X\text{ であって、}\\\ \\
K\subset V\subset\overline{V}\subset U,\quad\overline{V}\text{ はコンパクト}$$

      ・K={x}として、その開近傍Uでもよい。

</dd></dl>

---

・局所コンパクトHausdorff空間 $X$ とする。
このとき、$X$ は正則空間。
<br>

    ・閉集合で上と似たようなことができる！
<br>

- 局所コンパクトHausdorff空間 $X$、$X=\bigcup F_n$ となる閉集合列 $F_n$ とする。
このとき、
$$\exist n_0\in\bm{N}\text{ であって、}(F_{n_0})^i\neq\phi\\\ \\$$

      ・Baireのカテゴリ定理

---

## Urysohnの補題


<dl><dt>

・位相空間 $X$、コンパクト集合 $K$、開集合 $U$、$f:X\to\bm{R}$ とする。
このとき、
$$K\prec f\iff f\in C_c(X),\ f:X\to[0,1],\ f(x)=1\ \ (\forall x\in K)\\\ \\
f\prec U\iff f\in C_c(X),\ f:X\to[0,1],\ \mathrm{supp}\ f\subset U\\\ \\
K\prec f\prec U\iff f\in C_c(X),\ f:X\to[0,1],\ f(x)=1\ \ (\forall x\in K),\ \mathrm{supp}\ f\subset U\\\ \\$$

</dt><dd>

- 開集合 $U_1\subset U_2$、コンパクト集合 $K_1\sub K_2$ とする。
このとき、
$$f\prec U_1\Rightarrow f\prec U_2\\\ \\
K_2\prec f\Rightarrow K_1\prec f$$

---

- 局所コンパクトHausdorff空間 $X$、$K\subset U\sub X$ なるコンパクト集合 $K$、開集合 $U$ とする。
このとき、
$$\exist f:X\to\bm{R}\text{ であって、}K\prec f\prec U\\\ \\$$

- 局所コンパクトHausdorff空間 $X$、$K\subset \bigcup_{i=1}^n U_i$ なるコンパクト集合 $K$、開集合 $U_1,...,U_n$ とする。
このとき、$$\exist f_1,...,f_n\in C_c(X),\ f_i:X\to [0,1]\text{ であって、}\\\ \\
\sum_{i=1}^n f_i(x)=1\ \ (\forall x\in K),\quad \mathrm{supp}\ f_i\in U_i,\\\ \\
\forall x\in X\text{ に対して、}\sum_{i=1}^nf_i(x)\in[0,1]$$

</dd></dl>

---

## 一点コンパクト化

<dl><dt>

・局所コンパクトHausdorff空間 $X$、$X$ に含まれていない元 $\infty\notin X$ とする。
このとき、
$$\tilde{X}=X\cup\{\infty\}\\\ \\
\tilde{\mathcal{O}}=\{U\subset\tilde{X}\ |\ \infty\in U,\ \tilde{X}-U\subset X{はコンパクト}\}\cup\mathcal{O}$$
と定める。

</dt><dd>

- $\tilde{\mathcal{O}}$ は $\tilde{X}$ の位相で、$\mathcal{O}$ は $\tilde{\mathcal{O}}$ の $X$ における相対位相。
<br>

- $\tilde{X}$はコンパクトHausdorff空間

</dd></dl>

---

# 第二可算局所コンパクトHausdorff空間

<dl><dt>

・第二可算局所コンパクトHausdorff空間 $X$ とする。
このとき、$X$ は $\sigma$-コンパクト。
特に、$X$ は閉包がコンパクトな可算開基を持つ。
<br>

</dt><dd>

- 第二可算局所コンパクトHausdorff空間 $X$ とする。
このとき、
$$\exist\text{ 開集合列 }U_n\sub X\text{ であって、}\\\ \\
U_{n}\sub\overline{U_n}\sub U_{n+1}\text{ かつ }\quad\overline{U_n}\text{ はコンパクトかつ }X=\bigcup U_n$$

</dd></dl>

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

    ・xを含む任意の開集合が、少なくとも一つxと異なる点を持つ。？？？

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
<br>

- 距離空間 $X$、収束列 $x_n$ とする。
このとき、$x_n$ はCauchy列
  
---

### 等長写像

・距離空間 $X,Y$、全単射 $f:X\to Y$ とする。
このとき、等距離写像：
$$d(x,y)_X=d(f(x),f(y))_Y$$等距離写像が存在すれば、
$$X\cong Y\ (\text{同相})$$

    ・同相だけでは完備性などが保たれない。

- 完備性？

---

### 同値な距離

・集合 $X$、距離 $d_1,d_2:X\to[0,\infty)$ とする。
このとき、
$$\exist c_1,c_2>0\text{ であって、}\forall x,y\in X\text{ に対して、}\\\ \\
c_1d_1(x,y)\le d_2(x,y)\le c_2d_1(x,y)\\\ \\
\Rightarrow \mathcal{O}_{d_1}=\mathcal{O}_{d_2}$$
ここで、左側が成り立つような距離 $d_1,d_2$ を同値な距離という。

- 完備性？

---

### 有界性

・距離空間 $X$、部分集合 $A\sub X$ とする。
このとき、$A$ が有界：
$$\exist r>0,\exist x_0\in X\text{ であって、}\forall a\in A\text{ に対して }d(a,x_0)<r\\\ \\$$

- 距離空間 $X$、部分集合 $A\sub X$ とする。
このとき、$A$の直径 $d(A)：
$$d(A)=\sup\{d(x,y)\ |\ x,y\in A\}$$

---

## 局所コンパクト性

・距離空間 $X$ に対して、
$$\forall\text{ 有界閉集合 }A\subset X\text{ がコンパクト}\Rightarrow X\text{ は局所コンパクト}$$

    ・割と自明。

---

## 全有界,完備性

・距離空間 $X$ とする。
このとき、全有界空間 $X$：
$$\forall n\in\bm{N}\text{ に対して、}\exist x_{n,1},...,x_{n,m}\in X\text{ であって、}X=B(x_{n,1},1/n)\cup...\cup B(x_{n,m},1/n)\\\ \\$$

    ・全有界空間は有界。
<br>

- 全有界な距離空間は可分

---

### コンパクト距離空間と全有界性

・距離空間 $X$ とする。
このとき、
$$X\text{ はコンパクト}\iff X\text{ は点列コンパクト}\iff X\text{は全有界かつ完備}$$

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

<dl><dt>

・距離空間 $(X,d_X),(Y,d_Y)$、$f:X\to Y$ とする。
このとき、一様連続関数 $f$：
$$\forall\epsilon>0{ に対して、}\exist\delta>0{ であって、}\\\ \\
\forall x_1,x_2\in X\text{ に対して、}d_X(x_1,x_2)<\delta\Rightarrow d_Y(f(x_1),f(x_2))$$
明らかに、一様連続関数は連続。

    ・δがxによらない
<br>

- 集合 $X$、距離空間 $(Y,d)$、関数ネット $f_{\lambda}:X\to Y,\ f:X\to Y$ とする。
このとき、$f$ に一様収束する関数ネット $\lim f_{\lambda}=f$：
$$\forall\epsilon>0{に対して}\exist\lambda_0\in\Lambda{であって、}\forall x\in X\text{ に対して、}\\\ \\
\lambda\ge\lambda_0\Rightarrow d(f_{\lambda}(x),f(x))<\epsilon$$
明らかに、一様収束関数ネットは各点収束関数ネット。また、$X$ 上一様収束するならば、$X$ の任意の部分集合上でも一様収束する。
<br>

- 集合 $X$、完備距離空間 $(Y,d)$、関数列 $f_n:X\to Y$ とする。
このとき、一様Cauchy関数列 $f_n$：
$$\forall\epsilon>0{に対して}\exist n_0\in\bm{N}{であって、}\forall x\in X\text{ に対して、}\\\ \\
n,m\ge n_0\Rightarrow d(f_n(x),f_m(x))<\epsilon\quad(\forall x\in X)\\\ \\$$

</dt><dd>

- コンパクト距離空間 $(X,d_X)$、距離空間 $(Y,d_Y)$、連続関数  $f:X\to Y$ とする。
このとき、$f$ は一様連続。
<br>

- 位相空間 $X$、距離空間 $(Y,d)$、$f:X\to Y$ に一様収束する連続関数ネット列 $f_{\lambda}:X\to Y$ とする。
このとき、$f$ は連続。
<br>

- 集合 $X$、完備距離空間 $(Y,d)$、一様Cauchy関数列 $f_{n}:X\to Y$ とする。
このとき、$f_n$ はある関数 $f:X\to Y$ に一様収束する


</dd></dl>

---

### コンパクト一様収束

・位相空間 $X$、距離空間 $Y$、関数ネット列と関数 $f_{\lambda},f:X\to Y$ とする。
このとき、$f$ にコンパクト一様収束：
$$\forall\text{ コンパクト集合 }K\sub X\text{ に対して、}f_{\lambda} \text{ が }f\text{ に一様収束}$$

---

## Baireのカテゴリ定理

・完備距離空間 $X$、$X$ で稠密な開集合列 $V_n\subset X$ とする。
このとき、$\bigcap V_n$ は $X$ において稠密。
<br>

- 完備距離空間 $X$、$X=\bigcup_n F_n$ を満たす閉集合列 $F_n\subset X$ とする。
このとき、$\exist n\in\bm{N}$ であって、$F_n^{\circ}\neq\phi$ 

---