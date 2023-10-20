
- [$R^n$](#rn)
  - [基本的な性質](#基本的な性質)
    - [位相的性質](#位相的性質)
      - [開集合](#開集合)
    - [ベクトル空間的性質](#ベクトル空間的性質)
    - [位相幾何的性質](#位相幾何的性質)
- [微分幾何的性質](#微分幾何的性質)
  - [$R^n$ 上の積分](#rn-上の積分)
    - [向き](#向き)
- [Lebesgue測度](#lebesgue測度)
    - [線形変換](#線形変換)
    - [極大関数と不等式](#極大関数と不等式)
    - [Lebesgueの微分定理](#lebesgueの微分定理)
    - [変数変換](#変数変換)
      - [変数変換公式](#変数変換公式)



# $R^n$

## 基本的な性質

### 位相的性質

・局所コンパクトHausdorff空間。

---

#### 開集合

・任意の開集合 $U$ は、左半開立方体の非交叉列 $I_n$ の合併で表される。：
$$U=\bigcup_n I_n$$

---

### ベクトル空間的性質

・$C^*$-環。

- ノルム：$\|x\|=\sqrt{\sum |x_i|^2}$

### 位相幾何的性質

・可縮空間：$\Psi(x,t)=x+t(x_0-x)$
よって、弧状連結かつ単連結。


---

# 微分幾何的性質

・ $n$ 次元 $C^{\infty}$ 多様体：
$$\{(\bm{R}^n,1)\}\quad(\text{アトラス})$$

---

## $R^n$ 上の積分

### 向き

・連続な大域枠 $$\frac{\partial}{\partial r^i}:\bm{R}^n\to T(\bm{R}^n)$$ が存在する。したがって、向き付け可能である。

---

# Lebesgue測度

    ・平行移動不変性とかは、結局リーマン積分を流用してるからよいのか！

・$\bm{R}$ 上のLebesgue測度 $m$ に対して、
$$m_n:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]\\\ \\
m_n=\otimes^nm$$はRadon測度。
よって、この測度 $m_n$ を $\bm{R}^n$ 上のLebesgue測度という。

- $\bm{R}^n$上のLebesgue測度 $m_N$ に対して、$$m_n([a_1,b_1]\times...\times[a_n,b_n])=(b_1-a_1)...(b_n-a_n)$$

      ・通常の意味での体積。

- $\bm{R}^n$ 上のBorel測度 $\mu:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]$ に対して、
$$\mu\text{ がRadon測度}\iff\mu\text{ は任意の直方体に対して通常の体積を与える}$$

---

・閉直方体 $I\subset\bm{R}^n$、連続関数 $f:I\to \bm{C}$、Lebesgue測度 $m_n:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]$ とする。
このとき、
$$\int_Ifdm=\int_I f(x)dx\quad(\text{右辺はRiemann積分})$$

    ・以降、ルベーグ積分とリーマン積分を区別しない。

---

### 線形変換

・$$B\mapsto m_n(B+y)$$は $\bm{R}^n$ 上のRadon測度で、
$$m_n(B+y)=m_n(B)\quad(\forall B\in\mathfrak{B}_{\bm{R}^n},\forall y\in\bm{R}^n)$$
よって、Lebesgue測度はHarr測度。

    ・左辺自体を新たなLebesgue測度として定める。

- $A\in GL(n,\bm{R})$、$B\in \mathfrak{B}_{\bm{R}^n}$ とする。
このとき、
$$B\mapsto m_n(A(B)),\quad B\mapsto|\det A\ |m_n(B)$$はともに $\bm{R}^n$ 上のRadon測度であって、
$$m_n(A(B))=|\det A\ |m_n(B)$$

---

### 極大関数と不等式

<dl><dt>

・複素数値Borel測度 $\nu:\mathfrak{B}_{\bm{R}^n}\to\bm{C}$ とする。
このとき、Hardy-Littlewoodの極大関数：
$$M\nu:\bm{R}^n\to [0,\infty]\\\ \\
M\nu(x)=\sup_{r>0}\frac{|\nu|(B(x,r))}{m_n(B(x,r))}$$

</dt><dd>

- 複素数値測度 $\nu:\mathcal{B}_{\bm{R}^n}\to\bm{C}$、$\alpha>0$ とする。
このとき、$$(\alpha<M\nu)\subset \bm{R}^n$$は開集合。
よって、
$$M\nu:\bm{R}^n\to[0,\infty]$$ はBorel関数。

      ・∞取りうるし連続とは限らない。

- 複素数値測度 $\nu:\mathcal{B}_{\bm{R}^n}\to\bm{C}$、$\alpha>0$ とする。
このとき、
$$m_n((\alpha<M\nu))\le\frac{3^n}{\alpha}\|\nu\|$$

      ・||ν||=|ν|(X)、ノルムのこと。

- $f\in\mathcal{L}^1(\bm{R}^n)$ とする。
このとき、
$$Mf(x)=Mm_{n,f}=\sup_{r>0}\frac{1}{m_n(B(x,r))}\int_{B(x,r)}|f(y)|dy$$

      ・Hardy-Littlewoodの不等式

</dd></dl>

---

### Lebesgueの微分定理

<dl><dt>

・$f\in\mathcal{L}^1(\bm{R}^n)$、$x\in\bm{R}^n$ とする。
このとき、$f$ のLebesgue点 $x$：
$$\lim_{r\to +0}\frac{1}{m_n(B(x,r))}\int_{B(x,r)}|f(y)-f(x)|dy$$

</dt><dd>

- $f\in\mathcal{L}^1(\bm{R}^n)$ とする。
このとき、ほとんどすべての $x\in\bm{R}^n$ がLebesgue点。
<br>

- $f\in\mathcal{L}^1(\bm{R}^n)$ とする。
このとき、$x\in\bm{R}^n$ で $f$ が連続ならば、$x$ はLebesgue点。
<br>

- $f\in\mathcal{L}^1(\bm{R}^n)$ とする。
このとき、ほとんどすべての $x\in \bm{R}^n$ で
$$\lim_{r\to +0}\frac{1}{m_n(B(x,r))}\int_{B(x,r)}f(y)dy=f(x)$$

</dd></dl>

---

### 変数変換

---

#### 変数変換公式

---
