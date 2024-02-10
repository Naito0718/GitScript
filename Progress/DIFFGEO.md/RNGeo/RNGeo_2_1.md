
- [$R^n$ 内の多様体](#rn-内の多様体)
  - [局所座標 $(U,φ)$](#局所座標-uφ)
    - [$C^k$ 同値と局所座標](#ck-同値と局所座標)
  - [$R^N$ 内の多様体](#rn-内の多様体-1)
    - [$R^N$ 内の部分多様体](#rn-内の部分多様体)
- [$R^N$ 内の多様体上の関数](#rn-内の多様体上の関数)
- [$R^N$ 内の多様体の接空間](#rn-内の多様体の接空間)
  - [全微分 $df$](#全微分-df)
  - [$R^N$ 内の多様体の余接空間](#rn-内の多様体の余接空間)
- [種々の定理](#種々の定理)
  - [逆関数定理](#逆関数定理)
  - [埋め込み](#埋め込み)
  - [陰関数定理](#陰関数定理)
  - [Lagrange未定乗数法](#lagrange未定乗数法)



# $R^n$ 内の多様体

    ・埋め込まれた部分多様体と、はめ込まれた部分多様体は等しい。（もともと相対位相であること。）
    ・全部C^∞としちゃう。

## 局所座標 $(U,φ)$

    ・チャートのことだが、ちょっと拡張されてる。

<dl><dt>

・$M\sub\bm{R}^N$、$M$ の開集合 $U\sub M$、$\phi:U\to\bm{R}^k$ とする。
このとき、$(U,\phi)$ が $k$ 次元局所座標：
$$\phi\text{ は同相写像で、}\phi^{-1}\text{ は }C^{\infty}\\\ \\
\forall p\in M\text{ に対して、}\mathrm{rank}\ \phi^{-1'}(\phi(p))=k\\\ \\$$

    ・定義からk<N。
    ・φ^{-1}の微分は、U=V∩MのVで微分可能と考える。

<br>

</dt><dd>

- $M\sub\bm{R}^N$、$k$ 次元局所座標：$(U,\phi)\sub M$ とする。
このとき、
$$\forall p\in U\text{ に対して、}\\\exist\text{ 開集合} p\in V\sub\bm{R}^N,\ C^{\infty}\text{ 同相写像 }\psi:V\to\bm{R}^N\text{ であって、}\\\ \\
\psi(V\cap M)=\psi(V)\cap(\bm{R}^k\times\{0,0,...\}),\\\ \\
\psi(q)=(\phi(q),0,...),\quad(\forall q\in V\cap M)\\\ \\$$

- $M\sub\bm{R}^N$、$k_1$ 次元局所座標 $(U_1,\phi_1)\sub M$、$k_2$ 次元局所座標 $(U_2,\phi_2)\sub M$、$U_1\cap U_2\neq0$ とする。
このとき、
$$\phi_2\circ\phi_1^{-1}:\phi_1(U_1\cap U_2)\to \phi_2(U_1\cap U_2)$$
は $C^{\infty}$ 同相写像で、 特に $k_1=k_2$。
<br>

      ・次元の同一性はチェインルールによる。

</dd></dl>

### $C^k$ 同値と局所座標



---

## $R^N$ 内の多様体

・$M\sub\bm{R}^N$ とする。
このとき、$M$ が $k$ 次元多様体：
$$\forall p\in M\text{ に対して、}\exist k\text{ 次元局所座標が存在する}$$

    ・チャートの族でM=∪U：アトラス。
    ・第二可算、ハウスドルフは自明。局所コンパクトもよい。

---

### $R^N$ 内の部分多様体



<dl><dt>

・$k_1$ 次元多様体 $M_1\sub\bm{R}^N$、$k_2$ 次元多様体 $M_2\sub \bm{R}^N$ とする。
このとき、$M_2$ が $M_1$ の部分多様体：$M_2\sub M_1$
<br>

</dt><dd>

- $n$ 次元多様体 $M\sub\bm{R}^N$、$M$ の $k$ 次元部分多様体 $H\sub M$ とする。
このとき、$k\le n$ であって、
$$\forall\ H\text{ のチャート }(U,\phi)\text{ に対して、}\exist\ M\text{ のチャート }(V,\psi)\text{ であって、}\\\ \\
V\cap H\sub U,\quad \psi(V\cap H)=\psi(V)\cap(\bm{R}^k\times\{0,0,...\}),\\\ \\
\psi(q)=(\phi(q),0)\quad(\forall q\in V\cap H)$$
これは、一般の $m$ 次元 $C^{\infty}$ 多様体のときの正則部分多様体の定義と一致する。
<br>

      ・証明は結構ゴリ押しでいいみたい。
<br>

- $n$ 次元多様体 $M\sub\bm{R}^N$、部分集合 $H\sub M$ とする。
このとき、$1\le\exist k\le n$ であって、
$$\forall p\in H\text{ に対して、}\exist\ M\text{ のチャート }(U,\phi)\sub M\text{ であって、}\\\ \\
\psi(V\cap H)=\psi(V)\cap(\bm{R}^k\times\{0,0,...\})$$であるならば、
$H$ は $M$ の部分多様体であって、上記のチャート $(U,\phi)$ に対して、$(U\cap H,\psi_1,...,\psi_k)$ は $H$ のチャート。
これは、正則部分多様体の定義そのものである。
<br>

      ・別に{0,0,...}じゃなくても、定数ならよい！


</dd></dl>

---

# $R^N$ 内の多様体上の関数

    ・多様体への写像fは、R^lへの写像としてよい。
    ・一般の多様体と同じ。

---

# $R^N$ 内の多様体の接空間

・$n$ 次元多様体 $M\sub\bm{R}^N$、$p\in M$、$p$ 周りのチャート $(U,\phi)$ とする。
このとき、
$$T_pM=\mathrm{span}\left\{\frac{\partial \phi^{-1}}{\partial r^1}(\phi(p)),...,\frac{\partial\phi^{-1}}{\partial r^n}(\phi(p))\right\}$$
と定めると、これはチャートによらずwell-definedな $n$ 次元 $R$ 上ベクトル空間。また、$p$ の開近傍 $p\in D\sub M$ に対して、$T_pM=T_pD$
ここで、各 $\frac{\partial \phi^{-1}}{\partial r^i}(\phi(p))$ を $\frac{\partial}{\partial x^i}p$ と書く。
<br>

    ・偏微分作用素の空間ではない。また、T_pR^Nは標準基底が張る空間。

<br>

---

## 全微分 $df$

<dl><dt>

・$n$ 次元多様体 $M\sub\bm{R}^N$、$p\in M$、$p$ を含むチャート $(U,x^1,...,x^n)$、$p$ で微分可能な関数 $f:M\to \bm{R}^l$ とする。
このとき、
$$df_p:T_p(M)\to\bm{R}^l\\\ \\
df_p\left(\sum_{i=1}^na_i\frac{\partial}{\partial x^i}p\right)=\sum_{i=1}^na_i\frac{\partial f}{\partial x^i}(p)$$
と定めると、これは $R$-線形写像であって、別のチャート $(V,y^1,...,y^n)$ 上で
$$\sum_{i=1}^na_i\frac{\partial}{\partial x^i}p=\sum_{i=1}^nb_i\frac{\partial}{\partial y^i}p$$ならば
$$\sum_{i=1}^na_i\frac{\partial f}{\partial x^i}(p)=\sum_{i=1}^nb_i\frac{\partial f}{\partial x^i}(p)$$
より、チャートによらずwell-defined。
<br>

</dt><dd>

- $n_1,n_2$ 次元多様体 $M_1\sub\bm{R}^N,\ M_2\sub\bm{R}^l$、$p_1\in M_1$、$p_1$ で微分可能な関数 $f:M_1\to M_2$ とする。
このとき、$df_p(T_pM)\sub T_{f(p)}(M_2)$ であって、
$$d(f\circ g)_p=dg_{f(p)}\circ df_p$$



</dd></dl>

---

## $R^N$ 内の多様体の余接空間

    ・双対空間T_pM^*でよい。
<br>

・$n$ 次元多様体 $M\sub\bm{R}^N$、$p\in M$、$p$ を含むチャート $(U,x^1,...,x^n)$、$p$ で微分可能な関数 $f:M\to \bm{R}^l$ とする。
このとき、$dx_{i,p}\in T_p^*M$ は $\frac{\partial}{\partial}p$ に対する双対基底であって、
$$df_p=\sum_{i=1}^n\frac{\partial}{\partial x^i}dx_{i,p}$$

---

# 種々の定理

## 逆関数定理

## 埋め込み

---

## 陰関数定理

<dl><dt>

・$n$ 次元多様体 $M\sub\bm{R}^N$、開集合 $U\sub M$、$C^{\infty}$ 写像 $f_1,...,f_n:U\to\bm{R}$、$p\in M$ とする。
このとき、
$$df_{1,p},...,df_{n,p}\in T_p^*M\text{ が線形独立}\\\ \\
\Rightarrow\exist p\text{ の開近傍 }p\in U_0\sub U\text{ であって、}(U_0,f_1,...,f_n)\text{ は }M\text{ の局所座標}\\\ \\$$

</dt><dd>

- $1\le k\le n-1$ 個の $C^{\infty}$ 写像 $f_1,...,f_k:M\to\bm{R}$ とし、
$$H=\{p\in M\ |\ h_1(p)=...h_k(p)\}$$
このとき、
$$df_{1,p},...,df_{n,p}\in T_p^*M\text{ が線形独立}\\\ \\
\Rightarrow H\text{ は }M\text{ の }n-k\text{ 次元部分多様体であって、}\\
\forall p\in M,\ \forall p\text{ の周りの局所座標 }(U,x^1,...,x^n)\text{ に対して、}\exist\sigma\in S_n,\ \exist p\text{ の開近傍 }p\in U_0\sub U\text{ であって、}\\\ \\
(U_0\cap H,x_{\sigma(1)},...,x_{\sigma(n-k)})\text{ は }H\text{ の局所座標}\\\ \\$$


</dd></dl>

---

## Lagrange未定乗数法

・$1\le k\le n-1$ 個の $C^{\infty}$ 写像 $f_1,...,f_k:M\to\bm{R}$ とし、
$$H=\{p\in M\ |\ h_1(p)=...h_k(p)\}$$
とする。また、$C^1$ 写像 $g:M\to\bm{R}$、$p\in H$ とする。
このとき、
$$df_{1,p},...,df_{n,p}\in T_p^*M\text{ が線形独立であって、}g\text{ は }H\text{ 上 }p\text{ で極値を取る}\\\ \\
\Rightarrow \exist c_1,...,c_k\in\bm{R}\text{ であって、}dg_p=\sum_{i=1}^kc_idf_{i,p}\\\ \\$$

    ・H上pで極値：p周りのHの局所座標について、∂g/∂x^i=0

---


