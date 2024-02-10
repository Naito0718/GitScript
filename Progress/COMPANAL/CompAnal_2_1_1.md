
- [複素線積分](#複素線積分)
  - [複素線積分の性質](#複素線積分の性質)
    - [項別線積分](#項別線積分)
  - [原始関数](#原始関数)
  - [部分積分](#部分積分)
- [正則関数と線積分](#正則関数と線積分)
  - [コーシーの定理](#コーシーの定理)
    - [コーシーの積分表示](#コーシーの積分表示)
    - [コーシーの定理 $2$](#コーシーの定理-2)
  - [整級数展開](#整級数展開)
  - [正則関数列](#正則関数列)
- [パラメータ付き積分](#パラメータ付き積分)
  - [複素微分と複素線積分](#複素微分と複素線積分)
    - [実軸上の積分と複素微分](#実軸上の積分と複素微分)




# 複素線積分

・区分的に $C^1$ な係数付き曲線 $C=[z],z:[a,b]\to\bm{C}$、連続関数 $f:S_pC\to\bm{C}$ とする。
このとき、
$$\int_Cf(z)dz=\int_a^bf(z(t))z'(t)dt$$
と定めると、これはwell-defined、すなわち $C$ の同値類によらず、値は複素数。ここで、$\int_Cf(z)dz$ を複素線積分という。

---

## 複素線積分の性質

<dl><dt>

・区分的 $C^1$ 曲線 $C$、$C$ 上で定義されている連続関数 $f_1,f_2:C\to \bm{C}$、$\alpha\in\bm{C}$ とする。
<br>

    ・一次元チェインでも同様。
<br>

</dt><dd>

- $$\int_Cf_1(z)dz=\lim_{d(\Delta)\to0}\sum_{k=1}^{\max K(\Delta)}f(z(\xi_k))(z(t_k)-z(t_{k-1}))$$
ここで、$\Delta$ は $z(t)$ の定義域 $I$ の分割で、$\xi_k$ は分割区間 $I_k=[t_{k-1},t_k]$ の代表点。
<br>


- $$\int_C(f_1(z)+f_2(z))dz=\int_Cf_1(z)dz+\int_Cf_2(z)dz,\quad\int_C(\alpha f_1(z))dz=\alpha\int_Cf_1(z)dz\\\ \\$$

- $$\int_{-C}f_1(z)dz=-\int_Cf_1(z)dz\\\ \\$$

- $C$ の弧長 $l(C)$ とする。
このとき、
$$\left|\int_Cf_1(z)dz\right|\le\sup_{z\in C}|f_1(z)|l(C)$$

</dd></dl>

---

### 項別線積分

・部分集合 $A_n\sub\bm{C}$、$S_pC$ 上連続な関数列 $f_n:\bm{C}\supset A_n\to\bm{C}$ とする。
このとき、$f_n$ が $S_pC$ 上一様収束するならば、
$$\lim_{n\to\infty}\int_Cf_n(z)dz=\int_C\lim_{n\to\infty} f_n(z)dz$$

---

## 原始関数

<dl><dt>

・領域 $D\sub\bm{C}$、原始関数 $F$ を持つ連続関数 $f:D\to\bm{C}$、区分的 $C^1$ 曲線 $C\sub D$、$C$ の始点と終点 $z_0,z_1$ とする。
このとき、$$\int_Cf(z)dz=F(z_1)-F(z_0)$$
特に、$C$ が閉曲線ならば、$\int_Cf(z)dz=0$ であって、線積分は $z_0$ と $z_1$ を結ぶ経路によらない。
<br>

</dt><dd>

- 領域 $D\sub\bm{C}$、連続関数 $f:D\to\bm{C}$ とする。
このとき、
$$\forall D\text{ 内の区分的 }C^1\text{ 閉曲線 } C\sub D\text{ に対して、}\int_Cf(z)dz=0\\\ \\
\iff f\text{ は }D\text{ 上原始関数を持つ}$$
ここで、上記の仮定が満たされるとき、$z_0\in D$ とすると、
$$F(z)=\int_{z_0}^zf(\xi)d\xi$$
で与えられる。ただし、$\int_{z_0}^z$ は $z_0$ と $z_1$ を結ぶ任意の区分的 $C^1$ 閉曲線。
<br>

      ・弧状連結だから、結ぶ経路（折れ線）は存在する。
<br>

- 上記の命題に整級数展開を適用する。
領域 $D\sub\bm{C}$、連続関数 $f:D\to\bm{C}$ とする。
このとき、
$$\forall D\text{ 内の区分的 }C^1\text{ 閉曲線 } C\sub D\text{ に対して、}\int_Cf(z)dz=0\\\ \\
\Rightarrow f\text{ は }D\text{ 上正則}\\\ \\$$

      ・逆は、ホモローグ0のサイクルでだけ、線積分が0

</dd></dl>

---

## 部分積分

・領域 $D\sub\bm{C}$、$D$ 内の区分的 $C^1$ 曲線 $C\sub D$、正則関数 $f,g:D\to\bm{C}$ とする。
このとき、
$$\int_Cf(z)g'(z)dz=[f(z)g(z)]^{z_1}_{z_0}-\int_Cf'(z)g(z)\\\ \\$$

    ・整級数展開の直後で導関数の連続性を消せるが、消さなくてもいいなら結構初期でも示せる。

---



# 正則関数と線積分

    ・連続で複素微分可能。（微分可能なら連続）

## コーシーの定理

<dl><dt>

・領域 $D\sub\bm{C}$、正則関数 $f:D\to\bm{C}$、内部及び周が $D$ に含まれる三角形 $T\sub D$ とする。
このとき、$$\int_{\partial T}f(z)dz=0\\\ \\$$

    ・区間縮小とか
<br>

- 領域 $D\sub\bm{C}$、正則関数 $f:D\to\bm{C}$、内部及び周が $D$ に含まれる四角形 $T\sub D$ とする。
このとき、$$\int_{\partial T}f(z)dz=0\\\ \\$$

</dt><dd>

- 領域 $D\sub\bm{C}$、$p\in D$、$p$ を除いて正則な連続関数 $f:D\to\bm{C}$、内部及び周が $D$ に含まれる三角形 $T\sub D$ とする。
このとき、
$$\int_{\partial T}f(z)dz=0\\\ \\$$

  ・頂点をpとして考える。
<br>

- $a\in D$ で星形な領域 $D\sub\bm{C}$、$p\in D$、$p$ を除いて正則な連続関数 $f:D\to\bm{C}$ とする。
このとき、$D$ 上で $f$ の原始関数が存在する。特に、$D$ 内の任意の区分的 $C^1$ 閉曲線 $C\sub D$ に対して、
$$\int_Cf(z)dz=0\\\ \\$$

      ・aとz、aとz+h、zとz+hを結ぶ線分で三角形作る。

</dd></dl>

---

### コーシーの積分表示

・領域 $D\sub \bm{C}$、閉円板 $\overline{B}\sub D$、正則関数 $f:D\to\bm{C}$ とする。
このとき、
$$\forall z\in B\text{ に対して、}\\\ \\
f(z)=\frac{1}{2\pi i}\int_{\partial B}\frac{f(\zeta)}{\zeta-z}d\zeta$$
特に、$a\in\bm{C}$ を中心とする半径 $R>0$ の円板 $B(a,R)$ 上で正則な関数 $f:D(a,R)\to\bm{C}$ に対して、
$$0<\forall r<R\text{ に対して、}f(a)=\frac{1}{2\pi}\int_0^{2\pi}f(a+re^{i\theta})d\theta$$
が成り立つ。

---

### コーシーの定理 $2$

・領域 $D\sub\bm{C}$、$D$ 上正則な$f:D\to\bm{C}$、$D$ 内のホモローグ $0$ のサイクル $C\sub D$ とする。
このとき、$$\int_Cfdz=0\\\ \\$$

---

## 整級数展開

<dl><dt>

・領域 $U\sub\bm{C}$、正則関数 $f:U\to\bm{C}$ とし、$a\in U$ 開円板 $B(a,R)\sub U$ とする。
このとき、
$$\forall z\in B(a,R)\text{ に対して、}\\\ \\
f(z)=\sum_{n\in\bm{N}} a_n(z-a)^n\\\ \\
0<\forall r<R\text{ に対して、}a_n=\frac{1}{2\pi i}\int_{\partial B(a,r)}\frac{f(\zeta)}{(\zeta-a)^{n+1}}d\zeta$$
特に、$f$ は $D$ 上任意回複素微分可能であって、$n$ 階導関数は $D$ 上正則。
<br>

さらに、
$$a_n=\frac{f^{(n)}(a)}{n!}\\\ \\
\forall z\in B(a,R),\ 0<\forall r<R\text{ に対して、}f^{(n)}(z)=\frac{n!}{2\pi i}\int_{\partial B(a,r)}\frac{f(\zeta)}{(\zeta-z)^{n+1}}d\zeta\\\ \\
0<\forall r<R\text{ に対して、}|a_n|\le\frac{1}{r^n}\Big(\sup\left\{|f(\zeta)|\ |\ |\zeta-a|=r\right\}\Big)\\\ \\$$

    ・「さらに、」の後のやつは証明で部分積分使うが、部分積分公式の導関数の連続性の排除は整級数展開だけで達成されてる。
<br>

</dt><dd>

- 
$$\forall|h|<R\text{ なる }h\in\bm{C}\text{ に対して、}\\\ \\
f(a+h)=\sum_{n\in\bm{N}}\frac{f^{(n)}(a)}{n!}h^n\\\ \\$$

- $f(z)=u(z,y)+iv(x,y)$ とする。
このとき、$u,v:U_{\bm{R}^2}\to\bm{R}$ は $C^{\infty}$ であって、
$$\Delta u=0,\quad\Delta v=0\\\ \\$$

</dd></dl>

---

## 正則関数列

・領域 $D\sub\bm{C}$、正則関数列 $f_n:D\to\bm{C}$、$f:D\to\bm{C}$ とする。
このとき、
$$f_n\text{ が }f\text{ に }D\text{ 上広義一様収束}\\\ \\
\Rightarrow f\text{ は }D\text{ 上正則であって、}f_n'(z)\text{ は }D\text{ 上 }f'(z)\text{ に広義一様収束}$$

---
---
---

# パラメータ付き積分

## 複素微分と複素線積分

・領域 $D\sub\bm{C}$、区分的 $C^1$ 曲線 $C\sub\bm{C}$、連続関数 $f:C\times D\to\bm{C}$ とする。
このとき、
$$(1):\forall \xi\in C\text{ に対して、}f_{\xi}:D\to\bm{C},\quad f_{\xi}(z)=f(\xi,z)\text{ は }D\text{ 上正則}\\\ \\
(2):\frac{\partial f}{\partial z}:C\times D\to\bm{C}\text{ は連続}\\\ \\
\Rightarrow F:D\to\bm{C},\quad F(z)=\int_Cf(\xi,z)d\xi\\\ \\
\text{ は }D\text{ 上正則であって、}\forall z\in D\text{ に対して、}\\\ \\
\frac{dF}{dz}(z)=\int_C\frac{\partial f}{\partial z}(\xi,z)d\xi$$
特に、$F$ はコーシーリーマン方程式 $\frac{\partial F}{\partial x}=\int_C\frac{\partial f}{\partial x}(\xi,z)d\xi,\frac{\partial F}{\partial y}=\int_C\frac{\partial f}{\partial y}(\xi,z)d\xi$ を満たす。

---

### 実軸上の積分と複素微分

・領域 $D\sub\bm{C}$、$[a,b)\sub\bm{R}$、連続関数 $f:[a,b)\times D\to\bm{C}$ とする。
このとき、
$$(1):\forall x\in [a,b)\text{ に対して、}f_{x}:D\to\bm{C},\quad f_{x}(z)=f(x,z)\text{ は }D\text{ 上正則}\\\ \\
(2):\frac{\partial f}{\partial z}:C\times D\to\bm{C}\text{ は連続}\\\ \\
(3):\forall b\text{ に収束する点列 }(b_k)\sub[a,b)\text{ に対して、}F^{(b_k)}_{n}:D\to\bm{C},\quad F^{(b_k)}_{n}(z)=\int_a^{b_n}f(x,z)dx\text{ は }D\text{ 上 }F(z)=\int_a^bf(x,z)dx\text{ に広義一様収束}\\\ \\
\Rightarrow F\text{ は }D\text{ 上正則であって、}\forall z\in D\text{ に対して、}\\\ \\
\frac{dF}{dz}(z)=\lim_{x\to b}\int_a^{x}\frac{\partial f}{\partial z}(z,z)dx$$


    ・条件(3)：任意のε、任意のz∊Dに対して、あるN_0が存在して、n≧N_0⇒|F-F_n^{(b_k)}|<ε
    ・bは∞でもよい。