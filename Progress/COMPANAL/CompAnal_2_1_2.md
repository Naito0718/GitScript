
- [単一連結](#単一連結)
  - [単一連結とコーシーの定理](#単一連結とコーシーの定理)
- [囲むサイクル](#囲むサイクル)
- [ウリゾーン的なサイクル](#ウリゾーン的なサイクル)



# 単一連結

・領域 $D\sub\bm{C}$ とする。
このとき、$D$ が単一連結：
$$\forall D\text{ 内の区分的 }C^1\text{ 曲線 }C\sub D\text{ がホモローグ }0$$
ここで、星形領域 $D\sub\bm{C}$ は単一連結。


## 単一連結とコーシーの定理

<dl><dt>

・単一連結領域 $D\sub\bm{C}$、正則関数 $f:D\to\bm{C}$、$D$ 内の区分的 $C^1$ 曲線 $C\sub D$ とする。
このとき、$$\int_C fdz=0\\\ \\$$

</dt><dd>

- 領域 $D\sub\bm{C}$、正則関数 $f:D\to\bm{C}$、ホモローグ $0$ な $D$ 内の区分的 $C^1$ サイクル $C\sub D$ とする。
このとき、
$$\forall a\in D-\bm{C}\text{ に対して、}n(C,a)f(a)=\frac{1}{2\pi i}\int_C \frac{f(z)}{z-a}dz\\\ \\$$

</dd></dl>

---

# 囲むサイクル

<dl><dt>

・領域 $D\sub\bm{C}$、$\bm{C}$ 内の区分的 $C^1$ サイクル $C\sub D$ とする。
このとき、$D$ を囲む $C$：
$$\forall a\in\bm{C}-C\text{ に対して、}n(C,a)=\begin{dcases}
1 & a\in D\cap C^c  \\
0 & a\in D^c\cap C^c   \\
\end{dcases}$$
ここで、$C$ が $D$ を囲むならば、$D^b\sub C$ である。
<br>

</dt><dd>

- 領域 $D\sub\bm{C}$ を囲む $\bm{C}$ 内の区分的 $C^1$ サイクル $C$、正則関数 $f:D\cup C\to\bm{C}$ とする。
このとき、
$$\int_Cfdz=0\\\ \\
\forall w\in D\text{ に対して、}f(w)=\frac{1}{2\pi i}\int_C\frac{f(\xi)}{\xi-w}d\xi\\\ \\$$

      ・fの正則性は、あるC∪Dを含む領域が存在して、その上で正則ということ。

</dd></dl>

---

# ウリゾーン的なサイクル

<dl><dt>

・$$A=\{l_1,...,l_n\ |\ l_i\text{ は }\bm{C}\text{ 内の長さが正の線分であって、}\\\ \\
\forall z\in\bm{C}\text{ に対して、}z\text{ を始点とする }l_i\text{ の数}=z\text{ を終点とする }l_k\text{ の数}\}$$
このとき、$\bigcup A$ は $\bm{C}$ 内の区分的 $C^1$ サイクル。
<br>

</dt><dd>

- $K\sub U\sub\bm{C}$ を満たすコンパクト集合 $K$、開集合 $U$ とする。
このとき、
$$\exist U\text{ 内の区分的 }C^1\text{ サイクル }C\sub U\text{ であって、}\\\ \\
C\sub U-K,\quad\\\ \\
\forall z\in\bm{C}-C\text{ に対して、}n(C,z)=\{0,1\}\text{ であって、}n(C,z)=0\quad (\forall z\in K),\ n(C,z)=1\quad (\forall z\in U^c)$$
ここで、上記を満たす $C$ について、$K\prec C\prec U$ と書く。

</dd></dl>
