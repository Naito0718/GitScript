
- [有限加法族](#有限加法族)
  - [半集合代数](#半集合代数)
  - [有限加法族](#有限加法族-1)
    - [生成される有限加法族](#生成される有限加法族)
  - [単調族](#単調族)
    - [生成される単調族](#生成される単調族)
- [有限加法的測度](#有限加法的測度)
  - [半集合代数上の有限加法的測度](#半集合代数上の有限加法的測度)
    - [有限加法族上の有限加法的測度](#有限加法族上の有限加法的測度)
  - [$σ$-有限測度](#σ-有限測度)
- [Caratheodory外測度](#caratheodory外測度)
  - [$σ$-有限測度のとき](#σ-有限測度のとき)
- [$σ$-有限測度と直積可測空間](#σ-有限測度と直積可測空間)
  - [Tonelliの定理](#tonelliの定理)
  - [Fubiniの定理](#fubiniの定理)



# 有限加法族

## 半集合代数 

・空でない集合 $X$、部分集合 $\mathcal{I}\sub 2^X$ とする。
このとき、半集合代数 $\mathcal{I}$：
$$X,\phi\in \mathcal{I}\\\ \\
\forall E,F\in\mathcal{I}\text{ に対して、}E\cap F\in\mathcal{I}\\\ \\
\forall E\in\mathcal{I}\text{ に対して、}\exist \text{ 互いに交わらない } F_1,...,F_n\in\mathcal{I}\text{ であって、}E=\bigcup_i^n F_i\\\ \\$$

    ・半集合代数Iから生成される有限加法族A(I)={互いに交わらないIの要素の有限和}

---

## 有限加法族

・空でない集合 $X$、部分集合 $\mathcal{A}\sub 2^X$ とする。
このとき、有限加法族 $\mathcal{A}$：
$$X\in \mathcal{A}\\\ \\
\forall E\in\mathcal{A}\text{ に対して、}E^c\in\mathcal{A}\\\ \\
\forall E,F\in\mathcal{A}\text{ に対して、}E\cup F\in\mathcal{A}\\\ \\$$

- 空でない集合 $X$、有限加法族 $\mathcal{A}\sub2^X$、$E,F\in\mathcal{A}$ とする。
このとき、
$$E\cap F,\ E/F\in\mathcal{A}$$ であって、$\mathcal{A}$ は半集合代数。

---

### 生成される有限加法族

<dl><dt>

・空でない集合 $X$、有限加法族の族 $\mathcal{A}_j\sub 2^X$ とする。
このとき、$\bigcap \mathcal{A}_j$ は有限加法族。
<br>

- 空でない集合 $X$、部分集合 $\mathcal{I}\sub 2^X$ とする。
このとき、$$\mathcal{A}(\mathcal{I})=\bigcap\{\mathcal{A}\ |\ \text{有限加法族 }\mathcal{A}\text{ であって、}\mathcal{I}\sub\mathcal{A}\}$$
を含む最小の有限加法族。
<br>

</dt><dd>

- 空でない集合 $X$、半集合代数 $\mathcal{I}\sub 2^X$ とする。
このとき、
$$\mathcal{A}(\mathcal{I})=\left\{\bigcup I_j\ |\ (I_j)\sub \mathcal{I}\text{ は互いに交わらない集合族}\right\}$$

</dd></dl>

---

## 単調族

・空でない集合 $X$、部分集合 $\mathcal{M}\sub 2^X$ とする。
このとき、単調族 $\mathcal{M}$：
$$\forall\text{ 単調増加列 }(E_n)\sub\mathcal{M}\text{ に対して、}\bigcup E_n\in\mathcal{M}\\\ \\
\forall\text{ 単調減少列 }(E_n)\sub\mathcal{M}\text{ に対して、}\bigcap E_n\in\mathcal{M}\\\ \\$$

- 集合 $X$、部分集合 $\mathfrak{M}\sub2^X$ とする。
このとき、
$$\mathfrak{M}\text{ は }\sigma\text{-集合族}\iff\mathfrak{M}\text{ は有限加法族かつ単調族}$$

---

### 生成される単調族

<dl><dt>

・空でない集合 $X$、単調族の族 $\mathcal{M}_j\sub 2^X$ とする。
このとき、$\bigcap \mathcal{M}_j$ は単調族。
<br>

- 空でない集合 $X$、部分集合 $\mathcal{I}\sub 2^X$ とする。
このとき、$$\mathcal{M}(\mathcal{I})=\bigcap\{\mathcal{M}\ |\ \text{単調族 }\mathcal{M}\text{ であって、}\mathcal{I}\sub\mathcal{M}\}$$
を含む最小の単調族。
<br>

</dt><dd>

- 空でない集合 $X$、有限加法族 $\mathcal{A}\sub 2^X$ とする。
このとき、
$$\sigma(\mathcal{A})=\mathcal{M}(\mathcal{A})$$

</dd></dl>

---

# 有限加法的測度

## 半集合代数上の有限加法的測度

・集合 $X$、半集合代数 $\mathcal{I}$ とする。
このとき、有限加法的測度 $\mu$：
$$\mu:\mathcal{I}\to[0,\infty]\\\ \\
\mu(\phi)=0\\\ \\
\forall\text{ 交わりのない }I_1,...,I_n\in\mathcal{I},\ \ \bigcup_{i=1}^nI_i\in\mathcal{I}\text{ に対して、}\mu\left(\bigcup_{i=1}^nI_i\right)=\sum_{i=1}^n\mu(I_i)$$
さらに、有限加法的測度 $\mu$ が $\sigma$-加法的測度：
$$\forall\text{ 非交叉列 }(I_n)\sub\mathcal{I},\ \ \bigcup I_n\in\mathcal{I}\text{ に対して、}\mu\left(\bigcup I_n\right)=\sum\mu(I_n)$$

---

### 有限加法族上の有限加法的測度

<dl><dt>

・集合 $X$、半集合代数 $\mathcal{I}$、有限加法的測度 $\mu_0:\mathcal{I}\to[0,\infty]$ とする。
このとき、
$$\text{ある }\mu:\mathcal{A}(\mathcal{I})\to[0,\infty]\text{ が一意的に存在して、}\\\ \\
\mu\text{ は }\mu_0\text{ の拡張}$$
さらに、$\mu_0$ が $\sigma$-加法的ならば、$\mu$ は $\sigma$-加法的。
<br>

</dt><dd>

- 集合 $X$、有限加法族 $\mathcal{A}$、有限加法的測度 $\mu:\mathcal{A}\to[0,\infty]$ とする。
このとき、
$$\forall A,B\in\mathcal{A},\ A\sub B\text{ に対して、}\mu(A)\le\mu(B)\\\ \\
\forall A_1,...,A_n\in\mathcal{A}\text{ に対して、}\mu\left(\bigcup_{i=1}^nA_i\right)\le\sum_{i=1}^n\mu(A_i)\\\ \\
\mu\text{ が }\sigma\text{-加法的ならば、}\forall\text{ 点列 }(A_n)\sub\mathcal{A},\ \ \bigcup A_n\in\mathcal{A}\text{ に対して、}\\\mu\left(\bigcup A_n\right)\le\sum \mu(A_n)\\\ \\$$

- $A\sub B,\ \mu(A)<\infty$ なる $A,B\in\mathcal{A}$ とする。
このとき、
$$\mu(B-A)=\mu(B)-\mu(A)$$

</dd></dl>

---

## $σ$-有限測度

    ・有限測度はμ(X)<∞
<br>

・集合 $X$、半集合代数 $\mathcal{I}$、有限加法的測度 $\mu:\mathcal{I}\to[0,\infty]$ とする。
このとき、$\sigma$-有限測度 $\mu$：
$$\exist\text{ 集合列 }I_n\sub\mathcal{I}\text{ であって、}\\\ \\
X=\bigcup_n I_n\mu(I_n)<\infty\\\ \\$$

- 集合 $X$、有限加法族 $\mathcal{A}$、$\sigma$-有限測度である有限加法的測度 $\mu:\mathcal{I}\to[0,\infty]$ とする。
このとき、
$$\exist\text{ 非交叉列 }A_n\sub\mathcal{A}\text{ であって、}X=\bigcup_nA_n,\quad\mu(A_n)<\infty\\\ \\
\exist\text{ 単調増加列 }A_n\sub\mathcal{A}\text{ であって、}X=\bigcup_nA_n,\quad\mu(A_n)<\infty\\\ \\$$

      ・σ-加法的な有限加法的測度ではない。

---
---
---


# Caratheodory外測度

<dl><dt>

・集合 $X$、有限加法族 $\mathcal{A}\sub 2^X$、$\sigma$-加法的測度 $\mu:\mathcal{A}\to[0,\infty]$ とする。
このとき、
$$\mu^*:2^X\to[0,\infty]\\\ \\
\mu^*(E)=\inf\left\{\left.\sum_{n\in\bm{N}}\mu(A_n)\ \right|\ A_n\subset\mathcal{A},E\subset\bigcup A_n\right\},\\\ \\
\mathfrak{M}=\{A\in2^X\ |\ \mu^*(E\cap A)+\mu^*(E\cap A^c)=\mu^*(E),\ \forall E\in2^X\}$$
と定める。
<br>

</dt><dd>

- $$\mu^*(\phi)=0\\\ \\
\forall E,F\sub X,\ E\sub F\text{ に対して、}\mu^*(E)\le\mu^*(F)\\\ \\
\forall\text{ 集合列 }E_n\sub X\text{ に対して、}\mu^*\left(\bigcup_n E_n\right)\le\sum_{n}\mu^*(E_n)\\\ \\$$

      ・上記の性質を満たすμ:2^X→[0,∞]をCaratheodory外測度という。
<br>

- $$\mu^*(E)=0\Rightarrow E\in\mathfrak{M}\\\ \\$$

- $\mathfrak{M}$ は $\sigma$-加法族であって、
$$\forall\text{ 非交叉列 }(A_n)\sub\mathfrak{M},\ \forall E\sub X,\ \forall N\in\bm{N}-\{0\}\text{ に対して、}\\\ \\
\mu^*(E)=\sum_{n=1}^N\mu^*(E\cap A_n)+\mu^*\left(E-\bigcup_{n=1}^N A_n\right)\\\ \\$$

- $\mu^*:\mathfrak{M}\to[0,\infty]$ は測度、$\mathcal{A}\subset\mathfrak{M}$ であって、$\mu^*$ は $\mu$ の拡張。
<br>

      ・書いてある順番は証明どうりではない。

</dd></dl>

---

## $σ$-有限測度のとき

・集合 $X$、有限加法族 $\mathcal{A}\sub2^X$、$\sigma$-加法的測度 $\mu:\mathcal{A}\to[0,\infty]$ とすると、$\mu$ は $\sigma(\mathcal{A})$ 上の測度に拡張できる。
さらに、$\mu$ が $\mathcal{A}$ 上 $\sigma$-有限ならば、この拡張は一意的。

---

# $σ$-有限測度と直積可測空間

## Tonelliの定理

・直積測度：$$\otimes_{j=1}^N\mu_j:\otimes\mathfrak{M}\to[0,\infty],\quad X_i,\mathfrak{M}_i,\mu_i\ (i=1,...,N){は}\sigma{-有限な測度})$$

- $$μ(E_1×...×E_n)=μ_1(E_1)...μ_N(E_N)$$を満たすものがただ一つ存在する（直積測度）

---

・$(X_i,\mathfrak{M}_i,\mu_i)\ (i=1,...,N)$を$\sigma$-有限な測度空間、$f:X_1\times...\times X_N\to[0,\infty]$を非負値可測関数とする。
このとき、$$\Phi:X_1\times...\times \tilde X_k\times...\times X_N\to[0,\infty],\\\ \\(x_1,...,\tilde x_k,...,x_N)\mapsto\int_{X_k}f(x_1,...,x_k,...,x_N)d\mu_k$$は可測関数である

・$(X_i,\mathfrak{M}_i,\mu_i)\ (i=1,...,N)$を$\sigma$-有限な測度空間、$f:X_1\times...\times X_N\to[0,\infty]$を非負値可測関数、$\tau$を$n$次の置換とする。
このとき、$$\int_{\prod_{k=1}^N X_k}fd\otimes_{j=1}^N\mu_j=\int_{X_{\tau(1)}}\left(...\left(\int_{X_{\sigma(N)}}f(x_1,...,x_N)d\mu_{\sigma(N)}\right)...\right)d\mu_{\sigma(1)}$$

    ・このとき累次積分の各被積分部分は意味を持つ
    ・Tonelliの定理

---

## Fubiniの定理

・$(X_1,\mathfrak{M}_1,\mu_1)\ ,(X_2,\mathfrak{M}_2,\mu_2)$を$\sigma$-有限な測度空間、$f\in\mathcal{L}(X_1\times X_2,\mathfrak{M}_1\otimes\mathfrak{M}_2,\mu_1\otimes\mu_2)$とする。

- $N_1=\{x_1\in X_1\ |\ \int_{X_2}|f|d\mu_2=\infty\}$は$\mu_1$-零集合
- $$F_1(x_1)=\begin{cases}
\int_{X_2}|f|d\mu_2 & (x_1\in X_1-N_1) \\
0 & (x_1\in N_1)
\end{cases}$$は$\mu_1$-可積分
- $$\int_{X_1\times X_2}fd(\mu_1\otimes\mu_2)=\int_{X_1}F_1d\mu_1$$

        ・fは複素数値可積分関数
        ・定理は対称に成り立つ

---





