
- [Heizenberg群](#heizenberg群)
  - [シンプレクティック形式](#シンプレクティック形式)
  - [Heisenberg群](#heisenberg群)
- [Weyl型CCRの表現](#weyl型ccrの表現)




# Heizenberg群

## シンプレクティック形式

・$v=(x,y),v'=(x',y')\in\bm{R}^N\times\bm{R}^N=\bm{R}^{2N}$ とする。
このとき、
$$\omega:\bm{R}^{2N}\times\bm{R}^{2N}\to\bm{R}\\\ \\
\omega(v,v')=x\cdot y'-x'\cdot y$$
と定めると、これは双線形写像。ここで、$\omega$ を $\bm{R}^{2N}$ 上のシンプレクティック形式という。

- $J=\begin{pmatrix}
0_N & I_N    \\
-I_N & 0_N\\
\end{pmatrix}$ とする。
このとき、
$$J^{-1}=-J,\quad J^2=-I_{2N}\\\ \\
\omega(v,v')=(v,Jv')$$
特に、$v\in\bm{R}^{2N}$ に対して、
$$\forall v'\in\bm{R}^{2N}\text{ に対して、}\omega(v,v')=0\iff v=0$$

      ・最後のは正則性。

## Heisenberg群

<dl><dt>

・$(x,y,\lambda),(x',y',\lambda')\in\bm{R}^N\times\bm{R}^N\times\bm{R}$、シンプレクティック形式 $\omega:\bm{R}^{2N}\times\bm{R}^{2N}\to\bm{R}$ とする。
このとき、
$$(x,y,\lambda)(x',y',\lambda)=\left(x+x',y+y',\lambda+\lambda'+\frac{1}{2}\omega((x,y),(x',y'))\right)$$
と定める。
この演算を与えたもの $H_N$ を $N$ 次Heisenberg群という。

</dt><dd>

- $\bm{R}^{2N+1}$ は、上記の演算で群をなす。
特に、単位元：$(0,0,0)$、逆元 $(-x,-y,-\lambda)$ 。
<br>

- $\bm{R}^{2N+1}$ は、上記の演算で明らかに局所コンパクト群をなす。

</dd></dl>

---

# Weyl型CCRの表現

・







