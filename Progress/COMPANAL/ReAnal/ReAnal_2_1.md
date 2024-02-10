

- [多変数実解析的写像](#多変数実解析的写像)
  - [複素解析関数と実解析関数](#複素解析関数と実解析関数)
    - [拡張](#拡張)
    - [制限](#制限)
  - [演算](#演算)
    - [和,積,合成](#和積合成)
  - [逆関数定理](#逆関数定理)
- [収束する指数写像](#収束する指数写像)
- [実解析関数と常微分方程式](#実解析関数と常微分方程式)



# 多変数実解析的写像

・$u\in\bm{R}^n$、領域 $u\in U\sub\bm{R}^n$、$f:U\to\bm{R}$ とする。
このとき、$f$ が実解析的：
$$\exist\text{ 収束 }n\text{ ベキ級数 }F(x)\text{ であって、}\\\ \\
f(\xi)=F(\xi-u)=\sum a_I(\xi-u)^I\quad(\forall\xi\in U)$$
ここで、領域 $U\sub\bm{R}^n$ 上の各点で実解析的であるとき、$f$ を $U$ 上実解析的という。

    ・F_uをベキ級数展開とも言う。

- 領域 $U\sub\bm{R}^n$ 上実解析的な $f:U\to\bm{R}$ とする。
このとき、$f$ は $U$ 上 $C^{\infty}$ で、各点のベキ級数展開は一意的に定まる。

      ・一般のBanach～では微分はできない。


## 複素解析関数と実解析関数

### 拡張

・領域 $U\sub\bm{R}^N$、$u\in\bm{R}^N$、$u$ で実解析的な $f:U\to\bm{R}$、ベキ級数展開 $F_u$ とする。
このとき、$f$ の拡張 $\tilde{f}$：
$$\exist\text{ 領域 }u\in\tilde{U}\sub\bm{C}^N\text{ であって、}\\\ \\
\tilde{f}(\xi)=F(\xi-u)\quad(\forall\xi\in\tilde{U})\\\ \\
\text{ なる }\tilde{f}:\tilde{U}\to\bm{C}\\\ \\$$
ここで、$\tilde{f}$ は明らかにwell-definedで一意的に定まる。

---

### 制限

・領域 $U\sub\bm{C}^N$、$u\in\bm{C}^N$、$u$ で実解析的な $f:U\to\bm{C}$、ベキ級数展開 $F_u$ とする。
このとき、$f$ の制限 $f_R$：
$$u\in\bm{R}^N\text{ であって、}\\\ \\
f_R:U\cap\bm{R}^N\to\bm{C}\text{ において値域が }\bm{R}\text{ であるとき}$$
ここで、$f_R$ は明らかにwell-definedで一意的に定まる。

    ・すべての係数が当然実数でなければならない。複素数が発生するなら消えなければならないので0としてよい。

## 演算

### 和,積,合成

<dl><dt>

・収束ベキ級数 $F(\bm{x})\in\bm{R}[\bm{x}]$、$(r_1,...,r_N)\in\Gamma$ とする。
このとき、
$$f:\{\bm{\xi}\in\bm{R}^N\ |\ |\xi_i|<r_i\}\to\bm{R}\\\ \\
f(\bm{\xi})=F(\bm{\xi})$$
と定めると、これは実解析関数。

    ・複素数に拡張！

</dt><dd>

- 領域 $U\sub\bm{R}^N$、実解析関数 $f,g:U\to\bm{R}$ とする。
このとき、
$$f+g,fg\\\ \\
\forall \xi\in U\text{ に対して }f(\xi)\neq0\text{ なときの}1/f$$
はすべて実解析関数。
<br>

      ・実数倍も含む。
<br>

- $u\in\bm{R}^N$、領域 $u\in U\sub\bm{R}^N$、実解析関数 $g_1,...,g_M:U\to\bm{R}$、領域 $(\bm{g(u)})\in V\sub\bm{R}^M$、実解析関数 $f:V\to\bm{R}$ とする。
このとき、
$$f\circ \bm{g}:U\to\bm{R}$$
は実解析関数。

</dd></dl>

---

## 逆関数定理

・領域 $U\sub\bm{R}^N$、実解析関数 $f:U\to\bm{R}^N$、$u\in U$、$\det J(u)\neq0$ とする。
このとき、
$$\exist \text{ 開近傍 }V\in\mathcal{N}(u),\ V\sub U\text{ であって、}\\\ \\
\phi^{-1}:\phi(V)\to V\text{ が存在して実解析写像}$$

      ・？？？連続群論の基礎,p.120




# 収束する指数写像

<dl><dt>

・Banach単位的 $\bm{C,R}$-代数 $A$ とする。
このとき、
$$\exp:A\to A\\\ \\
\exp(\alpha)=\sum\frac{1}{n!}\alpha^n$$ は連続関数。
<br>

</dt><dd>

- $$\log:\{\alpha\in A\ |\ \|\alpha-1_A\|\le 1\}\to A\\\ \\
\log(\alpha)=\sum_{n\ge1}\frac{(-1)^{n-1}}{n}(\alpha-1_A)^n$$は連続関数。
<br>

- $$U=\{\alpha\in A\ |\ \|\alpha-1_A\|<1/2\},\quad N=\log U,\\\ \\
N_0=\{\alpha\in A\ |\ \|\alpha\|<\log 2\}$$ とする。
このとき、$\exp$ は $N_0$ 上単射で　
$$\log(\exp\alpha)=\alpha\ \ (\forall\alpha\in N_0)$$ であって、$N$ は$$N\sub N_0,\quad\exp N=U$$を満たす $0_A$ の開近傍。
さらに、$U$ は $1_A$ の開近傍で、開集合 $U,N$ は $\exp,\log$ によって同相。

</dd></dl>

---

# 実解析関数と常微分方程式