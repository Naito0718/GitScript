
- [零点](#零点)
  - [一致の定理](#一致の定理)
  - [最大値の原理](#最大値の原理)
- [孤立特異点](#孤立特異点)
  - [ローラン展開](#ローラン展開)
- [特異点の分類](#特異点の分類)
  - [除去可能特異点](#除去可能特異点)
  - [極](#極)
    - [極と零点](#極と零点)
  - [真性特異点](#真性特異点)
    - [孤立特異点の特徴づけ](#孤立特異点の特徴づけ)
- [留数定理](#留数定理)



# 零点

    ・普通にf(a)=0の点。f^(k)=0 (0≦k≦n-1)かつf^(n)(a)≠0ならn次の零点。任意のnで0なら無限次の零点。
<br>

|**$CompAnal-2-1$**|
|:-|

・領域 $D\sub\bm{C}$、正則な $0$ でない関数 $f:D\to\bm{C},\ f\neq0$、$f$ の零点 $a\in\bm{C}$ とする。
このとき、
$$(1):\exist N\in\bm{N}\text{ であって、}f^{N}(z)\neq0\text{、 すなわち、}a\text{ は無限次の零点ではありえない。}\\\ \\
(2):a\text{ は }f\text{ の }n\text{ 次の零点}\iff\forall\text{ 開球 } B(a,r)\sub D\text{ に対して、}\exist\text{ 正則関数 }f_n:B(a,r)\to\bm{C}\text{ であって、}\\\ \\
\forall z\in B(a,r)\text{ に対して、}f(z)=(z-a)^nf_n(z),\quad f_n(a)\neq0\\\ \\
(3):\exist\text{ 開球 }B(a,r)\sub D\text{ であって、}B(a,r)\text{ 内の }f\text{ の零点は }a\text{ のみ。}\\\ \\$$

---

## 一致の定理

|**$CompAnal-2-2$**|
|:-|

・領域 $D\sub\bm{C}$、正則関数 $f,g:D\to\bm{C}$、$a\in\bm{C}$ に収束する点列 $(z_n)\sub D$ とする。
このとき、
$$\forall n\in\bm{N}\text{ に対して、}f(z_n)=g(z_n)\\\ \\
\Rightarrow\forall z\in D\text{ に対して、}f(z)=g(z)\\\ \\$$

    ・条件を満たす点列が存在してればよい。
<br>

|**$CompAnal-2-3$**|
|:-|

- 領域 $D\sub\bm{C}$、正則関数 $f,g:D\to\bm{C}$ とする。
このとき、
$$(1):\exist\text{ 空でない開集合 }U\sub D\text{ であって、}\forall z\in U\text{ に対して、}f(z)=g(z)\\\ \\
(1'):\exist\text{ 一点でない連続曲線 }C\sub D\text{ であって、}\forall z\in C\text{ に対して、}f(z)=g(z)\\\ \\
\Rightarrow_{\text{どっちか}}\forall z\in D\text{ に対して、}f(z)=g(z)\\\ \\$$

---

## 最大値の原理

・領域 $D\sub\bm{C}$、定数でない正則関数 $f:D\to\bm{C}$ とする。
このとき、
$$(1):D\text{ 上 }|f(z)|\text{ の最大値は存在しない。} \\\ \\
(2):\forall z\in D\text{ に対して、}f(z)\neq0\\\ \\
\Rightarrow D\text{ 上 }|f(z)|\text{ の最小値は存在しない。} \\\ \\
\forall z\in B(a,r)\text{ に対して、}f(z)=(z-a)^nf_n(z),\quad f_n(a)\neq0\\\ \\
(3):D\text{ が有界領域であって、}f\text{ は連続関数}f:\overline{D}\to\bm{C}\text{ に拡張できる }\\\ \\
\Rightarrow \overline{D}\text{ 上 }|f(z)|\text{ は最大値をとって、その }z\in\overline{D}\text{ は }\partial \overline{D}\text{ に属する。}\\\ \\
(4):D\text{ が有界領域であって、}f\text{ は連続関数}f:\overline{D}\to\bm{C}\text{ に拡張でき、 }\forall z\in D\text{ に対して、}f(z)\neq0\\\ \\
\Rightarrow \overline{D}\text{ 上 }|f(z)|\text{ は最小値をとって、その }z\in\overline{D}\text{ は }\partial \overline{D}\text{ に属する。}\\\ \\$$

    ・(2)でf(z)=0なる点があれば、明らかに0が最小値。
    ・コンパクト集合上で最大値をとることの類似。

---

# 孤立特異点

    ・別にすべての特異点が孤立してるわけではない。
<br>

<dl><dt>

・$a\in\bm{C}$ を中心とする $a$ を除外した開円板 $B_{/a}(a,r)\sub\bm{C}$、$f_{/a}:B_{/a}(a,r)\to\bm{C}$、$f:B(a,r)\to\bm{C}$ とする。
このとき、$(1):a$ が $f_{/a}$ の孤立特異点、$(2):a$ が $f$ の孤立特異点：
$$(1):f_{/a}\text{ は }B_{/a}(a,r)\text{ 上正則であって、}f\text{ は }a\text{ で定義されていない。}\\\ \\
(2):f\text{ は }B_{/a}(a,r)\text{ 上正則であって、}a\text{ で複素微分できない。}\\\ \\$$

</dt><dd>

- $a\in\bm{C}$、異なる複素数 $b\neq c\in B(a,r)\sub \bm{C}$、$b,c$ を除いて開円板 $B(a,r)$ 上で正則な $f:\to\bm{C}$ とする。
このとき、
$$\forall\text{ 非交叉な開円板 }B(b,R),B(c,\rho)\sub B(a,r),\ B(b,R)\cap B(c,\rho)=\phi\text{ に対して、}\\\ \\
\int_{\partial B(a,r)}fdz=\int_{\partial B(b,R)}fdz+\int_{\partial B(c,\rho)}fdz$$
特に、$f$ が $c$ で正則ならば、
$$\int_{\partial B(a,r)}fdz=\int_{\partial B(b,R)}fdz$$

</dd></dl>

---

## ローラン展開

<dl><dt>

・$a\in\bm{C}$、正則関数 $f:B_{/a}(a,r)\to\bm{C}$ とする。
このとき、
$$\forall z\in B_{/a}(a,r)\text{ に対して、}\\\ \\
f(z)=\sum_{n\in\bm{Z}}a_n(z-a)^n,\\\ \\
\text{ また、}0<\forall R<r\text{ に対して、}a_n=\frac{1}{2\pi i}\int_{\partial B(a,R)}\frac{f(\xi)}{(\xi-a)^{n+1}}d\xi\\\ \\$$
ここで、この級数展開をローラン展開という。
<br>

</dt><dd>

- $a\in\bm{C}$、正則関数 $f:B_{/a}(a,r)\to\bm{C}$ とする。
このとき、
$$\forall\text{ ローラン展開 }f(z)=\sum_{n\in\bm{Z}}a_n(z-a)^n\quad(\forall z\in B_{/a}(a,r))\text{ に対して、}\\\ \\
\sum_{n\in\bm{Z}}a_n(z-a)^n\text{ は }B_{/a}(a,r)\text{ 上広義一様収束して、この展開は一意的に定まる。}$$


</dd></dl>

---


# 特異点の分類

・$a\in\bm{C}$ を孤立特異点にもつ関数 $f$、適当な $B_{/a}(a,r)$ 周りのローラン展開 $\sum_{n\in\bm{Z}}a_n(z-a)^n$ とする。
このとき、$(1):a$ が除去可能特異点、$(2):a$ が $m$ 次の極、$(3):a$ が真性特異点： 
$$(1):\forall n\in\bm{N}-\{0\}\text{ に対して、}a_{-n}=0\\\ \\
(2):\exist n_0\in\bm{N}-\{0\}\text{ であって、}a_{-n_0}\neq0,\ n> n_0\Rightarrow a_{-n}=0\\\ \\
(3):\forall n\in\bm{N}-\{0\}\text{ に対して、}n\le\exist n_0\in\bm{N}\text{ であって、}a_{-n_0}\neq0$$
明らかに、$(1),(2),(3)$ はすべての場合を尽くし、かつ排反である。
<br>

- $a\in\bm{C}$、$a$ を含む部分集合 $a\in A\sub\bm{C}$、$f:A\to\bm{C}$ とする。
このとき、$f$ が $a$ で正則：
$$\exist\text{ 開近傍 }B(a,r)\sub A\text{ であって、}f\text{ は }B(a,r)\text{ 上正則}$$

---

## 除去可能特異点

・$a\in\bm{C}$ を孤立特異点にもつ関数 $f$ とする。
このとき、
$$a\text{ は }f\text{ の除去可能特異点}\iff\lim_{z\to a}f(x)\in\bm{C}\iff\exist\text{ 除外近傍 }B_{/a}(a,r)\text{ であって、}f\text{ は }B_{/a}(a,r)\text{ 上有界}$$
特に、$a$ が $f$ の除去可能特異点ならば、$f(a)=_{z\to a}f(x)$ と定めると、$f$ は $a$ で正則になる。

---

## 極

・$a\in\bm{C}$ を孤立特異点にもつ関数 $f$ とする。
このとき、
$$a\text{ は }f\text{ の }m\text{ 次の極}\\\ \\
\iff\exist\text{ 適当な開近傍 }B(a,r)\text{ 上正則な }g\text{ であって、}\\\ \\
\forall z\in B_{/a}(a,r)\text{ に対して、}f(z)=\frac{g(z)}{(z-a)^m},\quad g(a)\neq0$$
さらに、$a$ が $f$ の $m$ 次の極ならば、
$$\lim_{z\to a}|f(z)|=\infty\\\ \\$$

---

### 極と零点

・$a\in\bm{C}$、$0$ でない正則関数 $f:B_{/a}(a,r)\to\bm{C}$ とする。
このとき、
$$a\text{ が }f\text{ の }m\text{ 次の極または }m\text{ 次の零点であるかに応じて、}\\\ \\
a\text{ は }g(z)=\frac{1}{f(z)}\text{ の }m\text{ 次の零点または }m\text{ 次の極}$$ 

---

## 真性特異点

・$a\in\bm{C}$ を真性特異点にもつ関数 $f$ とする。
このとき、
$$(1):\forall M>0\ ,\forall\delta>0\text{ に対して、}\exist z\in\bm{C}\text{ であって、}0<|z-a|<\delta\text{ かつ }|f(z)|>M\\\ \\
(2):\forall c\in\bm{C},\ \forall \epsilon[]>0\ ,\forall\delta>0\text{ に対して、}\exist z\in\bm{C}\text{ であって、}0<|z-a|<\delta\text{ かつ }|f(z)-c|>\epsilon\\\ \\$$
特に、$(1),(2)$ はそれぞれ以下に同値。
$$(1)':\exist\text{ 点列 }(z_n)\sub\bm{C}\text{ であって、}\lim_{n\to\infty}z_n=a\text{ かつ }\lim_{n\to\infty}|f(z_n)|=\infty\\\ \\
(2)':\forall c\in\bm{C}\text{ に対して、}\exist\text{ 点列 }(z_n)\sub\bm{C}\text{ であって、}\lim_{n\to\infty}z_n=a\text{ かつ }\lim_{n\to\infty}f(z_n)=c\\\ \\$$

---

### 孤立特異点の特徴づけ

・$a\in\bm{C}$ を真性特異点にもつ関数 $f$ とする。
このとき、
$$(1):a\text{ は }f\text{ の除去可能特異点}\iff\lim_{z\to a}f(z)\in\bm{C}\\\ \\
(2):a\text{ は }f\text{ の }m\text{ 次の極}\iff\lim_{z\to a}f(z)=\infty\\\ \\
(3):a\text{ は }f\text{ の真性特異点}\iff\lim_{z\to a}f(z)\in\bm{C}\text{ でも }\lim_{z\to a}f(z)=\infty\text{ でもない}\\\ \\$$

---

# 留数定理

<dl><dt>

・除外円板 $B_{/a}(a,r)\sub\bm{C}$、正則関数 $f:B_{/a}(a,r)\to\bm{C}$ とする。
このとき、留数 $\mathrm{Res}(f,a)$：
$$\forall z\in B_{/a}(a,r)\text{ に対して、}f(z)=\sum_{n\in\bm{Z}}a_n(z-a)^n\text{ であるが、このときの }a_{-1},\\\ \\
\text{ すなわち、}\mathrm{Res}(f,a)=a_{-1}\\\ \\$$

- 領域 $D\sub\bm{C}$、孤立特異点 $a_1,...,a_n\in D$ を除いて正則な $f:D\to\bm{C}$、$D-\{a_1,...,a_n\}$ 内のホモローグ $0$ な区分的 $C^1$ サイクル $C\sub D-\{a_1,...,a_n\}$ とする。
このとき、$$\int_Cfdz=2\pi i\sum_{k} n(C,a_k)\mathrm{Res}(f,a_k)\\\ \\$$

      ・留数を取るときは、毎回孤立特異点周りでローラン展開してると考える。
<br>

</dt><dd>

- 領域 $D\sub\bm{C}$ を囲む $\bm{C}$ 内の区分的 $C^1$ サイクル $C$、孤立特異点 $a_1,...,a_n\in D$ を除いて正則な $f:D\cup C\to\bm{C}$ とする。
このとき、
$$\int_Cfdz=2\pi i\sum_{k=1}^n\mathrm{Res}(f,a_k)$$

</dd></dl>




