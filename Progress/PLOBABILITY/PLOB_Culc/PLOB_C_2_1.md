
- [ディラック測度](#ディラック測度)
  - [積分](#積分)
  - [$R^N$ 上のディラック測度](#rn-上のディラック測度)
  - [分布](#分布)
  - [離散型分布とディラック分布](#離散型分布とディラック分布)
- [二項分布 $Bin(n,p)$](#二項分布-binnp)
  - [簡単な積分](#簡単な積分)
    - [分布関数](#分布関数)
    - [$n,k,n-k$ 十分大のとき](#nkn-k-十分大のとき)
    - [ベルヌーイ分布 $Be(p)$](#ベルヌーイ分布-bep)
    - [二項分布の実現](#二項分布の実現)
- [負の二項分布](#負の二項分布)
  - [簡単な積分](#簡単な積分-1)
    - [幾何分布 $Ge(p)$](#幾何分布-gep)
      - [確率関数](#確率関数)
      - [測度空間](#測度空間)
- [ポアソン分布 $Po(λ)$](#ポアソン分布-poλ)
  - [簡単な積分](#簡単な積分-2)
      - [確率関数](#確率関数-1)
      - [測度空間](#測度空間-1)
    - [一般化逆関数法？](#一般化逆関数法)



# ディラック測度

・可測空間 $(\Omega,\mathfrak{M})$、$a\in\Omega$ とする。
このとき、
$$\delta_a:\mathfrak{M}\to [0,\infty]\\\ \\
\delta_a(B)=\chi_B(a)$$
と定めると、これは確率測度。ここで、$\delta_a$ をディラック測度という。
<br>

- 可測空間 $(\Omega,\mathfrak{M})$、高々可算な集合 $\Gamma\sub\Omega$、$p:\Gamma\to[0,\infty]$ とする。
このとき、
$$\mu:\mathfrak{M}\to[0,\infty]\\\ \\
\mu(B)=\sum_{x\in\Gamma}p(x)\delta_x(B)$$
と定めると、これは測度であって、
$$\mu(B)=\sum_{x\in B\cap \Gamma}p(x)$$
特に、$\sum_{x\in\Gamma}p(x)<\infty$ を満たす $p:\Gamma\to[0,\infty)$ とすると、$\mu$ は有限測度。

---

## 積分

・測度空間 $(\Omega,\mathfrak{M},\delta_a)$、非負値可測関数 $f:\Omega\to[0,\infty]$ とする。
このとき、$$\int_{\Omega}fd\delta_a=f(a)$$

---

## $R^N$ 上のディラック測度

・高々可算な集合 $\Gamma\sub\bm{R}^N$、$p:\Gamma\to[0,\infty]$ とする。
このとき、
$$\mu:\mathfrak{M}\to[0,\infty]\\\ \\
\mu(B)=\sum_{x\in\Gamma}p(x)\delta_x(B)$$
と定めると、$A=\bm{R}^N-\Gamma$ に関して、$\mu$ と $m$ は特異な測度。

---

## 分布

    ・？？？

$$F(x)=\Delta_a(x)=\begin{cases}
1 & (a\le x) \\
0 & (x<a)  \\
\end{cases}$$ となる。
<br>

- 上記の確率変数から誘導される確率：
$$\mu_{\Delta_{a}}:\mathfrak{B}\to[0,1]\\\ \\
\mu_{\Delta_a}(E)=1_{a\in E}$$

      ・Eにaが入ってれば1

---

## 離散型分布とディラック分布

    ・？？？

<dl><dt>

・離散型確率変数 $X$、$A=\{a_i\ |i\in\bm{N}\}\sub\bm{R}^d$、確率関数 $p:A\to[0,1]$ とする。このとき、
$$f:\bm{R}^d\to\bm{R}\\\ \\
f(x)=\sum_{i=1}^{\infty} p(a_i)\delta(x-a_i)$$ と定める。

</dt><dd>

- $$F(x)=\sum_i^{\infty}p(a_i)\Delta_{a_i}(x)$$よって、$F$ は $\Delta_{a_i}$ による混合分布。
<br>

- $$F(x)=\int_{(-\infty,x_1]\times...\times(-\infty,x_n]}f(z)dz$$したがって、$f$ は $F$ の確率密度関数に相当する。

      ・離散型分布も絶対連続型分布と同様に計算できる。


</dd></dl>

---



# 二項分布 $Bin(n,p)$

・$n\in\bm{N},p\in[0,1]$ とする。
このとき、
$$P:\bm{N}\to[0,1]\\\ \\
P(k)=\binom{n}{k}p^k(1-p)^{n-k}$$
と定めると、これは $\sum_{k\in\bm{N}}P(k)=1$ を満たす。
したがって、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu=\sum_{k=0}^n\binom{n}{k}p^k(1-p)^{n-k}\delta_k$$
は $1$ 次元離散型分布。

---

## 簡単な積分


・$a\in\bm{R}$ とする。
このとき、
$$\int_{\bm{R}}e^{ax}d\mu=(pe^a+1-p)^n\\\ \\$$

    ・二項定理。
<br>

- 
$$\int_{\bm{R}}xd\mu=np\\\ \\
\int_{\bm{R}}x^2d\mu=np(1+np-p)\\\ \\$$

    ・上のやつの01,2階微分係数。


---

### 分布関数

- 分布関数：
$$F(x)=\sum_{k=0}^{[x]}p(k)\\\ \\
x\ge n\Rightarrow F(x)=1,\quad x<0\Rightarrow F(x)=0$$

- $F$ は単調増加で右連続

      ・床関数は右連続

---

<dl><dt>

・可測空間 $(\bm{N},2^{\bm{N}})$ とする。
このとき、
$$P(E)=\sum_{k\in E}p(k)=\sum_{k\in E}\begin{pmatrix}n\\k\end{pmatrix}p^k(1-p)^{n-k}$$ と定めると、これは確率。

</dt><dd>

- 
$$X:\bm{N}\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$P(X^{-1}(-\infty,x))=\sum_{k=0}^{[x]}p(k)=F(x)$$よって一致した。特に、この $X$ は離散型。

</dd></dl>

---

### $n,k,n-k$ 十分大のとき

・$$\mathrm{In}P(X=k)\sim-k\mathrm{In}\left(\frac{k}{np}\right)+(k-n)\mathrm{In}\left(\frac{n-k}{n(1-p)}\right)$$

    ・スターリング

- 
$$\mathrm{In}(1+x)=x-x^2/2+x^3/3-...\\
\mathrm{In}(1-x)=-x-x^2/2-x^3/3-...$$
より、
$$k\mathrm{In}\left(\frac{k}{np}\right)=k-np+\frac{(k-np)^2}{2np}-\frac{(k-np)^3}{6n^2p^2}+...\\\ \\
(k-n)\mathrm{In}\left(\frac{n-k}{n(1-p)}\right)=k-np-\frac{(k-np)^2}{2n(1-p)}-\frac{(k-np)^3}{6n^2(1-p)^2}-...\\\ \\$$

- $3$ 乗以降の項を無視すると、
$$P(X=k)\sim e^{-\frac{(k-np)^2}{2np(1-p)}}$$
これは、平均 $\mu=np$、分散 $\sigma=np(1-p)$ の正規分布の確率密度関数に一致する。

      ・確かに平均、分散も一致している。

---

### ベルヌーイ分布 $Be(p)$

    ・二項分布のn=1のとき

<dl><dt>

・可測空間：$(\{0,1\},2^{\{0,1\}})$ に対して、
$$P(E)=\sum_{k\in E}p(k)$$ は確率。

</dt><dd>

- 確率変数は、
$$X:\{0,1\}\to\bm{R}\\\ \\
X(\omega)=\begin{cases}
1 & (\omega=1,\ \text{確率 }p)  \\
0  & (\omega=0,\ \text{確率 }1-p) \\
\end{cases}$$

</dd></dl>

---

### 二項分布の実現

・箱の中には十分多く黒と白の球が入っており黒色が取り出される確率は常に $p$ とする。
このとき、$n$ 回箱の中から取り出すことを考えると、黒玉が $k$ 回取りだされる確率：
$$\binom{n}{k}p^k(1-p)^{n-k}$$

---

# 負の二項分布

    ・pが0だと和が1でなくなる。

・$t>0,\ p\in(0,1]$ とする。
このとき、
$$P:\bm{N}\to[0,1]\\\ \\
P(k)=\binom{t+k-1}{k}p^t(1-p)^{k}\\\ \\$$
と定めると、これは $\sum_{k\in\bm{N}}P(k)==p^t(1-(1-p))^{-t}=1$ を満たす。
したがって、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu=\sum_{k\in\bm{N}}\binom{t+k-1}{k}p^t(1-p)^{k}\delta_k$$
は $1$ 次元分布。

---

## 簡単な積分


・$a<-\log(1-p)$ とする。
このとき、
$$\int_{\bm{R}}e^{ax}d\mu=\left(\frac{p}{1-(1-pe^a)}\right)^t\\\ \\$$

    ・一般二項定理。また、p=1ならaは任意の実数。
<br>

- 
$$\int_{\bm{R}}xd\mu=?\\\ \\
\int_{\bm{R}}x^2d\mu=?\\\ \\$$

    ・上のやつの01,2階微分係数。


---

### 幾何分布 $Ge(p)$

    ・t=1

#### 確率関数

<dl><dt>

・
$$
p(k)=(1-p)^{k}p\quad(k=0,1,...)
$$

</dt><dd>

- 分布関数：
$$F(x)=\sum_{k=0}^{[x]}p(k)\\\ \\
\lim_{x\to\infty} F(x)=1,\quad x<0\Rightarrow F(x)=0$$

- $F$ は単調増加で右連続

      ・床関数は右連続

</dd></dl>

---

#### 測度空間

<dl><dt>

・可測空間 $(\bm{N},2^{\bm{N}})$ とする。
このとき、
$$P(E)=\sum_{k\in E}p(k)=\sum_{k\in E}\begin{pmatrix}n\\k\end{pmatrix}p^k(1-p)^{n-k}$$ と定めると、これは確率。

</dt><dd>

- 
$$X:\bm{N}\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$P(X^{-1}(-\infty,x))=\sum_{k=0}^{[x]}p(k)=F(x)$$よって一致した。特に、この $X$ は離散型。

</dd></dl>

---

# ポアソン分布 $Po(λ)$

・$c>0$ とする。
このとき、
$$P:\bm{N}\to[0,1]\\\ \\
P(k)=\frac{c^k}{k!}e^{-c}\\\ \\$$
と定めると、これは $\sum_{k\in\bm{N}}P(k)=1$ を満たす。
したがって、
$$\mu:\mathfrak{B}_{\bm{R}}\to[0,1]\\\ \\
\mu=\sum_{k\in\bm{N}}\frac{c^k}{k!}e^{-c}\delta_k$$
は $1$ 次元分布。

    ・c>0でないと値域、和が1であることと整合しない。

---

## 簡単な積分


・$a$ とする。
このとき、
$$\int_{\bm{R}}e^{ax}d\mu=\exp(c(e^z-1))\\\ \\$$

    ・一般二項定理。また、p=1ならaは任意の実数。
<br>

- 
$$\int_{\bm{R}}xd\mu=c\\\ \\
\int_{\bm{R}}x^2d\mu=c+c^2\\\ \\$$


---

#### 確率関数

<dl><dt>

・
$$
p(k)=e^{-\lambda}\frac{\lambda^k}{k!}\quad(k=0,1,...)
$$

</dt><dd>

- 分布関数：
$$F(x)=\sum_{k=0}^{[x]}p(k)\\\ \\
\lim_{x\to\infty} F(x)=1,\quad x<0\Rightarrow F(x)=0$$

- $F$ は単調増加で右連続

      ・床関数は右連続

</dd></dl>

---

#### 測度空間

<dl><dt>

・可測空間 $(\bm{N},2^{\bm{N}})$ とする。
このとき、
$$P(E)=\sum_{k\in E}p(k)=\sum_{k\in E}\begin{pmatrix}n\\k\end{pmatrix}p^k(1-p)^{n-k}$$ と定めると、これは確率。

</dt><dd>

- 
$$X:\bm{N}\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$P(X^{-1}(-\infty,x))=\sum_{k=0}^{[x]}p(k)=F(x)$$よって一致した。特に、この $X$ は離散型。

</dd></dl>

---


### 一般化逆関数法？

---

