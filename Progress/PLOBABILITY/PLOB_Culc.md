
- [確率論的な計算、具体例](#確率論的な計算具体例)
  - [離散的な確率](#離散的な確率)
        - [サイコロ](#サイコロ)
        - [コイン投げ](#コイン投げ)
        - [感染者問題](#感染者問題)
  - [連続的な確率](#連続的な確率)
        - [候補者が$n$人の時の選挙の投票結果](#候補者がn人の時の選挙の投票結果)
        - [ある株価の$1$年間の推移](#ある株価の1年間の推移)
        - [$\\int fdx=1$](#int-fdx1)
- [ディラック分布](#ディラック分布)
  - [離散型分布とディラック分布](#離散型分布とディラック分布)
- [基本的な離散分布](#基本的な離散分布)
  - [二項分布 $Bin(n,p)$](#二項分布-binnp)
    - [確率関数](#確率関数)
    - [測度空間](#測度空間)
    - [$n,k,n-k$ 十分大のとき](#nkn-k-十分大のとき)
      - [ベルヌーイ分布 $Be(p)$](#ベルヌーイ分布-bep)
    - [幾何分布 $Ge(p)$](#幾何分布-gep)
      - [確率関数](#確率関数-1)
      - [測度空間](#測度空間-1)
    - [ポアソン分布 $Po(λ)$](#ポアソン分布-poλ)
      - [確率関数](#確率関数-2)
      - [測度空間](#測度空間-2)
    - [一般化逆関数法？](#一般化逆関数法)
  - [連続型](#連続型)
    - [一様分布 $U(a,b)$](#一様分布-uab)
      - [測度空間](#測度空間-3)
    - [正規分布 $N(μ,σ^2)$](#正規分布-nμσ2)
      - [測度空間](#測度空間-4)
    - [指数分布 $Exp(λ)$](#指数分布-expλ)
      - [測度空間](#測度空間-5)
    - [ガンマ分布 $Γ(α,β)$](#ガンマ分布-γαβ)
      - [測度空間](#測度空間-6)
    - [コーシー分布 $Ca(μ,σ^2)$](#コーシー分布-caμσ2)
      - [測度空間](#測度空間-7)
    - [逆関数法？](#逆関数法)

# 確率論的な計算、具体例

## 離散的な確率

##### サイコロ
・標本空間：$\Omega=\{1,...,6\}$

---

・普通の確率加法族：$\mathcal{F}=2^{\Omega}$

→ラプラス的確率：$P(A)=\frac{\#A}{\#\Omega}$

→別の確率：$P(i)=p_i\quad\sum p_i=1$

---

・偶奇に関する確率：$\mathcal{F}=\{\{2,4,6\}.\{1,3,5\}\}$

---

##### コイン投げ
・標本空間：$\Omega=\{\omega_1,\omega_2\}$

→$\Omega=\bm{R},\ \omega<0{で表},\omega\ge0{で負}$としてもよい

---

・$n$回のコイン投げ：$\Omega=\{0,1\}^n$

##### 感染者問題
・日本人が病気にかかっている事象$T$、検査で陽性が出る事象$Y$、陰性が出る事象$N$とし、$P(T)=a,P(Y|T)=b,P(N|T^c)=c$が与えられている

→陽性が出た場合に真に病気にかかっている確率：
$$P(T|Y)=\frac{ab}{ab+(1-a)(1-c)}$$
よって、$a=0.1\%,\ b=99\%,c=98\%$ならば、$P(T|Y)=4.7\%$程度

---

## 連続的な確率

##### 候補者が$n$人の時の選挙の投票結果
・標本空間：$\Omega=\{(p_1,...,p_n)\in[0,1]^n\ |\ \sum p_i=1\}$

    ・別にR^nとして、起きえない事象は確率0としてもよい

##### ある株価の$1$年間の推移

    ・株価は時間に対して連続的に推移

・標本空間：$\Omega=C([0,1])$

    ・[0,1]上の連続関数全体

→より広い標本空間：$\Omega'=D([0,1])=\{[0,1]{上の右連続かつ左極限をもつような関数全体}\}$

    ・左端がつながって右端が穴、カドラグ関数

→微妙な標本空間：$\Omega'=\Pi_{t\in[0,1]}\bm{R}^t$

    ・基本直積でよいが、これは分かりにくい

##### $\int fdx=1$
・$\Omega=\bm{R}$、有限加法族$\mathcal{F}=\{{閉区間全体}\}$、$f:\bm{R}\to\bm{R}_{\ge0}$を可積分かつ$\int_{\bm{R}}fdx=1$とし、$P(I)=\int_I fdx$とする。

→$P$は有限加法的確率測度で、$\sigma(\mathcal{F})$上に一意拡張できる。
よって、$(\Omega,\mathfrak{B}_{\bm{R}},P)$は確率空間

---

# ディラック分布

・確率空間 $(\Omega,\mathfrak{M},P)$、$a\in\bm{R}$ とする。
このとき、
$$X:\Omega\to \bm{R}\\\ \\
X(\omega)=a$$は確率変数で、分布関数：
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

# 基本的な離散分布

## 二項分布 $Bin(n,p)$

    ・母数：n∈N、p∈(0,1)

### 確率関数



<dl><dt>

・
$$
p(k)=\begin{pmatrix}n\\k\end{pmatrix}p^k(1-p)^{n-k}\quad(k=0,1,...)
$$

</dt><dd>

- 分布関数：
$$F(x)=\sum_{k=0}^{[x]}p(k)\\\ \\
x\ge n\Rightarrow F(x)=1,\quad x<0\Rightarrow F(x)=0$$

- $F$ は単調増加で右連続

      ・床関数は右連続

</dd></dl>

---

### 測度空間

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

#### ベルヌーイ分布 $Be(p)$

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



### 幾何分布 $Ge(p)$

    ・母数：p∈(0,1)

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

### ポアソン分布 $Po(λ)$

    ・強度：λ>0

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

## 連続型

### 一様分布 $U(a,b)$

・確率密度関数：
$$f(x)=\frac{1}{b-a}$$

#### 測度空間

<dl><dt>

・可測空間 $\Omega=(a,b)$、$\mathfrak{B}=\{(a,b)\cap B\ |\ B\in\mathfrak{B}_{\bm{R}}\}$ とする。
このとき、
$$P(E)=\int_E\frac{1}{b-a}dx$$ と定めると、これは確率。

    ・非負値可測関数から定まる測度。

</dt><dd>

- 
$$X:(a,b)\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$F(x)=P(X^{-1}(-\infty,x))=\begin{cases}
0 & (x<a)  \\
\frac{x-a}{b-a} & (a\le x\le b)\\
1 & (b<x)
\end{cases}$$

</dd></dl>

---

### 正規分布 $N(μ,σ^2)$

    ・μ∈R、σ>0

・確率密度関数：
$$f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

#### 測度空間

<dl><dt>

・可測空間 $\Omega=\bm{R}$、$\mathfrak{B}=\mathfrak{B}_{\bm{R}}$ とする。
このとき、
$$P(E)=\int_E\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx$$ と定めると、これは確率。

    ・非負値可測関数から定まる測度。

</dt><dd>

- 
$$X:\bm{R}\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$F(x)=P(X^{-1}(-\infty,x))=\frac{1}{\sqrt{\pi}}\int_{-\infty}^{\frac{x-\mu}{\sqrt{2}\sigma}}e^{-t^2}dt$$

</dd></dl>

---

### 指数分布 $Exp(λ)$

    ・母数：λ>0

・確率密度関数：
$$f(x)=\lambda e^{-\lambda x}$$

#### 測度空間

<dl><dt>

・可測空間 $\Omega=(0,\infty)$、$\mathfrak{B}=\{(0,\infty)\cap B\ |\ B\in\mathfrak{B}_{\bm{R}}\}$ とする。
このとき、
$$P(E)=\int_E\lambda e^{-\lambda x}dx$$ と定めると、これは確率。

    ・非負値可測関数から定まる測度。

</dt><dd>

- 
$$X:(0,\infty)\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$F(x)=P(X^{-1}(-\infty,x))=\begin{cases}
0 & (x<0)  \\
1-e^{-\lambda x} & (0\le x)\\
\end{cases}$$

</dd></dl>

---



### ガンマ分布 $Γ(α,β)$

    ・形状母数：α>0、尺度母数：β>0

・確率密度関数：
$$f(x)=\frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$$

- $\Gamma(1,\beta)=Exp(\beta)$

      ・指数分布の拡張。
      ・Γ(n,β)=Erl(n,β)：アーラン分布

#### 測度空間

<dl><dt>

・可測空間 $\Omega=(a,b)$、$\mathfrak{B}=\{(a,b)\cap B\ |\ B\in\mathfrak{B}_{\bm{R}}\}$ とする。
このとき、
$$P(E)=\int_E\frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}dx$$ と定めると、これは確率。

    ・非負値可測関数から定まる測度。

</dt><dd>

- 
$$X:(0,\infty)\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$F(x)=P(X^{-1}(-\infty,x))=\begin{cases}
0 & (x<a)  \\
\int_0^x\frac{\beta^{\alpha}}{\Gamma(\alpha)}t^{\alpha-1}e^{-\beta t}dt & (0\le x)\\
\end{cases}$$

</dd></dl>

---

### コーシー分布 $Ca(μ,σ^2)$

    ・μ∈R、σ>0

・確率密度関数：
$$f(x)=\frac{\sigma}{\pi}\frac{1}{(x-\mu)^2+\sigma^2}$$

#### 測度空間

<dl><dt>

・可測空間 $\Omega=\bm{R}$、$\mathfrak{B}=\mathfrak{B}_{\bm{R}}$ とする。
このとき、
$$P(E)=\int_E\frac{\sigma}{\pi}\frac{1}{(x-\mu)^2+\sigma^2}dx$$ と定めると、これは確率。

    ・非負値可測関数から定まる測度。

</dt><dd>

- 
$$X:\bm{R}\to\bm{R}\\\ \\
X(\omega)=\omega$$は確率変数。
<br>

- 上記の確率変数から誘導される $\bm{R}$ 上の分布は、
$$F(x)=P(X^{-1}(-\infty,x))=\int_{-\infty}^x\frac{\sigma}{\pi}\frac{1}{(t-\mu)^2+\sigma^2}dt$$

</dd></dl>

---

### 逆関数法？