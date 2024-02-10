
- [可測空間](#可測空間)
  - [自明な $σ$-加法族](#自明な-σ-加法族)
  - [相対 $σ$-加法族](#相対-σ-加法族)
    - [可測関数の制限](#可測関数の制限)
    - [測度の制限](#測度の制限)
      - [制限測度の積分](#制限測度の積分)
  - [写像が誘導する $σ$-加法族](#写像が誘導する-σ-加法族)
    - [写像が誘導する測度空間](#写像が誘導する測度空間)
  - [直積可測空間](#直積可測空間)
    - [有限直積](#有限直積)
    - [第二可算空間の可算個の直積](#第二可算空間の可算個の直積)
  - [有限な $σ$-加法族](#有限な-σ-加法族)
    - [測度](#測度)
- [Borel集合族](#borel集合族)
  - [相対Borel集合族](#相対borel集合族)





# 可測空間

## 自明な $σ$-加法族

・集合 $X$ とする。
このとき、自明な$\sigma$-加法族：$\mathfrak{M}=\{\phi,X\}$、$2^X$

- 測度空間 $(X,2^X),\ (Y,\mathfrak{M})$、$f:X\to Y$ とする。
このとき、$f$ は可測。

---

## 相対 $σ$-加法族

・可測空間 $(X,\mathfrak{M})$、空でない部分集合 $A\sub X$ とする。
このとき、
$$\mathfrak{M}_A=\{A\cap E\ |\  E\in\mathfrak{M}\}$$
は $A$ 上の $\sigma$-加法族。
<br>

- 可測空間 $(X,\mathfrak{M})$、可測集合 $E\in\mathfrak{M}$ とする。
このとき、
$$\mathfrak{M}_E=\{F\in\mathfrak{M}\ |\  F\sub E\}\\\ \\$$

---

### 可測関数の制限


<dl><dt>

・可測空間 $(X,\mathfrak{M})$、可測集合 $E\in\mathfrak{M}$、可測関数 $f:X\to [-\infty,\infty]$ とする。
このとき、
$$f_E:E\to[-\infty,\infty]\\\ \\
f_E(x)=f(x)$$
と定めると、これは $(E,\mathfrak{M}_E)$ 上可測関数。
<br>

</dt><dd>

- 可測空間 $(X,\mathfrak{M})$、可測集合 $E\in\mathfrak{M}$、$f:X\to [-\infty,\infty]$ とする。
このとき、$f_E,\ f_{E^c}$ がそれぞれ $(E,\mathfrak{M}_E),\ (E^c,\mathfrak{M}_{E^c})$ 上可測ならば、$f$ は $(X,\mathfrak{M})$ 上可測。
<br>

      ・定義域の結合。


</dd></dl>

---

### 測度の制限

・測度空間 $(X,\mathfrak{M},\mu)$、可測集合 $E\in\mathfrak{M}$ とする。
このとき、
$$\mu_E:\mathfrak{M}_E\to[0,\infty]\\\ \\
\mu_E(F)=\mu(F)$$
は可測空間 $(E,\mathfrak{M}_E)$ 上の測度。

---

#### 制限測度の積分

・測度空間 $(X,\mathfrak{M},\mu)$、可測集合 $E\in\mathfrak{M}$、非負値可測関数 $f:X\to[0,\infty]$ とする。
このとき、
$$\int_X(f\chi_E)d\mu=\int_Ef_Ed\mu_E$$

    ・実数値、複素数値可積分関数でも同様。




---

## 写像が誘導する $σ$-加法族

・集合 $X$、可測空間 $(Y,\mathfrak{M})$、$f:X\to Y$ とする。
このとき、
$$\sigma(f)=\{f^{-1}(B)\sub X\ |\ \exist B\in\mathfrak{M}\}$$
と定めると、これは $X$ 上の $σ$-加法族。
<br>

- 可測空間 $(X,\mathfrak{M})$、集合 $Y$、$f:X\to Y$ とする。
このとき、$$\sigma(f)=\{B\sub Y\ |\ f^{-1}(B)\in\mathfrak{M}\}$$
と定めると、これは $Y$ 上の $σ$-加法族。
<br>

      ・2種類ある！

### 写像が誘導する測度空間

<dl><dt>

・可測空間 $(X,\mathfrak{M}_X)$、測度空間 $(Y,\mathfrak{M}_Y,\mu)$、全単射で $f^{-1}$ が可測な $f:X\to Y$ とする。
このとき、
$$\mu:\mathfrak{M}_X\to[0,\infty]\\\ \\
\mu(B)=\mu_Y(f(B))$$
と定めると、$\mu$ は測度。
<br>

</dt><dd>

- 非負値可測関数 $g:X\to[0,\infty]$ とする。
このとき、$$\int_Xgd\mu=\int_Yg\circ f^{-1}d\mu_Y$$

</dd></dl>

---

## 直積可測空間

<dl><dt>

・可測空間の族 $(X_j,\mathfrak{M}_j)$、射影 $\pi_j:\Pi\ X_j\to X_j$ とする。
このとき、
$$\bigotimes\mathfrak{M}_j=\sigma(\{\pi_j^{-1}(E)\ |\ E\in\mathfrak{M}_j\})$$
と定めて、$(\Pi\ X_j,\bigotimes\mathfrak{M}_j)$ を直積可測空間という。
ここで、各射影 $\pi_j$ は可測関数。
<br>

</dt><dd>

- 可測空間 $(X,\mathfrak{M}_X)$、直積可測空間 $(\Pi\ Y_j,\bigotimes\mathfrak{M}_{Y_j})$、$f:X\to\Pi\ Y_j$ とする。
このとき、
$$f\text{ は可測関数}\iff\forall\text{ 射影 }\pi_j\text{ に対して、}\pi_j\circ f\text{ は可測関数}$$
特に、
$$i_j:Y_j\to\Pi\ Y_j\\\ \\
i_j(y_j)=(y_1,...,y_j,...)\ \ (\forall y_j\in Y_j)$$
は可測関数。（ $y_1$ とかは固定。）

</dd></dl>

---

### 有限直積

<dl><dt>

・可測空間 $(X_1,\mathfrak{M}_1),...,(X_n,\mathfrak{M}_n)$ とする。
このとき、
$$\bigotimes_{i=1}^n\mathfrak{M}_i=\sigma(\{E_{k_1}\times...\times E_{k_n}\ |\ k\in\bm{N},\ E_{k_i}\in\mathfrak{M}_i\})\\\ \\$$

</dt><dd>

- $X_i$ 上の有限加法族 $\mathcal{A}_i$ とする。
このとき、
$$\left\{\left.\bigcup_{k=1}^nA^1_{k}\times...\times A_{k}^n\ \right|\ n\in\bm{N},\ A^i_{k}\in\mathcal{A}_i\right\}$$
と定めると、これは有限加法族。
また、$$\left\{\left.\bigcup_{k=1}^nA^1_{k}\times...\times A^n_{k}\ \right|\ n\in\bm{N},\ A^i_{k}\in\mathcal{A}_i,\quad(A^1_k\times...\times A^n_{k})\cap(A^1_{k'}\times...\times A^n_{k'}=\phi)\right\}$$
と定めると、これも有限加法族。
<br>

      ・2つ目の集合の非交叉性は、あるA^i_k∩A^i_k'=φであることと同値。

</dd></dl>

---

### 第二可算空間の可算個の直積

    ・このとき直積が第二可算になる。

・第二可算空間の列 $X_n$ とする。
このとき、
$$\mathfrak{M}_{\Pi\ X_n}=\bigotimes\mathfrak{M}_n$$

---

## 有限な $σ$-加法族

・集合 $X$、有限集合である有限加法族 $\mathcal{A}$ とする。
このとき、$\mathcal{A}$ は $\sigma$-加法族。

---

### 測度

・集合 $X$、有限族である有限加法族 $\mathcal{A}$、有限加法的測度 $\mu:\mathcal{A}\to[0,\infty]$ とする。
このとき、$\mu$ は $\sigma$-加法族 $\mathcal{A}$ 上の測度。

---

# Borel集合族

## 相対Borel集合族

・空でない集合 $X$、空でない部分集合 $A\sub X$、$\mathcal{I}\sub 2^X$ とする。
このとき、
$$\mathcal{I}\cap A=\{I\cap A\ |\ I\in\mathcal{I}\},\quad\sigma(\mathcal{I})\cap A=\{E\cap A\ |\ E\in\sigma(\mathcal{I})\}$$
とすると、
$$\sigma_A(\mathcal{I}\cap A)=\sigma(\mathcal{I})\cap A$$
ここで、$\sigma_A$ は $A$ 上の $\mathcal{I}\cap A$ を含む最小の $\sigma$-加法族。
<br>

- 位相空間 $(X,\mathcal{O})$、部分集合 $A\sub X$ とする。
このとき、$$\mathfrak{B}_A=\sigma(\mathfrak{O}_A)$$
すなわち、相対位相におけるBorel集合族と、相対 $\sigma$-加法族は等しい。

---

・直積Borel集合族

    ・第二可算空間の可算無限個の直積集合について、直積σ加法族＝直積位相のBorel集合族






