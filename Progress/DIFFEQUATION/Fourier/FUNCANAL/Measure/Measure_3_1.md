
- [Radon測度](#radon測度)
  - [Radon測度の性質](#radon測度の性質)
    - [有限測度とRadon測度](#有限測度とradon測度)
  - [$σ$-コンパクト性](#σ-コンパクト性)
    - [$σ$-コンパクト性とRadon測度](#σ-コンパクト性とradon測度)
  - [第二可算性とRadon測度](#第二可算性とradon測度)
    - [複素数値Radon測度](#複素数値radon測度)
- [Radon汎関数](#radon汎関数)
  - [Radon汎関数から定まる外測度](#radon汎関数から定まる外測度)
    - [Riesz-Markov-角谷の表現定理](#riesz-markov-角谷の表現定理)
- [複素数値Radon測度](#複素数値radon測度-1)
  - [複素数値Radon測度のなすBanach空間 $M(X)$](#複素数値radon測度のなすbanach空間-mx)
    - [$C0(X)$ との関係](#c0x-との関係)


# Radon測度

・$X$ が局所コンパクトHausdorffな測度空間 $(X,\mathfrak{B},\mu)$ とする。
このとき、Radon測度 $\mu$：
$$\forall\text{ コンパクト集合 }K\in\mathfrak{B}\text{ に対して、}\mu(K)<\infty\\\ \\
\forall E\in\mathfrak{B}\text{ に対して、}\mu(E)=\inf\{\mu(V)\ |\ E\subset V{なる開集合}\}\\\ \\
\text{任意の }\mu(E)<\infty\text{ または開集合である }E\in\mathfrak{B}\text{ に対して、}
\mu(E)=\sup\{\mu(K)\ |\ K\subset E{ なるコンパクト集合}\}$$

---

## Radon測度の性質

<dl><dt>

・$X$ が局所コンパクトHausdorffなRadon測度空間 $(X,\mathfrak{B},\mu)$ とする。
<br>

</dt><dd>

- $$f\in C_c(X)\Rightarrow f\in\mathcal{L}(X)\\\ \\$$

- 開集合 $V\sub X$ とする。
このとき、
$$\mu(V)=\sup\left\{\int_Xfd\mu\ |\ f\prec V\right\}\\\ \\$$

- コンパクト集合 $K\sub X$ とする。
このとき、
$$\mu(K)=\inf\left\{\int_Xfd\mu\ |\ K\prec f\right\}$$

- $$\mathcal{U}=\{U\in\mathcal{O}\ |\ \mu(U)=0\},\quad U_M=\bigcup \mathcal{U}$$
と定めると、$\mu(U_M)=0$
したがって、$U_M$ は $\mathcal{U}$ の包含関係における最大元である。ここで、$\mathrm{supp}\ \mu=(U_M)^c$ をRadon測度 $\mu$ の台という。


</dd></dl>

---


### 有限測度とRadon測度

・$X$ が局所コンパクトHausdorff空間な有限測度空間 $(X,\mathfrak{B},\mu)$ とする。
このとき、
$$\mu\text{ がRadon測度}\\\ \\
\iff\forall B\in\mathfrak{B}\text{ に対して、}\mu(B)=\sup\{\mu(K)\ |\ \text{コンパクト集合 }K\subset B\}\\\ \\$$

    ・内部正則性が成り立つこと。

---

## $σ$-コンパクト性

・位相空間 $X$ とする。
このとき、$X$ が $\sigma$-コンパクト：
$$\exist\text{ コンパクト集合列 }K_n\sub X\text{ であって、}X=\bigcup K_n\\\ \\$$

    ・コンパクト被覆。

---

### $σ$-コンパクト性とRadon測度

<dl><dt>

・$X$ が $\sigma$-コンパクトな局所コンパクトHausdorff空間なRadon測度空間 $(X,\mathfrak{B},\mu)$ とする。
<br>

</dt><dd>

- $$\forall B\in\mathfrak{B},\forall\epsilon>0\text{ に対して、}\exist\text{ 閉集合 }F\sub X,\ \exist\text{ 開集合 }U\sub X\text{ であって、}\\\ \\
F\subset B\subset U,\quad \mu(U-F)<\epsilon\\\ \\$$

- $$\forall B\in\mathfrak{B}\text{ に対して、}\\\ \\
\mu(B)=\sup\{\mu(K)\ |\ \forall{コンパクト集合}K\subset B\}$$

</dd></dl>

---

## 第二可算性とRadon測度

    ・一応証明にRadon汎関数使ったりする。

・第二可算空間は $\sigma$-コンパクト。
<br>

- $X$ が第二可算局所コンパクトHausdorff空間な測度空間 $(X,\mathfrak{B},\mu)$ とする。
このとき、
$$\forall\text{ コンパクト集合 }K\in\mathfrak{B}\text{ に対して、}\mu(K)<\infty$$ ならば、$\mu$ はRadon測度。

---

### 複素数値Radon測度

・第二可算局所コンパクトHausdorff空間 $X$、複素数値Borel測度 $\nu:\mathfrak{B}\to\bm{C}$ とする。
このとき、$\nu$ は複素数値Radon測度。

---
---
---

# Radon汎関数

・局所コンパクトHausdorff空間 $X$、$\Lambda:C_{c,\bm{R}}\to\bm{R}$ とする。
このとき、Radon汎関数 $\Lambda$：$$\Lambda\text{ は }\bm{R}{-線形汎関数であって、}\\\ \\\Lambda(f)\ge0\quad(f:0\to[0,\infty))\\\ \\$$

- 局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda:C_{c,\bm{R}}\to\bm{R}$、$f,g\in C_{c,\bm{R}}$ とする。
このとき、$f(x)\le g(x)\ \ (\forall x\in X)$ ならば、$$\Lambda(f)\le\Lambda(g)$$

---

## Radon汎関数から定まる外測度

<dl><dt>

・局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda$ とする。このとき、

- $$\mu_0:\mathcal{O}_X\to[0,\infty],\quad\mu_0(V)=\sup\{\Lambda(f)\ |\ f\prec V\}\\\ \\
\mu^*:2^X\to[0,\infty],\quad \mu^*(E)=\inf\{\mu_0(V)\ |\ V\in\mathcal{O},\ E\sub V\}\\\ \\
\mathfrak{M}_f=\{E\in2^X\ |\ \mu^*(E)<\infty,\ \mu^*(E)=\sup\{\mu^*(K)\ |\ \text{ コンパクト集合 }K\subset E\}\}\\\ \\
\mathfrak{M}=\{E\in 2^X\ |\ \forall\text{ コンパクト集合 }K\sub X\text{ に対して、}E\cap K\in\mathfrak{M}_f )\}$$
と定める。

</dt><dd>

- $\mu^*(\phi)=\mu_0(\phi)=0$ で、 $\mu^*,\mu_0$ は単調：$$
E\subset F\Rightarrow \mu_0(E)\subset \mu_0(F),\ \mu^*(E)\subset \mu^*(F)\\\ \\$$

      ・どっちの定義域でも単調。
<br>

- $\mu^*$ は $\mu_0$ の拡張。
<br>

- $\mu_0$ は劣 $\sigma$-加法的：
$$\forall\text{ 開集合列 }U_n\sub X\text{ に対して、}\mu_0\left(\bigcup U_n\right)\le\sum \mu_0(U_n)\\\ \\$$

- $\mu^*$は劣 $\sigma$-加法的：
$$\forall\text{ 集合列 }E_n\sub X\text{ に対して、}\mu^*\left(\bigcup E_n\right)\le\sum \mu^*(E_n)\\\ \\$$

---

- コンパクト集合 $K\sub X$ とする。
このとき、$K\in\mathfrak{M}_f$ であって、
$$\mu^*(K)=\inf\{\Lambda f\ |\ K\prec f\}=\inf\{\Lambda f\ |\ f\in C_{c,+}(X),\ f|_{K}=1\}\\\ \\$$

- 開集合 $V\sub X$ とする。
このとき、
$$\mu^*(V)=\sup\{\mu^*(K)\ |\ \text{ コンパクト集合 }K\subset V\}$$
したがって、$\mu^*(V)<\infty\Rightarrow V\in\mathfrak{M}_f$

---

・$$\forall\text{ 非交叉列 }E_n\in\mathfrak{M}_f\text{ に対して、}\mu^*\left(\bigcup E_n\right)=\sum\mu^*(E_n)$$
さらに、非交叉列 $(E_n)$ が $\mu^*(\bigcup E_n)<\infty$ を満たすならば、$\bigcup E_n\in\mathfrak{M}_f$

---

- 
$$\forall E\in\mathfrak{M}_f,\ \forall\epsilon>0\text{ に対して、}\exist\text{ コンパクト集合 } K\sub X,\ \exist\text{ 開集合 }V\sub X\text{ であって、}\\\ \\
K\subset E\subset V,\ \ \mu^*(V-K)<\epsilon\\\ \\$$

- $\mathfrak{M}$ は $\sigma$-加法族であって、$$\mathfrak{B}_X\subset\mathfrak{M}_f\\\ \\$$

- $$\mathfrak{M}_f=\{E\in\mathfrak{M}\ |\ \mu^*(E)<\infty\}$$

---

- $$\mu:\mathfrak{B}\to[0,\infty]\\\ \\
\mu(B)=\mu^*(B)$$
と定めると、これはwell-definedなRadon測度で、
$$\Lambda(f)=\int fd\mu\quad(\forall f\in C_{c,\bm{R}})\\\ \\$$

</dd></dl>

---

### Riesz-Markov-角谷の表現定理

・局所コンパクトHausdorff空間 $X$、Radon汎関数 $\Lambda:C_{c,\bm{R}}\to\bm{R}$ とする。
このとき、
$$\Lambda(f)=\int fd\mu$$を満たすRadon測度 $\mu$ がただ一つ存在する。

---
---
---

# 複素数値Radon測度

・局所コンパクトHausdorff空間 $X$、複素数値Borel測度 $\nu:\mathfrak{B}\to\bm{C}$ とする。
このとき、複素数値Radon測度 $\nu$：
$$\text{全変動 }|\nu|\text{ がRadon測度}$$

---

## 複素数値Radon測度のなすBanach空間 $M(X)$

<dl><dt>

・局所コンパクトHausdorff空間 $X$ とする。
このとき、
$$M(X)=\{\nu:\mathfrak{B}\to\bm{C}\ |\ \nu\text{ は複素数値Radon測度}\}\\\ \\
\|\cdot\|:M(X)\to[0,\infty]\\\ \\
\|\nu\|=|\nu|(X)$$
と定めると、$M(X)$ は $\bm{C}$ 上ベクトル空間で、$\|\cdot\|$ は $M(X)$ 上のノルム。

    ・別に複素数値Borel測度でもベクトル空間になるが、ノルムが入らない！

- 

</dt><dd>



- Radon測度 $\mu:\mathfrak{B}\to[0,\infty]$、$f\in\mathcal{L}^1(X,\mu)$ とする。
このとき、
$$\mu_f\in M(X),\quad \|\mu_f\|=\|f\|_1\\\ \\$$

- 複素数値Radon測度 $\nu\in M(X)$、$f\in\mathcal{L}^1(X,|\nu|)$ とする。
このとき、
$$\nu_f:\mathfrak{B}\to\bm{C},\quad\mu_f(B)=\int_Bfd\nu$$ は $M(X)$ の元で、
$$\|\nu_f\|=\|f\|_{|\nu|,1}\\\ \\$$

</dd></dl>

---

### $C0(X)$ との関係

- $\nu\in M(X)$ とし、
$$\phi_{\nu}:C_0(X)\to\bm{C}\\\ \\
\phi_{\nu}(f)=\int_Xfd\nu$$と定める。このとき、
$\phi_{\nu}\in C_0(X)^*$であって、
$$\psi:M(X)\to C_0(X)^*\\\ \\
\psi(\nu)=\phi_{\nu}$$ は等長写像。



