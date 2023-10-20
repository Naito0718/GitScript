
    ・Frechet空間終わった！

- [セミノルム](#セミノルム)
  - [絶対凸](#絶対凸)
    - [絶対凸の性質](#絶対凸の性質)
  - [セミノルム位相](#セミノルム位相)
    - [セミノルム位相の性質](#セミノルム位相の性質)
  - [汎弱位相](#汎弱位相)
  - [汎弱位相の性質](#汎弱位相の性質)
  - [HahnｰBanachの拡張定理](#hahnｰbanachの拡張定理)
    - [Minkowski汎関数](#minkowski汎関数)
    - [HahnｰBanachの拡張定理](#hahnｰbanachの拡張定理-1)
- [Frechet空間](#frechet空間)
  - [平行移動不変距離](#平行移動不変距離)
    - [一様有界性定理](#一様有界性定理)
    - [開写像定理](#開写像定理)
    - [閉グラフ定理](#閉グラフ定理)
- [Sovolev空間　](#sovolev空間)


# セミノルム 

## 絶対凸

・$\bm{R,C}$ 上ベクトル空間 $V$、$C\sub V$ とする。
このとき、絶対凸 $C$：$C$ は凸集合かつ $|\alpha|\le1,x\in C\Rightarrow\alpha x\in C$

    ・絶対凸なら0含む。
<br>

- $\bm{R,C}$ 上ベクトル空間 $V$、セミノルム $p:V\to[0,\infty)$、$r>0$ とする。
このとき、
$$\{v\in V\ |\ p(x)<r\}$$
は絶対凸。
<br>

      ・セミノルム空間では0の開近傍。
<br>

- $\bm{R,C}$ 上ベクトル空間 $V$、絶対凸な集合 $C_1,C_2\sub V$ とする。
このとき、$C_1+C_2,\beta C_1$ は絶対凸。
<br>

- $\bm{R,C}$ 上ベクトル空間 $V$、絶対凸な集合 $C\sub V$ とする。
このとき、$\overline{C}$ は絶対凸。
<br>

- $\bm{R,C}$ 上ベクトル空間 $V,W$、絶対凸な集合 $C_1\sub V,\ C_2\sub W$、線形写像 $f:V\to W$ とする。
このとき、$f(C_1),f^{-1}(C_2)$ は絶対凸。
<br>

- $\bm{R,C}$ 上ベクトル空間 $V$、絶対凸な集合列 $C_n\sub V$ とする。
このとき、$\bigcap_n C_n$ は絶対凸。

---

### 絶対凸の性質

・$\bm{R,C}$ 上ベクトル空間 $V$、絶対凸 $C\sub V$ とする。
このとき、$0\in C^{\circ}$

---

## セミノルム位相

・$\bm{R,C}$ 上ベクトル空間 $V$ とする。
このとき、セミノルム：
$$p:V\to [0,\infty),\quad p(x+y)\le p(x)+p(y),\ p(\alpha x)=|\alpha|p(x)$$

    ・p(x)=0→x=0がない、逆は言えてる

- セミノルムの分離族 $\mathcal{P}$：
$$\{x\in V\ |\ p(x)=0\ (\forall p\in \mathcal{P})\}=\{0\}$$を満たすセミノルムの集合 $\mathcal{P}$
<br>

- セミノルム位相：$$(p_a:V\to[0,\infty))_{(p,a)\in\mathcal{P}\times X},\quad p_a(x)=p(x-a)$$から誘導される始位相

      ・ノルム空間はセミノルム空間：（分離族は||・||だけ）、このとき始位相とノルム空間の位相は一致する。
      ・p_aはセミノルムではない。

<br>

---

### セミノルム位相の性質

・$\bm{R,C}$ 上セミノルム空間 $(V,p)$、ネット $x_{\lambda}\sub V$、$x\in V$  とする。
このとき、
$$x_{\lambda}\to x\iff p(x_{\lambda}-x)\to0\ (\forall p\in\mathcal{P})$$
特に、$p\in\mathcal{P}$ はセミノルム位相で連続。

- $V$ はセミノルム位相について位相線形空間。つまり、和とスカラー倍が連続。
<br>

- 
$$\forall x,y\in V,\ x\neq y\text{ に対して、}\exist(p,a)\in\mathcal{P}\times V\text{ であって、}p_a(x)\neq p_a(y)\\\ \\$$

- $V$ はセミノルム位相についてHausdorff空間。
<br>

---

- $$V(p_1,...,p_n:\epsilon)=\bigcap_{k=1}^n p_k^{-1}([0,\epsilon)),\ (\epsilon>0)$$
は $0\in V$ の絶対凸な開近傍。
<br>

- $$\{V(p_1,...p_n:\epsilon)\ |\ n\in\bm{N},p_i\in\mathcal{P},\epsilon>0\}$$は $0\in V$ の基本近傍系。
<br>

- $$\{x+V(p_1,...p_n:\epsilon)\ |\ x\in X,\ n\in\bm{N},p_i\in\mathcal{P},\epsilon>0\}$$は $V$ の基本近傍系。

      ・これがセミノルム空間の位相を定める。

---

## 汎弱位相

・$\bm{R,C}$ 上ベクトル空間 $V$ とする。
このとき、線形汎関数の分離族 $\mathcal{F}$：
$$\{x\in V\ |\ \phi(x)=0\ (\forall \phi\in \mathcal{F})\}=\{0\}$$を満たす線形汎関数の集合 $\mathcal{F}\subset V^*$
<br>

- $\bm{R,C}$ 上ベクトル空間 $V$、線形汎関数の分離族 $\mathcal{F}$ に対して、
$$\mathcal{P}=\{|\phi|\ |\ \phi\in\mathcal{F}\}$$はセミノルムの分離族。
よって、この $\mathcal{P}$ が誘導する $V$ のセミノルム位相を、$\mathcal{F}$ が誘導する $V$ の汎弱位相という。
<br>

- 汎弱位相において、$\phi\in\mathcal{F}$ は連続。

---

## 汎弱位相の性質

・$\bm{C,R}$ 上ベクトル空間 $V$、線形汎関数の分離族 $\mathcal{F}$、$\phi\in V^*$ に対して、
$$\phi\text{ は汎弱位相で連続}\iff\phi\in\mathrm{span}\mathcal{F}$$

    ・span Fは汎弱位相で連続な線形汎関数全体

---

## HahnｰBanachの拡張定理

### Minkowski汎関数

・$\bm{C,R}$ 上ベクトル空間 $V$ とする。 
このとき、Minkowski汎関数 $m:V\to\bm{R}$：
$$m(x+y)\le m(x)+m(y)\\\ \\
\forall\alpha\in[0,\infty)\text{ に対して }m(\alpha x)=\alpha m(x)$$

- セミノルムはMinkowski汎関数

---

### HahnｰBanachの拡張定理

・$\bm{R}$ 上ベクトル空間 $V$、Minkowski汎関数 $m:V\to\bm{R}$、部分空間 $M\subset V$、線形汎関数 $\phi:M\to\bm{R}$ とする。
このとき、$\phi(x)\le m(x)\ (\forall x\in M)$ ならば、
$$\tilde{\phi}|_M=\phi,\quad\tilde{\phi}(x)\le m(x)\ (\forall x\in X)$$を満たす線形汎関数 $\tilde{\phi}:V\to\bm{R}$ が存在する。

    ・ただ一つではない

- $\bm{C,R}$ 上ベクトル空間 $V$、セミノルム $p:V\to[0,\infty)$、部分空間 $M\subset V$、線形汎関数 $\phi:M\to\bm{R,C}$ とする。
このとき、$|\phi(x)|\le p(x)\ (\forall x\in M)$ ならば、
$$\tilde{\phi}|_M=\phi,\quad\tilde{\phi}(x)\le p(x)\ (\forall x\in X)$$を満たす線形汎関数 $\tilde{\phi}:V\to\bm{R}$ が存在する。

      ・φ(-x)≦p(-x)

- $\bm{C,R}$ 上ノルム空間 $V$、部分空間 $M\subset V$、$\phi\in M^{*}$ とする。
このとき、
$$\tilde{\phi}|_M=\phi,\quad\|\tilde{\phi}\|=\|\phi\|$$を満たす $\tilde{\phi}\in V^*$ が存在する。

      ・今回はノルム空間だから、ちゃんと有界線形汎関数。
      ・M上で制限してノルム取ってる。

- $\bm{C,R}$ 上ノルム空間 $V$、$x_0\in V-\{0\}$ とする。
このとき、
$$\phi(x_0)=\|x_0\|,\quad\|\phi\|=1$$を満たす $\phi\in V^*$ が存在する。

---
---
---

# Frechet空間

・$\bm{C,R}$ 上セミノルム空間 $V$ とする。
このとき、Frechet空間 $V$：
セミノルム位相を誘導するセミノルムの分離族として高々可算なものが存在し、$V$ の任意のCauchy列が収束する。

- Banach空間は明らかにFrechet空間。

---

## 平行移動不変距離

<dl><dt>

・$\bm{C,R}$ 上Frechet空間 $V$、高々可算なセミノルム分離族 $\mathcal{P}$ とする。
このとき、$$d:V\times V\to [0,\infty)\\\ \\
d(x,y)=\max_{n\in\bm{N}}\frac{1}{n}\frac{p_n(x-y)}{1+p_n(x-y)}$$と定める。これはwell-defined。
<br>

</dt><dd>

- $$\forall x,y,z\in V\text{ に対して、}d(x+z,y+z)=d(x,y)\\\ \\$$

      ・平行移動不変。
<br>

- $d$ は $V$ 上の距離。
<br>

      ・t/(1+t) は狭義単調増加。

<br>

- 開球 $B(0,r)=\{x\in V\ |\ d(0,x)<r\}$ はFrechet空間において絶対凸な開集合。さらに、
$$X=\bigcup_{n}nB(0,r)\\\ \\$$

- 距離 $d$ による距離位相はFrechet空間における位相と一致する。したがって、$V$ は $d$ に関して完備である。 
<br>

      ・コーシー列：ノルムでなく0近傍で定める。
<br>

- $$B(x,r)=\{y\in X\ |\ d(y,x)<r\}=\{y'+x\in X\ |\ d(y',0)<r\}$$であって、$$\{B(x,r)\ |\ x\in X,\ r>0\}$$はセミノルム位相についても基本近傍系。

      ・距離位相では基本近傍系。


</dd></dl> 

---

### 一様有界性定理

・$\bm{R,C}$ 上セミノルム空間 $V$、$B\subset X$ とする。
このとき、$B$ が有界：
$$\forall \text{ 絶対凸な開集合 }U\subset  V\text{ に対して、}\exist r>0\text{ であって、}\\\ \\
B\subset rU=\{rx\ |\ x\in U\}\\\ \\$$

- $\bm{R,C}$ 上セミノルム空間 $V$、$B\sub V$ とする。
このとき、$$B\text{ が有界}\\\ \\
\iff\forall\text{セミノルム位相を与える }p\text{ に対して、}\exist r>0\text{ であって、}\\\ \\
B\subset \{v\in V\ |\ p(v)<r\}$$

      ・後半の集合はr{p(x)<1}のこと

---

<dl><dt>

$\bm{R,C}$ 上セミノルム空間 $V$、$0\in V$ の開近傍 $0\in U\subset\mathcal{N}(0)$ とする。

</dt><dd>

- $W+W\subset U$ を満たす絶対凸な開集合 $W$ が存在する。
<br>


- $\overline{W}\subset U$ を満たす絶対凸な開集合 $W$ が存在する。

      ・上のWと同じ集合。

</dd></dl>

---

・$\bm{R,C}$ 上Frechet空間 $V$、$\bm{R,C}$ 上セミノルム空間 $W$、添え字付けられた連続線形写像 $f_j:X\to Y$ とする。
このとき、$\forall x\in V\text{ に対して }\{f_j(x)\}\subset W$ が有界集合ならば、
$$\forall U_2\in\mathcal{N}_W(0_W)\text{ に対して }\exist U_1\in\mathcal{N}_V(0_V)\text{ であって、}\\\ \\f_j(U_1)\subset U_2\ (\forall j)$$

    ・一様有界性定理

- $\bm{R,C}$ 上Frechet空間 $V$、$\bm{R,C}$ 上ノルム空間 $W$、連続線形写像列 $f_n:V\to W$ とする。
このとき、$\forall x\in V\text{ に対して }\lim_{n\to\infty} f_n(x)\in W$ ならば、
$$f(x)=\lim_{n\to\infty}f_n(x)$$は連続線形写像。

---

### 開写像定理

・$\bm{R,C}$ 上Frechet空間 $V,W$、全射連続線形写像 $f:X\to Y$ とする。
このとき、$f$ は開写像。

    ・開写像定理。

- $\bm{R,C}$ 上Frechet空間 $V,W$、連続線形同型写像 $f:X\to Y$ とする。
このとき、$f^{-1}$ は連続。

---

### 閉グラフ定理

・$\bm{R,C}$ 上Frechet空間 $V,W$、線形写像 $f:V\to W$、グラフ $G(f)=\{(x,f(x))\in V\times W\ |\ x\in V\}$ とする。
このとき、$G(f)$ は $V\times W$ の部分空間で、
$$f\text{ は連続}\iff G(f)\text{ は閉集合}$$

    ・グラフってV×f(V)じゃダメなのか。


---
---
---

# Sovolev空間　