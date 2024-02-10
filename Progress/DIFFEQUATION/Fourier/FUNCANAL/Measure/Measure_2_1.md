
- [複素数値測度](#複素数値測度)
  - [密度関数](#密度関数)
    - [非負値可測関数](#非負値可測関数)
    - [実数値可積分関数](#実数値可積分関数)
    - [複素数値可積分関数](#複素数値可積分関数)
- [実数値測度とHahn分解](#実数値測度とhahn分解)
  - [実数値測度の細かい性質](#実数値測度の細かい性質)
  - [実数値測度と非正,非負可測集合](#実数値測度と非正非負可測集合)
  - [実数値測度の性質](#実数値測度の性質)
- [互いに特異な測度](#互いに特異な測度)
  - [実数値測度とJordan分解](#実数値測度とjordan分解)
- [測度の絶対連続性](#測度の絶対連続性)
  - [Radon-Nikodymの定理](#radon-nikodymの定理)
  - [Radon-Nikodym微分](#radon-nikodym微分)
- [複素数値測度に対する全変動](#複素数値測度に対する全変動)
  - [実数値測度と全変動](#実数値測度と全変動)
    - [測度空間上の実数値測度](#測度空間上の実数値測度)
      - [$σ$-有限測度空間](#σ-有限測度空間)


# 複素数値測度

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、$\nu:\mathfrak{M}\to\bm{C}$ とする。
このとき、複素数値測度 $\nu$：
$$\forall\text{ 非交叉列 }(E_n)\sub\mathfrak{M}\text{ に対して、}\\\ \\
\nu\left(\bigcup_{n\in\bm{N}} E_n\right)=\sum_{n\in\bm{N}}\nu(E_n)\\\ \\$$
明らかに、$\forall E\in\mathfrak{M}\text{ に対して、}\nu(E)\ge0\text{ または }\nu(E)\le0$ ならば、$\nu\text{ または }-\nu$ は有限測度。

    ・実数値測度も同様。また、明らかにReν、Imνは実数値測度。
<br>

</dt><dd>

- $$\nu(\phi)=0\\\ \\$$

- 
$$\forall\text{ 非交叉な可測集合 }E_1,...,E_N\in \mathfrak{M}\text{ に対して、}\\\ \\
\nu\left(\bigcup_{n=1}^NE_n\right)=\sum_{n=1}^n\nu(E_n)\\\ \\$$

- 
$$\forall\text{ 単調増加列 }(E_n)\subset\mathfrak{M},\ E_n\sub E_{n+1}\text{ に対して、}\\\ \\
\nu\left(\bigcup E_n\right)=\lim_{n\to\infty}\nu(E_n)\\\ \\
\forall\text{ 単調減少列 }(E_n)\subset\mathfrak{M},\ E_n\supset E_{n+1}\text{ に対して、}\\\ \\
\nu\left(\bigcap E_n\right)=\lim_{n\to\infty}\nu(E_n)\\\ \\$$

      ・実数値測度でも同様。
<br>

- 複素数値測度 $\mu_1,\mu_2$ とする。
このとき、
$$\mu_1+\mu_2,\quad \lambda\mu_1$$ も複素数値測度であって、$\mathrm{Re}\ \mu,\quad\mathrm{Im}\ \mu$ は実数値測度。
<br>

      ・実数値測度も同様。

</dd></dl>

---


## 密度関数

    ・全変動は積分のあたりで述べる。

### 非負値可測関数

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、
$$\mu_f:\mathfrak{M}\to[0,\infty]\\\ \\
\mu_f(E)=\int_Efd\mu$$
と定めると、これは $(X,\mathfrak{M})$ 上の測度で、$\mu$ に対して絶対連続。

---

### 実数値可積分関数

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$、$f\in\mathcal{L}^1_{\bm{R}}(X)$ とする。
このとき、
$$\mu_f:\mathfrak{M}\to\bm{R}\\\ \\
\mu_f(E)=\int_Efd\mu$$
と定めると、これは $(X,\mathfrak{M})$ 上の実数値測度で。$\mu$ に関して絶対連続。
<br>

</dt><dd>

- $$(f\ge0),\ (f<0)\in\mathfrak{M}$$
と定めると、これは $\mu_f$ のHahn分解。
<br>

- $$\mu_{f_{\pm}}(E)=\int_Ef_{\pm}d\mu\in[0,\infty)$$
と定めると、これは $\mu_f$ のJordan分解。

</dd></dl>

---

### 複素数値可積分関数

・測度空間 $(X,\mathfrak{M},\mu)$、$f\in\mathcal{L}^1(X)$ とする。
このとき、
$$\mu_f:\mathfrak{M}\to\bm{C}\\\ \\
\mu_f(E)=\int_Efd\mu$$
と定めると、これは $(X,\mathfrak{M})$ 上の複素数値測度で、$\mu$ に関して絶対連続。

---

# 実数値測度とHahn分解

## 実数値測度の細かい性質

・可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$、加速集合列 $(E_n)\sub\mathfrak{M}$ とする。
このとき、
$$\nu(\ \overline{\lim}E_n)\ge\overline{\lim}\ \mu(E_n)\\\ \\
\mu(\ \underline{\lim}E_n)\le\underline{\lim}\ \mu(E_n)$$

---

## 実数値測度と非正,非負可測集合

・可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$、可測集合 $P\in\mathfrak{M}$ とする。
このとき、$P$ が $\nu$ に対して非負、非正：
$$\text{非正：}\forall E\in\mathfrak{M}\text{ に対して、 }\nu(E\cap P)\ge0\\\ \\
\text{非負：}\forall E\in\mathfrak{M}\text{ に対して、 }\nu(E\cap P)\le0$$

    ・非負な集合列E_nの合併∪E_nも非負

---

## 実数値測度の性質

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
<br>

</dt><dd>

- 
$$\forall A\in \mathfrak{M},\ \forall \epsilon>0\text{ に対して、}\exist B\in\mathfrak{M}\text{ であって、}\\\ \\
B\subset A,\quad\nu(B)\ge\nu(A),\\\ \\
\forall E\in\mathfrak{M},\ E\sub B\text{ に対して、}\nu(E)\ge-\epsilon\\\ \\$$

- 
$$\forall A\in\mathfrak{M}\text{ に対して、}\exist\ \nu\text{ に対して非負な } P\in\mathfrak{M}_A\text{ であって、}\\\ \\
\nu(P)\ge\nu(A)\\\ \\$$ 

    ・P⊂A
<br>

- $$\sup\{\nu(E)\ |\ E\in\mathfrak{M}\}<\infty\\\ \\$$

- $X$ の可測分割 $A_+,A_-$ であって、それぞれ非負、非正であるものが存在する。特に、$A_-=(A_+)^c$
ここで、この分解をHahn分解という。
<br>

      ・別に一意的ではない。Jordanの方が一意的。

</dd></dl>

---

# 互いに特異な測度

・可測空間 $(X,\mathfrak{M})$、測度 $\mu_1,\mu_2:\mathfrak{M}\to[0,\infty]$ とする。
このとき、互いに特異な測度 $\mu_1\perp\mu_2$：
$$\exist\text{ 可測分割 }X=A_1\cup (A_1)^c\text{ であって、}\\\ \\
\mu_1(E)=\mu_1(E\cap A_1),\ \mu_2(E)=\mu_2(E\cap (A_1)^c)\quad(\forall E\in\mathfrak{M})\\\ \\$$

    ・実数値測度、複素数値測度でも同様。
<br>

- 可測空間 $(X,\mathfrak{M})$、測度 $\mu_1,\mu_2:\mathfrak{M}\to[0,\infty]$ とする。
このとき、
$$\mu_1\text{ と }\mu_2\text{ が }A\text{ で特異}\iff \mu_1(A)=0\text{ かつ }\mu_2(A^c)=0\\\ \\$$

      ・実数値測度とかでは成り立たない。


---

## 実数値測度とJordan分解

- 可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
このとき、
$$\text{ ある有限測度 }\nu_+,\ \nu_-:\mathfrak{M}\to[0,\infty)\text{ がただ一つ存在して、}\\\ \\
\nu_+\perp\nu_-,\quad\nu=\nu_+-\nu_-$$
さらに、任意のHahn分解 $A_+,A_-$ に対して、
$$\nu_{\pm}(E)=\pm\nu(E\cap A_{\pm})\quad(\forall E\in\mathfrak{M})$$
が成り立つ。ここで、$\nu=\nu_+-\nu_-$ をJordan分解といい、$\nu_+$ を上変動、$-\nu_-$ を下変動という。
<br>

      ・有限測度：μ(X)<∞
      ・正負はこれでよい。また、あるHahn分解に対して上記のようにν_±を定めれば、それはJordan分解。

---

# 測度の絶対連続性

・可測空間 $(X,\mathfrak{M})$、測度 $\mu,\nu:\mathfrak{M}\to[0,\infty]$ とする。
このとき、$\nu$ が $\mu$ に対して絶対連続 $\nu<<\mu$：
$$\mu(E)=0\Rightarrow\nu(E)=0\\\ \\$$

    ・実数値測度、複素数値測度 ν に対しても同様。
<br>

- 可測空間 $(X,\mathfrak{M})$、測度 $\mu:\mathfrak{M}\to[0,\infty]$、$\mu$ に対して共に絶対連続な測度 $\nu_1,\nu_2:\mathfrak{M}\to[0,\infty]$、$a,b\ge0$ とする。
このとき、$a\nu_1+b\nu_2$ は $\mu$ に対して絶対連続。
<br>

      ・実数値測度、複素数値測度でも同様。
    
---

## Radon-Nikodymの定理

<dl><dt>

・有限測度空間 $(X,\mathfrak{M},\mu)$、有限測度 $\nu:\mathfrak{M}\to[0,\infty)$ とする。
このとき、
$$\exist\text{ 非負値可積分関数 }f\in\mathcal{L}^1(X,\mu),\ f:X\to[0,\infty),\ \exist\text{ 有限測度 }\lambda:\mathfrak{M}\to[0,\infty)\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

    ・有限測度：μ(X)<∞
<br>

</dt><dd>

- $\sigma-$有限測度空間 $(X,\mathfrak{M},\mu)$、$\sigma-$有限測度 $\nu:\mathfrak{M}\to[0,\infty]$ とする。
このとき、
$$\exist\text{ 非負値可測関数 }f:X\to[0,\infty),\ \exist\ \sigma\text{-有限測度 }\lambda:\mathfrak{M}\to[0,\infty]\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

- $\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
このとき、
$$\exist f\in\mathcal{L}_{\bm{R}}^1(X,\mu),\ \exist\text{ 実数値測度 }\lambda:\mathfrak{M}\to\bm{R}\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

- $\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$ とする。
このとき、
$$\exist f\in\mathcal{L}^1(X,\mu),\ \exist\text{ 複素数値測度 }\lambda:\mathfrak{M}\to\bm{C}\text{ であって、}\\\ \\
\nu=\mu_f+\lambda,\quad\lambda\perp\mu\\\ \\$$

</dd></dl>

---

## Radon-Nikodym微分

    ・a.e.で一意的。

<dl><dt>

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$ とする。

</dt><dd>

- $\mu$ に対して絶対連続な $\sigma-$有限測度 $\nu:\mathfrak{M}\to[0,\infty)$ に対して、
$$\exist\text{ 非負値可測関数} f:X\to[0,\infty)\text{ であって、}\\\ \\
\nu=\mu_f$$
ここで、$f$ を $\nu$ の $\mu$ に関するRadon-Nikodym微分という。
<br>

      ・このfは∞取らない。
<br>

- $\mu$ に対して絶対連続な実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ に対して、
$$\exist f\in\mathcal{L}^1_{\bm{R}}(X,\mu)\text{ であって、}\\\ \\
\nu=\mu_f$$
ここで、$f$ を $\nu$ の $\mu$ に関するRadon-Nikodym微分という。
<br>

- $\mu$ に対して絶対連続な複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$ に対して、
$$\exist f\in\mathcal{L}^1(X,\mu)\text{ であって、}\\\ \\
\nu=\mu_f$$
ここで、$f$ を $\nu$ の $\mu$ に関するRadon-Nikodym微分という。
<br>

- $f_1,f_2$ を共に $\nu$ の $\mu$ に対するRadon-Nikodym微分とする。
このとき、
$$f_1=f_2\ \ (\mu-a.e.)\\\ \\$$

      ・どのRadon-Nikodym微分でも成り立つ。

</dd></dl>

---

# 複素数値測度に対する全変動

<dl><dt>

・可測空間 $X$、複素数値測度 $\nu:\mathfrak{M}\to \bm{C}$ とする。
このとき、全変動 $|\nu|$：
$$|\nu|:\mathfrak{M}\to[0,\infty]\\\ \\
|\nu|(E)=\sup\left\{\sum_{i=1}^n|\nu(E_i)|\ |\ E_1,...,E_n\subset E\text{ は } E\text{ の有限可測分割} \right\}\\\ \\$$

    ・別にwell-defined。また、有限測度であることが以下で分かる。
<br>

</dt><dd>

- 実数値測度 $\nu:\mathfrak{M}\to \bm{R}$ とする。
このとき、
$$|\nu|=\nu_++\nu_-\quad(\nu_{\pm}\text{ はJordan分解})\\\ \\$$

- 測度空間 $(X,\mathfrak{M},\mu)$、$f\in \mathcal{L}^1(X)$ とする。
このとき、全変動 $|\mu_f|$ は有限測度で、
$$|\mu_f|=\mu_{|f|}\\\ \\$$

- 複素数値測度 $\nu:\mathfrak{M}\to\bm{C}$ の全変動 $|\nu|:\mathfrak{M}\to[0,\infty)$ は有限測度で、$\nu$ は $|\nu|$ に対して絶対連続。
よって、$\nu$ は有界関数、すなわち、$\forall E\in\mathfrak{M}\text{ に対して、}|\nu(E)|\le|\nu|(X)$

</dd></dl>

---

## 実数値測度と全変動

<dl><dt>

・可測空間 $(X,\mathfrak{M})$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$、$E\in\mathfrak{M}$ とする。
このとき、上変動 $\overline{V}_\nu$、下変動 $\underline{V}_\nu$、全変動 $V_\nu$：
$$\overline{V}_\nu,\ \underline{V}_\nu,\ V_\nu:\mathfrak{M}\to\bm{R}\\\ \\
\overline{V}_\nu(E)=\sup\{\nu(F)\ |\ F\in\mathfrak{M}\text{ かつ }F\sub E \}\\\ \\
\underline{V}_\nu(E)=\inf\{\nu(F)\ |\ F\in\mathfrak{M}\text{ かつ }F\sub E \}\\\ \\
V_\nu(E)=|\overline{V}_{\nu}(E)|+|\underline{V}_{\nu}(E)|$$
と定めると、これらの値域はwell-defined、すなわち、
$$\forall E\in\mathfrak{M}\text{ に対して、}\\\ \\
\underline{V}_{\nu}(E)\le 0,\ \nu(E)\le\overline{V}_{\nu}(E)\le V_{\nu}(E)<\infty\\\ \\$$

</dt><dd>

- 
$$\forall E\sub F\text{ なる }E,F\in\mathfrak{M}\text{ に対して、}\\\ \\
\overline{V}_{\nu}(E)\le\overline{V}_{\nu}(F),\quad\underline{V}_{\nu}(E)\ge\underline{V}_{\nu}(F),\quad V_{\nu}(E)\le V_{\nu}(F)\\\ \\$$

- $$\overline{V}_{\nu}(\phi)=\underline{V}_{\nu}(\phi)=V_{\nu}(\phi)=0\\\ \\
\forall\text{ 非交叉列 }(E_n)\sub\mathfrak{M}\text{ に対して、}\\\ \\
\overline{V}_{\nu}\left(\bigcup_nE_n\right)=\sum_{n}\overline{V}_{\nu}(E_n),\quad\underline{V}_{\nu}\left(\bigcup_nE_n\right)=\sum_{n}\underline{V}_{\nu}(E_n),\quad V_{\nu}\left(\bigcup_nE_n\right)=\sum_{n}V_{\nu}(E_n)\\\ \\
\forall E\in\mathfrak{M}\text{ に対して、}\nu(E)=\overline{V}_{\nu}(E)+\underline{V}_{\nu}(E)$$
したがって、$\overline{V}_{\nu},\ -\underline{V}_{\nu},V_{\nu}$ は $\mathfrak{M}$ 上の有限測度。
<br>

- $$\exist A\in\mathfrak{M}\text{ であって、}\underline{V}_{\nu}(A)=0,\ \overline{V}_{\nu}(X-A)=0$$
したがって、$$\forall E\in \mathfrak{M}\text{ に対して、}\\\ \\
\nu(E\cap A)=\overline{V}_{\nu}(E\cap A)=\overline{V}_{\nu}(E),\quad \nu(E\cap A^c)=\underline{V}_{\nu}(E\cap A^c)=\underline{V}_{\nu}(E)\\\ \\$$
したがって、$\overline{V}_{\nu},-\underline{V}_{\nu}$ は互いに特異な測度であって、$\nu$ の一意的に定まっていたJordan分解。特に、$V_{\nu}=|\nu|$。
<br>

- 
$$\forall E\in\mathfrak{M}\text{ に対して、}|\nu(E)|<V(X)$$
したがって、$\nu$ は $\mathfrak{M}$ 上有界。
<br>

</dd></dl>

---

### 測度空間上の実数値測度

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
このとき、
$$\nu\text{ が }\mu\text{ に対して絶対連続}\iff\overline{V}_{\nu},\ \underline{V}_{\nu}\text{ が共に }\mu\text{ に対して絶対連続}\\\ \\
\nu\text{ が }\mu\text{ と互いに }A\text{ で特異}\iff\mu(A)=0\text{ かつ }\forall E\sub A^c\text{ に対して }\nu(E)=0\iff\overline{V}_{\nu},\ \underline{V}_{\nu}\text{ が共に }\mu\text{ と互いに }A\text{ で特異}\\\ \\$$

</dt><dd>

- 共に $\mu$ と共に特異な実数値測度 $\nu_1,\nu_2:\mathfrak{M}\to\bm{R}$、$a,b\in\bm{R}$ とする。
このとき、$a\nu_1+b\nu_2$ は $\mu$ と互いに特異な測度。
<br>

- $$\nu\text{ が }\mu\text{ に対して絶対連続}\\
\iff\forall\epsilon>0\text{ に対して、}\exist\delta>0\text{ であって、}\forall E\in\mathfrak{M}\text{ に対して、}\mu(E)<\delta\Rightarrow|\nu(E)|<\epsilon\\\ \\
\nu\text{ が }\mu\text{ と互いに特異}\\
\iff\forall\epsilon>0\text{ に対して、}\exist E\in\mathfrak{M}\text{ であって、}\mu(E)<\epsilon\text{ かつ }|\nu|(E^c)<\epsilon\\\ \\$$

- $$\nu\text{ が }\mu\text{ に対して絶対連続かつ互いに特異}\Rightarrow\nu=0\\\ \\$$  

- $\nu\neq0$ を満たす互いに特異でない有限測度 $\mu,\nu:\mathfrak{M}\to[0,\infty)$ とする。
このとき、
$$\exist N_0,\ \exist E\sub\mathfrak{M}\text{ であって、}\\\ \\
\mu(E)>0\text{ かつ }\forall F\sub E\text{ なる }E\in\mathfrak{M}\text{ に対して、}\nu(F)\ge\frac{1}{n}\mu(F)\text{ かつ }\forall F\sub E^c\text{ なる }F\in\mathfrak{M}\text{ に対して、}\nu(F)\le\frac{1}{n}\mu(F)$$

</dd></dl>

---

#### $σ$-有限測度空間

・$\sigma$-有限測度空間 $(X,\mathfrak{M},\mu)$、$X=\bigcup_nX_n,\ \mu(X_n)<\infty$、実数値測度 $\nu:\mathfrak{M}\to\bm{R}$ とする。
このとき、
$$\forall X_n\text{ に対して、}\nu\text{ が }\mu\text{ に対して }\mathfrak{M}_{X_n}\text{ 上で絶対連続}\Rightarrow\nu\text{ が }\mu\text{ に対して絶対連続}\\\ \\
\forall X_n\text{ に対して、}\nu\text{ が }\mu\text{ と }\mathfrak{M}_{X_n}\text{ 上で互いに特異}\Rightarrow\nu\text{ が }\mu\text{ と互いに特異}\\\ \\$$

---
---
---



