
- [$L(Ω)$ と合成](#lω-と合成)
  - [超関数の変数変換](#超関数の変数変換)
  - [平行移動とスケール変換](#平行移動とスケール変換)
- [超関数の台](#超関数の台)


# $L(Ω)$ と合成

・開集合 $\Omega_1,\Omega_2\sub\bm{R}^N$、$C^1$ 微分同相写像 $\Psi:\Omega_1\to \Omega_2$、$f,g:\Omega_2\to\bm{C}$ とする。
このとき、
$$f(x)=g(x)\quad(a.e.)\Rightarrow (f\circ\Psi)(x)=(g\circ\Psi)(x)\quad(a.e.)$$
したがって、$\forall [f]\in L(\Omega_2)$ に対して、$[f]\circ\Psi=[f\circ\Psi]$ と定めると、これはwell-defined。
<br>

    ・L(Ω)はa.e.で等しいBorel関数の同値類全体。
<br>

- 開集合 $\Omega_1,\Omega_2\sub\bm{R}^N$、$C^1$ 微分同相写像 $\Psi:\Omega_1\to \Omega_2$、$[f]\in L^1_{loc}(\Omega_2)$ とする。
このとき、$[f]\circ\Psi\in L^1_{loc}(\Omega_1)$

---

## 超関数の変数変換

<dl><dt>

・開集合 $\Omega_1,\Omega_2\sub\bm{R}^N$、$C^{\infty}$ 微分同相写像 $\Psi:\Omega_1\to \Omega_2$、$[f]\in L^1_{loc}(\Omega_2)$、$\phi\in D(\Omega_1)$ とする。
このとき、
$$([f]\circ\Psi)(\phi)=[f]\Big((\phi\circ\Psi^{-1})|\det\Psi^{-1'}|\Big)\\\ \\$$

- 開集合 $\Omega_1,\Omega_2\sub\bm{R}^N$、$C^{\infty}$ 微分同相写像 $\Psi:\Omega_1\to \Omega_2$、$u\in D'(\Omega_2)$ とする。
このとき、
$$u\circ\Psi:D(\Omega_1)\to\bm{C}\\\ \\
u\circ\Psi(\phi)=u\Big((\phi\circ\Psi)|\det\Psi^{-1'}|\Big)$$
と定めると、$u\circ\Psi\in D'(\Omega_1)$ であって、$u=[f]$ の時と整合する。ここで、$u\circ\Psi$ を $u$ の $\Psi$ による変数変換という。
<br>

</dt><dd>

- 
$$\circ\Psi:D'(\Omega_)\to D'(\Omega_1)\\\ \\
\circ\Psi(u)=u\circ\Psi$$
と定めると、これは連続線形写像。
<br>

- 開集合 $\Omega_1,\Omega_2,\Omega_3\sub\bm{R}^N$、$C^{\infty}$ 微分同相写像 $\Psi:\Omega_1\to \Omega_2,\ \Phi:\Omega_2\to\Omega_3$、$u\in D'(\Omega_2)$、$u\in D'(\Omega)$ とする。
このとき、
$$u\circ(\Psi\circ\Phi)=(u\circ\Psi)\circ\Phi\\\ \\$$

- $$\forall\phi\in D(\Omega_1)\text{ に対して、}\sum_{i=1}^N(\phi\circ\Psi^{-1})\partial_j\Big(\{(\partial_j\Psi_i)\circ\Psi^{-1}\}|\det\Psi^{-1'}|\Big)=0$$
したがって、
$$\partial_j(u\circ\Psi)=\sum_{i=1}^N\partial\Psi_i((\partial_j u)\circ\Psi)$$

      ・最後の式の右辺はε(Ω)と超関数の積。


</dd></dl> 

---

## 平行移動とスケール変換

・$u\in D'(\bm{R}^N)$、$y\in\bm{R}^N$、$r\in\bm{R}-\{0\}$ とする。
このとき、
$$T_y,S_r:\bm{R}^N\to\bm{R}^N\\\ \\
T_y(x)=x-y,\quad S_r(x)=rx$$
と定めると、これらは $C^{\infty}$ 微分同相写像。ここで、$u$ の $T_y$ による変数変換を $T_yu=u\circ T_y$、$u$ の $S_r$ による変数変換を $u_r=u\circ S_r$ と書く。
<br>

- 多重指数 $I$ とする。
このとき、
$$\partial^I(T_yu)=T_y(\partial^Iu),\quad\partial^I(u_r)=r^{|I|}(\partial^Iu)$$


---

# 超関数の台

<dl><dt>

・開集合 $\Omega\sub\bm{R}^N$、$u\in D'(\Omega)$ とする。
このとき、
$$A_u=\{U\sub\Omega\ |\ U\text{ は開集合であって、}\forall\phi\in D(U)\text{ に対して、}u(\phi)=0\}$$
と定めると、$\bigcup A_u\in A_u$。
したがって、この集合は包含関係について最大元 $U_u=\bigcup A_u$ を持つ。ここで、$\Omega\cap U_u^c$ を超関数 $u$ の台といい、$\mathrm{supp}\ u=\Omega\cap U_u^c$ と書く。
<br>

</dt><dd>

- $u_1,u_2\in D'(\Omega)$ とする。
このとき、
$$\mathrm{supp}\ u_1\sub\mathrm{supp}\ u_2\iff\forall \phi\in D(\Omega-\mathrm{supp}\ u_2)\text{ に対して、}u_1(\phi)=0\\\ \\
\iff U_{u_2}\sub U_{u_1}\iff\forall\phi\in D(U_{u_2})\text{ に対して、}u_1(\phi)=0\\\ \\
x\in\mathrm{supp}\ u\Rightarrow\forall\text{ 開集合 }x\sub U\sub\Omega\text{ に対して、}\exist\phi\in D(U)\text{ であって、}u(\phi)\neq0\\\ \\$$

      ・結局包含の含まれる側でD取ってみればよい。
<br>

- $u\in D'(\Omega)$、多重指数 $I$ とする。
このとき、
$$\mathrm{supp}\ \partial^Iu\sub\mathrm{supp}\ u\\\ \\$$

- $u\in D'(\Omega)$、$f\in\epsilon(\Omega)$ とする。
このとき、
$$\mathrm{supp}\ fu\sub\mathrm{supp}\ f\cap\mathrm{supp}\ u\\\ \\$$

      ・suppfはコンパクトとは限らない。
<br>

- 開集合 $\Omega_1,\Omega_2\sub\bm{R}^N$、$C^{\infty}$ 微分同相写像 $\Psi:\Omega_1\to\Omega_2$、$u\in D'(\Omega_2)$ とする。
このとき、
$$\mathrm{supp}\ (u\circ\Psi)=\Psi^{-1}(\mathrm{supp}\ u)\\\ \\$$

- $[f]\in L^1_{loc}(\Omega)$ とする。
このとき、
$$\mathrm{supp}\ [f]\sub\mathrm{supp}\ f\\\ \\$$
特に、
$$f\in C(\Omega)\Rightarrow\mathrm{supp}\ [f]=\mathrm{supp}\ f$$

      ・左辺は超関数の台、右辺は関数の台。
<br>

</dd></dl>

---

