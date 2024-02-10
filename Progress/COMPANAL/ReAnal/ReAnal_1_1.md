
- [非負値級数](#非負値級数)
  - [広義一様収束](#広義一様収束)
- [$n$ 重級数](#n-重級数)
  - [正項](#正項)
  - [絶対収束](#絶対収束)
- [実関数空間](#実関数空間)
  - [各点収束列](#各点収束列)
    - [一様収束列](#一様収束列)
  - [収束族](#収束族)
- [実数上の関数族](#実数上の関数族)
- [無限級数](#無限級数)
  - [複素級数と同様に成り立つこと](#複素級数と同様に成り立つこと)


# 非負値級数

・非負点列 $(a_n)\sub(0,\infty)$ とする。
このとき、
$$\lim_{n\to\infty}\frac{a_{n+1}}{a_n}\in[0,1)\text{ が存在する}\Rightarrow\sum a_n\text{ は収束する}$$

---

## 広義一様収束

・$a\in\bm{R}$、収束ベキ級数 $\sum_{n\in\bm{N}}a_n(x-a)^n$、収束半径 $\rho>0$ とする。
このとき、
$$\sum_{n\in\bm{N}}a_n(x-a)^n\text{ は }\{x\in\bm{R}\ |\ |x-a|<\rho\}\text{ 内で広義一様収束する}$$

---

# $n$ 重級数

    ・添え字集合が任意の集合でも、収束するなら結局たかだか可算になって、一列化できる。

・対応 $a_I\sub\bm{R}$、$\bm{N}^n$ の有限部分集合に包含順序を入れた有向集合 $\mathcal{F}_{N}$ とする。
このとき、$n$ 重級数 $\sum_{I\in \bm{N}^n}a_I$：
$$\text{ネット列 }\left(\sum_{I\in F}x_j\right)_{F\in\mathcal{F}_N}\text{ が収束すること}\\\ \\
\sum_{I\in \bm{N}^n}a_I=\lim_{F\to \bm{N}^n}\sum_{I\in F}a_I$$

    ・a_Iを点列とは呼び難い。

## 正項

・正項 $n$ 重級数 $\sum_{I\in \bm{N}^n}a_I$、$a_I\ge0$ とする。
このとき、
$$\sum_{I\in \bm{N}^n}a_I\text{ が }X{ に収束する}\\\ \\
\iff \begin{cases}
F_i\sub F_{i+1}      \\
\forall F\in\mathcal{F}_N\text{ に対して、}\exist n\in\bm{N}\text{ であって、}F\sub F_n      \\
\end{cases}\\\ \\
\text{なる }(F_n)\sub\mathcal{F}_N{ に対して、}\lim_{n\to\infty} \sum_{I\in F_n}a_I=X\\\ \\
\iff\text{部分和 }s_F=\sum_{I\in F}a_I\text{ に対して、}\sup_{D\in\mathcal{F}_N} s=s_F\text{ が有限}$$

      ・一般の級数では⇒しか成り立たない。
      ・最後のは、結果としてs=Xとなる。

## 絶対収束

・実 $n$ 重級数 $\sum_{I\in \bm{N}^n}a_I$ とする。
このとき、絶対収束：
$$\sum_{I\in \bm{N}^n}|a_I|\in\bm{R}$$

- 実 $n$ 重級数 $\sum_{I\in \bm{N}^n}a_I$ とする。
このとき、
$$\sum_{I\in \bm{N}^n}a_I\text{ が絶対収束}\\\ \\
\iff a_I^+=\max\{a_I,0\},\ a_I^-=\max\{-a_I,0\}\text{ に対して、}\\\ \\
\sum_{I\in \bm{N}^n}a_I^+,\ \sum_{I\in \bm{N}^n}a_I^-\text{ が共に収束}\\\ \\
\iff s=\sum_{I\in \bm{N}^n}a_I^++\sum_{I\in \bm{N}^n}a_I^-\text{ が収束}\\\ \\
\iff \left\{\sum_{I\in F}|a_I|\ |\ F\in\mathcal{F}_N\right\}\text{ が上に有界}$$

      ・絶対収束すれば、元の級数もネット列の意味で収束する。
<br>

- 実 $n$ 重級数 $\sum_{I\in \bm{N}^n}a_I$ とする。
このとき、ある $\sum$ を取る順番で級数が絶対収束すれば、すべての順番で同じ値に絶対収束し、元の級数もすべての順番で同じ値に収束する。

      ・二重級数なら3通り。

- 実 $n$ 重級数 $\sum_{I\in \bm{N}^n}a_I$、全単射 $\phi:\bm{N}\to\bm{N}^n$ とする。
このとき、
$$\sum_{I\in \bm{N}^n}a_I\text{ が絶対収束}\\\ \\
\sum_{I\in \bm{N}^n}a_I\text{ の任意の一列化 }\sum_n b_n=\sum_n a_{\phi(n)}\text{ が絶対収束}$$

      ・⇐はある一つの一列化が絶対収束していればよい。



---
---
---

# 実関数空間

## 各点収束列

・集合 $A$、関数列 $f_n:A\to\bm{R}^m$ とする。
このとき、各点収束：
$$\exist f:A\to\bm{R}^m\text{ であって、}\forall a\in A,\forall\epsilon>0\text{ に対して、}\exist n_0\text{ であって、}\\\ \\
n\ge n_0\Rightarrow|f_n(a)-f(a)|<\epsilon\\\ \\$$ 

---

### 一様収束列

<dl><dt>

・集合 $A$ とする。
このとき、
$$B(A,\bm{R}^m)=\\
\{f:A\to\bm{R}^m\ |\ \exist M>0\text{であって、}|f(a)|<M\ \ (\forall a\in A)\}\\\ \\
\|f\|=\sup_{a\in A}|f(a)|$$
とする。このとき、$B(A,\bm{R}^m)$ は $\bm{R}$ ベクトル空間で、$\|f\|$ はノルム。

    ・Bは有界関数全体の集合。
<br>

- 集合 $A$、関数列 $f_n:A\to\bm{R}^m$ とする。
このとき、一様収束：
$$\exist f:A\to\bm{R}^m\text{ であって、}\forall\epsilon>0\text{ に対して、}\\
\exist n_0\text{ であって、}\forall a\in A\text{ に対して、}\\\ \\
n\ge n_0\Rightarrow|f_n(a)-f(a)|<\epsilon\\\ \\$$ 

</dt><dd>

- 集合 $A$、関数列と関数 $f_n,f:A\to\bm{R}^m$ とする。
このとき、
$$f_n\text{ は }f{ に一様収束する}\iff\lim_{n\to\infty}\|f-f_n\|=0\\\ \\$$

- $$\exist n_0\text{ であって、}n\ge n_0\Rightarrow f_n\in B(A,\bm{R}^m)\\\ \\
\iff f\in B(A,\bm{R}^m)$$

      ・常に一様収束極限がB(A,R^m)に入ってるわけではない。

</dd></dl>

---

## 収束族

<dl><dt>

・集合 $A$、$T\sub \bm{R}^m$、$f:A\times T\to\bm{R}^l$、$g:A\to\bm{R}^l$ とする。
また、$f_t:A\to\bm{R}^l,\ \ f_t(a)=f(a,t)$、$b\in\overline{T}$ とする。
このとき、$f_t$ が $t\to b$ で $g$ に一様収束：
$$\lim_{t\to b}\|g-f_t\|=0\\\ \\$$

    ・∞は普通関数列の方で考える。

</dt><dd>

- 関数族 $f_t:A\to\bm{R}^l$ が $t\to b$ で $g$ に $A$ 上一様収束するとする。
このとき、$f_t$ は $t\to b$ で $A$ 上 $A$ に各点収束する。

      ・各点a∊AでTのb近傍が存在すること。
      ・関数列でも同様。
<br>

</dd></dl>


---
---
---

# 実数上の関数族

・$A\sub\bm{R}^n$、連続関数族 $f_t:A\to\bm{R}^l$ が $t\to b$ で $g$ に $A$ 上一様収束するとする。
このとき、$g$ は $A$ 上連続。

    ・関数列でも同様。
    ・極限同士の交換。
    ・$A$ に位相が無いと成立しない。

---




# 無限級数

    ？？？

## 複素級数と同様に成り立つこと

    ・すべて複素変数と同様に証明できる。

・$K$ 係数形式的ベキ級数 $F(x)=\sum a_ip^i$ 、収束半径 $\rho$ とする。

- $$\frac{1}{\rho}=\overline{\lim_{n\to\infty}}|a_n|^{1/n}\\\ \\
\frac{1}{\rho}=\lim_{n\to\infty}|\frac{a_n}{a_{n+1}}|$$

      ・級数の収束

- $F'(x)=\sum_{n\ge1}na_nx^{n-1}$ において、収束半径は $F(x)$ と一致する。

      ・項別微分

- $F:\{z\in\bm{C,R}\ |\ |z|<\rho\}\to\bm{C,R},\quad F(z)=\sum a_nz^n$ とする。
このとき、$F$ は微分可能で、
$$\frac{d}{dz}F(z)=F'(z)=\sum_{n\ge1}na_nz^{n-1}$$

      ・実数上でも0を含む開区間で一致すればF(x)=G(x)