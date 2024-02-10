
- [一変数関数とルベーグ積分](#一変数関数とルベーグ積分)
  - [連続関数と零集合](#連続関数と零集合)
  - [偶関数と積分](#偶関数と積分)
- [一変数連続関数の微分とルベーグ積分](#一変数連続関数の微分とルベーグ積分)
  - [一変数連続非負値関数の微分とルベーグ積分](#一変数連続非負値関数の微分とルベーグ積分)
- [一変数関数と部分積分](#一変数関数と部分積分)
- [一変数関数と可積分条件](#一変数関数と可積分条件)
  - [部分積分と可積分条件](#部分積分と可積分条件)
- [一変数連続関数と単調増加な変数変換](#一変数連続関数と単調増加な変数変換)


# 一変数関数とルベーグ積分

## 連続関数と零集合

・正値連続関数 $f:\bm{R}\to(0,\infty)$、$A\in\mathfrak{B}_R$ とする。
このとき、$$\int_Afdm=0\iff m(A)=0$$

---

## 偶関数と積分

・$a\in\bm{R}$、非負値Borel関数 $f:\bm{R}\to[0,\infty]$ が $a$ に関して偶関数、すなわち
$\forall x\in\bm{R}\text{ に対して }f(2a-x)=f(x)$ が成り立つとする。
このとき、
$$\int_{\bm{R}}fdm=2\int_a^{\infty}fdm$$

---

# 一変数連続関数の微分とルベーグ積分

・$a<b$ なる $a,b\in[-\infty,\infty]$、連続かつ可積分な $f:(a,b)\to\bm{C}$ とする。
このとき、
$$F:(a,b)\to\bm{C}\\\ \\
F(x)=\int_a^xfdm$$
と定めると、$F$ は $(a,b)$ 上 $C^1$ であって、
$$\forall x\in(a,b)\text{ に対して、}\frac{dF}{dx}(x)=f(x)\\\ \\
\int_a^bf(x)=\lim_{x\to -b}F(x)-\lim_{x\to +a}F(x)$$
ただし、最下段の式の右辺の各項はそれぞれ有限値。
<br>

- $a<b$ なる $a,b\in[-\infty,\infty]$、連続な $f:(a,b)\to\bm{C}$ とする。
このとき、
$$F:(a,b)\to\bm{C}\\\ \\
F(x)=\begin{cases}
\int_0^xfdm  & (x\ge0)    \\
-\int_x^0fdn & (x<0)    \\
\end{cases}$$
と定めると、$F$ は $(a,b)$ 上 $C^1$ であって、
$$\forall x\in(a,b)\text{ に対して、}\frac{dF}{dx}(x)=f(x)\\\ \\$$

      ・fは可積分でなくても原始関数が存在する。

---

## 一変数連続非負値関数の微分とルベーグ積分

・$a<b$ なる $a,b\in[-\infty,\infty]$、連続な $f:(a,b)\to[0,\infty),\ g:(a,b)\to(-\infty,0]$、$f,g$ の原始関数 $F,G:(a,b)\to\bm{R}$ とする。
このとき、$F$ は単調増加、$G$ は単調減少であって、
$$\int_a^bfdm=\sup_{x\in(a,b)}F(x)-\inf_{x\in(a,b)}F(x)=\lim_{x\to b}F(x)-\lim_{x\to a}F(x)\\\ \\
\int_a^bgdm=\inf_{x\in(a,b)}G(x)-\sup_{x\in(a,b)}G(x)=\lim_{x\to b}G(x)-\lim_{x\to a}G(x)$$
であって、
$$F\text{ が有界}\iff f\in \mathcal{L}^1(a,b),\quad G\text{ が有界}\iff g\in \mathcal{L}^1(a,b)$$

---

# 一変数関数と部分積分

・$a<b$ なる $a,b\in[-\infty,\infty]$、連続関数 $f:(a,b)\to\bm{C}$、$C^1$ 関数 $G:(a,b)\to\bm{C}$ とする。
このとき、
$$fG\in\mathcal{L}^1(a,b)\text{ かつ、ある }f\text{ の原始関数 }F\text{ であって、}F\frac{dG}{dX}\in\bm{L}^1(a,b)\\\ \\
\Rightarrow\int_{(a,b)}fGdm=\lim_{x\to -b}\Big[F(x)G(x)\Big]-\lim_{x\to +a}\Big[F(x)G(x)\Big]-\int_{(a,b)}\Big[F\frac{dG}{dx}\Big]dm$$
ただし、最下段の式の右辺の各項はそれぞれ有限値。
<br>


---

# 一変数関数と可積分条件

・古典的なやつ？？？

---

## 部分積分と可積分条件

・$a<b$ なる $a,b\in[-\infty,\infty]$、連続関数 $f:(a,b)\to\bm{C}$、$C^1$ 関数 $G,H:(a,b)\to\bm{R}$ とする。
このとき、
$$fG\in\mathcal{L}^1(a,b)\text{ かつ、ある }f\text{ の原始関数 }F\text{ であって、}F\frac{dG}{dX}+\frac{dH}{dx}\text{ は }(a,b)\text{ 上非負値}\\\ \\
\Rightarrow\int_{(a,b)}fGdm+\int_{(a,b)}\Big[F\frac{dG}{dx}+\frac{dH}{dx}\Big]dm=\lim_{x\to -b}\Big[F(x)G(x)+H(x)\Big]-\lim_{x\to +a}\Big[F(x)G(x)+H(x)\Big]\\\ \\$$
特に、
$$FG+H\text{ が }(a,b)\text{ 上有界 }\iff F\frac{dG}{dX}+\frac{dH}{dx}\in\mathcal{L}^1(a,b)\\\ \\$$

      ・常にFは固定して考える。

---

# 一変数連続関数と単調増加な変数変換

・単調増加または単調減少な $C^1$ 写像 $\Psi:(a,b)\to\bm{R}$ が、$\inf_{x\in(a,b)}\Psi(x),\sup_{x\in(a,b)}\Psi(x)\in\bm{R}$ を満たすとする。
このとき、
$$\forall\text{ 連続関数 }f:(\inf_{x\in(a,b)}\Psi(x),\sup_{x\in(a,b)}\Psi(x))\to\bm{R}\text{ に対して、}\\\ \\
\int_{\inf_{x\in(a,b)}\Psi(x)}^{\sup_{x\in(a,b)}\Psi(x)}fdm=\int_a^b(f\circ\Psi)\Psi'dm$$


