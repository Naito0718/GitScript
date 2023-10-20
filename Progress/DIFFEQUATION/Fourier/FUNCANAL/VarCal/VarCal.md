
- [フレシェ微分](#フレシェ微分)
- [汎関数 $J$](#汎関数-j)
  - [区分的に $C^1$ な関数](#区分的に-c1-な関数)




# フレシェ微分

・ノルム空間 $V,W$、$f:V\to W$、$a\in V$ とする。
このとき、$f$ が $a$ でフレシェ微分可能：
$$\exist U(a,\delta)\sub V,\exist L\in B(V,W)\text{ であって、}\\\ \\
\epsilon:U(a,\delta)\to\bm{R}\\
\epsilon(h)=\|f(a+h)-f(a)-L(h)\|\text{ が}\\\ \\
\lim_{\|h\|\to0}\frac{\epsilon(h)}{\|h\|}=0\text{ を満たす}$$
ここで、$f$ が $\forall v\in V$ で微分可能な時、
$$f':V\to B(V,W)$$
を $f$ の導関数という。

    ・ノルム空間だから、連続線形⇔有界線形。

---

<dl><dt>

ノルム空間 $V,W$、$a\in V$、$f,g:V\to W$ は $a$ でフレシェ微分可能とする。

</dt><dd>

- $f$ は $a$ で連続。

- 微分 $f'(a)=L$ は一意的に定まる。

      ・0の近傍で定まってれば、全体は一意的に定まる。
<br>

- $f+g,\alpha f\ \ (\alpha\in\bm{R})$ も $a$ で微分可能で、
$$(f+g)'(a)=f'(a)+g'(a),\quad(\alpha f)'(a)=\alpha f'(a)$$

<br>

- $f\in B(V,W)$ とする。
このとき、$f$ は $V$ 上微分可能で、$f'(x)=f(x)$
<br>

- $v\in V$ とする。
このとき、
$$h:\bm{R}\to W\\\ \\
h(t)=f(a+tv)$$
は $t=0$ でフレシェ微分可能で、
$$h'(0)=f'(a)(v)\\\ \\
f'(a)(v)=\lim_{t\to 0}\frac{h(t)-h(0)}{t}$$

</dd></dl>

---
---
---

# 汎関数 $J$

・$G_{[a,b]}^d=\{q:[a,b]\to\bm{R}^d\}$、$G_{\Omega}^m=\{u:\Omega\to\bm{R}\ |\ \Omega\sub\bm{R}^m\text{ は開集合 }\}$ とする。
このとき、汎関数 $J$：
$$J:F_{[a,b]}^d(F_{\Omega}^m)\to\bm{R}$$

- $q\in F_{(a,b)}^d$、$u\in F_{\Omega}^m$ とする。
このとき、
$$J(q)=\int_a^b F(t,q(t),q'(t)),\quad F:[a,b]\times\bm{R}^d\times\bm{R}^d\to\bm{R}\\\ \\
J(u)=\int_{\Omega}F(x,u(x),\nabla u(x)),\quad F:\Omega\times\bm{R}\times\bm{R}^m\to\bm{R}$$
は共に汎関数。

---

## 区分的に $C^1$ な関数

・$C^1$ 関数 $F:[a,b]\times\bm{R}^d\times\bm{R}^d\to\bm{R}$ とする。
このとき、
$$J:PC^1([a,b],\bm{R}^d,\|\cdot\|_1)\to\bm{R}\\\ \\
J(q)=\int_a^b F(t,q(t),q'(t))$$
は連続関数。

    ・有限増分の定理より、$F$ は一様連続。
    ・PCの元を用いることで、F_nが可積分関数族になる。

