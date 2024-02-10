
- [Lebesgue測度](#lebesgue測度)
  - [$R$ 上のBorel集合](#r-上のborel集合)
    - [Borel集合の性質](#borel集合の性質)
  - [$R$ 上のLebesgue測度 $m$](#r-上のlebesgue測度-m)
    - [簡単な性質](#簡単な性質)
  - [$R^n$ 上のLebesgue測度](#rn-上のlebesgue測度)
    - [簡単な性質](#簡単な性質-1)
    - [Riemann積分との整合](#riemann積分との整合)
  - [線形変換](#線形変換)
  - [極大関数と不等式](#極大関数と不等式)
  - [Lebesgueの微分定理](#lebesgueの微分定理)
  - [変数変換](#変数変換)
    - [変数変換公式](#変数変換公式)
- [ルベーグ積分と微分](#ルベーグ積分と微分)



# Lebesgue測度

    ・平行移動不変性とかは、結局リーマン積分を流用してるからよいのか！

---

## $R$ 上のBorel集合

・$$\mathfrak{B}_{\bm{R}}=\sigma(\{開区間全体\})=\sigma(\{閉区間全体\})=\sigma(\{区間塊全体\})\\\ \\$$

      ・開基の性質による。
<br>

- $$\mathfrak{B}_{\bm{R}^n}=\sigma(\{開区間全体\})=\sigma(\{閉区間全体\})=\sigma(\{区間塊全体\})$$

---

### Borel集合の性質

・$B\in\mathfrak{B}_{\bm{R}^n}$、$a\in\bm{R}$、$b\in\bm{R}$、$A\in GL(n,\bm{R})$ とする。
このとき、
$$aB+b,\ A(B)\in\mathfrak{B}_{\bm{R}^n}$$

---

## $R$ 上のLebesgue測度 $m$

・ 
$$\Lambda :C_{c,\bm{R}}\to\bm{R},\quad \Lambda f=\int_I f(x)dx\\\ \\
(\mathrm{supp} f\subset I{なる任意の有界閉区間},\int{はRiemann積分})$$
と定めると、これはRadon汎関数。ここで、この $\Lambda$ に対して一意的に定まるRadon測度 $m$ をLebesgue測度という。

---

### 簡単な性質

・開集合 $O\sub\bm{R}$ とする。
このとき、$m(O)>0$
<br>

    ・R^nでも同様。
<br>

- $\bm{R}$ 上のLebesgue測度 $m$ に対して、$m([b-a])=b-a$
<br>

      ・普通の意味での長さを与える。
<br>



---

## $R^n$ 上のLebesgue測度

・$\bm{R}$ 上のLebesgue測度 $m$ に対して、
$$m_n:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]\\\ \\
m_n=\otimes^nm$$はRadon測度。ここで、この測度 $m_n$ をLebesgue測度という。
<br>

- $\bm{R}^n$上のLebesgue測度 $m_N$ とする。
このとき、
$$m_n([a_1,b_1]\times...\times[a_n,b_n])=(b_1-a_1)...(b_n-a_n)\\\ \\$$

      ・通常の意味での体積。
<br>

- $\bm{R}^n$ 上のBorel測度 $\mu:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]$ とする。
このとき、
$$\mu\text{ はRadon測度}\iff\mu\text{ は任意の直方体に対して通常の体積を与える}$$
特に、$\mu$ がRadon測度ならば、$\mu$ は $\sigma$-有限測度。

---

### 簡単な性質

・$k<N$ とする。このとき、
$$m_N(\bm{R}^k\times\{0\})=0$$



---

### Riemann積分との整合

・閉直方体 $I\subset\bm{R}^n$、連続関数 $f:I\to \bm{C}$、Lebesgue測度 $m_n:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]$ とする。
このとき、
$$\int_Ifdm_n=\int_I f(x)dx\quad(\text{右辺はRiemann積分})$$

    ・以降、ルベーグ積分とリーマン積分を区別しない。

---

## 線形変換

・$y\in\bm{R}^n$ とする。
このとき、
$$m_n^b:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]\\\ \\
m_n^b(B)=m_n(B+y)$$
と定めると、これは $\bm{R}^n$ 上のRadon測度で、
$$m_n^b=m_n$$
よって、Lebesgue測度はHarr測度。
<br>

- $A\in GL(n,\bm{R})$ とする。
このとき、
$$m_n^A,m_n^{\det A}:\mathfrak{B}_{\bm{R}^n}\to[0,\infty]\\\ \\
m_n^A(B)=m_n(A(B)),\quad m_n^{\det A}B=|\det A\ |m_n(B)$$はともに $\bm{R}^n$ 上のRadon測度であって、
$$m_n(A(B))=|\det A\ |m_n(B)$$

---

## 極大関数と不等式

<dl><dt>

・複素数値測度 $\nu:\mathfrak{B}_{\bm{R}^n}\to\bm{C}$ とする。
このとき、
$$M\nu:\bm{R}^n\to [0,\infty]\\\ \\
M\nu(x)=\sup_{r>0}\frac{|\nu|(B(x,r))}{m_n(B(x,r))}$$
と定めると、これはwell-defined。ここで、$M\nu$ をHardy-Littlewoodの極大関数という。
<br>

- $f\in\mathcal{L}^1(\bm{R}^n)$ とする。
このとき、
$$Mm_{n,f}=\sup_{r>0}\frac{1}{m_n(B(x,r))}\int_{B(x,r)}|f(y)|dy$$
である。ここで、$Mf=Mm_{n,f}$ と書く。
<br>

</dt><dd>

- 複素数値測度 $\nu:\mathcal{B}_{\bm{R}^n}\to\bm{C}$、$\alpha>0$ とする。
このとき、$$(\alpha<M\nu)\subset \bm{R}^n$$
は開集合。よって、
$$M\nu:\bm{R}^n\to[0,\infty]$$ はBorel関数。
<br>

      ・Mνは∞取りうるし連続とは限らない。
<br>


- 複素数値測度 $\nu:\mathcal{B}_{\bm{R}^n}\to\bm{C}$、$\alpha>0$ とする。
このとき、
$$m_n((\alpha<M\nu))\le\frac{3^n}{\alpha}\|\nu\|$$

      ・||ν||=|ν|(X)、ノルムのこと。

</dd></dl>

---

## Lebesgueの微分定理

<dl><dt>

・$f\in\mathcal{L}^1(\bm{R}^n)$、$x\in\bm{R}^n$ とする。
このとき、$f$ のLebesgue点 $x$：
$$\lim_{r\to +0}\frac{1}{m_n(B(x,r))}\int_{B(x,r)}|f(y)-f(x)|dy\\\ \\$$

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

## 変数変換

・開集合 $U\sub\bm{R}^N$、$C^1$ 同相写像 $f:U\to f(U)\sub\bm{R}^N$、$a\in U$、$\det f'(a)\neq0$ とする。
このとき、
$$\lim_{r\to+0}\frac{m(f(B(a,r)))}{|m(a,r)|}=|\det(f'(a))|\\\ \\$$

- 開集合 $U\sub\bm{R}^N$、$C^1$ 写像 $f:U\to\bm{R}^N$、$\sigma$-コンパクトな $m$-零集合 $N\sub U$ とする。
このとき、$f(E)$ は $\sigma$-コンパクトな $m$-零集合。

---

### 変数変換公式

・開集合 $U\sub\bm{R}^N$、$C^1$ 微分同相写像 $\Psi:U\to f(U)\sub\bm{R}^N$、非負値Borel関数 $g:\Psi(U)\to[0,\infty]$ とする。
このとき、
$$\int_{\Psi(U)}g(x)dm=\int_U (g\circ \Psi)(x)|\det \Psi'(x)|dm$$
特に、$\Psi$ は零集合を零集合に移す。
<br>

- $B\in\mathfrak{B}_{\bm{R}^N}$、$B$ に含まれる、$B$ を含む開集合 $B_0\sub B\sub U$、$C^1$ 写像 $\Psi:U\to\bm{R}^N$ とする。
このとき、
$$\begin{cases}
\Psi(B)\sub\mathfrak{B}_{\bm{R}^N}\\
\Psi\text{ は }B_0\text{ 上単射で }\forall x\in B_0\text{ に対して }\det \Psi'(x)\neq0\\
\exist\sigma\text{-コンパクトな零集合 }N\in\mathfrak{B}_{\bm{R}^n}\text{ であって、}B-B_0\sub N\\
\end{cases}\\\ \\
\Rightarrow\forall\text{ 非負値Borel関数 }f:\Psi(B)\to[0,\infty]\text{ に対して、}\\\ \\
\int_{\Psi(B)}f(x)dm=\int_Bf(x)|\det\Psi'(x)|dm$$

---

# ルベーグ積分と微分

・星形開集合 $U\sub\bm{R}^m$、$C^1$ 関数 $f:U\times\bm{R}^N\to\bm{C}$ とし、
$$F,G:U\to\bm{C}\\\ \\
F(t)=\int_{\bm{R}^N}f(t,x)dm(x)\\\ \\
G(t)=\int_{\bm{R}^N}\frac{\partial}{\partial t_j}f(t,x)dx$$
とする。このとき、
$$\forall t\in U\text{ に対して、}\exist\delta>0\text{ であって、}\forall 0<|h|<\delta\text{ に対して、 }\left|\frac{\partial f}{\partial t_j}(t+h,x)-\frac{\partial f}{\partial t_j}(t,x)\right|\le H(x)\text{ なる }H\in\mathcal{L}^1(\bm{R}^N)\text{ が存在する}\\\ \\
\Rightarrow\frac{\partial}{\partial t_j}\int_{\bm{R}^N}f(t,x)dx=\int_{\bm{R}^N}\frac{\partial}{\partial t_j}f(t,x)dx\\\ \\$$

      ・結局G(t)が連続なことが言えればいい。
      ・G(t)が広義一様収束してるでもいい？杉浦p.320





