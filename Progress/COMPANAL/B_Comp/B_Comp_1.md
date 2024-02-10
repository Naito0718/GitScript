
    ・複素解析（小平）

- [複素線積分](#複素線積分)
  - [曲線上の連続関数全体と複素線積分](#曲線上の連続関数全体と複素線積分)
  - [重積分](#重積分)
- [複素Banach空間値正則関数](#複素banach空間値正則関数)
  - [ベキ級数](#ベキ級数)
- [Banach空間値正則関数の性質](#banach空間値正則関数の性質)
  - [原始関数](#原始関数)
  - [Liouvilleの定理,一致の定理](#liouvilleの定理一致の定理)
  - [Laurant展開](#laurant展開)
  - [留数定理](#留数定理)

# 複素線積分

<dl><dt>

・$\bm{C}$ 上Banach空間 $X$、区分的 $C^1$ 曲線 $C_1,...,C_k\sub\bm{C}$、連続関数 $f:\bigcup_{i=1}^kC_i\to X$ とする。
このとき、$(f\circ c_i)c'_i\in\mathcal{L}^1(I_i,m)$ であって、
$$I_c(f)=\sum_{i=1}^k\int_{I_i}f(c_i(t))c'_i(t)dt\quad(\text{Bochner積分})$$
はwell-definedであって、$$\forall \phi\in B^{\vee}\text{ に対して、}\phi(I_c(f))=\int_{\bigcup_{i=1}^kC_i}(\phi\circ f)(z)dz\quad(\text{複素線積分})$$
ここで、$I_c(f)$ を $f$ の複素線積分といい、$$I_c(f)=\int_{\bigcup_{i=1}^kC_i}f(z)dz$$ と書く。
<br>

    ・明らかに積分曲線の加法性が成り立つ。
<br>

</dt><dd>

- $\bm{C}$ 上Banach空間 $X$、区分的 $C^1$ 曲線 $C_1,...,C_k$、連続関数 $f:\bigcup_{i=1}^kC_i\to X$、$x\in X$ とする。
このとき、$$\forall \phi\in B^{\vee}\text{ に対して、}\phi(x)=\int_{\bigcup_{i=1}^kC_i}(\phi\circ f)(z)dz\\\ \\
\iff x=\sum_{i=1}^k\int_{I_i}f(c_i(t))c'_i(t)dt$$
すなわち、この意味で複素線積分は一意的。
<br>

- 
$$\left\|\int_{\bigcup_{i=1}^kC_i}f(z)dz\right\|\le\sup_{z\in \bigcup_{i=1}^kC_i}f(z)l(C)<\infty\\\ \\$$

- $b\in X$ とする。
このとき、
$$\int_{C}bdz=l(C)b$$


</dd></dl>

---

## 曲線上の連続関数全体と複素線積分

・$\bm{C}$ 上Banach空間 $X$、区分的 $C^1$ 曲線 $C_1,...,C_k\sub\bm{C}$、連続関数 $c=\bigcup_{i=1}^kC_i$ とする。
このとき、
$$C(c,X)=\{f:c\to X\ |\ f\text{ は連続}\}\\\ \\
\|\cdot\|:C(c,X)\to[0,\infty),\quad\|f\|=\sup_{x\in c}\|f(x)\|\\\ \\
\psi:C(c,X)\to X,\quad\psi(f)=\int_cf(z)dz$$
と定めると、$C(c,X)$ は $\|\cdot\|$ をノルムとする $\bm{C}$ 上Banach空間で、$\psi$ は
$$\sup_{\|f\|=1}\|\psi(f)\|\le l(c)$$
を満たす有界線形写像。

---

## 重積分

<dl><dt>

・$\bm{C}$ 上Banach空間 $X$、$\bm{C}$ 内の区分的 $C^1$ 曲線 $C$、コンパクト集合 $K\sub\bm{C}$、連続関数 $f:C\times K\to X$ とする。
このとき、
$$g:K\to X\\\ \\
g(z)=\int_Cf(z,w)dw$$
と定めると、$g$ は連続関数。
<br>

</dt><dd>

- $\bm{C}$ 内の区分的 $C^1$ 曲線 $C_1,C_2$、連続関数 $f:C_1\times C_2\to X$ とする。
このとき、
$$g_i:C_i\to X\\\ \\
g_i(z)=\int_{C_j}f(z_1,z_2)dw(z_j)$$
と定めると、これは連続関数であって、
$$\int_{C_1}\left(\int_{C_2}f(z,w)dw\right)dz=\int_{C_2}\left(\int_{C_1}f(z,w)dz\right)dw$$

</dd></dl>

---

# 複素Banach空間値正則関数

<dl><dt>

・開集合 $\Omega\sub\bm{C}$、$\bm{C}$ 上Banach空間 $X$、$f:\Omega\to X$、$z_0\in\Omega$ とする。
このとき、$f$ が $z_0$ で複素微分可能：
$$\exist b\in X\text{ であって、}\\\ \\
f'_{z_0}:\Omega\to X\\\ \\
f'_{z_0}(z)=\begin{cases}
\frac{f(z)-f(z_0)}{z-z_0}  & (z\neq z_0)  \\
b  & (z=z_0)  \\
\end{cases}\\\ \\
\text{ が }z_0\text{ で連続}\\\ \\$$
ここで、$f'_{z_0}(z_0)=b$ の値は存在すればただ一つであって、$f$ が $z_0$ で複素微分可能ならば、$f$ は $z_0$ で連続。
また、$\forall z\in \Omega$ で $f$ が複素微分可能なとき、$f':\Omega\to X$ を $f$ の複素導関数といい、$f'$ が連続ならば正則であるという。
<br>

    ・n階微分も同様。
<br>

</dt><dd>

- $z_0\in\Omega$ で複素微分可能な $f,g:\Omega\to X$、$\phi:\Omega\to\bm{C}$ とし、$\alpha\in\bm{C}$ とする。
このとき、
$$f+g,\ \alpha f,\ \phi f,\ fg\text{ は }z_0\text{ で複素微分可能であって、}\\\ \\
(f+g)'_{z_0}(z_0)=f'_{z_0}(z_0)+g'_{z_0}(z_0),\quad (\alpha f)'_{z_0}(z_0)=\alpha f'_{z_0}(z_0)\\\ \\
(\phi f)'_{z_0}(z_0)=\phi'_{z_0}(z_0)f(z_0)+\phi(z_0)f'_{z_0}(z_0),\quad (fg)'_{z_0}(z_0)=f'_{z_0}(z_0)g(z_0)+f(z_0)g'_{z_0}(z_0)$$
特に、$f,g,\phi$ が $\Omega$ 上正則ならば、$f+g,\ \alpha f,\ \phi f,\ fg$ は $\Omega$ 上正則。

</dd></dl>




---

## ベキ級数

    ・Hilbert_5_1参照
<br>

・$\bm{C}$ 上Banach空間 $X$、収束半径 $R>0$ の点列 $(x_n)\sub X$ とする。
このとき、
$$f:B(0,R)\to X\\\ \\
f(z)=\sum x_nz^n$$
と定めると、$f$ は何回でも微分可能であって、
$$f^{(k)}(z)=\sum_{n\in\bm{N}}\frac{(n+k)!}{n!}x_{n+k}z^n$$
特に、導関数に現れる点列 $\left(\frac{(n+k)!}{n!}x_{n+k}\right)_{n\in\bm{N}}$ の収束半径は $R$。


---

# Banach空間値正則関数の性質



・領域 $\Omega\sub\bm{C}$、$\bm{C}$ 上Banach空間 $X$、連続関数 $f:\Omega\to X$ とする。
このとき、
$$f\text{ は }\Omega\text{ 上正則}\\\ \\
\iff\forall\phi\in X^*\text{ に対して、}\phi\circ f:\Omega\to\bm{C}\text{ は }\Omega\text{ 上正則}\\\ \\
\iff \forall\text{ ホモローグ }0\text{ の }\Omega\text{ 内の区分的 }C^1\text{ サイクル }C\text{ に対して、}\\\ \\
\forall z\in \Omega-C\text{ に対して、}n(C,a)f(z)=\frac{1}{2\pi i}\int_C\frac{f(w)}{w-z}dw\\\ \\
\iff f\text{ は }\Omega\text{ 上何回でも複素微分可能であって、}\\\ \\\forall z\in B(a,r)\sub\Omega\text{ に対して、}f(z)=\sum\frac{f^{(n)}(a)}{n!}(z-a)^n\\\ \\$$
特に、$\Omega$ 上正則な $f$ に対して、
$$\frac{d}{dz}(\phi\circ f)(z)=(\phi\circ f')(z)$$
であって、
$$\forall D\text{ 内の区分的 }C^1\text{ 閉曲線 } C\sub D\text{ に対して、}\int_Cf'(z)dz=0\\\ \\
\forall\text{ ホモローグ }0\text{ の }\Omega\text{ 内の区分的 }C^1\text{ サイクル }C\text{ に対して、}\int_Cfdz=0\\\ \\$$

---

## 原始関数

・$\bm{C}$ 上Banach空間 $X$、$a\in D$ で星形な領域 $D\sub\bm{C}$、$p\in D$、$p$ を除いて正則な連続関数 $f:D\to X$ とする。
このとき、$D$ 上で $f$ の原始関数 $F$ が存在する。特に、$D$ 内の任意の区分的 $C^1$ 閉曲線 $C\sub D$ に対して、
$$\int_Cf(z)dz=0\\\ \\$$

---

## Liouvilleの定理,一致の定理

<dl><dt>

・領域 $\Omega\sub\bm{C}$、$\bm{C}$ 上Banach空間 $X$、正則関数 $f:\Omega\to X$ とする。
このとき、
$$\forall B(a,R)\sub\Omega\text{ に対して、}\\\ \\
\|f^{(n)}(a)\|\le\frac{n!}{R^n}\sup_{z\in\partial B(a,R)}|f(z)|\\\ \\$$

</dt><dd>

- 有界正則関数 $f:\bm{C}\to X$ とする。
このとき、$f$ は定数関数。
<br>

- 領域 $\Omega\sub\bm{C}$、$\bm{C}$ 上Banach空間 $X$、正則関数 $f:\Omega\to X$、$a\in\Omega$ とする。
このとき、
$$\exist w\in\Omega\text{ であって、}\forall n\in\bm{N}\text{ に対して、}f^{(n)}(w)=0\\\ \\
\Rightarrow f(z)=0\quad(\forall z\in\Omega)\\\ \\$$

- 領域 $\Omega\sub\bm{C}$、$\bm{C}$ 上Banach空間 $X$、正則関数 $f,g:\Omega\to X$、$a\in\Omega$ とする。
このとき、
$$a\in\bm{C}\text{ に収束する }\exist \text{ 点列 }(z_n)\sub\Omega\text{ であって、}\\\ \\
(1):f(z_n)=g(z_n)\forall n\in\bm{N}\\\ \\
(2):\forall n\in\bm{N}\text{ に対して、}z_n\neq a\\\ \\
\Rightarrow f(z)=g(z)\quad(\forall z\in\Omega)\\\ \\$$

</dd></dl>

---

## Laurant展開

## 留数定理
