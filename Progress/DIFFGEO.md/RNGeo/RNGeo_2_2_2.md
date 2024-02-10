
- [ベクトル積](#ベクトル積)
- [計量行列 $G(p)$](#計量行列-gp)
- [$R^N$ の正の向きの直交座標](#rn-の正の向きの直交座標)
- [$R^N$ 上のgrad](#rn-上のgrad)
  - [$R^N$ 上のdiv](#rn-上のdiv)
  - [$R^N$ 上のrot](#rn-上のrot)
  - [$R^N$ 上の$Δ$](#rn-上のδ)
- [星形集合](#星形集合)
  - [Poincareの補題](#poincareの補題)




# ベクトル積

    ・Hodge*によるv_1∧...v_{N-1}の像。
<br>

<dl><dt>

・$v_1,...,v_{N-1}\in\bm{R}^N$ とする。
このとき、
$$\{v_1,...,v_{N-1}\}\text{ が線形独立}\iff\star(v_1\wedge...\wedge v_{N-1})\neq0\\\ \\$$

</dt><dd>

- $$|\star(v_1\wedge...\wedge v_{N-1})|^2=\det(v_i,v_j)_{i,j}\\\ \\$$

- $u\in\bm{R}^N$ とする。
このとき、
$$(\star(v_1\wedge...\wedge v_{N-1}),u)=\det(v_1,...,v_{N-1},u)$$ 
特に、$v_i$ は $\star(v_1\wedge...\wedge v_{N-1})$ と直交する。
<br>

- 線形独立な $v_1,...,v_{N-1}\in\bm{R}^N$ とする。
このとき、平行 $N-1$ 面体
$$A=\left\{\sum_{i=1}^{N-1} t_iv_i\ |\ 0\le t_i\le1\right\}$$
において、$v(A)=|\star(v_1\wedge...\wedge v_{N-1})|$
<br>

      ・一応ルベーグ測度。

</dd></dl>

---

# 計量行列 $G(p)$

<dl><dt>

・$n$ 次元多様体 $M\sub\bm{R}^N$、$M$ の局所座標 $(U,\phi)$ とする。
このとき、
$$g_{U,\phi}:U\to GL(n,\bm{R})\\\ \\
g_{(U,\phi)}(p)=\left(\frac{\partial}{\partial x^i}p,\frac{\partial}{\partial x^j}p\right)_{i,j}\\\ \\
G_{U,\phi}:U\to\bm{R}\\\ \\
G_{U,\phi}(p)=\det g_{U,\phi}(p)=\left(\frac{\partial}{\partial x^1}p\wedge...\wedge\frac{\partial}{\partial x^n}p,\ \frac{\partial}{\partial x^1}p\wedge...\wedge\frac{\partial}{\partial x^n}p\right)_n>0$$
と定めると、対称行列 $g_{U,\phi}$ の値域はwell-definedで、$G$ 
は $C^{\infty}$ 写像。ここで、$g_{U,\phi}$ を $M$ の $(U,\phi)$ に関する計量行列という。
<br>

</dt><dd>

- $n=N-1$ のとき、すなわち超曲面の時は、
$$G_{U,\phi}(p)=\left|\star\left(\frac{\partial}{\partial x^1}p\wedge...\wedge\frac{\partial}{\partial x^n}p\right)\right|^2$$
であって、$\sqrt{G_{U,\phi}(p)}$ は $\frac{\partial}{\partial x^i}p$ の張る平行 $N-1$ 面体の体積。
<br>

- $M$ の局所座標 $(U,\phi;x^1,...,x^n)$、$(V,\psi;y^1,...,y^n)$、$p\in U\cap V$ とする。
このとき、
$$\sqrt{G_{(U,\phi)}(p)}=\sqrt{G_{V,\psi}}\left|\det\left(\frac{\partial y^i}{\partial x^j}\right)_{i,j}\right|$$

</dd></dl>

---

# $R^N$ の正の向きの直交座標

    ・R^Nの局所座標って、まあ極座標とかか。
<br>
<dl><dt>

・$R^N$ の局所座標 $(U,\phi;y^1,...,y^N)$ とする。
このとき、直交座標、正の向きの直交座標：
$$\text{直交：}\forall p\in U\text{ に対して、}\left(\frac{\partial}{\partial y^i}p,\frac{\partial}{\partial y^j}p\right)=\delta_{ij}\\\ \\
\text{正の向き：}\forall p\in U\text{ に対して、}\det\left(\frac{\partial}{\partial y^1}p,...,\frac{\partial}{\partial y^N}p\right)>0\\\ \\$$

</dt><dd>

- $R^N$ の正の向きの局所座標 $(U,\phi;y^1,...,y^N)$ とする。
このとき、
$$h_i:U\to\bm{R}\\\ \\
h_i(p)=\left|\frac{\partial}{\partial y^i}p\right|>0$$
と定めると、これは $C^{\infty}$。
<br>

- 標準座標 $dx^i$ とする。
このとき、
$$(h_1dy^1\wedge...\wedge h_Ndy^N)_p=(dx_1\wedge...\wedge dx^N)_p$$
であって、
$$\star(h_{\sigma(1)}dy^{\sigma(1)}\wedge...\wedge h_{\sigma(r)}dy^{\sigma(r)})=\mathrm{sgn}(\sigma)h_{\sigma(r+1)}dy^{\sigma(r+1)}\wedge...\wedge h_{\sigma(N)}dy^{\sigma(N)}\\\ \\
\star(1)=\frac{1}{h_1...h_N}dy^1\wedge...\wedge dy^N$$

</dd></dl>

---

# $R^N$ 上のgrad

<dl><dt>

・$n$ 次元多様体 $M\sub\bm{R}^N$、$p$ で微分可能な関数 $f:M\to\bm{R}$ とする。
このとき、$df_p\in (T_pM)^*$ より、
$$\text{ある }\mathrm{grad}_pf\in T_pM\text{ がただ一つ存在して、}\forall v\in T_pM\text{ に対して、}\\\ \\
(\mathrm{grad}_pf,v)_{T_pM}=df_p(v)$$
ここで、$\mathrm{grad}_pf$ を $f$ の勾配という。
<br>

</dt><dd>

- $p$ まわりの局所座標 $(U,\phi;x^1,...,x^n)$、$(U,\phi)$ に関する計量行列 $g_{ij,U,\phi}(p)$、逆行列 $g^{ij}_{U,\phi}(p)$ とする。
このとき、
$$\mathrm{grad}_pf=\sum_{i,j=1}^ng^{ij}_{U,\phi}(p)\frac{\partial f}{\partial x^j}\frac{\partial}{\partial x^i}p\\\ \\$$

      ・逆行列で表されてることに注意。
      ・基底は∂/∂x^i

</dd></dl>

---

## $R^N$ 上のdiv

<dl><dt>

・開集合 $U\sub\bm{R}^N$、$C^1$ 関数 $u:U\to\bm{R}^N$ とする。
このとき、$$j(u)_p=\sum_{i=1}^Nu^i(p)dx^i_p\in\Lambda^1(T_p(U))$$
は $C^1\ 1$ 形式。 
<br>

</dt><dd>

- $d\circ\star(j(u))$ は $U$ 上の連続 $N$ 形式であって、$\star\circ d\circ\star(j(u))$ は $U$ 上の連続関数。
ここで、
$$\mathrm{div}\ u=\star\circ d\circ\star(j(u))$$
と書いて、発散という。
<br>

      ・αdx^I→α
<br>

- $\bm{R}^N$ の正の向きの局所座標 $(V,\phi;y^1,...,y^N)$ とする。
このとき、
$$\forall p\in V\text{ に対して、}\\\ \\
(\mathrm{div}\ u)(p)=\frac{1}{h_1(p)...h_N(p)}\sum_{k=1}^N\left.\frac{\partial }{\partial y_k}(h_1...h_Nu_k)\right|_p$$

</dd></dl>

---

## $R^N$ 上のrot

<dl><dt>

・開集合 $U\sub\bm{R}^3$、$C^1$ 関数 $u:U\to\bm{R}^3$ とする。
このとき、$$j(u)_p=\sum_{i=1}^Nu^i(p)dx^i_p\in\Lambda^1(T_p(U))$$
は $C^1\ 1$ 形式。 
<br>

</dt><dd>

- $\star\circ d(j(u))$ は $U$ 上の連続 $1$ 形式。
ここで、
$$j(\mathrm{rot}\ u)=\star\circ d(j(u))$$
と書いて、このときただ一つ定まる連続関数 $\mathrm{rot}\ u:U\to\bm{R}^3$ を回転という。
<br>

- $\bm{R}^3$ の正の向きの局所座標 $(V,\phi;y^1,...,y^3)$ とする。
このとき、
$$\forall p\in V\text{ に対して、}\\\ \\
(\mathrm{rot}\ u)(p)=\frac{1}{h_1(p)h_2(p)h_3(p)}\sum_{i,j,k=1}^3\epsilon_{ijk}\frac{\partial(h^2_ku_k)}{\partial y^j}(p)\frac{\partial}{\partial y^i}p$$

</dd></dl>

---

## $R^N$ 上の$Δ$

<dl><dt>

・開集合 $U\sub\bm{R}^N$、$C^2$ 関数 $u:U\to\bm{R}$ とする。
このとき、$$(\star\circ d)u$$
は $C^1\ N-1$ 形式。 
<br>

</dt><dd>

- $(\star\circ d\circ\star\circ d)u$ は $U$ 上の連続関数。
ここで、
$$\Delta u=(\star\circ d\circ\star\circ d)u$$
と書く。
<br>

- $\bm{R}^N$ の正の向きの局所座標 $(V,\phi;y^1,...,y^N)$ とする。
このとき、
$$\forall p\in V\text{ に対して、}\\\ \\
(\Delta u)(p)=\frac{1}{h_1(p)...h_N(p)}\sum_{k=1}^N\left.\frac{\partial }{\partial y_k}\left(\frac{h_1...h_N}{h_k^2}\frac{\partial u}{\partial y_k}\right)\right|_p$$

</dd></dl>

---

# 星形集合

<dl><dt>

・部分集合 $S\sub \bm{R}^N$、$a\in S$ とする。
このとき、$a$ を中心とする星形集合 $S$：
$$\forall x\in S\text{ に対して、}\\\ \\
\{a+t(x-a)\ |\ 0\le t\le1\}\sub S\\\ \\$$

</dt><dd>

- 凸集合 $C\sub\bm{R}^n$、$a\in C$ とする。
このとき、$C$ は $a$ を中心とする星形集合。
<br>

- $a\in S$ を中心とする星形集合 $S\sub\bm{R}^N$ とする。
このとき、$S-a$ は $0\in S$ を中心とする星形集合。


</dd></dl>

---

## Poincareの補題

・適当な $a$ に関する星形開集合 $U\sub\bm{R}^N$、$d\omega=0$ を満たす $C^1\ r$ 形式 $\omega:U\to \Lambda^r(T^*U)$ とする。
このとき、
$$\exist C^1\ r-1\text{ 形式 }\theta:U\to\Lambda^{r-1}(T^*U)\text{ であって、}\\\ \\
d\theta=\omega\\\ \\$$

- 適当な $a$ に関する星形開集合 $U\sub\bm{R}^N$、$C^1$ 関数 $u:U\to\bm{R}^3$ とする。
このとき、
$$\mathrm{div}\ u=0\Rightarrow\exist C^1\text{ 写像 }v:U\to\bm{R}^3\text{ であって、}u=\mathrm{rot}\ v\\\ \\
\mathrm{rot}\ u=0\Rightarrow\exist C^1\text{ 写像 }f:U\to\bm{R}\text{ であって、}u=\mathrm{grad}\ f\\\ \\$$



