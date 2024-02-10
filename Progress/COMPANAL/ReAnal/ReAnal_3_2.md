
- [一変数での向きの付いた積分](#一変数での向きの付いた積分)
- [不定積分](#不定積分)
  - [不定積分と微分](#不定積分と微分)
- [一変数での広義積分](#一変数での広義積分)
  - [広義積分](#広義積分)
        - [収束判定](#収束判定)

# 一変数での向きの付いた積分

    ・R^nでは多様体でないと向き付けできない。
<br>

・$a,b\in\bm{R}$、$a,b$ を端とする区間で可積分な関数 $f$ とする。
このとき、
$$\int_a^bf(x)dx=\begin{cases}
\int_{[a,b]}f(x)dx & (a<b)  \\
-\int_{[b,a]}f(x)dx & (b<a)  \\
\end{cases}$$
と定めると、
$$\forall a,b,c\in\bm{R}\text{ に対して、}\\\ \\
\int_a^af(x)dx=0,\quad\int_a^cf(x)dx=\int_a^bf(x)dx+\int_b^cf(x)dx$$
が成り立つ。

---

# 不定積分

<dl><dt>

・有界閉区間 $I\sub\bm{R}$、$a\in I$、$I$ 上可積分な $f:I\to\bm{R}$ とする。
このとき、
$$F_a:I\to\bm{R}\\\ \\
F_a(x)=\int_a^xf(x)dx$$
と定めると、これはwell-defined。
<br>

</dt><dd>

- $$F_a(a)=0,\quad F_a(x)-F_b(x)=\int_a^bf(x)dx\\\ \\$$

- $I$ 上有界な可積分関数 $f:I\to\bm{R}$、$a\in I$ とする。
このとき、$F_a$ は $I$ 上リプシッツ連続。

</dd></dl>

---

## 不定積分と微分

    ・Fがfの原始関数ならば、fの原始関数はF+C

<dl><dt>

・有界閉区間 $I\sub\bm{R}$、$I$ 上微分可能で $f'$ が $I$ 上可積分な $f:I\to\bm{R}$ とする。
このとき、
$$\forall a,b\in I\text{ に対して、 }\int_a^bf'(x)=f(b)-f(a)\\\ \\$$

</dt><dd>

- $I$ 上可積分かつ $a\in I$ で連続な $f:I\to \bm{R}$、 とする。
このとき、


</dd></dl>

---


# 一変数での広義積分

## 広義積分

・関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分かつ $\int_a^{\to b}fdx\in \bm{R}$

    ・両側可積分は積分区間を分割する

→関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分ならば、
$\int_a^{\to b}fdx\in \bm{R}\iff\forall\epsilon>0{に対して}\exist c\in I{であって}c<v<u<b{ならば}|\int_v^uf(x)dx|<\epsilon$

---

・絶対収束：$|f|$が広義可積分なこと

→$\int fdx$が絶対収束するならば、$\int fdx$は収束する

→$|f(x)|\le g(x)$かつ広義可積分な$g(x)$が存在すれば、$\int|f(x)|dx\le\int g(x)dx$（絶対収束）

---

##### 収束判定

→関数$f:[a.b)\to\bm{R}$が $\forall[a,u]$ で可積分とする

・$b=\infty$ で $f(x)=O(x^{\alpha})(x\to\infty)$を$\alpha<-1$で満たすならば、$\int_a^{\infty}f(x)dx\in\bm{R}$

---

・$b\in\bm{R}$ で $f(x)=O((b-x)^{\alpha})(x\to -b)$を$\alpha>-1$で満たすならば、$\int_a^{\to b}f(x)dx\in\bm{R}$

---
---
---








      