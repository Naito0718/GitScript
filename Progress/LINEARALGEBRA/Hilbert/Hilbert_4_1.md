
- [Frechet空間](#frechet空間)
  - [平行移動不変距離](#平行移動不変距離)
    - [一様有界性定理](#一様有界性定理)
    - [開写像定理](#開写像定理)
    - [閉グラフ定理](#閉グラフ定理)
  - [Banach空間との関係](#banach空間との関係)



# Frechet空間

・$\bm{R,C}$ 上セミノルム空間 $V$ とする。
このとき、Frechet空間 $V$：
セミノルム位相を誘導するセミノルムの分離族として高々可算なものが存在し、$V$ の任意のCauchy列が収束する。

---

## 平行移動不変距離

<dl><dt>

・$\bm{R,C}$ 上Frechet空間 $V$、高々可算なセミノルム分離族 $\mathcal{P}$ とする。
このとき、$$d:V\times V\to [0,\infty)\\\ \\
d(x,y)=\sup_{n\in\bm{N}}\frac{1}{n}\frac{p_n(x-y)}{1+p_n(x-y)}$$と定めると、これはwell-defined。
<br>

</dt><dd>

- $$\forall x,y,z\in V\text{ に対して、}d(x+z,y+z)=d(x,y)\\\ \\$$

- $d$ は $V$ 上の距離で、$d_r=d$。
<br>

      ・t/(1+t) の狭義単調増加性による。

<br>

- 開球 $B(0,r)=\{x\in V\ |\ d(0,x)<r\}$ とする。
このとき、$B(0,r)$ は $V$ の絶対凸な開集合で、
$$V=\bigcup_{n}nB(0,r)\\\ \\$$

- $B(x,r)=\{y\in V\ |\ d(y,x)<r\}$ とする。
このとき、
$$B(x,r)=x+B(0,r)$$であって、$$\{B(x,r)\ |\ x\in X,\ r>0\}$$
は $\mathcal{O}$ の基本近傍系。したがって、距離 $d$ による距離位相 $\mathcal{O}_d$ とすると、
$$\mathcal{O}_d=\mathcal{O}_V$$
であって、$V$ は $d$ に関して完備距離空間。 
<br>

      ・距離位相の基本近傍系と一致することによる。


</dd></dl> 

---

### 一様有界性定理


・$\bm{R,C}$ 上Frechet空間 $V$、$\bm{R,C}$ 上セミノルム空間 $W$、添え字付けられた連続線形写像の族 $f_j:V\to W$ とする。
このとき、
$$\forall x\in V\text{ に対して、 }\{f_j(x)\ |\ j\in J\}\subset W\text{ が有界}\\\ \\
\Rightarrow
\forall \text{ 開近傍 }U_2\in\mathcal{N}_W(0_W)\text{ に対して、 }\exist\text{ 開近傍 }U_1\in\mathcal{N}_V(0_V)\text{ であって、}\\\ \\\forall j\in J\text{ に対して、 }f_j(U_1)\subset U_2\\\ \\$$

- $\bm{R,C}$ 上Frechet空間 $V$、$\bm{R,C}$ 上ノルム空間 $W$、各点収束する連続線形写像の列 $f_n:V\to W$ とする。
このとき、
$$f:V\to W\\\ \\
f(x)=\lim_{n\to\infty}f_n(x)$$
と定めると、これは連続線形写像。

---

### 開写像定理

・$\bm{R,C}$ 上Frechet空間 $V,W$、全射連続線形写像 $f:X\to Y$ とする。
このとき、$f$ は開写像。
<br>

- $\bm{R,C}$ 上Frechet空間 $V,W$、連続線形同型写像 $f:X\to Y$ とする。
このとき、$f$ は同相写像。

---

### 閉グラフ定理

・$\bm{R,C}$ 上Frechet空間 $V,W$、線形写像 $f:V\to W$、グラフ $G(f)=\{(x,f(x))\in V\times W\ |\ x\in V\}$ とする。
このとき、$G(f)$ は $V\times W$ の部分空間で、
$$f\text{ は連続}\iff G(f)\text{ は直積位相に関して閉集合}\\\ \\$$
すなわち、$f$ の連続性は、$x_i\to x,\ f(x_i)\to y$ の時、$y=f(x)$ であることと同値。

    ・グラフはV×f(V)ではない。

---

## Banach空間との関係

・$\bm{R,C}$ 上Banach空間 $(V,\|\cdot\|)$ とする。
このとき、
$$\mathcal{P}=\{\|\cdot\|\}$$
と定めると、これは高々可算なセミノルムの分離族で、任意のCauchy列は収束する。
よって、Banach空間はFrechet空間。

---
---
---

