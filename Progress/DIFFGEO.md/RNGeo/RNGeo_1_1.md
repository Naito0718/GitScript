
- [$R^N$ のベクトル空間的性質](#rn-のベクトル空間的性質)
- [$R^N$ の位相的性質](#rn-の位相的性質)
  - [開集合](#開集合)
  - [閉集合](#閉集合)
    - [有界閉集合](#有界閉集合)
    - [有界閉区間と区間縮小法](#有界閉区間と区間縮小法)
  - [連続関数](#連続関数)
    - [関数極限](#関数極限)
    - [関数列と級数](#関数列と級数)
- [$R^N$ の位相幾何的性質](#rn-の位相幾何的性質)
  - [領域](#領域)
- [$R^N$ の微分幾何的性質](#rn-の微分幾何的性質)
  - [開集合と微分同相性](#開集合と微分同相性)
  - [$1$ の分割](#1-の分割)
    - [滑らかな階段関数](#滑らかな階段関数)
    - [$R^n$ 内の多様体におけるUrysohnの補題](#rn-内の多様体におけるurysohnの補題)
    - [$1$ の可算分割](#1-の可算分割)
  - [$R^n$ 上の積分](#rn-上の積分)
    - [向き](#向き)
    - [境界](#境界)




# $R^N$ のベクトル空間的性質

・内積：$(x,y)=\sum x_iy_i$ であって、$\bm{R}$ 上Hilbert空間。

---

# $R^N$ の位相的性質

・局所コンパクトHausdorff空間。

---

## 開集合

・開集合 $U\sub\bm{R}^N$、左半開区間 $I\sub\bm{R}^N$ とする。
このとき、
$$\exist \text{ 左半開立方体の非交叉列 }I_n\sub\bm{R}^N\text{ であって、}U=\bigcup_n I_n\\\ \\
\exist I\text{ を含む開集合 }I\sub U_n\sub\bm{R}^N\text{ であって、}I=\bigcap_n U_n$$


---

## 閉集合

・非交叉な閉集合 $F_1,...,F_n\sub\bm{R}^{N_1}$、各 $F_i$ 上連続な $f:F_1\cup...\cup F_n\to\bm{R}^{N_2}$ とする。
このとき、$f$ は $F_1\cup...\cup F_n$ 上連続。
<br>

    ・正則空間であることとか使ってる。

---

### 有界閉集合

・有界閉集合 $K\sub\bm{R}^N$ とする。
このとき、$K$ はコンパクト。
<br>

    ・下の区間縮小法使う。結構簡単。

---

### 有界閉区間と区間縮小法

・単調減少、すなわち $I_{n}\sup I_{n+1}$ を満たす有界閉区間列 $I_n=[a_{n,1},b_{n,1}]\times...\times[a_{n,N},b_{n,N}]\sub\bm{R}^N$ とする。
このとき、
$$\bigcap_n I_n\neq\phi$$
特に、$$\lim_{n\to\infty}\max_{1\le i\le N}(b_{n,i}-a_{n,i})=0\Rightarrow \bigcap_n I_n\text{ は一点集合}\\\ \\$$

---

## 連続関数

・コンパクト集合 $K\sub\bm{R}^N$、連続関数 $f:A\to\bm{R}^n$ とする。
このとき、$f$ は $A$ 上一葉連続。

     ・TPSP_2_1参照。

---

### 関数極限

・部分集合 $A\sub B\sub\bm{R}^N$、$f:B\to\bm{R}^m$、$a\in\overline{A}$ とする。
このとき、
$$\lim_{\substack{x\to a \\ x\in A}}f(x)=b\\\ \\
\iff\forall a\text{ に収束する点列 }(a_n)\sub A\text{ に対して、}\lim_{n\to\infty}f(a_n)=f(a)\\\ \\$$

    ・帰納法的なよく見る論法使う。これ選択公理らしい！？
    ・ルベーグ積分論で使ったりする。

---

### 関数列と級数

・部分集合 $A\sub\bm{R}^N$、関数列 $f_n:A\to\bm{R}^m$、非負点列 $(M_n)\sub[0,\infty)$ とする。
このとき、
$$\sum_{n\in\bm{N}}M_n\text{ は収束して、}\forall n\in\bm{N}\text{ に対して、}\sup_{x\in A}|f_n(x)|\le M_n\\\ \\
\Rightarrow \text{ 関数列 }s_n(x)=\sum_{k=0}^{n}f_n(x)\text{ は }A\text{ 上一様収束する}$$

---

# $R^N$ の位相幾何的性質

・$\bm{R}^n$ は可縮空間：$\Psi(x,t)=x+t(x_0-x)$
よって、弧状連結かつ単連結。

---

## 領域

・空でない開集合 $\phi\neq U\sub\bm{R}^N$ とする。
このとき、
$$U\text{ は領域}\iff U\text{ 内の任意の二点は折れ線で結ぶことができる}\\\ \\
\iff U\text{ は弧状連結}\\\ \\$$

    ・折れ線：連続関数であって、ある有限分割の上で一次関数であるもの。

---

# $R^N$ の微分幾何的性質

・ $n$ 次元 $C^{\infty}$ 多様体：
$$\{(\bm{R}^n,1)\}\quad(\text{アトラス})$$

---

## 開集合と微分同相性

・開集合 $U\sub\bm{R}^n$、部分集合 $S\sub\bm{R}^n$、微分同相写像 $f:U\to S$ とする。
このとき、$S$ は $\bm{R}^n$ の開集合。
特に、$\bm{R}^n$ の開集合 $O\sub U$ に対して、$f(O)$ は $\bm{R}^n$ の開集合。

---

## $1$ の分割

<dl><dt>

・$$f:\bm{R}\to[0,\infty)\\\ \\
f(t)=\begin{cases}
e^{-\frac{1}{t}} & (t>0) \\
0 & (t\le0) \\
\end{cases}$$
と定めると、これは $C^{\infty}$ 写像。
<br>

</dt><dd>

- $x\in\bm{R}^n$ とする。
このとき、
$$\forall\epsilon>0\text{ に対して、}\exist f\in C^{\infty}_{C,+}(\bm{R}^n)\text{ であって、}\\\ \\
(f>0)=B(x_0,\epsilon)\\\ \\
\forall x,y\in\bm{R}^n,\ |x-x_0|=|y-y_0|\text{ に対して、}f(x)=f(y)\\\ \\$$

</dd></dl>

---

### 滑らかな階段関数

・$\epsilon>0$ とする。
このとき、
$$\exist C^{\infty}\text{ 単調増加関数 }f:\bm{R}\to\bm{R}\text{ であって、}\\\ \\
f(t)=0\quad(\forall t\in(-\infty,0)),\quad 0\le f(t)\le 1\quad(t\in[0,\epsilon]),\quad f(t)=1\quad(\forall t\in(\epsilon,\infty))$$

---

### $R^n$ 内の多様体におけるUrysohnの補題

<dl><dt>

・$k$ 次元 $C^{\infty}$ 多様体 $M\sub\bm{R}^n$ とする。
このとき、
$$\forall p\in M,\ \forall\text{ 開近傍 }p\in U\sub M\text{ に対して、}\exist f\in C^{\infty}_{c,+}(M)\text{ であって、}\\\ \\
f(p)>0,\quad\mathrm{supp}\ f\sub U$$
さらに、
$$\forall K\sub V\sub M\text{ なるコンパクト集合 }K,\ \text{ 開集合 }V\text{ に対して、}\exist f\in C^{\infty}_{c,+}(M)\text{ であって、}\\\ \\
\forall p\in K\text{ に対して、}f(p)>0,\quad\mathrm{supp}\ f\sub V\\\ \\$$

</dt><dd>

- $K\sub V\sub M$ なる $M$ のコンパクト集合 $K$、開集合 $V$ とする。
このとき、
$$\exist f\in C^{\infty}_{c,+}(M)\text{ であって、}\\\ \\
\forall x\in M\text{ に対して }0\le f(x)\le 1,\quad\forall x\in K\text{ に対して }f(x)=1,\quad\mathrm{supp}\ f\sub V\\\ \\$$

- $K\sub\bigcup_{i=1}^l V_i\sub M$ なる $M$ のコンパクト集合 $K$、開集合 $V_1,...,V_l$ とする。
このとき、
$$\exist f_1,...,f_l\in C^{\infty}_{c,+}(M)\text{ であって、}\\\ \\
\forall x\in M\text{ に対して }0\le f_i(x)\le 1,\quad\forall x\in K\text{ に対して }\sum_{i=1}^lf_i(x)=1,\quad\mathrm{supp}\ f_i\sub V_i\\\ \\$$

</dd></dl>

---

### $1$ の可算分割

<dl><dt>

・$k$ 次元 $C^{\infty}$ 多様体 $M\sub\bm{R}^n$ とする。
このとき、
$$\forall M\text{ の開被覆 }M=\bigcup \mathcal{U}\text{ に対して、}\exist\text{ 関数列 }(f_n)\sub C^{\infty}_{c,+}(M)\text{ であって、}\\\ \\
\forall n\text{ に対して、}\exist O_n\in\mathcal{U}\text{ であって、}\mathrm{supp}\ f_n\sub O_n\text{ かつ }\forall f_n\text{ に対して、}(f_n>0)\cap(f_k>0)\neq\phi\text{ となる }k\text{ は有限かつ }\forall p\in M\text{ に対して、}\sum_{n\in\bm{N}}f_n(p)=1\\\ \\$$

</dt><dd>

- $F\sub V\sub M$ なる $M$ の閉集合 $F$、$M$ の開集合 $V$ とする。
このとき、
$$\exist C^{\infty}\text{ 写像 }f:M\to[0,1]\text{ であって、}\\\ \\
\forall x\in F\text{ に対して、}f(x)=1\text{ かつ }\forall x\in V^c\text{ に対して、}f(x)=0$$

</dd></dl>


---

## $R^n$ 上の積分

### 向き

・連続な大域枠 $$\frac{\partial}{\partial r^i}:\bm{R}^n\to T(\bm{R}^n)$$ が存在する。したがって、向き付け可能であり、$dx^1\wedge...\wedge dx^n$ で向き付けられる。

- 標準的な向きを持つ開集合 $U,V\sub\bm{R}^n$、微分同相写像 $F:U\to V$ とする。
このとき、
$$F\text{ は向きを保つ}\iff\forall u\in U\text{ に対して、}\det\frac{\partial F^i}{\partial x^j}>0\\\ \\$$ 

      ・微分同相でなくてC^∞でもよい。

---

### 境界

・上半空間 $\mathcal{H}^n=\{(x^1,...,x^n)\in\bm{R}^n\ |\ x^n>0\}$、$\mathcal{H}^n$ の開集合 $U,V\sub\mathcal{H}^n$、微分同相写像 $f:U\to V$ とする。
このとき、$$f(U\cap(\mathcal{H}^n)^i)\sub(\mathcal{H}^n)^i,\quad f(U\cap(\mathcal{H}^n)^f)\sub(\mathcal{H}^n)^f$$
すなわち、$f$ は内点を内点に移し、境界を境界に移す。

---

