
- [非負値可測単関数の積分](#非負値可測単関数の積分)
  - [基本的な性質](#基本的な性質)
- [非負値可測関数の積分](#非負値可測関数の積分)
  - [基本的な性質](#基本的な性質-1)
    - [単調収束定理](#単調収束定理)
    - [零集合上の積分](#零集合上の積分)
- [実数値可測関数の積分](#実数値可測関数の積分)
  - [可積分性](#可積分性)
  - [積分の定義](#積分の定義)
- [複素数値可測関数の積分](#複素数値可測関数の積分)
  - [可積分性](#可積分性-1)
  - [積分の定義](#積分の定義-1)
    - [積分の基本的な性質](#積分の基本的な性質)
- [基本定理](#基本定理)
  - [測度論の基本定理](#測度論の基本定理)
  - [測度の演算と積分](#測度の演算と積分)



# 非負値可測単関数の積分

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測単関数 $f:X\to[0,\infty)$ とする。
このとき、
$$\int_Xfd\mu=\sum_{i=1}^n a_i\mu(E_i)\\\ \\
\text{ただし、}f=\sum_{i=1}^n a_i\chi_{E_i}$$
と定めると、これはwell-defined、すなわち、$\int_Xfd\mu$ は指示関数たちの線形結合の表し方によらない。

---

## 基本的な性質

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測単関数 $f,g:X\to[0,\infty)$、$a\ge0$ とする。

</dt><dd>

- $f(x)\le g(x)\ \ (\forall x\in X)$ ならば、
$$\int_Xfd\mu\le\int_Xgd\mu$$特に、
$$0\le\int_Xfd\mu\\\ \\$$

- $$\int_X(f+g)d\mu=\int_Xfd\mu+\int_Xgd\mu,\quad\int_X(af)d\mu=a\int_Xfd\mu\\\ \\$$

- 非負値可測単関数の単調増加列 $f_n:X\to[0,\infty),\ f_n(x)\le f_{n+1}(x)\ \ (\forall x\in X)$ とし、$\forall x\in X\text{ に対して }g(x)\le\sup_{n\in\bm{N}} f_n(x)$ とする。
このとき、
$$\int_X gd\mu\le\sup\int_X f_nd\mu$$

</dd></dl>

---

# 非負値可測関数の積分

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、
$$\int_Xfd\mu=\sup\left\{\int_Xsd\mu\ |\ s:X\to[0,\infty)\text{ は非負値可測単関数で、}s(x)\le f(x)\ \ (\forall x\in X)\right\}\\\ \\$$
と定めると、これは非負値可測単関数の積分の定義と整合する。

    ・値は一意的！

---

## 基本的な性質

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数 $f,g:X\to[0,\infty)$、$a\ge0$ とする。

</dt><dd>

- $f(x)\le g(x)\ \ (\forall x\in X)$ ならば、
$$\int_Xfd\mu\le\int_Xgd\mu$$特に、
$$0\le\int_Xfd\mu\\\ \\$$

- 非負値可測単関数の単調増加列 $f_n:X\to[0,\infty),\ f_{n}(x)\le f_{n+1}(x)$ とする。
このとき、
$$\int_X\left(\sup_{n\in\bm{N}}f_n\right)d\mu=\sup_{n\in\bm{N}}\left\{\int_Xf_nd\mu\right\}$$
<br>

      ・supf_n(x)は非負値可測関数。
<br>

- $$\int_X(f+g)d\mu=\int_Xfd\mu+\int_Xgd\mu,\quad\int_X(af)d\mu=a\int_Xfd\mu\\\ \\$$

      ・一応∞をlim nとみれば、∞倍の線形性も成り立つ。
<br>

</dd></dl>

---

### 単調収束定理

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数の単調増加列 $f_n:X\to[0,\infty),\ f_{n}(x)\le f_{n+1}(x)$ とする。
このとき、
$$\int_X\left(\sup_{n\in\bm{N}}f_n\right)d\mu=\sup_{n\in\bm{N}}\left\{\int_Xf_nd\mu\right\}\\\ \\$$

- 測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数列 $f_n:X\to[0,\infty]$ とする
このとき、
$$\int_X\left(\sum_{n\in\bm{N}}f_n\right)d\mu=\sum_{n\in\bm{N}}\left(\int_Xf_nd\mu\right)$$

---

### 零集合上の積分

・測度空間 $(X,\mathfrak{M},\mu)$、$\mu$-零集合 $N$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、
$$\int_X(f\chi_N)d\mu=0\\\ \\$$

- 測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、
$$\int_Xfd\mu=0\iff\exist\text{ 零集合 }N\in\mathfrak{M}\text{ であって、}f(x)=0\ \ (\forall x\in N)\\\ \\
\int_Xfd\mu<\infty\iff\exist\text{ 零集合 }N\in\mathfrak{M}\text{ であって、}f(x)<\infty\ \ (\forall x\in N)\\\ \\$$
特に、$B\in\mathfrak{M}$ とすると、
$$\exist\text{ 正値可測関数 }f:\bm{R}\to(0,\infty]\text{ であって、}\int_Bfd\mu=0\iff \mu(B)=0$$



---

# 実数値可測関数の積分

## 可積分性

・測度空間 $(X,\mathfrak{M},\mu)$、実数値可測関数 $f:X\to\bm{R}$ とする。
このとき、$f$ が $\mu$-可積分：
$$\int_X|f|d\mu<\infty$$

- 測度空間 $(X,\mathfrak{M},\mu)$、実数値可測関数 $f:X\to\bm{R}$ とする。
このとき、
$$f\text{ は可積分}\iff f_{\pm}\text{ は可積分}$$

---

## 積分の定義

・測度空間 $(X,\mathfrak{M},\mu)$、実数値可測関数 $f:X\to\bm{R}$ とする。
このとき、
$$\int_X fd\mu=\int_Xf_+d\mu-\int_Xf_-d\mu$$
と定めると、これは非負値可測関数の積分の定義と整合する。
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$ とする。
このとき、
$$\mathcal{L}_{\bm{R}}^1(X,\mathfrak{M},\mu)=\{f\in\mathcal{L}_{\bm{R}}(X,\mathfrak{M})\ |\ f\text{ は }\mu\text{-可積分}\}\\\ \\
I:\mathcal{L}^1_{\bm{R}}(X,\mathfrak{M},\mu)\to\bm{R}\\\ \\
I(f)=\int_Xfd\mu$$
と定めると、$\mathcal{L}^1_{\bm{R}}(X,\mathfrak{M},\mu)$ は $\bm{R}$ 上ベクトル空間で、$I$ は $\bm{R}$-線形写像。

---

# 複素数値可測関数の積分

## 可積分性

・測度空間 $(X,\mathfrak{M},\mu)$、複素数値可測関数 $f:X\to\bm{C}$ とする。
このとき、$f$ が $\mu$-可積分：
$$\int_X|f|d\mu<\infty$$

- 測度空間 $(X,\mathfrak{M},\mu)$、複素数値可測関数 $f:X\to\bm{C}$ とする。
このとき、
$$f\text{ は可積分}\iff \mathrm{Re}\ f,\ \mathrm{Im}\ f\text{ は可積分}$$

---

## 積分の定義

・測度空間 $(X,\mathfrak{M},\mu)$、複素数値値可測関数 $f:X\to\bm{R}$ とする。
このとき、
$$\int_X fd\mu=\int_X(\mathrm{Re}\ f)d\mu+i\int_X(\mathrm{Im} f)d\mu$$
と定めると、これは実数値可積分関数の積分の定義と整合する。
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$ とする。
このとき、
$$\mathcal{L}^1(X,\mathfrak{M},\mu)=\{f\in\mathcal{L}(X,\mathfrak{M})\ |\ f\text{ は }\mu\text{-可積分 }\}\\\ \\
I:\mathcal{L}^1(X,\mathfrak{M},\mu)\to\bm{C}\\\ \\
I(f)=\int_Xfd\mu$$
と定めると、$\mathcal{L}^1_{\bm{R}}(X,\mathfrak{M},\mu)$ は $\bm{R}$ 上ベクトル空間でも、$I$ は $\bm{R}$-線形写像。

---

### 積分の基本的な性質

<dl><dt>

・測度空間 $(X,\mathfrak{M},\mu)$、$f\in\mathcal{L}^1(X)$ とする。

</dt><dd>

- $$\left|\int_Xfd\mu\right|\le\int_X|f|d\mu$$

・複素数値可測関数 $g:X\to\bm{C}$ とする。
このとき、
$$f(x)=0\ \ (a.e.)\iff\int_X |f|d\mu=0\\\ \\
\iff \forall E\in\mathfrak{M}\text{ に対して、}\int_X f\chi_E d\mu=0$$

</dd></dl>

---

# 基本定理

## 測度論の基本定理

・測度空間 $(X,\mathfrak{M},\mu)$、非負値可測関数列 $f_n:X\to[0,\infty]$ とする。
このとき、$$\int_X\left(\sup_{n\in\bm{N}}\inf_{k\ge n} f_k\right)d\mu\le\sup_{n\in\bm{N}}\inf_{k\ge n} \left(\int_X f_kd\mu\right)$$
<br>

- 測度空間 $(X,\mathfrak{M},\mu)$、各点収束複素数値可測関数列 $f_n:X\to\bm{C},\ \ f(x)=\lim f_n(x)\in\bm{C}\ \ (\forall x\in X)$ とする。
このとき、
$$\exist h\in\mathcal{L}^1(X),\ 0\le h(x)\text{ であって、}|f_n(x)|\le h(x)\ \ (\forall n\in\bm{N},\forall x\in X)$$が成り立つならば、$f,f_n\in\mathcal{L}^1(X)$ であって、
$$\int_X fd\mu=\lim_{n\to\infty}\left(\int_X f_nd\mu\right)\\\ \\$$

      ・優収束定理
      ・これパラメータに関する偏微分でも使える！

---

## 測度の演算と積分

・可測空間 $(X,\mathfrak{M})$、測度 $\mu_1,\mu_2:\mathfrak{M}\to[0,\infty]$、$\alpha_1,\alpha_2\ge0$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、
$$\int_Xfd(\alpha_1\mu_1+\alpha_2\mu_2)=\alpha_1\int_Xfd(\mu_1)+\alpha_2\int_Xfd(\mu_2)\\\ \\$$

    ・実数値、複素数値可積分関数でも同様。
<br>

- 可測空間 $(X,\mathfrak{M})$、測度列 $\mu_n:\mathfrak{M}\to[0,\infty]$、非負点列 $\alpha_n\ge0$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、$$\int_Xfd\left(\sum\alpha_n\mu_n\right)=\sum\left[\alpha_n\int_Xfd(\mu_n)\right]$$

      ・実数値、複素数値可積分関数でも同様。


