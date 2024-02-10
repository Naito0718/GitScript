
- [$1$ 形式](#1-形式)
  - [余接束](#余接束)
      - [リウヴィル（ポアンカレ）形式](#リウヴィルポアンカレ形式)
  - [微分 $df$](#微分-df)
    - [双対基底 $dx$](#双対基底-dx)
    - [一形式の性質](#一形式の性質)
    - [引き戻し](#引き戻し)
- [微分 $k$ 形式](#微分-k-形式)
  - [余接束の $k$ 次外積 $Λ^k(T^＊M)$](#余接束の-k-次外積-λktm)
    - [$Λ^k(T^＊M)$ の多様体構造](#λktm-の多様体構造)
  - [$k$ 形式の性質](#k-形式の性質)
    - [ベクトル場との関係](#ベクトル場との関係)
    - [微分 $df$ のウェッジ積](#微分-df-のウェッジ積)
  - [$k$ 形式のウェッジ積](#k-形式のウェッジ積)




# $1$ 形式

## 余接束

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、余接束：
$$T^*M=\bigcup_{p\in M}(T_pM)^{\vee}$$
ここで、位相構造、多様体構造は接束とまったく同様に定められる。
さらに、$(T^*M,M,\pi,\bm{R}^m)$ は $C^{\infty}$ ベクトル束。

    ・非交和。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ 写像 $\omega:M\to T^*M$ とする。
このとき、
$$\omega\text{ は }C^{\infty}1\text{ 形式 }\iff \omega\text{ は }C^{\infty}\text{ 切断}\\\ \\$$

      ・各点pにT^*pMの元を割り当てる。
      ・結局係数関数がC^∞かどうかを見ればよい。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、
$$\Omega^1(M)=\{\omega:M\to T^*M\ |\ \omega\text{ は }C^{\infty}\text{ 一形式}\}$$
は $\bm{R}$ 上ベクトル空間。
<br>

      ・下で示した各成分との関係による。

---

#### リウヴィル（ポアンカレ）形式

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ ベクトル束 $(T^*M,M,\pi,\bm{R}^m)$ とする。
このとき、
$$\lambda:T^*M\to T^*(T^*M)\\\ \\
\lambda(\omega_p)(X_{\omega_p})=\omega_p(\pi_*(X_{\omega_p}))\\\ \\
(\omega_p\in T_p^*M,\ X_{\omega_p}\in T_{\omega_p}(T^*M),\ \lambda(\omega_p)\in T^*_{\omega_p}(T^*M))$$
と定めると、これはwell-defined。
これをリウヴィル（ポアンカレ）形式という。

    ・定義にチャートを用いない。
    ・アーノルド、p.202

- リウヴィル形式は、引き戻しの言葉を用いると、
$$\lambda(\omega)=\pi^*(\omega)$$
と書ける。
したがって、$\lambda\in\Omega^1(T^*M)$

---

## 微分 $df$

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ 写像 $f:M\to\bm{R}$、$p\in M$ とする。
このとき、微分 $(df)_p$：
$$(df)_p\in (T_pM)^{\vee}\\\ \\
(df)_p(X_p)=X_pf$$

    ・dfはMから余拙速への写像。
    ・f_*は接束から接束への写像？？
<br>

- $$f_{*}(X_p)=(df)_p(X_p)\left.\frac{d}{dt}\right|_{f(p)}$$
したがって、同一視 $T_{f(p)}\bm{R}\leftrightarrow\bm{R}$ において、$f_{*}$ と $df$ は同じ。
<br>

- $$p\in M\text{ が }f\text{ の臨界点}\iff (df)_p=0$$

---

    ・一応係数のC^∞を示した後
<br>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ 写像 $f:M\to\bm{R}$ とする。
このとき、
$$df:M\to T^M\\\ \\
(df)(p)=df_p$$
は $C^{\infty}$ 一形式


---

### 双対基底 $dx$

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$p\in M$ とする。
このとき、$(dx^i)_p$ は $(T_pM)^{\vee}$ の双対基底。ただし、対応：$\partial/\partial x^i|_p\leftrightarrow (dx^i)_p$

    ・xはC^∞写像。
    ・dx^iはチャート(U,φ)上の1形式。
<br>

</dt><dd>


- $C^{\infty}$ 写像 $f:M\to\bm{R}$、チャート $(U,\phi)$、$p\in U$ とする。
このとき、
$$(df)_p=\sum\left.\frac{\partial f}{\partial x^i}\right|_p(dx^i)_p\\\ \\$$

- ・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)\sub M$ とする。
このとき、
$$dx^i:U\to T^*U$$
は $C^{\infty}$ 枠。

</dd></dl>

---

### 一形式の性質

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)\sub M$、一形式 $\omega:U\to T^*U$ とする。
このとき、
$$\omega\text{ は }C^{\infty}\iff\omega=\sum a_idx^i\text{ としたとき、}a^i:U\to\bm{R}\text{ は }C^{\infty}\\\ \\$$

</dt><dd>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ ベクトル束 $(T^*M,M,\pi,\bm{R}^m)$ とする。
このとき、
$$\Omega(M)=\{\omega:M\to T^*M\ |\ \omega\text{ は }C^{\infty}\text{ 切断}\}\\\ \\
(\omega_1+\omega_2)(p)=\omega_1(p)+\omega_2(p)\\\ \\
(\alpha\omega)(p)=\alpha(\omega(p))$$
と定めると、これは $\bm{R}$ 上ベクトル空間。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、一形式 $\omega:M\to T^*M$ とする。
このとき、
$$\omega\text{ が }C^{\infty}\\\ \\
\iff\exist\text{ アトラス }\{U_{\alpha},\phi_{\alpha}\}\text{ であって、}\\
\forall\text{ チャート }(U_{\alpha},\phi_{\alpha})\text{ 上で枠 }dx^i\text{ の係数 }a_i\text{ が }C^{\infty}\\\ \\
\iff\forall\text{ チャート }(U_{\alpha},\phi_{\alpha})\text{ に対して、枠 }dx^i\text{ の係数 }a_i\text{ が }C^{\infty}\\\ \\
$$

</dd></dl>

---

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、一形式 $\omega:M\to T^M$、ベクトル場 $X:M\to TM$ とする。
このとき、
$$\omega(X):M\to\bm{R}\\\ \\
\omega(X)(p)=\omega_p(X_p)$$
と定める。
<br>

- $\omega=\sum a_idx^i,\ X=\sum b^i\frac{\partial}{\partial x^i}$ とすると、
$$\omega(X)=\sum a_ib^i\\\ \\$$

      ・チャート上の話。
<br>

</dt><dd>

- $f:M\to\bm{R}$ とする。
このとき、
$$\omega(fX)=f\omega(X)$$

      ・fX(p)=f(p)X_p。fω(X)はただの実関数の積。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、一形式 $\omega:M\to T^*M$ とする。
このとき、
$$\omega\text{ は }C^{\infty}\\\ \\
\iff\forall C^{\infty}\text{ ベクトル場 }X:M\to TM\text{ に対して、}\\
\omega(X):M\to\bm{R}\text{ が }C^{\infty}\\\ \\$$

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ 一形式 $\omega:M\to T^*M$ とする。
このとき、
$$F:X^{\infty}(M)\to C^{\infty}(M)\\\ \\
F_{\omega}(X)=\omega(X)$$
は $\bm{R}$-線形かつ 単位的可換環 $C^{\infty}$ 上線形。


</dd></dl>

---

### 引き戻し



<dl><dt>

・$m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$ とする。
このとき、余微分 $F^*$：
$$F^*_p:(T_{F(p)}N)^{\vee}\to (T_pM)^{\vee}\\\ \\
F_p^*(\omega_{F(p)})=\omega_{F(p)}\circ F_{*,p}$$
はwell-definedな線形写像。
ここで、$F^*_p(\omega_p)$ を $F$ によるコベクトル $\omega_{F(p)}$ の引き戻しという。

    ・双対のこと。Category参照。

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$ とする。
このとき、関数の引き戻し：
$$F^*:C^{\infty}(N)\to C^{\infty}(M)\\\ \\
F^*(f)=f\circ F$$
はwell-definedな線形写像。
<br>

</dt><dd>

- 一形式 $\omega:N\to T^*N$ とする。
このとき、
$$F^*\omega:M\to T^*M\\\ \\
(F^*\omega)(p)=F^*_p(\omega_{F(p)})$$
は $M$ 上の一形式。

      ・C^∞とかはない。
<br>

- $m,n$ 次元 $C^{\infty}$ 多様体 $M,N$、$C^{\infty}$ 写像 $F:M\to N$、$\omega,\tau\in\Omega^1(N)$、$g\in C^{\infty}(N)$ とする。
このとき、
$$F^*(\omega+\tau)=F^*(\omega)+F^*(\tau)\\\ \\
F^{*}(g\omega)=(F^*g)(F^*\omega)$$

<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ 写像 $F:M\to N$、$\omega\in\Omega^1(N)$ とする。
このとき、
$$F^*\omega\in\Omega^1(M)\\\ \\$$
また、このときあるチャート $(U,\phi)\sub M$、$(V,\psi)\sub N$、$F(U)\sub V$ が存在して、
$$F^*(\omega)=\sum (a_i\circ F)\frac{\partial F^i}{\partial x^j}dx^j\quad(U\text{ 上})\\\ \\$$

<br>

- $h\in C^{\infty}(M)$ とする。
このとき、
$$F^*(dh)=d(F^*h)\\\ \\$$

      ・一形式の引き戻しと、関数の引き戻し。
<br>

</dd></dl>

---


# 微分 $k$ 形式

    ・とりあえず、同型なk次外積の形を区別せずに用いる。結局C^∞性とかで同値。

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、$k\ (\le m)$ 形式 $\omega$：
$$\text{各点 }p\in M\text{ に対して、}\omega_p\in(\Lambda^k(T_pM))^{\vee}\\\ \\$$

- $m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)$、$k$ 形式 $\omega$ とする。
このとき、チャート $U$ 上において、
$$\omega_p=\sum a_I(p)dx^I\quad(\forall p\in U)$$
と書ける。
<br>

      ・結局同型だから、この形で展開できてる。

---


## 余接束の $k$ 次外積 $Λ^k(T^＊M)$

・$m$ 次元 $C^{\infty}$ 多様体 $M$ とする。
このとき、余接束の $k$ 次外積 $\Lambda^k(T^*M)$：
$$\Lambda^k(T^*M)=\bigcup_{p\in M}\Lambda^k((T_pM)^{\vee})\cong\bigcup_{p\in M}(\Lambda^k(T_pM))^{\vee}\ \ (\bm{R}-\text{同型})$$

- $m$ 次元 $C^{\infty}$ 多様体 $M$、余接束の $k$ 次外積 $\Lambda^k(T^*M)$ とする。
このとき、射影 $\pi$：
$$\pi:\Lambda^k(T^*M)\to M\\\ \\
\pi(\alpha)=p$$
はwell-defined。


---

### $Λ^k(T^＊M)$ の多様体構造

・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)\sub M$、余接束の $k$ 次外積 $\Lambda^k(T^*M)$ とする。
このとき、
$$\psi:\Lambda^k(T^*U)\to\phi(U)\times\bm{R}^{\binom{n}{k}}\\\ \\
\psi(\alpha)=(\phi(p), \{c_I(\alpha)\})$$
と定めると、$\psi$ は全単射。
したがって、この $\psi$ によって $\Lambda^k(T^*M)$ に位相を入れることで、接束 $TM$ と全く平行に定理が成り立つ。特に、$(\Lambda^k(T^*M),M,\pi,\bm{R}^{\binom{n}{k}})$ は 階数 $\binom{n}{k}$ の $C^{\infty}$ ベクトル束。

    ・結局ここで全単射でつないだので、A_k(V)でもΛ^k(V^*)でも議論は平行。よって、C^∞性も同値が成り立つ。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ ベクトル束 $(\Lambda^k(T^*M),M,\pi,\bm{R}^{\binom{n}{k}})$、$\omega:M\to \Lambda^k(T^*M)$ とする。
このとき、
$$\omega\text{ は }k\text{ 形式}\iff\omega\text{ は切断}$$
よって、$C^{\infty}$ $k$ 形式を、$C^{\infty}$ 切断であることとして定める。

---

## $k$ 形式の性質

・$0$ 形式 $\omega:M\to \Lambda^0(T^*M)$ は単に実数値関数。
したがって、
$$\Omega^0(M)=C^{\infty}(M)\\\ \\$$

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$k$ 形式 $\omega:M\to\Lambda^k(T^*M)$ とする。
このとき、$k>m$ ならば、$\omega=0$
<br>

---

・$m$ 次元 $C^{\infty}$ 多様体 $M$、開近傍 $p\in U\sub M$、$C^{\infty}$ $k$ 形式 $\omega:U\to \Lambda^k(T^*U)$ とする。
このとき、
$$\exist\text{ 開近傍 }V\sub\mathcal{N}(p),\ \exist\ C^{\infty}\ k\text{ 形式 }\tilde{\omega}:M\to\Lambda^k(T^*M)\text{ であって、}\\\ \\
\omega(q)=\tilde{\omega}(q)\quad(\forall q\in V)$$

      ・いつもの拡張。

---

### ベクトル場との関係

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$k$ 形式 $\omega:M\to \Lambda^k(T^*M)$、ベクトル場 $X_1,...,X_k:M\to TM$ とする。
このとき、
$$\omega(X_1,...,X_k):M\to\bm{R}\\\ \\
\omega(X_1,...,X_k)(p)=\omega(p)(X_{1}(p)\wedge...\wedge X_{k}(p))$$
と定めると、これはwell-defined。
<br>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$k$ 形式 $\omega:M\to \Lambda^k(T^*M)$、ベクトル場 $X_1,...,X_k:M\to TM$、$h:M\to\bm{R}$ とする。
このとき、
$$\omega(X_1,...,hX_i,...,X_k)=h\omega(X_1,...,X_i,...,X_k)\\\ \\$$

      ・hω、hX_iは普通にスカラー倍みたいな定義でよい。
<br>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$k$ 形式 $\omega:M\to \Lambda^k(T^*M)$ とする。
このとき、
$$\omega\text{ は }C^{\infty}\\\ \\
\iff\forall C^{\infty}\text{ ベクトル場 }X_1,...,X_k:M\to TM\text{ に対して、}\\
\omega(X_1,...,X_k):M\to\bm{R}\text{ が }C^{\infty}\\\ \\$$

---


### 微分 $df$ のウェッジ積

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi)$、$f^1,...,f^k\in C^{\infty}(U)$ とする。
このとき、
$$df^1\wedge...\wedge df^k=\sum_I \frac{\partial (f^1,...,f^k)}{\partial x^I}dx^I$$
したがって、$df^I$ は $C^{\infty}$ $k$ 形式。

    ・df^I：M→Λ^k(T^*U)の切断である。
    ・明らかに1形式のときと整合する。
<br>

</dt><dd>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、チャート $(U,\phi),\ (V,\psi)$、$k$ 形式 $\omega:U\cap V\to \Lambda^k(T^*(U\cap V))$ とし、$\omega=\sum a_Idx^I=\sum b_Idy^I$ とする。
このとき、$(U\cap V)$ 上において、
$$dy^J=\sum_I\frac{\partial y^J}{\partial x^I}dx^I\\\ \\
a_I=\sum_J\frac{y^J}{x^I}b_J$$


</dd></dl>

---

## $k$ 形式のウェッジ積

    ・k形式全体、C^∞k形式全体Ω^k(M)はR上ベクトル空間。

<dl><dt>

・$m$ 次元 $C^{\infty}$ 多様体 $M$、$k$ 形式 $\omega:M\to\Lambda^k(T^*M)$、$l$ 形式 $\tau:M\to\Lambda^l(T^*M)$ とする。
このとき、
$$\omega\wedge\tau:M\to\Lambda^{k+l}(T^*M)\\\ \\
(\omega\wedge\tau)(p)=\omega(p)\wedge\tau(p)$$
と定めると、これはwell-defined。

    ・どっちももとになるベクトル空間が一致してるからよい。

<br>

</dt><dd>

- $m$ 次元 $C^{\infty}$ 多様体 $M$、$C^{\infty}$ $k$ 形式 $\omega:M\to\Lambda^k(T^*M)$、$C^{\infty}$ $l$ 形式 $\tau:M\to\Lambda^l(T^*M)$ とする。
このとき、$\omega\wedge\tau$ は $C^{\infty}$ $k+l$ 形式。


</dd></dl>

---

