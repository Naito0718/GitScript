

- [連結性](#連結性)
  - [連結成分](#連結成分)
  - [連結性と連続写像](#連結性と連続写像)


# 連結性

<dl><dt>

・位相空間 $X$ とする。
このとき、$X$ が連結：
$$\forall\text{ 開集合 }O_1,O_2\sub X,\ X=O_1\cup O_2,\ O_1\cap O_2=\phi\text{ に対して、}\\\ \\
O_1=\phi\text{ または }O_2=\phi\\\ \\$$

    ・部分空間のときは、 「A⊂O_1∪O_2,A∩O_1∩O_2=φ、A∩O_1,A∩O_2が共に空でない」 でもよい
    ・空集合は連結でないとする。
<br>

</dt><dd>

- $x\in X$ とする。
このとき、一点集合 $\{x\}$ は連結。
<br>

- 連結な集合族 $A_{\lambda}\subset X$ であって、$A_{\lambda}\cap A_{\lambda'}\neq\phi$ とする。
このとき、$\bigcup A_{\lambda}$ は連結。
<br>

- 連結部分空間 $A\subset X$、部分空間 $A\sub B\sub\overline{A}$ とする。
このとき、$B\subset X$ は連結。

</dd></dl>

---

## 連結成分

<dl><dt>

・位相空間 $X$、$x,y\in X$ とする。
このとき、$$x\sim y\iff \exist\ {連結部分空間 }A\sub X{ であって、} x,y\in A$$
と定めると、これは同値関係。ここで、同値類 $C(x)$ を $x$ の連結成分という。
<br>

</dt><dd>

- $x\in X$、連結成分 $C(x)$ とする。
このとき、$C(x)$ は閉集合であって、
$$C(x)=\bigcup\{A\sub X\ |\ x\in A\text{ であって、}A\text{ は連結部分空間}\}\\\ \\$$

</dd></dl>

---

## 連結性と連続写像

・連結な位相空間 $X$、位相空間 $Y$、連続写像 $f:X\to Y$ とする。
このとき、$f(X)\sub Y$ は連結空間。




