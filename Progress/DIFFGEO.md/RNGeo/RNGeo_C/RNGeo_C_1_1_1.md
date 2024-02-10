
- [局所座標の線形変換](#局所座標の線形変換)
- [多様体と正則曲線,超曲面](#多様体と正則曲線超曲面)
  - [超曲面と計量](#超曲面と計量)



# 局所座標の線形変換

    ・テンソル解析につながる。
<br>

---

# 多様体と正則曲線,超曲面

・開集合 $U\sub\bm{R}^n\sub\bm{R}^N$、$C^{\infty}$ 写像 $\phi:U\to\bm{R}^{N}$ とする。
このとき、
$$(\phi(U),\phi^{-1})\text{ がある }n\text{ 次元多様体の局所座標}\iff\phi\text{ は }U\text{ 上単射かつ同相であって、}\forall u\in U\text{ に対して、}\mathrm{rank}\ \phi'(u)=n\\\ \\$$

ここで、$\phi$ が単射になるような開集合 $U$ があったとする。このとき、任意の $x\in U$ に対して、ある $x$ を含む閉球 $\overline{B}\sub U$ が存在して、$\phi$ は $\overline{B}$ 上同相。
よって、$\phi$ は開球 $B$ 上同相。これは、$\phi(U)$ のアトラスとして $\{(\phi(B_{x}),\phi)\}$ が取れることを意味する。
したがって、$\phi$ が正則曲線かどうかなどを確かめるときは、$C^{\infty}$ 性、単射性、$\mathrm{rank}\phi'=n$ を示せばよい。

---

## 超曲面と計量

・開集合 $U\sub\bm{R}^n\sub\bm{R}^N$、正則写像 $\phi:U\to\bm{R}^N$ とする。
このとき、
$$\forall u\in U\text{ に対して、}(g_{(\phi(U),\phi^{-1})})_{ij}(\phi(u))=\left(\frac{\partial\phi}{\partial r^i}(u),\ \frac{\partial\phi}{\partial r^j}(u)\right)$$
これは、第一基本形式の定義と整合する。