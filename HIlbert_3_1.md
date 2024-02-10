
    ・Frechet空間終わった！

- [セミノルム](#セミノルム)
  - [セミノルムと凸集合](#セミノルムと凸集合)
- [セミノルム位相](#セミノルム位相)
  - [セミノルム位相の性質](#セミノルム位相の性質)
    - [凸集合](#凸集合)
    - [ノルム空間との関係](#ノルム空間との関係)
  - [有界性](#有界性)
- [汎弱位相](#汎弱位相)
  - [双対空間とセミノルム](#双対空間とセミノルム)
  - [汎弱位相](#汎弱位相-1)
    - [汎弱位相の性質](#汎弱位相の性質)
- [Minkowski汎関数とセミノルム](#minkowski汎関数とセミノルム)
  - [Hahn-Banachの拡張定理](#hahn-banachの拡張定理)
  - [Hahn-Banachの分離定理](#hahn-banachの分離定理)

 

# セミノルム

・$\bm{R,C}$ 上ベクトル空間 $V$ とする。
このとき、セミノルム $p$：
$$p:V\to [0,\infty)\\\ \\
\forall x,y\in V,\forall\alpha\in\bm{R,C}\text{ に対して、}\\\ \\
p(x+y)\le p(x)+p(y),\quad p(\alpha x)=|\alpha|p(x)$$

    ・p(x)=0→x=0がない、逆は言えてる。

## セミノルムと凸集合

- $\bm{R,C}$ 上ベクトル空間 $V$、セミノルム $p:V\to[0,\infty)$、$r>0$ とする。
このとき、
$$\{v\in V\ |\ p(v)<r\}$$
は絶対凸で、
$$\{v\in V\ |\ p(v)<r\}=r\{v\in V\ |\ p(v)<1\}\\\ \\$$

      ・セミノルム位相では0の開近傍。

---


# セミノルム位相

・$\bm{R,C}$ 上ベクトル空間 $V$、セミノルムの集合 $\mathcal{P}$ とする。
このとき、セミノルムの分離族 $\mathcal{P}$：
$$\{x\in V\ |\ p(x)=0\quad (\forall p\in \mathcal{P})\}=\{0\}$$
ここで、
$$(p_a:V\to[0,\infty))_{(p,a)\in\mathcal{P}\times X},\quad p_a(x)=p(x-a)$$から誘導される始位相をセミノルム位相という。

      ・p_aはセミノルムではない。

---

## セミノルム位相の性質

<dl><dt>

・$\bm{R,C}$ 上セミノルム空間 $(V,\mathcal{P})$、ネット $(x_{\lambda})\sub V$、$x\in V$  とする。
このとき、
$$x_{\lambda}\to x\iff \forall p\in\mathcal{P}\text{ に対して、}p(x_{\lambda}-x)\to0$$
特に、$p\in\mathcal{P}$ はセミノルム位相で連続写像。
<br>

    ・右側はy_λ=p(x_λ-x)で定まるネット。
<br>

- $V$ はセミノルム位相について位相線形空間。すなわち、和とスカラー倍が連続であって、$T_1$ 空間である。
<br>

</dt><dd>

- 
$$\forall x,y\in V,\ x\neq y\text{ に対して、}\exist(p,a)\in\mathcal{P}\times V\text{ であって、}p_a(x)\neq p_a(y)\\\ \\$$

---

- $p_1,...p_n\in\mathcal{P}$、$\epsilon>0$ とする。
このとき、
$$V(p_1,...,p_n:\epsilon)=\bigcap_{k=1}^n p_k^{-1}([0,\epsilon))$$
と定めると、これは $0\in V$ の絶対凸な開近傍。さらに、
$$\{V(p_1,...p_n:\epsilon)\ |\ n\in\bm{N},p_i\in\mathcal{P},\epsilon>0\}$$
は $0\in V$ の基本近傍系。
<br>

- $v\in V$ とする。
このとき、
$$v+\{V(p_1,...p_n:\epsilon)\ |\ n\in\bm{N},\ p_i\in\mathcal{P},\ \epsilon>0\}$$
と定めると、これは $v$ の基本近傍系。
したがって、$V$ の位相は絶対凸な $0$ の開近傍によって定まる。
<br>

      ・位相群と同様。

</dd></dl> 

---

### 凸集合

・$\bm{R,C}$ 上セミノルム空間 $V$、$0\in V$ の開近傍 $0\in U\subset\mathcal{N}(0)$ とする。
このとき、
$$\exist\text{ 絶対凸な開集合 } W\in\mathcal{N}(0)\text{ であって、}\\\ \\
\overline{W},\ W+W\sub U\\\ \\$$

    ・位相群と同様。



---

### ノルム空間との関係

・$\bm{R,C}$ 上ノルム空間 $(V,\|\cdot\|)$ とする。
このとき、
$$\mathcal{P}=\{\|\cdot\|\}$$
と定めると、これはセミノルムの分離族で、セミノルム位相とノルム空間の位相は一致する。
<br>

    ・一個だけで分離できるなら、それはノルムだし、定まる基本近傍系は距離位相と同じ。

## 有界性

・$\bm{R,C}$ 上セミノルム空間 $V$、部分集合 $B\subset X$ とする。
このとき、$B$ が有界：
$$\forall \text{ 絶対凸な開集合 }U\subset  V\text{ に対して、}\exist r>0\text{ であって、}\\\ \\
B\subset rU=\{rx\ |\ x\in U\}\\\ \\$$

- $\bm{R,C}$ 上セミノルム空間 $V$、部分集合 $B\sub V$ とする。
このとき、$$B\text{ が有界}\\\ \\
\iff\forall p\in\mathcal{P}\text{ に対して、}\exist r>0\text{ であって、}\\\ \\
B\subset \{v\in V\ |\ p(v)<r\}$$
ただし、$\mathcal{P}$ はセミノルム位相を与える分離族。
<br>

---
---
---

# 汎弱位相

## 双対空間とセミノルム

・$\bm{R,C}$ 上ベクトル空間 $V$、双対空間 $V^*$、$\phi\in V^*$ とする。
このとき、
$$|\phi|:V\to[0,\infty)\\\ \\
|\phi|(x)=|\phi(x)|$$
と定めると、これは $V$ 上のセミノルム。
<br>

    ・ノルムではない。
  
---

## 汎弱位相

・$\bm{R,C}$ 上ベクトル空間 $V$、$\mathcal{F}\sub V^*$ とする。
このとき、線形汎関数の分離族 $\mathcal{F}$：
$$\{x\in V\ |\ \phi(x)=0\ (\forall \phi\in \mathcal{F})\}=\{0\}$$
ここで、
$$\mathcal{P}=\{|\phi|\ |\ \phi\in\mathcal{F}\}$$
と定めると、これはセミノルムの分離族。
よって、この $\mathcal{P}$ が誘導する $V$ のセミノルム位相を、$\mathcal{F}$ が誘導する $V$ の汎弱位相という。
明らかに、$V$ 上の $\mathcal{F}$ から定まる汎弱位相において、$\phi\in\mathcal{F}$ は連続関数。

---

### 汎弱位相の性質

・$\bm{R,C}$ 上ベクトル空間 $V$、線形汎関数の分離族 $\mathcal{F}$、$\phi\in V^*$ に対して、
$$\phi\text{ は汎弱位相で連続}\iff\phi\in\mathrm{span}\mathcal{F}$$
したがって、$\mathrm{span}\ \mathcal{F}$ は汎弱位相で連続な線形汎関数全体。
<br>

    ・span：線形結合全体。和だけの<S>ではない。

---
---
---

# Minkowski汎関数とセミノルム

・$\bm{R,C}$ 上ベクトル空間 $V$、セミノルム $p:V\to[0,\infty)$ とする。
このとき、$p$ はMinkowski汎関数。

---

## Hahn-Banachの拡張定理

・$\bm{R,C}$ 上ベクトル空間 $V$、セミノルム $p:V\to[0,\infty)$、部分空間 $M\subset V$、線形汎関数 $\phi:M\to\bm{R,C}$ とする。
このとき、$|\phi(x)|\le p(x)\ (\forall x\in M)$ ならば、
$$\tilde{\phi}|_M=\phi,\quad\tilde{\phi}(x)\le p(x)\ (\forall x\in X)$$を満たす線形汎関数 $\tilde{\phi}:V\to\bm{R}$ が存在する。
<br>

    ・条件からφ(-x)≦p(-x)が成り立つ。
    ・Hilbert_0_1のRとCの関係、線形写像参照。
<br>

---

## Hahn-Banachの分離定理 

・$\bm{R,C}$ 上セミノルム空間 $V$、閉凸集合 $C\subset V$ とする。
このとき、
$$\forall x\in V-C\text{ に対して、}\exist\text{ 絶対凸な開近傍 }C'\sub V\text{ であって、}\\\ \\
x\in C'\text{ かつ }C\cap C'=\phi\\\ \\$$ 

- $\bm{R,C}$ 上のベクトル空間 $V$、セミノルム位相$\mathcal{O}_1,\mathcal{O}_2$ とする。
このとき、
$$\{\mathcal{O}_1\text{ に関して連続な線形汎関数全体}\}=\{\mathcal{O}_2\text{ に関して連続な線形汎関数全体}\}\\\ \\
\Rightarrow\forall \text{ 凸集合 }C\subset V\text{ に対して、 }\\\ \\
C\ {が}\ \mathcal{O}_1\text{ について閉}\iff C\ {が}\ \mathcal{O}_2\text{ について閉}$$

---
---
---

