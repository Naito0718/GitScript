
- [Bochner積分](#bochner積分)
  - [Bochner可測関数](#bochner可測関数)
        - [Buchner可測関数](#buchner可測関数)
        - [Bochner可測関数の単関数近似](#bochner可測関数の単関数近似)
  - [Banach空間値 $L^p$ 関数](#banach空間値-lp-関数)
        - [Hilbert空間値 $L^2$ 関数](#hilbert空間値-l2-関数)
  - [Bochner積分](#bochner積分-1)
        - [定義](#定義)
        - [Bochner積分の性質](#bochner積分の性質)
        - [Bochner-Lebesgue優収束定理](#bochner-lebesgue優収束定理)
        - [Bochner-Fubiniの定理](#bochner-fubiniの定理)




# Bochner積分

## Bochner可測関数

##### Buchner可測関数

・Bochner可測：可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$f:X\to B$ とする。
このとき、
- $f(X)$ は可分
- $\forall \phi\in B^*$ に対して、$\phi\circ f:X\to\bm{R,C}$ が可測

であるとき、$f$ をBochner可測であるという。

・Bochner可測単関数：可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$、$f:X\to B$ とする。
このとき、
- $f(X)$ は有限集合
- $\forall \phi\in B^*$ に対して、$\phi\circ f:X\to\bm{R,C}$ が可測

であるとき、$f$ をBochner可測単関数という。

    ・Bochner可測単関数ならば、Bochner可測関数
    ・定数関数はBochner可測単関数

<br>

・$\bm{注意}$：ノルム空間 $B$ に対して、$A\subset B$ が可分ならば、$\mathrm{span}A$ も可分

- $A,B$ が可分ならば、$A+B,\bm{F}A$ も可分

---
可測空間 $(X,\mathfrak{M})$、$\bm{R,C}$ 上Banach空間 $B$ とする。

- Bochner可測関数 $f,g:X\to B$、可測関数 $h:X\to\bm{R,C}$ に対して、
$f+g,hf$ はBochner可測関数
<br>

- 各点収束極限 $\lim_{n\to\infty}f_n(x)=f(x)$ を持つBochner可測関数列 $f_n:X\to B$ に対して、
$f$ はBochner可測関数。
<br>

- Bochner可測関数 $f:X\to B$ に対して、
$\|f\|$ は可測関数。
<br>

- $f:X\to B$ に対して、
$f$ はBochner可測単関数$\iff\exist b_1,...,b_n\in B$ とある有限可測分割 $E_1,...,E_n\subset\mathfrak{M}$ であって、$$f=\sum_{i=1}^n\chi_{E_i}(x)b_i$$

---

##### Bochner可測関数の単関数近似

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、Bochner可測関数 $f:X\to B$ とする。
このとき、
$$\|s_n(x)\|\le\|f(x)\|\ (\forall n\in\bm{N},\forall x\in X)\\\ \\
\lim_{n\to\infty}s_n(x)=f(x)\ (\mu-a.e.)$$ を満たすBochner可測単関数列 $s_n$ が存在する。

 ---

 ・可測空間 $(X,\mathfrak{M})$、$\bm{C,R}$ 上Banach空間 $B$、$E\in\mathfrak{M}$ に対して、
 $E$ 上の準可測単関数 $f:X\to B$：
$$\forall\epsilon>0\ {に対して、}\ \exist\ {有限可測分割}\ E_1,...,E_n\subset E\ {であって、}\\\ \\
\forall j\in{1,...,n},\ \forall x,y\in E_j\ \|f(x)-f(y)\|<\epsilon\\\ \\$$ 

    ・このとき、fは任意の可測集合F⊂Eでも準可測単関数


・ 測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$ に対して、
性質 $P(\mu)$ を満たす関数 $f:X\to B$：
$$\forall \mu{-有限な}\ E\in\mathfrak{M},\ \forall\epsilon>0\ {に対して、}\\\ \\
\exist F\subset E,\ \mu(E-F)<\epsilon\ {を満たす}\ F\in\mathfrak{M}\ {であって、}\\\ \\
f\ {は}\ {F}\ {上準可測単関数}$$ 

- 測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$ 、Bochner可測関数 $f:X\to B$ とする。
このとき、$f$ は性質 $P(\mu)$ を満たす。

---

## Banach空間値 $L^p$ 関数

    ・そもそもBochner可測関数ならL^1？

・可測空間 $(X,\mathfrak{M})$、$\bm{C,R}$ 上Banach空間 $B$ とする。
このとき、Bochner可測関数全体 $$\mathcal{L}(X,\mathfrak{M},B)$$は $\bm{C,R}$ 上ベクトル空間。

- 測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、Bochner可測関数全体 $\mathcal{L}(X,\mathfrak{M},B)$ とする。
このとき、同値関係と演算：
$$f\sim g\iff f(x)=g(x)\quad (\mu-a.e.)\\\ \\
[f]+[g]=[f+g],\quad \alpha[f]=[\alpha f]$$はwell-defined
この同値関係によって、$L(X,\mathfrak{M},B,\mu)$ を定義する。


---

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$p\in[1,\infty)$、$f\in L(X,\mathfrak{M},B,\mu)$ とする。
このとき、$$\|f\|_{p}=\left(\int\|f(x)\|^pd\mu\right)^{\frac{1}{p}}$$で定義すると、これはノルム。

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$f\in L(X,\mathfrak{M},B,\mu)$ とする。
このとき、$$\|f\|_{\infty}=\inf\{\alpha\in[0,\infty)\ |\ \mu((\alpha<\|f(x)\|))=0\}\\\ \\
({右辺が空なら}\ \infty)$$で定義すると、これはノルム。


- $[f]=[g]\Rightarrow \|f\|_{p,\infty}=\|g\|_{p,\infty}$

- $L^{p,\infty}(X,B)=\{f\in L(X,B)\ |\ \|f\|_{p,\infty}<\infty\}$ はBanach空間

---

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$p\in[1,\infty)$、$f\in \mathcal{L}^p(X,B)$ とする。
このとき、
$$\|s_n(x)\|\le\|f(x)\|\ (\forall n\in\bm{N},\forall x\in X)\\\ \\
\lim_{n\to\infty}\|f-s_n\|_{\mu,p}=0$$を満たすBochner可測単関数 $s_n\in \mathcal{L}^p(X,B)$ が存在する。

---

##### Hilbert空間値 $L^2$ 関数

・測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Hilbert空間 $\mathcal{H}$、$f,g\in L^2(X,\mathcal{H})$ とする。
このとき、$$(f,g)_2=\int (f(x),g(x))d\mu\in\bm{C,R}$$と定めると、これは $L^2(X,\mathcal{H})$ 上の内積。

    ・共役演算は、Banach空間の元に対して存在しないと考えられない

- Bochner可測関数 $f,g:X\to \mathcal{H}$ に対して、
$$\phi:X\to\bm{C,R},\quad\phi(x)=(f(x),g(x))$$は可測関数。
<br>

- $f,g:X\to L^2(X,\mathcal{H})$ に対して、
$|(f,g)_2|\le\|f\|_2\|g\|_2$

---

## Bochner積分

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$f\in \mathcal{L}^1(X,B)$ とする。
このとき、$$I(f):B^{*}\to\bm{C,R}\\\ \\
I(f)(\phi)=\int_X\phi(f(x))d\mu $$と定義する。

- $\|I(f)\|<\|f\|_{1},\quad |I(f)(\phi)|\le\|\phi\|\|f\|_1$

        ・よって値域はwell-defined

- $$I(\alpha f+\beta g)(\phi)=\alpha I(f)(\phi)+\beta I(g)(\phi)\\\ \\
I(f)(\alpha\phi+\beta\psi)=\alpha I(f)(\phi)+\beta I(\psi)$$
<br>

---

・Bochner可測単関数 $s_n\in \mathcal{L}^1(X,B)$ とする。

- $$s_n(x)=\sum\chi_{E_i}(x)b_i$$に対して、各 $E_i$ は $\mu$-有限。
<br>

$$I(s_n)(\phi)=\phi(\sum \mu(E_i) b_i)$$よって、$I(s_n)\in\iota(B)$
<br>

---

##### 定義

・Bochner可測関数 $f\in \mathcal{L}^1(X,B)$ に対して、
$$I(f)=\lim_{n\to\infty} I(s_n)\in \iota(B)$$であって、
$$I(f)=\iota(b_f)$$を満たす $b_f\in B$ がただ一つ存在する。

よって、この $b_f\in B$ を
$$b_f=\int_Xfd\mu\in B$$と表し、$f\in\mathcal{L}^1(X,B)$ の $\mu$ に関するBochner積分という。

- $\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$f\in \mathcal{L}^1(X,B)$ とする。
このとき、$$\phi\left(\int_Xfd\mu\right)=\int_X\phi(f(x))d\mu\quad (\forall\phi\in B^*)$$
<br>

-  $\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$ に対して、
$$\psi:L^1(X,B)\to B\\\ \\
\psi(f)=\int_Xfd\mu$$は線形写像。
<br>

- Bochner積分の定義は、Banach空間として $\bm{C,R}$ を選んだ時のLebesgue積分と整合する。

      ・このとき、Bochner可測⇔可測
      ・恒等写像 id:C→Cに対して、b_f=∫fdμ=I(f)(id)

---

##### Bochner積分の性質

$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、$f\in \mathcal{L}^1(X,B)$ とする。

- $$\left\|\int_X fd\mu\right\|=\sup_{\|\phi\|=1}\left|\int_X\phi(f(x))\right|d\mu\le\int_X\|f\|d\mu$$

      ・積分の不等式

- 有界線形作用素 $T\in B(B,C)$ に対して、
$T\circ f\in\mathcal{L}^1(X,B)$ であって、
$$T\left(\int_X fd\mu\right)=\int_XT(f(x))d\mu$$
<br>

- $$\int_X f(x)d\mu\in\overline{\mathrm{span}f(X)}$$

---

##### Bochner-Lebesgue優収束定理

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$\bm{C,R}$ 上Banach空間 $B$、Bochner可測関数列 $f_n:X\to B$ とする。
ここで、
- $f_n$ は各点収束極限 $\lim f_n(x)=f(x)\in B\ (\forall x\in X)$ を持ち、
- $\|f_n(x)\|\le h(x)\ (\forall n\in\bm{N},\forall x\in X)$ を満たす非負値の $h\in\mathcal{L^1}(X,B)$ が存在する。

が成り立つとする。
このとき、$f,f_n\in\mathcal{L^1}(X,B)$ であって、
$$\int_X fd\mu=\lim_{n\to\infty}\int_Xf_nd\mu$$

    ・hは普通の実数値関数。

---

##### Bochner-Fubiniの定理

・$\sigma$-有限測度空間 $(X_i,\mathfrak{M}_i,\mu_i)\ \ (i=1,2)$、$\bm{C,R}$ 上Banach空間 $B$、$f\in\mathcal{L^1}(X_1\times X_2,B)$ とする。
ここで、$i\neq j$ とし、
- $$N_i=\{x_i\in X_i\ |\ \int_{X_j}\|f(x_1,x_2)d\mu_j\|=\infty\}$$
- $F_i(x_i)=\begin{cases}
\int_{X_j}f(x_1,x_2)d\mu_j & x_i\in X/N_i    \\
0  &  x_i\in N_i  \\
\end{cases}$

と定める。

---

・$N_i$ は $\mu_i$-零集合。

- $\forall x_2\in X_2$ に対して、
$$g:X_1\to B\\\ \\
g(x_1)=f(x_1,x_2)$$はBochner可積分。

      ・Bochner可測関数 f に対して、g はBochner可測関数。
<br>

- $F_i\in\mathcal{L^1}(X_i,B)$
<br>

- $$\int_{X_i}F_id\mu=\int_{X_1\times X_2}f(x_1,x_2)d\mu_1\otimes\mu_2$$

---