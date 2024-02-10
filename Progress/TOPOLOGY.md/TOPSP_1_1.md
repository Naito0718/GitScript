- [集合演算](#集合演算)
  - [閉包](#閉包)
- [基本近傍系](#基本近傍系)
  - [連続性と基本近傍系](#連続性と基本近傍系)
  - [開基](#開基)
  - [準開基](#準開基)
- [可算公理](#可算公理)
  - [第二可算](#第二可算)
  - [第一可算](#第一可算)
  - [可分](#可分)
    - [他の可算公理との関係](#他の可算公理との関係)
  - [Lindelof空間](#lindelof空間)
  - [分離公理](#分離公理)
    - [$T1$](#t1)
    - [Hausdorff空間](#hausdorff空間)
    - [正則空間](#正則空間)
    - [正規空間](#正規空間)
  - [連続性](#連続性)
  - [開写像](#開写像)

# 集合演算

## 閉包

・位相空間 $X$、部分集合 $A,B\sub X$ とする。
このとき、
$$\overline{A\cup B}=\overline{A}\cup\overline{B},\quad\overline{A\cap B}\subset \overline{A}\cap\overline{B}$$

- 位相空間 $X$、部分集合族 $A_{\lambda}\sub X$ とする。
このとき、$$\bigcup_{\lambda}\overline{A}_{\lambda}\subset\overline{\bigcup_{\lambda} A_{\lambda}}\\\ \\$$

        ・左辺は閉集合とは限らない

 ---

・$(A\cap B)^i=A^i\cap B^i,\quad A^i\cup B^i\subset(A\cup B)^i$

- 開集合 $U\sub X$、$A\sub X$ とする。
このとき、$$U\cap A=\phi\Rightarrow U\cap\overline{A}=\phi$$


---

# 基本近傍系

・基本近傍系 $\mathcal{N}_F(x)$ が与えられているとする。
 このとき、
 $O\in\mathcal{O}\iff \forall x\in O{に対して、}\exist U_x\in\mathcal{N}_F(x){であって、}U_x\subset O$

 - 位相空間 $X$ に対して、
$$\mathcal{N}_F(x)\text{が基本近傍系}\\\ \\
\iff\begin{cases}
U\in\mathcal{N}_F(x)\Rightarrow x\in U    \\
U,V\in\mathcal{N}_F(x)\Rightarrow\exist W\in\mathcal{N}_F(x);\ W\subset U\cap V \\
U\in\mathcal{N}_F(x),y\in U\Rightarrow\exist V\in\mathcal{N}_F(y);V\subset U\\
\end{cases}$$

       ・基本近傍系の要素は開集合。

---

## 連続性と基本近傍系

<dl><dt>

・位相空間 $X,Y$、基本近傍系 $\mathcal{U}_X(x),\ \mathcal{U}_Y(y)$ とする。

</dt><dd>

- $$\forall x\in X,\ \forall U\in\mathcal{U}_Y(f(x))\text{ に対して、}\exist V\in\mathcal{U}_X(x)\text{ であって、}\\
f(V)\sub U\\\ \\
\iff f\text{ は連続}\\\ \\$$

- $$\forall x\in X,\ \forall V\in\mathcal{U}_X(x)\text{ に対して、}\exist U\in\mathcal{U}_Y(f(x))\text{ であって、}\\
U\sub f(V)\\\ \\
\iff f\text{ は開写像}$$


</dd></dl> 


---

## 開基

 ・第二可算空間はLindelof空間。

    ・任意の開被覆に対して可算個の部分被覆を取れる。

 - 第二可算空間は可分。

 ---

## 準開基

 ・位相 $\mathcal{O}$ に対して、
 準開基 $\mathcal{J}$ ：
 $$\forall O\in\mathcal{O},\ \forall x\in O\ {に対して、}\\\ \\
 \exist J_1,...,J_n\in\mathcal{J}\ {であって、}x\in J_1\cap...J_n\ {かつ}\ J_1\cap...\cap J_n\subset O$$

 - 準開基 $\mathcal{J}$ に対して、
 $$\mathcal{B}=\{J_1\cap...\cap J_n\ |\ n\in\bm{N},\ J_i\in\mathcal{J}\}$$は開基。

       ・有限個の共通部分。

 ---


# 可算公理

## 第二可算

・位相空間 $X$ とする。
このとき、第二可算空間 $X$：$$X\text{は高々可算な開基を持つ}$$

- 第二可算$\Rightarrow$可分かつLindelof空間

---

## 第一可算

・位相空間 $X$ とする。
このとき、第一可算空間：$X$：
$$X\text{ は各点で高々可算な基本近傍系を持つ}$$

---

## 可分

・位相空間 $X$ とする。
このとき、$X$ が可分：
$$\exist \text{ 高々可算な部分集合 }A\sub X\text{ であって }X=\overline{A}$$

・可分な位相空間 $X$、位相空間 $Y$、連続写像 $f:X\to Y$ とする。
このとき、$f(X)$ は可分。

- 位相空間 $X$、Hausdorff空間 $Y$、$\overline{M}=X$ なる部分集合 $M$、$f(x)=g(x)\ (\forall x\in M)$ なる連続関数 $f,g:X\to Y$ とする。
 このとき、$$f=g$$

---

### 他の可算公理との関係

・位相空間 $X$ とする。
このとき、
$$X\text{ は可分かつ第一可算}\Rightarrow X\text{ は第二可算}$$

---

---

## Lindelof空間

・位相空間 $X$ とする。
このとき、Lindelof空間 $X$：
$$\forall\text{ 開被覆 }X=\bigcup \mathcal{U}\text{ に対して、}\exist\text{ 高々可算な部分被覆 }\mathcal{U}_0\sub\mathcal{U},\ X=\bigcup\mathcal{U}_0$$

---

## 分離公理

### $T1$

・位相空間 $X$ に対して、
$T_1$：$$\forall x\in X\text{ に対して、}\{x\}\text{ は閉集合}$$

- 位相空間 $X$ に対して、
$$X\text{ は }T_1\iff \forall x\in X\text{ に対して、}\bigcap\{N\ |\ N\text{ は }x\text{ の近傍 }\}=\{x\}\\\ \\
\iff\forall x,y\in X,\ x\neq y\text{ に対して、}\exist U\in\mathcal{N}(x)\text{ であって、}y\notin U$$

---

### Hausdorff空間

<dl><dt>

・Hausdorff空間 $X$、コンパクト集合 $A\sub X$ とする。

</dt><dd>

- $A$ は $X$ の閉集合。
<br>

- $x\in A^c$ とする。
このとき、
$$\exist\text{ 開集合 }U,V\sub X\text{ であって、}x\in U,\ A\sub V,\ U\cap V=\phi\\\ \\$$

- コンパクト集合 $A,B\sub X$、$A\cap B=\phi$ とする。
このとき、$$\exist\text{ 開集合 }U,V\sub X\text{ であって、}A\sub U,\ B\sub V,\ U\cap V=\phi$$


</dd></dl>

---

### 正則空間

・正則空間 $X$ ：$$\begin{cases}
 T_1    \\
 {閉集合}\ F,\ x\in F^c\  {に対して、}\ x\in U,\ F\subset V,\ U\cap V=\phi\  {なる開集合}\  U,V {が存在する。}      \\
 \end{cases}$$ 

- 位相空間 $X$ に対して、
$X$ が正則空間$\iff x\in X, U\in\mathcal{N}(x)$ に対して、$x\in V\subset\overline{V}\subset U$ なる開近傍 $V$ が存在する。
<br>

- 正則空間$\Rightarrow$Hausdorff空間

---

---

### 正規空間

---



## 連続性


 ---
## 開写像



 ---

