
- [フレシェ微分](#フレシェ微分)
  - [フレシェ微分の性質](#フレシェ微分の性質)
  - [停留値](#停留値)
  - [フレシェ二階微分](#フレシェ二階微分)
- [汎関数 $J$](#汎関数-j)
  - [区分的に $C^1$ な関数](#区分的に-c1-な関数)
  - [汎関数 $J$](#汎関数-j-1)




# フレシェ微分

・$\bm{R,C}$ 上ノルム空間 $V,W$、$f:V\to W$、$a\in V$ とする。
このとき、$f$ が $a$ でフレシェ微分可能：
$$\exist U(0,\delta)\sub V,\exist L_a\in B(V,W)\text{ であって、}\\\ \\
\epsilon:U(0,\delta)\to\bm{R}\\
\epsilon(h)=\|f(a+h)-f(a)-L_a(h)\|\text{ が}\\\ \\
\lim_{\|h\|\to0}\frac{\epsilon(h)}{\|h\|}=0\text{ を満たす}$$
ここで、$f$ が $\forall v\in V$ で微分可能な時、
$$f':V\to B(V,W)\\\ \\
f'(v)=L_v$$
を $f$ の導関数といい、$f'$ が連続ならば $C^1$ という。
<br>

    ・ノルム空間だから、連続線形⇔有界線形。
<br>

---

## フレシェ微分の性質

<dl><dt>

・$\bm{R,C}$ 上ノルム空間 $V,W$、$a\in V$、$f,g:V\to W$ は $a$ でフレシェ微分可能とする。

</dt><dd>

- $f$ は $a$ で連続。

- 微分 $f'(a)=L_a$ は一意的に定まる。
<br>

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
$$h:\bm{C}\to W\\\ \\
h(t)=f(a+tv)$$
と定めると、$h$ は $t=0$ でフレシェ微分可能で、
$$h'(0)=f'(a)(v)\\\ \\
\lim_{t\to 0}\left\|\frac{h(t)-h(0)}{t}-f'(a)(v)\right\|=0$$

</dd></dl>

---

## 停留値

・$\bm{R,C}$ 上ノルム空間 $V$、極値 $v_0\in V$ で微分可能な $f\in V^{\vee}$、$ とする。
このとき、$$f'(v_0)=0$$

---
---
---

## フレシェ二階微分

・


---

# 汎関数 $J$

・$G_{[a,b]}^d=\{q:[a,b]\to\bm{R}^d\}$、$G_{\Omega}^m=\{u:\Omega\to\bm{R}\ |\ \Omega\sub\bm{R}^m\text{ は開集合 }\}$ とする。
このとき、汎関数 $J$：
$$J:F_{[a,b]}^d(F_{\Omega}^m)\to\bm{R}\\\ \\$$

- $q\in F_{(a,b)}^d$、$u\in F_{\Omega}^m$ とする。
このとき、
$$J(q)=\int_a^b F(t,q(t),q'(t)),\quad F:[a,b]\times\bm{R}^d\times\bm{R}^d\to\bm{R}\\\ \\
J(u)=\int_{\Omega}F(x,u(x),\nabla u(x)),\quad F:\Omega\times\bm{R}\times\bm{R}^m\to\bm{R}$$
は共に汎関数。

---

## 区分的に $C^1$ な関数

<dl><dt>

・$$PC^1([a,b],\bm{R}^d)=\{f:[a,b]\to\bm{R}^d\ |\ f\text{ は }[a,b]\text{ 上区分的に }C^1\}\\\ \\
\|\cdot\|_0,\|\cdot\|_1:PC^1([a,b],\bm{R}^d)\to[0,\infty)\\\ \\
\|f\|_0=\sup_{x\in[a,b]}|f(x)|\\\ \\
\|f\|_1=\sup_{x\in[a,b]}|f(x)|+\sup_{x\in[a,b]}|f'(x)|\\\ \\$$
と定めると、$PC^1([a,b],\bm{R}^d)$ は $\bm{R}$ 上ベクトル空間で、$\|\cdot\|_0,\|\cdot\|_1$ は $PC^1([a,b],\bm{R}^d)$ のノルム。
<br>

    ・一般に環ではない。
<br>

</dt><dd>

- $f\in PC([a,b],\bm{R}^d)$ とする。
このとき、
$$\|f\|_1=0\Rightarrow \|f\|_0=0\\\ \\$$

      ・点列の収束でも同様。
<br>

- $$PC^1([a,b],\bm{R}^d)\sub L^2[a,b]$$
したがって、
$$(\cdot)_{L^2}:PC^1([a,b],\bm{R}^d)\times PC^1([a,b],\bm{R}^d)\to\bm{R}\\\ \\
(f,g)_{L^2}=\int_a^bf(t)g(t)dt$$
はP $C^1([a,b],\bm{R}^d)$ 上の内積。

</dd></dl>

---

## 汎関数 $J$

<dl><dt>

・$C^1$ 関数 $F:[a,b]\times\bm{R}^d\times\bm{R}^d\to\bm{R}$ とする。
このとき、
$$J:PC^1([a,b],\bm{R}^d,\|\cdot\|_1)\to\bm{R}\\\ \\
J(q)=\int_a^b F(t,q(t),q'(t))$$
と定めると、これは連続関数。
<br>

    ・有限増分の定理より、Fは一様連続。
    ・PCの元を用いることで、F_nが可積分関数族になる。
<br>

</dt><dd>

- $J$ は $PC^1([a,b],\bm{R}^d,\|\cdot\|_1)$ 上 $C^1$ であって、
$$J'(q)(g)=\int_a^b\Big\{F_q(t,q(t),q'(t))\cdot g(t)+F_v(t,q(t),q'(t))\cdot g'(t)\Big\}dt\\\ \\
=(F_q(t,q(t),q'(t)),g(t))_{L^2}+(F_v(t,q(t),q'(t),g'(t)))_{L^2}$$
ただし、$$F_q=\left(\frac{\partial F(t,q,v)}{\partial q^1},...,\frac{\partial F(t,q,v)}{\partial q^d}\right)$$
とする。

</dd></dl>


