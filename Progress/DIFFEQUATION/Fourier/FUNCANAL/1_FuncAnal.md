- [関数環](#関数環)
  - [連続関数環 $C(X)$](#連続関数環-cx)
  - [局所コンパクトHausdorff空間上の連続関数環](#局所コンパクトhausdorff空間上の連続関数環)
  - [コンパクトHausdorff空間上の連続関数環](#コンパクトhausdorff空間上の連続関数環)
    - [$A$-反対称集合](#a-反対称集合)


# 関数環 

・空でない集合 $X$ とする。
このとき、
$$FA(X)=\left\{f:X\to\bm{C}\ |\ \sup_{x\in X}|f(x)|<\infty\right\}\\\ \\
\|\cdot\|:FA(X)\to[0,\infty)\\\ \\
\|f\|=\sup_{x\in X} |f(x)|$$
と定めると、$FA(X)$ は $\bm{C}$ 上ベクトル空間であって、$\|\cdot\|$ は $FA(X)$ 上のノルム。
特に、$FA(X)$ は $\bm{C}$-ノルム*単位的可換環。

---

## 連続関数環 $C(X)$

<dl><dt>

・位相空間 $X$ とする。
このとき、
$$C(X)=\{f:X\to\bm{C}\ |\ f\text{ は連続関数}\}\\\ \\
C_b(X)=\{f\in C(X)\ |\ f{は有界}\}\\\ \\
C_0(X)=\{f\in C(X)\ |\ \forall\epsilon>0{に対して}(|f|>\epsilon){はコンパクト}\}\\\ \\
C_c(X)=\{f\in C(X)\ |\ suppf{はコンパクト}\}$$
と定める。
<br>

</dt><dd>

- $C(X)$ は $\bm{C}$-可換単位的$*$-環。
<br>

      ・ノルムは入ってない。
<br>

- $C_b(X)$ は $C^*$-環で、$C(X)$の部分$*$-環。特に、$C_b(X)$ はBanach空間。

<br>

- $\forall\epsilon>0$ に対して $(|f|\ge\epsilon)$ は閉集合であって、$C_0(X)$ は $C_b(X)$ の閉$*$-イデアル。特に、$C_b(X)$ の閉部分空間。
<br>

      ・補集合を考えるとよい！
      ・結局Banach空間。
<br>

- $C_c(X)$ は $C(X)$ の $*$-イデアルで、
$$C_c(X)\subset C_0(X)\\\ \\
\forall f\in C_{c}(X)\text{ に対して、}|f|\in C_c(X)\\\ \\
\forall f,g\in C_{c,\bm{R}}(X)\text{ に対して、}\max\{f,g\}\in C_{c,\bm{R}}(X)$$

</dd></dl>

---

## 局所コンパクトHausdorff空間上の連続関数環

<dl><dt>

・位相空間 $X$、$X\sub\tilde{X}$、$f:X\to\bm{C}$ とする。
このとき、$0$ 拡張：$\tilde{f}$:
$$\tilde{f}:\tilde{X}\to\bm{C}\\\ \\
\tilde{f}(x)=f(x)\ \ (x\in X),\quad\tilde{f}(x)=0\ \ (x\in\tilde{X}-X)\\\ \\$$

</dt><dd>

- 局所コンパクトHausdorff空間 $X$ とする。
このとき、
$$\overline{C_c(X)}=C_0(X)$$
<br>

- 局所コンパクトHausdorff空間 $X$、$f:X\to\bm{C}$、一点コンパクト化 $\tilde{X}$、$0$ 拡張 $\tilde{f}$ とする。
このとき、
$$f\in C_0(X)\iff \tilde{f}\in C(\tilde{X})$$

</dd></dl>

---

## コンパクトHausdorff空間上の連続関数環

### $A$-反対称集合

<dl><dt>

・コンパクトHausdorff空間 $X$、$K\sub X$、連続関数環 $C(X)$、$\mathcal{A}\sub C(X)$ とする。
このとき、$\mathcal{A}$-反対称集合 $K$：
$$\forall f\in C(X),\ f(x)\in\bm{R}\ \ (\forall x\in K)\text{ に対して、}\exist a\in\bm{R}\text{ であって、}\\\ \\
f(x)=a\ \ (\forall x\in K)\\\ \\$$

</dt><dd>

- $x\in X$ とする。
このとき、$\{x\}$ は $\mathcal{A}$-反対称集合であって、
$$K=\bigcup\{A\sub X\ |\ x\in A,\ A\text{ は }\mathcal{A}\text{-反対称集合}\}$$
と定めると、$K$ は集合の包含関係において極大な $\mathcal{A}$-反対称集合。
<br>

      ・Kよりでかい反対称集合Lがあれば、K=L
<br>

- $\mathcal{A}$-反対称集合 $K_0\sub X$ とする。
このとき、
$$K=\bigcup\{A\sub X\ |\ K_0\sub A,\ A\text{ は }\mathcal{A}\text{-反対称集合}\}$$
と定めると、これは $K$ を含む極大な反対称性集合。

</dd></dl>




